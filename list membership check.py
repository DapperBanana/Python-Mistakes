import time

with open('names.txt') as f:
    names = f.readlines()[:1000000]
    names_set = set(names)

def in_names():
    ret = []
    for i in range(100):
        ret.append(str(i) in names)
    return ret

def in_names_set():
    ret = []
    for i in range(100):
        ret.append(str(i) in names_set)
    return ret

print("running in_names")
s = time.time()
in_names()
print("Time taken:", time.time() - s)

print("running in_names_set")
s = time.time()
in_names_set()
print("Time taken:", time.time() - s)

#this mainly has to do with order 1 operations (if you don't know what that means look it up)
#sets and hachtables are CONSIDERABLY faster than lists and if you're doing anything in the order of searching for something (usually string compare) inside of a list then a set or hash will be significantly faster
