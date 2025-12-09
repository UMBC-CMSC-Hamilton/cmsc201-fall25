"""
1) b 12 - count or subtract
2) d
3) b
4) d
5) b
6) c
7) d
8) c
9) c
10) a
11) c
12) c - del if you want an index, remove only removes the first element that matches, otherwise ValueError

13) ValueError = some kind of error because you can't use a string as an index in a list
14) cucumber
15) 5

16)
'Obi Wan' in hopes and len(hopes) == 1
['Obi Wan'] == hopes

17)
len(sandwiches) >= 5 and 'grilled cheese' in sandwiches and 'reuben' in sandwiches

18)
    x = 1
    while x > 0:
        x += 1

    This doesn't terminate because it's waiting for x to be zero or negative and x is growing, and starts out at 1.

    while True: pass
    This doesn't terminate because True is always True so it will never be able to exit, and pass doesn't do anything
        so no variables would be changed anyway.

    if num > 10:
        print ( ' num is larger than 10 ')
        if num > 20:
            print ( ' num is larger than 20 ')

    if num > 10:
        print ( ' num is larger than 10 ')
    if num > 20:
        print ( ' num is larger than 20 ')

    It doesn't make a difference because if you pick num = 5, 15, 25 the results are the same for both version.
    For 5, it prints nothing, for 15 it only prints the first statement, and for 25 it prints both.

    20)
        start stop step
        start stop
        stop

    21) x == 3 or 5, 5 is always true so this statement always evaluates to true
        x == 3 or x==5 tests whether x is either 3 or 5 as we 'expect.'

    22) False
        (4 or 5) == True
        not (4 or 5) == False

    23)
        49 > 27 and True
        True
    First -> algebra; highest precedence
    comparisons > < in == != all of those
    logic
        not
        and-or [left->right, sisnistrodextral]
"""

print(3 and 'munchies')

the_list = [1, 9, 3, 14, 2, 7, 8, 20]
for i in range(len(the_list)):
    if the_list[i] % 2 == 0 and i % 2 == 0:
        print(i, the_list[i])

"""
    4 2
    6 8
"""

x = 15
y = 7
if x % 5 == 0 and y % 2 == 0:
    print(' beagle ')
elif x % 5 == 0:
    print(' endeavor ')
elif y % 2 == 0:
    print(' resolution ')
else:
    print(' victory ')

x = 4
y = 2
while x < 20 and y < 25:
    x += 1
    y *= 2
    print(x, y)

"""
Line 12 - if len ( posx ) == len ( posy ): change == to !=
    you don't have to copy the entire line of code "change == to !="
Line 14 - change elif: to else:
Line 15 - close_objects = False (x2)
Line 16: add a colon to the end
Line 17: for j in range(len(posx)):
Line 19: **2 on the second term
Line 20: f string
"""
import string

alphabet = list(string.ascii_lowercase)

snt = input('Check String: ')
for letter in snt.lower():
    if letter in alphabet:
        alphabet.remove(letter)

if not alphabet:
    print('All letters were in the string')
else:
    print('Some letters were missing: ' + ', '.join(alphabet))


def add_evens(L):
    total = 0
    for x in L:
        if x % 2 == 0:
            total += x
    print(x)
    return x

float('0.0')
