"""
1) D
2) A
3) B
4) B
5) D
6) C
7) B
8) C
9) A

10 ) 17 65 31
11) Did you mean Ruby?
12) KeyError
13) 60 = 52 + 8



"""
# 14
animals = {}
len(animals) >= 5 and 'platypus' in animals and 'parrot' in animals

# NOT going to be this, always keys not values
my_dict = {}
val = 'platypus'
any(my_dict[x] == val for x in my_dict)

row = 1
col = 1
array = [[12, 23, 23], [12, 12, 12]]
# 15 most important part is array[row] because it's checking to make sure col is in that sublist not the total list.
0 <= row < len(array) and 0 <= col < len(array[row])

"""
16) 

    A local variable is accessible only in its local scope, and only for the lifetime of that scope or function.  
    
    Global variables can be accessed anywhere both in the global and the local scope and they live as long as the program 
        does.  

17) 
    pass by value, when you pass an immutable thing like an int, float, bool, string, NoneType
        you make a copy of the variable, the local variable can be modified but doesn't affect the global variable or
            [the variable in the outer scope]
    
    pass by reference, when you pass a mutable thing like a list or dict
        renaming the variable from the outer scope, it's actually a reference to the same data. 
        you can modify it in the function and it DOES change the outer scope variable.  
        
18) clockwise (from the top left)
    name
    parameters / arguments
    definition
    function call
    body

19) 8
    16
    
20) 
     ’abccaaaabaaab’. split ( ’ab’ ) = ['', 'ccaaa', 'aa', '']
     ';'.join(['', 'ccaaa', 'aa', ''])
     = ;ccaaa;aa; THat's it


matrix = [[1 , 2 , 3] , [7 , 8 , 9] , [5 , 6 , -1]]
for i in range (3):
    print (( i + 7) % 3, (4 * i + 1) % 3, matrix [( i + 7) % 3][(4 * i + 1) % 3])
21) 
    1 1 8
    2 2 -1
    0 0 1

22) 

def branchy ( x ):
    if x <= 2:
        return 1
    a = 2 * branchy ( x - 1)
    b = branchy ( x - 3)
    return a + b

print ( branchy (6))

33

please show work

branchy(6) = 2 * branchy(5) + branchy(3) = 2 * 15 + 3 = 33
branchy(5) = 2 * branchy(4) + branchy(2) = 2 * 7 + 1 = 15
branchy(4) = 2 * branchy(3) + branchy(1) = 2 * 3 + 1 = 7
branchy(3) = 2 * branchy(2) + branchy(0) = 2 * 1 + 1 = 3
branchy(2) = 1
branchy(1) = 1
branchy(0) = 1
                              128  64   32  16  8421
23. Convert the binary number 1    0     1  1   0001 to decimal.
    128 + 32 + 16 + 1 = 177

24. Convert the binary number 0110 1010 to decimal.
    64 + 32 + 8 + 2 = 106
    
25. Convert the decimal number 72 to binary.
    72 even => 36 even => 18 even => 9 (odd) => 4 (even) => 2 (even) => 1 (odd)
    
    0100 1000
    <----
    
26. Convert the decimal number 133 to binary.
    133 (odd) => 66 (even) => 33 (odd) => 16 (even) => 8 (even) => 4 (even) => 2(even) => 1 (odd)
       1000 0101
    <-----
    128 + 4 + 1 = 132 + 1 = 133 yes



"""

"""
Line 7 for row in range ( len( the_board ) ):
Line 8 count = 0
Line 9 for col in range ( len ( the_board[row] )):
Line 10 if the_board [ row ][ col ] == letter:
Line 14 return True
Line 24 missing letter argument.  
"""

L = [1, 2, 3, ]

"""
Let grid be a two-dimensional list. Write a function which calculates the average of each
list, if the list is empty the average is zero.
For instance if the list is grid = [ [1, 2, 3], [6, 9, 15], [1, 2, 3, 4, 5, 6], [], [2, 2, 2] ] then the
average should list should be [2, 10, 3.5, 0, 2].
"""


def average_of_lists(grid):
    averages = []

    for row in grid:
        the_avg = 0
        for val in row:
            the_avg += val
        if len(row) != 0:
            the_avg /= len(row)
        averages.append(the_avg)

    return averages

"""
29. We’re going to model a version of an ”exploding d6” meaning a die with 6 sides. If the die
lands on 1, 2, 3 the value is 1. If the die lands on 4 or 5, you should roll another die which
then follows the same rules, and your score here is 1 + the score of the roll of the next die.
If it lands on 6, you roll two such dice so your new score for this is 1 + the score of the two
dice rolls. Use a single call in your function to randint(1, 6) to generate a number between 1
and 6 inclusively. Don’t call it multiple times or that would be equivalent to getting a second
roll. The solution you make must be recursive.
First Roll = 6
Second Roll = 4
Third Roll = 2
Second Roll = 3
The result here would be to return 4 (the number of rolls).
from random import randint
"""
from random import randint

def exploding_d6 ():
    roll = randint (1 , 6)
    # if roll in [1, 2, 3]:
    if roll == 1 or roll == 2 or roll == 3:
        return 1
    elif roll == 4 or roll == 5:
        return 1 + exploding_d6()
    else:
        return 1 + exploding_d6() + exploding_d6()
