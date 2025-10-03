"""

    Exam 1 reviews have been posted.
        Solutions to the Fall 2023 exam.
    6:00 pm Tuesday - ROOM TBD - TA led review session

    Our Exam is Thursday 10-09 at 4:00 pm.

    HW5 will be released this friday, due next friday

    Labs next week are canceled (for the exam).

"""

"""

    Functions in Python.  
    
    Mutability - can an object be "modified"
        When you pass an argument which is an IMMUTABLE thing:
            int float string and booleans pass by VALUE => a copy is made that copy can be modified 
                doesn't affect the original value
        When you pass a mutable thing [list, dict, class]
            it passes by reference = a new variable name but it refers to the same underlying data
                if you modify that variable, the original list is also modified.  
    
    
    Scope - 
    
    Global Scope
        Lifetime - lives as long as the program does. 
        Accessibility - we can access a global variable anywhere in the program [after it's been defined]
    Local Scope
        Lifetime - as long as the current function is running
        Accessibility - we can access a local variable inside that function but the name is lost after the function 
            returns.  

"""

"""
    is prime function, how would we code that?
    
    if we want to check to see if a number is prime
        0 negatives, return False
        1 not prime return False
        otherwise run the prime check
    We need to know the number we're going to test.  
        n = number we're going to check
"""


def is_prime(n):
    if n <= 1:
        return False

    # 0 is Zero Division
    # 1 always divides
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


print(is_prime(-10))
print(is_prime(0))
print(is_prime(1))
print(is_prime(5), is_prime(9), is_prime(13), is_prime(51))

"""
    count the number of vowels in a word
    
    aeiou = vowels
    y = allow the programmer to turn on or off.  
    
    1st parameter = word
    2nd parameter = y is vowel or not
"""


def count_vowels(word, use_y):
    """
    :param word: a string
    :param use_y: Boolean whether to use y as a vowel.
    :return: the count of vowels
    """

    count = 0
    for c in word:
        if c.lower() in 'aeiou':
            count += 1
        elif c.lower() == 'y' and use_y:
            count += 1

    return count


print('isoscales', count_vowels('isoscales', False))
print('aardvarky', count_vowels('aardvarky', True))
print('by', count_vowels('by', False))
print('queueing', count_vowels('queueing', False))
print('', count_vowels('', False))

"""
    mean average of a set of values
    
        parameters:
            list of the numbers
        
"""


def mean(the_list):
    """
    :param the_list: a list of numbers (ints or floats)
    :return: the mean average of those numbers
    """
    if len(the_list) == 0:  # not the_list
        return 0

    total = 0
    for x in the_list:
        total += x
    return total / len(the_list)


print(mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(mean([]))
print(mean([4, 4, 4, 4, 4]))
print(mean([6, 9, 3, 5, 6, 7, 5, 1, 6, 6, 4, 4, 6, 4, 4, 6, 4, 6]))


"""
    Remove all elements from a list, that match x <- input value

    parameters = the_list, x
"""
def remove_all(the_list, x):
    while x in the_list:
        the_list.remove(x)
    return the_list


random_list = [4, 6, 9, 1, 4, 5, 6]
guess = random_list.append(7)
print(guess)
guess = random_list.remove(9)
print(guess)


"""
    Fibonacci numbers as a function
    
    F(n) = F(n - 1) + F(n - 2)
    F(0) = F(1) = 1
"""

def fibonacci(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    current = 0
    prev = 1  # F(1)
    two_prev = 1 # F(0)
    for i in range(2, n + 1):
        current = prev + two_prev

        two_prev = prev
        prev = current

    return current

print(fibonacci(-5), fibonacci(0))
for i in range(1, 20):
    print(i, fibonacci(i))


"""
    first = [2, 4, 7, 2, 4, 9, 1]
    second = [2, 9]
    
    remove all/any instance of an element from the second list in the first list 
"""
def list_difference(first_list, second_list):
    for x in second_list:
        while x in first_list:
            first_list.remove(x)
    return first_list


def list_difference_again(first_list, second_list):
    for x in first_list:
        pass  # can be made to work but has some issues because of the example down below.

    # return first_list


"""
    when you get to the index 6, you remove a 3 the next 3 shifts down and gets missed by the loop
"""
stuff = [1, 2, 4, 3, 9, 4, 2, 3, 3, 4]
#  0  1  2  3  4  5  6  7
# [1, 2, 4, 9, 4, 2, 3, 4]
for x in stuff:
    if x == 3:
        stuff.remove(3)
    print(stuff)