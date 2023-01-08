
# imports 

import json
import tui      # importing `tui.py` as library for code simplicity
import config   # importing the file `config.py` as a library for getting the settings of `config.json`
import curses   # library for maiking TUI (Terminal User Interface)
from curses.textpad import rectangle    # importing a rectangle / border from the library
import ctypes   # library for .NET integration ( library name : pythonnet )

# code for maximizing the command prompt for better experience
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_MAXIMIZE = 3

hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_MAXIMIZE)


screen = curses.initscr()       # initialising a console screen
curses.curs_set(0)              # setting to hide the cursor
screen.nodelay(True)            # setting to make the program not wait for user input 
data = config.ImportConfig()    # importing the `config.json` settings 

def main(screen):
    """
    Main block of code for rendering and handling the TUI

    arg : 
        screen : variable that stores the information about
        intialised console screen
    """

    curses.init_pair(1 , curses.COLOR_BLACK , curses.COLOR_WHITE)   # initalising a colour code with black text on white bg
    counter = 0     # counter variable for keeping the track of presently highlighted option
    xcord , ycord = 60 , 20     # co-ordinates for elements on screen (x : characters , y : lines)
    options = [key for key in data['profiles'].keys()]      # getting a list of all the profiles in `config.json`

    while True:     # main loop for redrawing things on console
        usrkey = screen.getch()     # getting the key that user presses in ASCII code 
        
        # KEY MAPPING for TUI
        if usrkey == ord('q'):      # checking if user pressed 'q'
            exit()                      # exiting the option selection
        if usrkey == curses.KEY_UP:     # checking if user pressed " UP ARROW "
            if counter > 0:
                counter -= 1            # decreasing the counter by 1 hence moving up in the list
        if usrkey == curses.KEY_DOWN:       # checking if user pressed " DOWN ARROW "
            if counter < len(options) - 1:      # check to avoid the counter passing the indexes of list
                counter += 1                # increasing the counter by 1 and hence moving down in the list
        if usrkey == curses.KEY_ENTER or usrkey == 10 or usrkey == 13:      # checking if user pressed "ENTER" 
            return(options[counter])            # returning the option selected

        # Making a border arounf the options select area     
        rectangle(screen , ycord - 2 , xcord - 3 , ycord + 6 , xcord + 25 )
        
        # Function to render the accounts available to select 
        tui.optionsRender(
            xcord ,
            ycord ,
            options,
            'choose account type : ' ,
            counter, 
            )

# Checking if no user is specified in the `config.json`
if data['current'] == None:
    result = curses.wrapper(main)   # running the TUI to select the account
    data['current'] = result
    with open('config.json' , 'w') as f:        # updating the `config.json` with selected account type
        json.dump(data, f , indent=4)
