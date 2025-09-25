"""
    What is if __name__ == '__main__':

        void main() {}
        int main() { return 0; }
        public static void main( String [] args )

    What is the equivalent in python?
        There is no 'main' FUNCTION in python = there is no function name that will be called without you calling it

    if __name__ == '__main__':
        there are some secret variables that python defines whenever a script is running.

"""

print(globals())
print(__name__)
import new_file

if __name__ == '__main__':
    # tests to see if the current file is the one being run
    print('yes we are the main file')
    # useful for testing out individual files
    # useful for checking to make sure the current file is the one that the user is actually running, not being imported
    x = 3
    x **= 0.5

"""
    back to for loops
    
    s(n) = n^2 + 5n - 3
"""

n = int(input('How far do you want to evaluate the sequence? '))
for i in range(n + 1):
    print(f's({i}) = {i ** 2 + 5 * i - 3}')


"""
    Fibonacci 
        1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
    
"""
prev_1 = 1
prev_2 = 1
current = 0

n = int(input('How far do you want to calculate Fibonacci numbers? '))
for i in range(n + 1):
    current = prev_1 + prev_2
    print(f'The {i + 2}th fibonacci number is {current}')
    prev_2 = prev_1
    prev_1 = current
    # you have to assign prev2 first so that we don't overwrite prev1 before we actually push the values down


# draw a box
# nesting loops
height = int(input('Tell me the height: '))
width = int(input('Tell me the width: '))

for y in range(height):
    for x in range(width):
        print('*', end='')  # print automatially puts a newline at the end, i'm turning that off
    print()  # this will print the newline and push us down.



# draw a triangle.

for y in range(height):
    for x in range(width):
        if x < y + 1:
            print('*', end='')  # print automatially puts a newline at the end, i'm turning that off
    print()  # this will print the newline and push us down.

print('\n\n') # \n prints a newline

# draw a triangle.

for y in range(height):
    for x in range(width):
        if x < height - y:
            print('*', end='')  # print automatially puts a newline at the end, i'm turning that off
    print()  # this will print the newline and push us down.


# draw an X

"""
*  *
 **
*  *
      0123456
y = 0 *     * x = 6 - y
y = 1  *   *
y = 2   * *
y = 3    *
y = 4   * *
y = 5  *   *
y = 6 *     * y = x line


"""

print('\n\n') # \n prints a newline

for y in range(height):
    for x in range(width):
        if x == y or y == height - 1 - x:
            print('*', end='')  # print automatially puts a newline at the end, i'm turning that off
        else:
            print(' ', end='')
    print()  # this will print the newline and push us down.


# x^2 + y^2 = r^2
for y in range(-1 * height, height + 1):
    for x in range(-1 * height, height + 1):
        if (height - 1/2) ** 2 <= x ** 2 + y ** 2 <= (height + 1/2) ** 2:
            print('*', end='')  # print automatially puts a newline at the end, i'm turning that off
        else:
            print(' ', end='')
    print()  # this will print the newline and push us down.


"""
    Non-shape drawing...
        find the maximum of elements in a list
"""

my_list = []
for i in range(10):
    x = int(input('Tell me an int: '))
    my_list.append(x)

the_max = my_list[0]  # what you might do if you're a little lazy... mostly it's going to work
for x in my_list:
    if x > the_max:
        the_max = x

print(f'The max value is {the_max}')

the_min = my_list[0]
for x in my_list:
    if x < the_min:
        the_min = x

print(f'The min value is {the_min}')



the_max_index = 0  # works as long as the list isn't empty.  [always check for empty lists]
for i in range(len(my_list)):  # for i rather than for each
    if my_list[i] > my_list[the_max_index]:
        the_max_index = i

print(f'The max value is {my_list[the_max_index]} at position {the_max_index}')

"""
    count the number of a's in a particular string
"""

my_string = input('TELL ME STRING: ')
count = 0

for c in my_string:
    if c.lower() == 'a':
        count += 1

print(f'The a count is {count}')

"""
    Escape Sequences
    
    \n = newline
    \t = tab
    \\ = backslash
    \r = carriage return
    \u2313
    \a = kinda doesn't really work
"""