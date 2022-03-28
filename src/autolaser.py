import cv2
import imutils
import time
import serial
import pickle
import PySimpleGUI as sg
import gui

a_file = open("data.pkl", "rb")
balloon_bounds = pickle.load(a_file)
a_file.close()

KNOWN_DISTANCE = 12 #inches
KNOWN_RADIUS = 5 #inches
KNOWN_RADIUS_IN_IMAGE = 200 #pixels

arduino = serial.Serial(port='COM3', baudrate=115200)
def write_read_arduino(command):
    arduino.write(bytes(command, 'utf-8'))


def focalLengthFinder(knownDistance, knownRadius, radiusInImage):
    '''
    This function calculates the focal length which is used to find the distance between the object and the camera.
    :param1 knownDistance(int/float) : Distance from object to camera measured in real world.
    :param2 knownRadius(float): Real world radius of the object.
    :param3 radiusInImage(float): Pre-measured radius of the object in the image, measured in pixels.
    returns FocalLength(float):
    '''
    focalLength = ((radiusInImage * knownDistance) / knownRadius)
    return focalLength


focalLength = focalLengthFinder(KNOWN_DISTANCE, KNOWN_RADIUS, KNOWN_RADIUS_IN_IMAGE)


def distanceFinder(focalLength, knownRadius, radiusInVideo):
    '''
    This function estimates the distance. It takes the three arguments: focallength, knownRadius, radiusInImage.
    :param1 focalLength: Focal length found through another function.
    :param2 knownRadius(float): Real world radius of the object.
    :param3 radiusInVideo(float): Radius of the object in the video stream, measured in pixels.
    :returns the distance:
    '''
    distance = ((knownRadius * focalLength) / radiusInVideo)
    return distance


# Modifies the frame in order to isolate the HSV range of our balloon and create a mask
def get_mask(color, frame):
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # Isolates the frame to only show the selected balloon's HSV range
    mask = cv2.inRange(hsv, balloon_bounds[color]['lower'], balloon_bounds[color]['upper'])
    # These get rid of any small artifacts that may be left behind and help smooth out our shape
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    return mask


# Finds the largest isolated shape once we have modified the frame
def get_max_contour(mask):
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    if len(contours):
        max_contour = max(contours, key=cv2.contourArea)
        return max_contour
    return []


# Finds both the center point of the balloon contour and also maps this to angles for the servos
def find_center_point(max_contour):
    global L
    global radius
    moments = cv2.moments(max_contour)
    center = (int(moments["m10"] / moments["m00"]), int(moments["m01"] / moments["m00"]))

    # Get the x and y coords of the center dot location on the image
    x_coord = int(moments["m10"] / moments["m00"])
    y_coord = 450 - int(moments["m01"] / moments["m00"])
    
    # Scale the coordinates down and convert them to angles that the servos can make use of.
    # The x and y coefficients are hardcoded calibration values.
    # The numerators are the horizontal and vertical field of view of the camera "Logitech HD Pro WebCam C910" (http://www.therandomlab.com/2013/03/logitech-c920-and-c910-fields-of-view.html)
    # The denominators are the horizontal and vertical length of the image in terms of pixels.
    # This is part of how we correlate the location of the dot in an image to the real-life location of the balloon.
    x_coef = 70 / video_stream.get(cv2.CAP_PROP_FRAME_WIDTH)
    y_coef = 55 / video_stream.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # Calculate the angles to set the servos to point the laser at the center dot
    # The numbers "55" and "70" are the "zero" angles of the servos
    # I.E. The coordinate (55, 70) would be equivalent to (0, 0) on a grid
    x_angle = round(55 + (x_coef * x_coord))
    y_angle = round(70 + (y_coef * y_coord))

    # If the laser is off, turn it on
    if L is False:
        L = True
        write_read_arduino("0L") #Toggle laser on

    write_read_arduino(f"{180-x_angle}x") #Send the x-angle
    write_read_arduino(f"{y_angle}y") #Send the y-angle
    return center


