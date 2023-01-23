import traceback

try:
    raise Exception('bad exception with stupid message')
except Exception as e:
    print("This is what printing the excpetion is like")
    print(e) #this just gives us whatever message there was associated with the exception
                #while this could be useful there's a better chance you're going to want the raised message AS WELL as the actual traceback so you can inspect

    print()

    print("This is what traceback.print_exc() is like")
    traceback.print_exc() #this prints directly to standard out

    print()

    print("This is what printing traceback.format_exc() is like")
    str = traceback.format_exc() #this gives more flexibility if you're wanting to inspect the message in some other way
    print(str)