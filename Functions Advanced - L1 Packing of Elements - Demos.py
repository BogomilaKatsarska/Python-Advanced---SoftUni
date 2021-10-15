#1. Packing of Elements - Demos:
# A PARAMETER is the variable which is part of the method's signature(method declaration). An argument is an expression used when calling the method.

#2.*Args
# If you only use 'args' as a parameter the compulsory # of arguments is 0.

def add_with_list (numbers):
    return sum(numbers)

def add (*args): # gives us the possibility to collect many values without including them in a list. All the parameters go to a tuple - 'numbers'.
    return sum(args)

def add_v2 (x, *args): #first given string goes to 'x' and the others are packed in 'numbers'
    return sum(args)

def add_v3 (*args): # "args' can be 'called' from 0 to infinite # of el
    return sum(args)

print(add_with_list([1, 2, 3, 4])) #result = 10
print(add(1, 2, 3, 4)) #result = 10
print(add_v2(1, 2, 3, 4)) #result = 9 [1 goes to 'x' and the others go to 'args']
print(add_v3()) #result = 0

#3. **Kwargs: allows you to pass keyworded variable length of arguments to a function. '**' are used for dictionary

def add_v3 (*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args)
    #return sum(args) + sum(kwargs.values()) --> if we want the sum of the values of args and kwargs together

print(add_v3(1, 2, 3)) # (1, 2, 3); {}; 6
print(add_v3(x=1, y=2, z=3)) #(); {'x':1, 'y':2, 'z':3}; 0
print(add_v3(y=1, x=2, z=3)) #(); {'y':1, 'x':2, 'z':3}; 0
print(add_v3(1, 2, z=3)) # (1, 2); {'z':3}, 3
print(add_v3(1, 2, x=1)) # (1, 2); {'x':3}, 3
print(add_v3()) # (); {}; 0

#4. Functions - Recap:
def add_recap(x, y, z):
    return x + y + z

print(add_recap(1, 2, 3))
print(add_recap(x=1, y=2, z=3)) #named parameter
print(add_recap(y=1, x=2, z=3)) #can be reordered
print(add_recap(1, 2, z=3)) # one can be named and others can be without name
print(add_recap(1, 2, x=1)) # does not work; 'x' will have 2 values