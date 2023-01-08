# importing libraries
import json     # library for parsing json
import sys      # for using "sys.exit()" 


# basic template for the config.json file
TEMPLATE = '''
{
    "current": null ,
    "profiles": {
        "admin": [],
        "teacher": [],                                  
        "student": []
    }
}
'''


# Function definations 
def makeConfig():
    '''
    Makes the config.json file in the same
    directory.
    '''
    with open('config.json' , 'w+') as f:   # making the config file
        f.write(TEMPLATE)   # writing the config using the declared template
        sys.exit()

def ImportConfig() :
    '''
    Read the `config.json`
    for the settings and return the 
    parsed settings. 
    Makes the file if not found.
    '''
    try:
        with open("config.json" , 'r+') as f:   # trying to open the config file
            data = json.load(f)     # loading the file data and converting it to python format
            return data         # returning the settings retrieved
    except:
        makeConfig()        # if file not found calling the function to make file

