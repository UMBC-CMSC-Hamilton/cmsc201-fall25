"""

List Comprehensions
    you can have a for expression within array brackets, dictionary brackets


"""

new_list = []
for i in range(10):
    new_list.append(i + 1)

print(new_list)

#               function/expression  for i in some iterable object
newer_list = [i + 1 for i in range(10)]
print(newer_list)

square_list = [i ** 2 for i in range(100)]
print(square_list)

words = ['happy', 'to', 'sad', 'robots', 'fishing', 'queueing', 'bamboo']

word_map = {word: len(word) for word in words}
print(word_map)

list_of_ints = [2, 8, 4, 3, 6, 7, 8, 9, 10, 2]
# annoying problem in python:
# can we output this list with hyphens between each number?
print(' - '.join([str(x) for x in list_of_ints]))

"""
Ternary expressions = something that exists in other languages
    condition ? if_true_thing : if_false_thing
"""

x = int(input('Tell me an integer: '))
y = int(input('Tell me an integer: '))

print(y // x if x != 0 else -1)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_list = [k if is_prime(k) else -1 for k in range(100)]
print(prime_list)
# only add to the list if the is_prime comes back true.
new_prime_list = [k for k in range(100) if is_prime(k)]
print(new_prime_list)

students = {}
honors_list = [student for student in students if student['gpa'] > 3.75 and student['credits'] < 120]


"""
    try except raise
        
        try catch throw [other languages = C++, Java, javascript, most languages] 
"""


float_entered = False
while not float_entered:
    try:
        # the error occurs when float is called
        f = float(input('Enter a float please, pretty please, not a string, please: '))
        index = int(input('Enter an index for the list: '))
        print(index, new_prime_list[index])
        # if the error happens, we never get to this line
        float_entered = True
    except ValueError as ve:
        print(ve)
        print('No fluffy, bad.  ')
    except IndexError as ie:
        print('That was a bad index.  ')


try:
    import bad_file
    if r and s:
        print('hi')
except SyntaxError as se:
    print("There was a syntax error", se)
except NameError as the_name_error:
    print(the_name_error)



def average(the_list):
    if not the_list:
        raise ValueError('The list is empty, no average is possible. ')

    return sum(the_list) / len(the_list)



try:
    empty_list = []
    average(empty_list)
except ValueError as ve:
    print(ve)


class NonsenseError(BaseException):
    pass

try:

    raise NonsenseError('hello there')
#except NonsenseError as ne:
#    print(ne)
except:
    print('Something happened')

x = 10
while x > 0:
    x -= 1
else:
    print('hi')

two_d = [[i + j for i in range(5)] for j in range(5)]
print(two_d)

try:
    filename = input('What is the filename: ')
    file_handle = open(filename, 'r')
    print(file_handle.read())
except FileNotFoundError:
    print('The file was not found. ')
except FileExistsError:
    print('The file already exists. ')
finally:
    # if any error happens, do this to cleanup
    print('Now this. ')