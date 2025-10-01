"""

    First Exam is next week (Thursday)
        Review session (Tuesday)
        TA extra review session Tuesday at around 7 pm.
        I'll release the practice exams tonight.
"""

"""
    Functions - when you're writing a piece of code that needs to do a bunch of different tasks
        you tend to want to be able to have pieces of code that you can call over and over again. 
        
    Goal is to write the functionality once, and then use it many times. 
    
    How do you declare a function?
    
    def function_name():
        tabbed in code
        tabbed in code
        more tabbed in code
"""


# in this function n is a variable that is called a parameter (input into the function)
def count_to_n(n):
    for i in range(1, n + 1):
        print(f'The number is {i}')


# if we don't call the function it doesn't run

count_to_n(5)
print()
count_to_n(7)
print()
count_to_n(3)


def distance(p1, p2):
    """
    Determines the euclidean distance between the two points
    :param p1: p1 = [x, y]
    :param p2: p2 = [x, y]
    :return:
    """
    # d^2 = (x2 - x1)^2 + (y2 - y1)^2
    # d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

    d = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** (1 / 2)

    return d


print(distance((0, 3), (4, 0)))

print(distance((3.2, 7.9), (5.1, 18.2)))

print(distance((5, 0), (0, 12)))


def nothing():
    x = 1
    # return None


print(nothing())


def pick_number():
    v = int(input('Pick a number between 1 and 10'))
    while v < 1 or v > 10:
        v = int(input('Pick a number between 1 and 10'))
    return v


"""
    As soon as you return the function ends.  
"""


def pick_menu():
    m = int(input('1) Play, 2) Load, 3) Save, 4) Options, 5) Quit'))
    if m == 1:
        return 'play'
    elif m == 2:
        return 'load'
    elif m == 3:
        return 'save'
    elif m == 4:
        return 'options'
    elif m == 5:
        return 'quit'

    return 'no pick'


option = pick_menu()
#  none is always False.
if option:
    print("That is a good option")


def find_match(the_list, the_thing):
    for i in range(len(the_list)):
        print(f'looking at position {i} we see {the_list[i]}')
        if the_list[i] == the_thing:
            return i
            # after a return it's inaccessible
    # put a return value even if it's some kind of nonsense value
    # sentinel value = value that you return or you look for, the value is not actually valid but it tells us we didn't find the element
    return -1


example_list = [4, 3, 9, 7, 8, 9, 7, 3, 4, 7, 8]  # 3, 4, 7, 8,9 NOT 1, 5, 6
print(find_match(example_list, 9))
print(find_match(example_list, 5))


"""
    Scope has to do with the lifetime of a variable and accessibility.  
    
    Global Scope = variable is accessible anywhere in the program 
        the variable "lives" as long as the program is running
        the variable doesn't lose its value or its name during the program's runtime
        
    Local Scope = variable is accessible only in the function that declares it
        variable 'lives' as long as the function does, when the function returns the variable name no longer exists
"""

def random_nonsense():
    x = 4
    y = 7
    print(x + y)
    return x + 2 * y


def different_function():
    x = 3
    y = 18
    print(x ** 2 + y ** 3)


random_nonsense()
different_function()


def add_to_x(y):
    global x  # I am a banned keyword
    print(x + y)
    x = 5
    print(x + y)


# this weirdness should not happen
x = 14
add_to_x(5)
print(x)
add_to_x(78)
print(x)


"""
    Mutability:
    
        int, bool, string, float = immutable = cannot be changed
        
        lists, dictionaries, classes, other objects = mutable = can be changed
        
    Pass-By-Value = we make a copy, and the local variable is a new piece of memory, doesn't modify the 
        [other = global or other local scope] variable
        immutable things 
    Pass-By-Reference = we pass a reference to the original variable, we can modify that variable inside of the function
        mutable things = lists, dicts, other things...

"""

print('pass by value')
def change_an_int(z):
    z = 22


my_int = 5
print(my_int)
change_an_int(my_int)
print(my_int)

def change_a_string(s):
    s = 'Hello I am Changed'
    print(s)

my_string = 'I am always the same'
change_a_string(my_string)
print(my_string)


def change_a_list(ell):
    ell.append(14)

new_list = [3, 4, 5, 6, 7]
print(new_list)
change_a_list(new_list)
print(new_list)

# big_list = [2 * x ** 2 + 3 for x in range(20000000)]
# print('Big list made')
# copy_list = list(big_list)
# print('Copy done')

# returning multiple values

def return_two_things():
    x = int(input('Tell me an int: '))
    s = input('Tell me a story: ')

    return [x, s]  # if you need to return multiple things return them as a list

my_return = return_two_things()
print(my_return[0], my_return[1])
the_int, the_story = return_two_things()
# needs to be the right number of arguments
# x, y, z = return_two_things()
print(the_int, the_story)


def calculate(x, y, z):
    return x + 2 * y + 3 * z

# always provide the correct number of arguments in the correct order
# print(calculate(2, 5, 4, 5))

# legal but generally think about why you're doing it
calculate(z = 2, x = 4, y = 3)


