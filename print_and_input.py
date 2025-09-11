"""
    Test homework will be a print statement

    How do print statements work in python?

        they can print a few types of things
            strings = collection of characters, spaces, letters, numbers, symbols !@#$%^&*asdfgh1234
            integers = ints = -5, -4, -3, -2, -1, 0, 1,2, 3, 4, 5
            floats = floating point (floating decimal point) 4.2, 3.99, 7.21, -15.8
            booleans = True / False

    Multi-line comment
"""

print('hello there')
print(3, 5.2, -8.1, True, False)
print("Like this with double quote")
print('Strings also like this with single quote')
# you have to start and end with the same symbol
# print('what about this?") does not match

"""
    Variables:
        What are they?
            We need a way to remember pieces of data.
            Computers have RAM [memory] but RAM is actually addressed as numbers
            0 - 1048575
            You don't want your program to have to remember user's name - 43872478 age 12937
            Allocate a block of memory that has a specific name. We can use that name to access that piece of memory.
        How are they named?
            Variables must start with either _ or a letter
            contain letters, numbers, underscores, but no other symbols (not !@#$%^&*(),./)
"""

ThisIsAVariable = 3
x = 17
pi = 3.141592653589
name = 'Eric'
what = True
print(x, what, name)
name += " Robot"

name = 51
print(name)
# name += " Robot"
# variables are not strictly typed, which means that they can be one type then another type.
# I recommend that a variable not really change type.

addition = 4 + 17 + 22 + 81
print(addition)

# not_allowed = 4 + 'happy'
you_can_do_this = str(4) + 'happy'  # concatenation.
print(you_can_do_this)

"""
    Input data from the console [command line]
        Input ALWAYS gives you a string. NEVER an int or float.
        
        In order to get an int or float, you need to cast
"""

statement = input('What do you want to say? ')
print('You said', statement, x)



favorite_number = int(input('What is your favorite number? '))  # put a space after your prompt to look better
favorite_float = float(input('What is a float? '))
print(favorite_number + 2)

print(2 ** 4)
