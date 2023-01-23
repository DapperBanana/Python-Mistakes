import time

while True:
    try:
        print("Wheeee! You can't stop me")
        time.sleep(0.1)
    except:  #in this case if we forget to include the bare except we will never be able to 
             #cntrl+C out and regain control of the terminal. The exception will be raised but
             #not found
        print("Oww... Whatever imma keep running")

while True:
    try:
        print("Wheeee! You can't stop me")
        time.sleep(0.1)
    except Exception:  #Once we include the bare minimum except, we'll be able to actually end
                       #script and raise the exception of whatever the issue was
        print("Oww... Whatever imma keep running")