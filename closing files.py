def manually_calling_close_on_a_file(filename):
    with open(filename) as f:
        f.write("hello!\n")

#instead of manually closing the file (as depicted below)
    #f = open(filename, "w")
    #f.write("hello!\n")
    #f.close()
#Be sure to with the "with open" statement as this will close the file if you ever throw an exception. This is unlike the explicit commands as if there's ever an issue in there the file will be stuck open 
