
# Auto Laser: Getting Started

## Prerequisites
Auto Laser has a few prerequisites you will have to satisfy before you are able to use the software. 
1. Download the PyCharm IDE and the Arduino IDE and drivers.
2. Clone the "src" folder of this repository. 
3. Open the autolaser.py file in PyCharm and build the project to make sure there are no build errors.
4. Open the AutoLaser_ArduinoCode.ino file in the Arduino IDE and make sure there are no build errors.
5. Connect the Arduino to your PC via the Serial port.
6. Upload the AutoLaser_ArduinoCode.ino file to the arduino.

### Physical Assembly
You must construct this 3d printed servo assembly which can be found [here](https://www.instructables.com/CheetahBeam-a-DIY-Automatic-Cat-Laser-Toy/). This is a necessary physical part which will control the laser assembly. Other supplies necessary will be a camera to feed data into the system, and balloons to use as targets.

### Cloning the Repo
You also must clone the "src" folder of this repo using [git](http://git-scm.com/), this will give you the software necessary to use and control the physical aspect of this project.

## Setting up the system
Assemble the 3D-printed housing and the wiring for the servos and laser (follow the linked guide). Connect the arduino to your PC via the Serial port and set the port to COM3. Upload the AutoLaser_ArduinoCode.ino file to the arduino. Place the webcam directly underneath the laser. Now the system is ready to be run.

## Running the system
These are the steps for running the program:
1. Open the autolaser.py code in PyCharm. 
2. With the arduino and a webcam connected to your PC, run the code and you should see a GUI pop up on your screen.
3. Within this GUI, you can either select "Perform Calibration" to calibrate the program to lighting of your specific environment, or you can click "Start" to begin the detection and targeting of balloons. 
4. If you click "Perform Calibration", you will be faced with a number of different slider options. Using the image on the right of the GUI as reference, hold the balloon in plain view of the camera and adjust the sliders until only the balloon is visible in the image. Ideally, the image will be completely black with a white circle in the area where the balloon is detected.
5. If you click start, the GUI will change and you will have the ability to select which color of balloon you want to target. You will also see a Distance counter in the bottom left of the image which is an estimation of the distance between the balloon and the camera.
