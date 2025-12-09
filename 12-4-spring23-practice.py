"""
Final Exam: Friday 12th at 6:00 - 8:00 pm

[rooms TBD]

"""

L = [51, 24, 33, 71, 89, 31, 12, 5, 19, 1]
"""
0th [51, 24, 33, 71, 89, 31, 12, 5, 19, 1]
1st [24, 33, 51, 71, 31, 12, 5, 19, 1, 89]
2nd [24, 33, 51, 31, 12, 5, 19, 1, 71, 89]
3rd [24, 33, 31, 12, 5, 19, 1, 51, 71, 89]

Selection Sort
 [5,7,12,31,24,1,17,3,9,2]
finds the minimum and swaps
0th [5,7,12,31,24,1,17,3,9,2]
1st [1,7,12,31,24,5,17,3,9,2]
2nd [1,2,12,31,24,5,17,3,9,7]
3rd [1,2,3,31,24,5,17,12,9,7]

"""


"""
15. Write a boolean expression which is True if and only if a list sandwich contains the strings
 ’ham’, ’cheese’, and ’mayo’, but not ’tuna’.
 
 
 16. Write a boolean expression which is True if and only if a variable x is at least two times the
 value of a variable y or ’happy’ is in the string emotion but not both.

    Exclusive or, only one is true, (a and not b) or (b and not a)
"""
sandwich = []
'ham' in sandwich and 'cheese' in sandwich and 'mayo' in sandwich and not 'tuna' in sandwich

emotion = ''
x = 0
y = 0

((x >= 2 * y and 'happy' not in emotion) or \
 (x < 2 * y and 'happy' in emotion))

"""
17) Example
    [1 2 5 10 20] searching for 2 this will work
    [1 20 5 10 2] searching for 2 again, 
        midpoint is 5 so we go left:
    [1 20] => search the element 20 != 2, search 
    [1] 1 != 2 return False
"""


def search_list(a_list, element):
    print('searching for', element)

    for x in a_list:
        if x == element:
            print(element, 'found')
            return True
    print(element, 'not found')
    return False


def create_list(start, stop, step):
    new_list = []
    for i in range(start, stop, step):
        new_list.append(i)
    return new_list

a_list = create_list(3, 100, 2)  # [3, 5, 7, 9, ... 99]
b_list = create_list(0, 51, 5)   # [0, 5, 10, 15, 20, 25, ..., 50]
search_list(a_list, 77)  # Prints: Searching for 77, 77 found
search_list(a_list, 22)  # Prints: Searching for 22, 22 not found
search_list(b_list, 50)  # Prints: Searching for 50, 50 found
search_list(b_list, 24)  # Prints: Searching for 24, 24 not found


def calculate_inner(a, b, c):
    print('inner', a, b, c)
    if a > b:
        return (a - b) * c
    else:
        return a * b

"""
======================================
inner 6 3 0
middle 6 3 0
inner 3 6 9
middle 3 6 18
outer 3 6 39
======================================
work
calculate_outer(3)
 call w = calculate_middle(6, 3) = 6
    x = calculate_inner(6, 3, 0) = 0
 call z = calculate_middle(3, 6) = 39
    x = calculate_inner(3, 6, 9) = 18
    

    x = calculate_inner(a, b, 2 * b- a)
    print(’middle’, a, b, x)
    return 2*x + a
"""

"""
24)
row_list = [1, 2, 3, 4]
my_list = [row_list, row_list, row_list]

row_list = [1, 2, 7, 4]

why is it 1 2 7 4 printed 3 times?
    because each element in my_list is a reference to row_list, NOT a copy of a list [1,2 ,3, 4]
    all the exact same data, when we modify row_list we change them all.  
    
How do you get this not to happen?
my_list = [list(row_list), list(row_list), list(row_list)]

"""

"""
Write out how a binary search for the element 6 works on this list below. Write for each
 step the index that you are considering as the midpoint and whether you go up or down
 (right/left), or you can write out the part/slice of the list that you are still considering.
 [1, 2, 6, 8,12,30,41,46,51,77] n = 10
 index = 10//2 = 5
Go to 30: 6 < 30 go left
[1, 2, 6, 8, 12] n = 5
    midpoint = 5//2, value = 6
    6 == 6, return True
"""


"""
Write a recursive function that outputs all combinations of a’s, b’s and c’s of length n which
 is the parameter given to the function. The second parameter current will be set to ” (an
 empty string) when the function is called.
"""

def abcs(n, current):
    if n == 0:
        print(current)
    else:
        abcs(n - 1, current + 'a')
        abcs(n - 1, current + 'b')
        abcs(n - 1, current + 'c')

"""
n = 2:

aa
ab
ac
ba
bb
bc
ca
cb
cc
"""


"""
You are writing part of a program’s login features where if a user has not performed an action
 within 30 minutes then they should be logged out for security purposes. A dictionary of users
 where the keys are usernames will be sent to you, this outer dictionary contains dictionaries
 with a key named ’last-access’ which is an integer in minutes. You must return a list of
 usernames to be logged out who have not been active.
 Here is an example of the dictionary you may be given:
 
  users = {
 ’eric8’: {’credits’: 3, cart: [’typewriter’], ’last-access’: 27},
 ’jeanlucp’: {’credits’: 7, cart: [’flute’], ’last-access’: 55},
 ’rikerwt’: {’credits’: 100, cart: [’trombone’], ’last-access’: 31}
 }
"""


def find_inactive_users(users):
    log_em_out = []
    for username in users:
        if users[username]['last-access'] >= 30:
            log_em_out.append(username)
    return log_em_out