# Adds an outline around the balloon and adds a center dot on the frame displayed to users
def draw_outline(max_contour, frame):
    center = None
    ((x, y), radius) = cv2.minEnclosingCircle(max_contour)

    center = find_center_point(max_contour)
    
     # Find the distance between the balloon and the camera
    distance = distanceFinder(focalLength, KNOWN_RADIUS, radius)

    ft_distance = round(int(distance) / 12, 1)

    if radius > 10:
        cv2.circle(frame, center, 5, (0, 0, 255), -1)
        cv2.drawContours(frame, [max_contour], 0, (0, 255, 0), 3)
        distance_text = "Distance (FT): " + str(ft_distance)
    else:
        distance_text = "Distance (FT): N/A"

    cv2.rectangle(frame, (15, 400), (240, 435), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, distance_text, (15, 425), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=.75, color=(255, 255, 255))


# start up the gui
auto_laser_gui = gui.initialize_gui(balloon_bounds)

# start up the video feed
video_stream = cv2.VideoCapture(0)
time.sleep(1.0)
L = False

while True:
    event, values = auto_laser_gui.read()

    if event == "Start":
        start = True
        auto_laser_gui['main'].update(visible=False)
        auto_laser_gui['targeting'].update(visible=True)
        while start:
            event, values = auto_laser_gui.read(timeout=0)
            ret, frame = video_stream.read()

            # Pulls the selected color from the gui
            balloon_color = list(values.keys())[list(values.values()).index(True)]
            if event == "Quit0" or event == sg.WIN_CLOSED:
                write_read_arduino("0L")
                write_read_arduino("90x")
                write_read_arduino("90y")
                auto_laser_gui.close()
                quit()
            elif event == "Back":
                auto_laser_gui['main'].update(visible=True)
                auto_laser_gui['targeting'].update(visible=False)
                break

            frame = imutils.resize(frame, width=600)

            mask = get_mask(balloon_color, frame)
            max_contour = get_max_contour(mask)

            if len(max_contour):
                draw_outline(max_contour, frame)

            png_frame = cv2.imencode('.png', frame)[1].tobytes()
            auto_laser_gui['target'].update(data=png_frame)
    elif event == "Perform calibration":
        auto_laser_gui['main'].update(visible=False)
        auto_laser_gui['calibration'].update(visible=True)
        while True:
            event, values = auto_laser_gui.read(timeout=0)
            ret, frame = video_stream.read()
            print(event)

            if event == "Back1":
                auto_laser_gui['main'].update(visible=True)
                auto_laser_gui['calibration'].update(visible=False)
                break
            elif event == "calibration_color":
                auto_laser_gui['h_min'].update(value=balloon_bounds[values['calibration_color']]['lower'][0])
                auto_laser_gui['s_min'].update(value=balloon_bounds[values['calibration_color']]['lower'][1])
                auto_laser_gui['v_min'].update(value=balloon_bounds[values['calibration_color']]['lower'][2])
                auto_laser_gui['h_max'].update(value=balloon_bounds[values['calibration_color']]['upper'][0])
                auto_laser_gui['s_max'].update(value=balloon_bounds[values['calibration_color']]['upper'][1])
                auto_laser_gui['v_max'].update(value=balloon_bounds[values['calibration_color']]['upper'][2])
            elif event == "Save":
                lower_tuple = tuple([values['h_min'], values['s_min'], values['v_min']])
                upper_tuple = tuple([values['h_max'], values['s_max'], values['v_max']])
                balloon_bounds[values['calibration_color']]['lower'] = lower_tuple
                balloon_bounds[values['calibration_color']]['upper'] = upper_tuple
                a_file = open("data.pkl", "wb")
                pickle.dump(balloon_bounds, a_file)
                a_file.close()
            elif event == sg.WIN_CLOSED:
                auto_laser_gui.close()
                cv2.destroyAllWindows()
                quit()

            color_adjusted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            adjusted = cv2.inRange(color_adjusted, (values['h_min'], values['s_min'], values['v_min']),
                                 (values['h_max'], values['s_max'], values['v_max']))

            png_frame = cv2.imencode('.png', frame)[1].tobytes()
            auto_laser_gui['original'].update(data=png_frame)

            png_adjusted = cv2.imencode('.png', adjusted)[1].tobytes()
            auto_laser_gui['adjusted'].update(data=png_adjusted)
    elif event == "Quit" or event == sg.WIN_CLOSED:
        auto_laser_gui.close()
        quit()

cv2.destroyAllWindows()
auto_laser_gui.close()
