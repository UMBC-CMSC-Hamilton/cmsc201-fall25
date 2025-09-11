"""

    ssh [your username]@gl.umbc.edu
    type your password carefully
    Duo Auth

    ls - list the structure of the current directory
        ls -la = give you the file sizes and more information but primarily file sizes.
    pwd - tells you where you are currently.
    cd changes directory
        cd .. goes back by one level
    emacs [filename] opens a file for editing
        CTRL+X CTRL+S = Save
        CTRL+X CTRL+C = Exit

    submit cmsc201 HW0 hw0.py
    submitls cmsc201 HW0

"""

"""
Let's get back to Python.  

variables
    start with underscore or a letter (upper or lower case)
    case sensitive variable system
    rest of the characters are underscores letters or numbers. 
    
    a variable is a name for a place in memory [RAM]
    
    
snake case - python coding standard
    variables should be lowercase letters and numbers separated by underscores 

"""

A = 3
a = 4
r2d2 = 52
__hi = 'hello there'

t = 0b11010101010
f = 0x52af

print(A, a)

radius_of_earth = 6370  # km
pi = 3.14159265358979
random_thing = 'water'
radius_1 = 14
radius_2 = 17

# algebra = works mostly as usual, be careful of order of operations
# PEDMAS / BODMAS
print((6 - 3) - 3)

# powers in python

print(5 ** 0.5)  # ** means power, ^ caret
# be careful of order of operations because in the first case, 5 ** 1 goes first then / 2
print(5 ** 1 / 2, 5 ** (1 / 2))

x = 3
y = 7
z = 11
print((y + z) / x)
print(x / (y + z))
# more order of operations stuff... use parentheses liberally.

# floating point division, integer division
print(6 / 3, 6 // 3)

print(15 / 4, 15 // 4)

# 15 // 4 = 3 ==> 15 = 3 * 4 + (REM = 3)
# rule: remainder has to be positive
print(16 // 4, 17 // 4, 18 // 4, 19 // 4, 20 // 4)
# there's a way to get the remainder, it's called "modulus division" mod
print(16 % 4, 17 % 4, 18 % 4, 19 % 4, 20 % 4)

# if you mod by 2 you're checking the parity of the number, meaning whether it's even or odd
print(923 % 2, 8844 % 2, 123445 % 2)
# -3 // 5 what is that ?
# -3 = 5 (quot) + rem
# -3 = 5 (-1) + 2

print(-3 // 5, -3 % 5)

# string formatting... super cool and important
number_of_ostriches = 233
print(f'The number of ostriches is {number_of_ostriches}')
print('The number of ostriches is ' + str(number_of_ostriches))
print('The number of ostriches is', number_of_ostriches)
print('The number of ostriches is {}'.format(number_of_ostriches))  # ugly don't do it, just use f strings
print('The number of ostriches is %d' % number_of_ostriches)

x = 4
y = 22.7
z = 'happy'
print(f'{x // 3} {y} {z}')

"""
If statements
    the way programs can make decisions - branch
    either you can go down one path or you can skip that path or go down another path

[conditions] evaluate to either True or False

if [condition]:
    [stuff must be tabbed one level]
    [more stuff]
    [even more stuff]
    
not in the if statement

"""

y = 0
x = int(input('Tell me x: '))
if x > 20:
    print('x is really big')
    y = 5

if x < 0:
    print('x is sad')
    y = 2

print(x, y)

y = int(input('What is y? '))

if y == 0:  # == equality tester
    print('No. I cannot divide that, Stan.')
else:
    print(x // y)

