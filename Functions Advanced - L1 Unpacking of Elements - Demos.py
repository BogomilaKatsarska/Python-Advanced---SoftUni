#1. Unpacking Arguments [Unpack Lists, Tuples and Dictionaries]:
# We can use * to unpack the list so that all elements of it can be passed as different parameters
# And we can use ** to unpack a dictionary, so all of its elements are passed as keyworded arguments
# Note that the length of the list that you unpack must be the same as the number of parameters in the function

tt = (1, 2, 3)
x, y, z = tt

def print_nums(a, b, c):
    print(a, b, c)
nums = [1, 2, 3]
print_nums(*nums)

def add(x, y, z):
    return x+y+z
numbers = (1, 2, 3)
#Option 1:
print(add(numbers[0], numbers[1], numbers[2]))
#Option 2:
a, b, c = numbers
print(add(a, b, c))
#Option 3:
print(add(*numbers)) # --> Unpack as positional arguments

#The order of the keys in the dictionary does not matter

numbers_dict = {
    'x':1,
    'y':2,
    'z':3,
}
#Option 1:
print(add(numbers_dict['x'], numbers_dict['y'], numbers_dict['z']))
#Option 2:
print(add(**numbers_dict)) # --> Unpacks named argumens(**kwargs)