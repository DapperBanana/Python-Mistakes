def manual_string_format(name, subscribers):
    if subscribers > 1000:
        print("Wow " + name + "! You have " + str(subscribers) + " subscribers!")
    else:
        print("Lol " + name + " that's not that many subs")

#When looking at the first example we can see that the injected strings take much more code, created a string that's harder to read, and in general is much worse off
#Taking a look at the second example it's much easier to read the better format

def better_string_format(name, subscribers):
    if subscribers > 1000:
        print("Wow {name}! You have {subscribers} subscribers!")
    else:
        print("Lol {name} that's not that many subs")