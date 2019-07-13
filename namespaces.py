#1. local namespace − specific to the current function or class method. If the function defines a local variable x,
#or has an argument x, Python will use this and stop searching.
#2.  global namespace − specific to the current module. If the module has defined a variable, function, or class called x, Python will use that and stop searching.
#3.  built−in namespace − global to all modules. As a last resort, Python will assume that x is the name of built−in function or variable.


def foo(arg):
    x = 1
    print(locals())

foo(100)


print(globals().items())


#With import module: the module itself is imported, but it retains its own namespace,  use the module name to access any of its functions or attributes: module.function. 
#With from module import, you're actually importing specific functions and attributes from another module into your own namespace, which is why you access them directly without referencing the original module they came from. With the globals function, you can actually see this happen.

#What locals does for the local (function) namespace, globals does for the global (module) namespace.  globals is more exciting, though, because a module's namespace is more exciting.[3] Not only does the module's namespace include module−level variables and constants, it includes all the functions and classes defined in the module. Plus, it includes anything that was imported into the module.


# locals is read−only, globals is not

def foo2(arg):
    x = 1
    print(locals())
    locals()["x"] = 2
    print("x=",x)
z = 7
print( "z=",z)
foo2(3)
globals()["z"] = 8
print("z=",z) 

# locals() returns a dictionary, however, it does not actually return the local namespace, it returns a copy.
# globals() returns the actual global namespace, not a copy! So any changes to the dictionary returned by globals directly affect your global variables.

