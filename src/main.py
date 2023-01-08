
# imports 

import os                           # library for os related functions
import psutil as p                  # module to check the running programs 
from threading import Thread        # threading for running multiple operations at once and not disturbing the code flow
from time import sleep              # for pausing the code flow
import ctypes                       # .NET integration with python ( pythonnet )
import config                       # to get the settings from `config.json` 
import sys                          # importing sys for exiting the python code

consoleTasks = []   # initialising empty list for task objects to store


def taskChecker():
    """
    Check the running applications and services after every 1 second
    and add them to the taskList.
    """
    while True:
        consoleTasks.clear()
        for task in p.process_iter():
            consoleTasks.append(task)
        sleep(1)

def Killbroadcast():
    """
    Creates a windows native error message dialoge box.
    """
    msg = ctypes.windll.user32.MessageBoxW      # .NET library responsible for making messages dialoge box.
    msg(None , "You can not access the application you are trying to open." , "Access Denied" , 0x10)

# importing settings 
setting = config.ImportConfig()

try:
    if setting['current'] == None:   # checking if the account type is not selected 
        os.system('test.exe || py test.py')     
        sys.exit()      # exiting the code 
except:
    sys.exit()  

# starting the thread to keep checking the processes 
checker = Thread(target = taskChecker , daemon = True)
checker.start()
sleep(1)

# starting the broadcast thread
broadcast = Thread(target = Killbroadcast )


while True:
    for task in consoleTasks:
        for taskName in setting['profiles'][setting['current']]:        # checking the config for the restricted tasks 
            if taskName in task.name():
                try:
                    task.kill()     # killing the restricted task
                    broadcast.start()
                except:
                    pass
