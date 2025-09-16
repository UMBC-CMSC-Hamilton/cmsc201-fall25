"""

Lists in python.
    int, string, bool, lists can be an object
    need to store a number of them

    array - another term you sometimes hear for them

    starts out empty in general
"""
my_empty = []  # you don't have to declare the size of the list or anything, it can resize dynamically
other_empty = list()  #

my_empty.append("prunes")
my_empty.append("apples")
my_empty.append("turnips")

print(my_empty)

# indices are the place in the list where you can find the element
#           0  1  2  3  4  5
new_list = [3, 9, 2, 8, 4, 1]
# always goes from zero to one less than the length of the array.

print(new_list[0], new_list[3], new_list[5])
new_list[2] = 17
print(new_list)

print(len(new_list))

x = int(input('Tell me an index'))
# chained inequality if 0 <= x and x < len(new_list)
if 0 <= x < len(new_list):
    print(new_list[x])
else:
    print('That index was out of range. ')

"""
Two ways to remove an element from a list
    
    By element value
        .remove(x) - finds and removes the first instance of x in the list.  
        not in the list => ValueError
            to avoid that check if the object is in the list with the in keyword.  
    By index
        del keyword
        removes by index not element
"""

big_list = [2, 8, 1, 4, 9, 2, 3, 5, 4, 7, 6, 4, 4, 3, 9]

big_list.remove(4)
print(big_list)

other_list = [2, 2, 2, 2, 2, 2]
print(other_list)
y = int(input('What do you want to remove? '))
if y in other_list:
    other_list.remove(y)

print(other_list)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

del numbers[4]
print(numbers)
#                0  1  2  3  4  5
other_numbers = [5, 3, 7, 9, 2, 1]
del other_numbers[4]
print(other_numbers)

# index error here
# del other_numbers[17]

# TypeError
# 4 + 'hello'

zebra = 3
del other_numbers[zebra]

print(other_numbers)

"""
    for loops - allows you to look through or modify a list element by element, scan through one at a time.  
    
for [variable] in [object - list, dictionary, range]:
    tabbed in code
    tabbed in code

outside of the for loop
"""

newer_list = [1, 9, 5, 6, 3, 4, 7, 6, 5, 3, 2]
for x in newer_list:
    print(x)

print('Now just the evens:')
for x in newer_list:
    if x % 2 == 0:
        print(x)


my_words = ['pies', 'cakes', 'spindle', '', 'train', 'steam', 'plane', 'robots']
# goal: pick out the words that start with 's'
#       012345
word = 'rabbit'
print(word[0], word[3], word[5])

for w in my_words:
    # short circuiting checks the first part of and statement, if false doesn't check the other
    # or when the first part of an or statement is TRUE
    if len(w) > 0 and w[0] == 's':
        print(w)

"""
    Let's talk about range...
    
    What if you just need all numbers between 0 and 9 [inclusively]
"""

for i in range(10):
    print(i, end=' ')


n = int(input('How high do you want to add? '))
# Goal 1 + 2 + 3 + 4 + .... + n #  Gauss sum, Faulhaber formula
total = 0
for j in range(n + 1):
    total += j
    # total = total + j
    # total -= j
    # total *= j
    # total //= 2
    # total **=2
print(total)

print(len(my_words))
for i in range(len(my_words)):  # range(len(a_list)) <-- memorize this
    print(f'At position {i} the word is {my_words[i]}')

"""
    More on the range object
        
        Rule: never is allowed to hit the stop, regardless of what start, step you're doing
    
        range(stop) = 0 ... (stop - 1)
        range(start, stop) = start, start + 1, start + 2, ..., stop - 1
        range(start, stop, step)
        
            step = increment        
"""

for x in range(2, 8):
    print(x, end=' ')

print()

for y in range(2, 100, 7):
    print(y, end=" ")

print('Starting z loop - doesn\'t do anything')  # \' = escape character, escape sequence
for z in range(30, 5, 2):
    print(z, end=" ")
print('\nEnding z loop')


for w in range(30, 5, -2):
    print(w, end=" ")

# how to scan through a list backwards
print('')
for i in range(len(my_words) - 1, -1, -1):
    print(my_words[i])


"""
    very python specific.  
    two different kinds of for loops
        for each loops
            scanning over elements of the list
            variable is a COPY of the element, not the element itself, can't actually modify it
        for-i loops
            for-i loop is one where the loop is over INDICES. 
            you can modify elements by index
        

"""
for w in range(len(my_words)):
    print(w, my_words[w])  # this is a for-i loop


best_list = ['a', 't', 'r', 'q', 'p']
for x in best_list:
    print(x, end=', ')
    x = 'z'
    print(x)

print(best_list)

for k in range(len(best_list)):
    best_list[k] = 'z'

print(best_list)


boring_list = [3, 9, 4, 8, 2, 7, 1]
# Goal: square every element that is odd (and change the list)
for i in range(len(boring_list)):
    if boring_list[i] % 2 == 1:
        boring_list[i] **= 2

print(boring_list)



