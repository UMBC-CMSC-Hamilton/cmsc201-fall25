"""

    recursion

        recursion is when a function calls itself
        why do we need it?
            sometimes you need to solve a problem that involves something that needs more than a loop
            branching occurs when you have to make a choice, but you don't know which choice is right

            it's a bit harder to do some of this kind of thing iteratively = using loops

            L F R (but you don't know which) the algorithm should try all of them.

        first example of recursion we'll do doesn't actually branch
            you don't even have to do it recursively.  But I will because it's helpful to see

        Factorial

            n! = n * (n - 1)!
            0! = 1 [base case]

            5! = 5 * 4! = 5 * 4 * 3! = 5 * 4 * 3 * 2! = 5 * 4 * 3* 2 * 1! = 5 * 4 * 3 * 2 * 1 * 0! = 5 * 4 * 3 * 2 * 1 = 120

    rec_fact(5)
        return 5 * rec_fact(4) [pause button]
        [unpause]
        return 5 * 24 = 120
        [done]
    rec_fact(4)
        return 4 * rec_fact(3) [pause]
        [unpause]
        return 4 * 6 = 24
    rec_fact(3)
        return 3 * rec_fact(2) [pause]
        [unpause]
        return 3 * 2 = 6
    rec_fact(2)
        return 2 * rec_fact(1) [pause]
        [unpause]
        return 2 * 1
    rec_fact(1)
        return 1 * rec_fact(0) [pause]
        [unpause]
        return 1 * 1
    rec_fact(0)
        return 1

rf(0) ->  returns 1 stops the recursion [pops off the stack]
    [pop = remove the top element]

rf(1) [pop]
rf(2) [pop]
rf(3) [pop]
rf(4) [pop]
rf(5) [pop]
================

"""


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def rec_fact(n):
    # base cases
    if n <= 0:
        return 1

    return n * rec_fact(n - 1)


for i in range(1, 21):
    print(i, factorial(i), rec_fact(i))

"""
    Fibonacci 
        fib(0) = fib(1) = 1
        fib(n) = fib(n - 1) + fib(n - 2)

    branching recursion
"""


def fib(n):
    if n < 2:
        return 1

    return fib(n - 1) + fib(n - 2)


# not necessary for CMSC 201
# import sys
# import math
# sys.setrecursionlimit(5000)
# print(math.log(rec_fact(2000), 10))


for i in range(1, 30):
    print(i, fib(i))

"""
    Letters
    
        count the number of a's in a string RECURSIVELY FOR NO REASON
"""


def count_as(the_string):
    """
    :param the_string:
        what's the simplest string you can imagine? empty
    :return:
    """

    print(the_string)
    if not the_string:
        return 0

    if the_string[0].lower() == 'a':
        # 1 + number of A's in the rest of the string
        # count_as will consider the string after we pull off the first letter which was an a
        return 1 + count_as(the_string[1:])
    else:
        # here the first letter is NOT an a, so we pull it off and it doesn't affect the count.
        return 0 + count_as(the_string[1:])


print(count_as('aaaaa'))
print(count_as('aardvark'))
print(count_as('avacado'))
print(count_as('quiet'))

"""
ballerina = 0 + count(allerina) = 0 + 2 = 2
allerina = 1 + count(llerina) = 1 + 1 = 2
llerina = 0 + count(lerina) = 0 + 1 = 1
lerina = 0 + count(erina) = 0 + 1 = 1
erina = 0 + count(rina) = 0 + 1 = 1
rina = 0 + count(ina) = 0 + 1 = 1
ina = 0 + count(na) = 0 + 1 = 1
na = 0 + count(a) = 0 + 1 = 1
a = 1 + count(empty) = 1 + 0 = 1
empty = 0
"""

"""
    racecar => return True
    aceca => return True
    cec => return True
    e => return True
    
    racefar => return False
    acefa => return False
    cef => return False

    tacocat
    racecar
    amanaplanacanalpanama

    base case (what is the simplest input, that we know the output for?)
        Is '' a palindrome? 
        Is 'aa' a palindrome? yes
        Strip off the A's then we get '' => revesed is '' so it's a palindrome, not a very interesting one.  
        Is 'c' a palindrome? 'f' 'd' 'p' yes
        Any string of length 1 or 0 is a palindrome
"""


def palindrome(a_string):
    print(a_string)
    if len(a_string) <= 1:
        return True
    if a_string[0] == a_string[len(a_string) - 1]:
        # we found a match, keep going
        return palindrome(a_string[1:len(a_string) - 1])
    else:
        # we found a non-match, return False
        return False


message = ''.join(input('>> ').split())
while message != 'quit':
    print(message, palindrome(message))
    message = ''.join(input('>> ').split())

"""
I want every combination of a's and b's [order matters, repetitions allowed]

n = 4
aaaa
aaab
aaba
aabb
abaa
abab
abba
abbb
baaa
baab
baba
babb
bbaa
bbab
bbba
bbbb

n = 2

aa
ab
ba
bb

n = 3


aaa
aab
aba
abb
baa
bab
bba
bbb

Thinking:
    To make strings of length n we need all the strings of length n - 1 and then add an 'a' to the front
        also we need all the strings of length n - 1 and add a 'b' to the front

Base case in this case?
    n = 0
        ''
n = 1
    a 
    b
"""



# default parameters work when the programmer does not enter an argument for that slot, it gets populated by the value ('')
def ab_maker(n, current=''):
    if n == 0:
        print(current)
        return
    ab_maker(n - 1, current + 'a')
    ab_maker(n - 1, current + 'b')


n = int(input('Enter num: '))
while n >= 0:
    ab_maker(n)
    n = int(input('Enter num: '))
