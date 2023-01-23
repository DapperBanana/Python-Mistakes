import time

def useful_function():
    for i in range(5):
        print("I swear I'm useful: {}".format(i))
        time.sleep(1.0)

# useful_function()
        #To start us off... If we ever want to call this script in another function
        #we need to call the if __name__ statement in order to prevent the program from 
        #running on import (when importing another file it runs that python script)

if __name__ == '__main__':
    #Remember that the double underscore is called "dunder"

    #This __name__ statement is now the official entry point for your script and you can
    #still use the rest as an import
    useful_function()