global_var = 10

def bar(x):
    global global_var
    print(global_var)
    global_var = x
    print(global_var)

def foo(x):
    print(global_var)
    global_var = x
    print(global_var)

bar(20) #this will run as the global is being defined as actually existing outside the definition
foo(10) #this will not run as EVEN THOUGH the variable name is that same as the variable it is in fact a local variation of that. Since it's definted later in the statement the code has an error and can't complete
print(global_var)