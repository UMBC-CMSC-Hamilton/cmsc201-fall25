"""

the_map = generate_map(size, seed)
for i in range(len(the_map)):
    print_map.append( f'{i} {the_map[i]}')


We talked about recursion last time:
    Recursion is when a function calls itself.

    We need a base case to prevent an infinite recursion
        you can also have many base cases

    But in python there's another safety feature too
        RecursionError that occurs after 1000 recursion depth

    Recursive case is the place where the recursion is called inside the function
        you can have many of these
"""

def ab_maker(n, current=''):
    if n == 0:
        print(current)
        return
    ab_maker(n - 1, current + 'a')
    ab_maker(n - 1, current + 'b')


"""
What if instead of printing all combinations of a's and b's we want specifically the combinations where the 
    number of a's is equal to the number of b's
    
aabb
abab
baba
abbb [not]

Thinking:
    aaxx +2 on A's 
    bbxx -2 on A's
    
    bbaa #a's - #b's = 0 for any correct answer
    abab
    baba
    abba
    baab all going to be zero when you subtract the number of a's - number of b's

    Add new parameter to the function call it diff = difference
"""

def ab_equal(n, diff = 0, current=''):
    if n == 0:
        # this detects when the number of a's is EQUAL to the number of b's
        # what if the number of a's is greater? diff > 0
        if diff == 0:
            print(current)
        return
    ab_equal(n - 1, diff + 1, current + 'a')
    ab_equal(n - 1, diff - 1, current + 'b')


def test_ab_stuff():
    n = int(input('Enter num: '))
    while n >= 0:
        ab_equal(n)
        n = int(input('Enter num: '))



"""
    Goal is to make sure that the characters are increasing
        abc yes
        acb no
        ADFpz yes, why? lower case letters start at 65 and upper at 97
        
    Base case:
        what happens on an empty string? is that increasing? yeah sure
        what happens on a string with a single character, is that increasing? sure 
    What do we need to check in our recursive case? 
"""
def detect_increasing(a_string):
    if len(a_string) <= 1:
        return True

    if a_string[0] < a_string[1]:
        return detect_increasing(a_string[1:])
    else:
        return False # another base case, it doesn't actually call a recursion.


the_string = input('>> ')
while the_string != 'quit':
    print(detect_increasing(the_string))
    the_string = input('>> ')

the_num = int(input('>> '))
while the_num != 0:
    print(chr(the_num))
    the_num = int(input('>> '))


