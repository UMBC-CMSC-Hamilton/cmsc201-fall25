"""

    What is a while loop?

        unlike a for loop which usually scans through a range object [indices]
                or a list, or dictionary, to see each element
        a while loop is basically an if statement on repeat.
"""

my_string = input('Tell me a string: ')
while 's' in my_string.lower():
    my_string = input('Tell me a string: ')

"""
infinite loop, slight problem

for loops don't loop infinitely but while loops [[can]]
"""
if False:
    x = 1
    while x > 0:
        print(x)
        # input()
        x += 1

"""
skipped loop - if the while condition is false, then the loop doesn't execute at all. 
"""

my_var = True # be careful here, even if you want my_var to be False once you enter the loop, you have to make sure
    # that you get into the loop the first time.
x = 20
while x > 0 and my_var:
    if input('Set myvar to false? ').lower().strip() == 'yes':
        my_var = False
    x -= 1

    print(x)


"""
    all for loops can be recoded into while loops, but not the other way
    not all while loops can be made into for loops.  
"""

total = 0
for i in range(20):
    total += i ** 2 + i + 2
print(f'The total is {total}')

total = 0
i = 0
while i < 20:
    total += i ** 2 + i + 2
    i += 1  # manually increment this variable, don't forget or it's an infinite loop


my_list = ['a', 't', 'r', 'a', 'q', 'v', 'a', 's', 'a']
count = 0
for x in my_list:
    if x == 'a':
        count += 1

count = 0
index = 0
while index < len(my_list):
    if my_list[index] == 'a':
        count += 1

    index += 1

# user validation loops
"""
    We're not allowed to give you the wrong data type:
        "Enter a positive integer" --> not allowed to say "horse"
    I'm allowed to do this:
        "Enter a positive integer" --> -12
    I can give you bogus values as long as they are the correct data type
"""
the_num = int(input('Enter a positive number '))
while the_num <= 0:
    the_num = int(input('That was not positive, Enter a positive number '))

print(200 // the_num)

my_name = input('Enter your name (only two things): ')
names = my_name.split()
while len(names) != 2:
    print('Please enter a first and last name, make it two parts only. ')
    my_name = input('Enter your name (only two things): ')
    names = my_name.split()  # variable is being modified as the last thing here, before we go back up


"""
    You run a while loop whenever you DON'T KNOW how many iterations you're going to run.
        len(the_list) -> you know
        range(100) -> you know
        for x in my_object: -> len(my_object) -> you know
        
"""


"""
    Newton-Raphson Method
    
    f(x) = 0
    
    x_{n + 1} = x_n - f(x) / f'(x)

    f(x) = x^2 - 5 = 0 ==> 5 = x^2 ==> sqrt(5) = \\pm x

    f'(x) = 2x

"""

prev = 0
current = 1
error = 0.00001
while abs(current - prev) >= error:
    prev = current
    current -= (current ** 2 - 789) /  (2 * current)
    print(current)


"""
    What else uses a while loop?
        GUI = Graphical User Interface 
        TUI = Text User Interface (it is all that was)
        CLI = Command Line Interface
    
    GUI = web browser, pycharm, books, calculator, texting programs
        while the_message != WM_QUIT:
            is it a keyboard press -> do something
            is it a mouse click -> do something else?
            is it a window resize -> redraw things
            
    Servers = while server_message != QUIT:
        request = get_request()
        figure out if it's valid
        check permissions
        send them the meme or the site or whatever
            
"""

"""
Think of something that isn't validation, isn't approximation... 
    weirdness
"""

i = 0
while i < 100:
    letter = input('Enter a, b, c: ').lower()
    if letter == 'a':
        i += 1
    elif letter == 'b':
        i += 5
    elif letter == 'c':
        i += 2

    print(i)



for i in range(10):
    x = input('>> ')
    print(i)
    if x == 'inc':
        i += 1
    print(i)


