import PySimpleGUI as sg


# set up layouts and return gui
def initialize_gui(balloon_bounds):
    main_menu = [
        [sg.Text("Welcome to Auto Laser")],
        [sg.Button("Start")],
        [sg.Button("Perform calibration")],
        [sg.Button("Quit")]
    ]

    targeting_options = [
        [sg.Text("Choose which balloon color to target")],
        [sg.Radio("Teal", "colors", default=True, key="teal")],
        [sg.Radio("Purple", "colors", default=False, key="purple")],
        [sg.Radio("Lime", "colors", default=False, key="lime")],
        [sg.Radio("Blue", "colors", default=False, key="blue")],
        [sg.Radio("Red", "colors", default=False, key="red")],
        [sg.Radio("Yellow", "colors", default=False, key="yellow")],
        [sg.Radio("Pink", "colors", default=False, key="pink")],
        [sg.Button("Back")],
        [sg.Button("Quit")]
    ]

    targeting_image = [
        [sg.Image(filename='', key='target', size=(600, 400))]
    ]

    targeting_layout = [[
        sg.Column(targeting_options),
        sg.VSeperator(),
        sg.Column(targeting_image)
    ]]

    calibration_options = [
        [sg.Text("Choose which balloon color to calibrate")],
        [sg.Combo(["teal", "purple", "lime", "blue", "red", "yellow", "pink"], default_value="teal", enable_events=True,
                  key="calibration_color")],
        [sg.Text("H Min")],
        [sg.Slider(range=(0, 255), default_value=balloon_bounds['teal']['lower'][0], orientation='horizontal',
                   enable_events=True, key="h_min")],
        [sg.Text("S Min")],
        [sg.Slider(range=(0, 255), default_value=balloon_bounds['teal']['lower'][1], orientation='horizontal',
                   enable_events=True, key="s_min")],
        [sg.Text("V Min")],
        [sg.Slider(range=(0, 255), default_value=balloon_bounds['teal']['lower'][2], orientation='horizontal',
                   enable_events=True, key="v_min")],
        [sg.Text("H Max")],
        [sg.Slider(range=(0, 255), default_value=balloon_bounds['teal']['upper'][0], orientation='horizontal',
                   enable_events=True, key="h_max")],
        [sg.Text("S Max")],
        [sg.Slider(range=(0, 255), default_value=balloon_bounds['teal']['upper'][1], orientation='horizontal',
                   enable_events=True, key="s_max")],
        [sg.Text("V Max")],
        [sg.Slider(range=(0, 255), default_value=balloon_bounds['teal']['upper'][2], orientation='horizontal',
                   enable_events=True, key="v_max")],
        [sg.Button("Save")],
        [sg.Button("Back")]
    ]

    calibration_views = [[
        sg.Column([[sg.Image(filename='', key='original', size=(600, 400))]]),
        sg.VSeperator(),
        sg.Column([[sg.Image(filename='', key='adjusted', size=(600, 400))]])
    ]]

    calibration_layout = [[
        sg.Column(calibration_options),
        sg.Column(calibration_views)
    ]]

    layouts = [
        [sg.Column(main_menu, key='main'), sg.Column(targeting_layout, visible=False, key='targeting', expand_x=True),
         sg.Column(calibration_layout, visible=False, key='calibration')]
    ]

    sg.theme("DarkTeal2")
    return sg.Window(title="Auto Laser", layout=layouts)
