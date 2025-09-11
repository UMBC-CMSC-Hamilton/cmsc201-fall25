"""
https://bitvise.com/download-area - for pc
https://cyberduck.io/download/ - for mac
    You have to change the protocol from FTP to SFTP

You can navigate on the GL server and then drag and drop files to transfer.
Once you transfer you can then open an ssh terminal and submit.
    just sending the files to the GL server doesn't submit.

Let's talk about conditionals

condition is an expression which evaluates to True or False
if it's True, then the if statement executes, if not then it gets skipped
there is a syntax feature

if [condition]:
    code
    more code
    even more code

end of if statement
"""

the_word = input('What is a word? ')
# assignment is =, testing is ==
if the_word == 'happy' or the_word == 'sad':
    print('That is an emotion')

if the_word == 'happy' or 'sad':
    pass
"""
# 1) python has an order of operations called operator precedence
        highest precedence = first thing that happens = algebra
        next precedence is conditional operators
            == <=. >=, !=, <, >,  in [keyword]
        lowest precedence (logical operators)
            not
            and, or
  2) Variables / Values have a truth value 
  
        Integers are true when they are not zero, if zero ==> False (0)
        Floats are true when they are not zero, else, if zero ==> False (0.0)
        strings are true when they are not empty, else False ==> '' [the empty string]
    
"""

is_good = False
is_bad = True

if is_good or is_bad:
    print('it is either good or bad')


if 'happy':
    print('one of these is true')

if '':
    print('the empty string is true')

x = 0
y = 2
if x or y:
    print('x or y')


"""
    or and not
    
    A or B = inclusive or
    A \\ B       True    False
    True        True    True
    False       True    False
    
    exclusive or = you can only accept one
    ^ = bitwise xor = exclusive or
    
    A and B     True    False
    A \\ B 
    True        True    False
    False       False   False
    
    not A
    True        False
    False       True

not A or B
--> (not A) or B
XXX not (A or B)
"""

"""
elif and the else
else if = an if statement that checks the condition when the prior if statements are False.

else = a statement that executes when ALL of the if/elif statements are False
    catchall for everything that didn't happen. 
"""
x = 0
while x != -10:
    x = int(input('Tell me a number: '))
    if x == 1:
        print('hello there')
    elif x == 2:
        print('I like robots')
    elif x == 3:
        print('Turnips')
    elif x == 4:
        print('Four is a square')
    elif x == 5:
        print('Five is prime')
    else:
        print('Oh well try again...')

x = 5
while x > 0:
    x = int(input('NUMBER!!! '))

    if x > 1000:
        print('x is really big')
    elif x > 100:
        print('x is kinda large')
    elif x > 0:
        print('x is positive')


    if x > 1000:
        print('x is really big')
    if x > 100:
        print('x is kinda large')
    if x > 0:
        print('x is positive')


# month of the year
# we're going to enter a number of months, 0 -> infinity
# what month that is in whatever year it ends up being.
num_months = 0
while num_months != -100:
    num_months = int(input('How many months? '))
    # mod_months = num_months % 12
    if num_months % 12 == 1:
        print('January')
    elif num_months % 12 == 2:
        print('February')
    elif num_months % 12 == 3:
        print('March')
    elif num_months % 12 == 4:
        print('April')
    elif num_months % 12 == 5:
        print('May')
    elif num_months % 12 == 6:
        print('June')
    elif num_months % 12 == 7:
        print('July')
    elif num_months % 12 == 8:
        print('August')
    elif num_months % 12 == 9:
        print('September')
    elif num_months % 12 == 10:
        print('October')
    elif num_months % 12 == 11:
        print('November')
    elif num_months % 12 == 0:
        print('December')


"""
Nesting - 
    if statement inside of an if statement

    Star Wars
"""

while True:
    human = input('Are you human? ')
    if human.lower() == 'yes':
        smuggler = input('Are you a smuggler? ')
        if smuggler.lower() == 'yes':
            print('You are Han Solo')
        else:
            light_side = input('Are you on the light side? ')
            if light_side.lower() == 'yes':
                num_hands = int(input('How many hands do you have? '))
                if num_hands == 1:
                    print("You are Luke")
                else:
                    would_work = input('Did you really think Old Ben Was going to hide you from the empire? ')
                    if would_work.lower() == 'yes':
                        print('You are Obi Wan, that could not have worked')
                    else:
                        print('You are Leia')
            else:
                legs = input('Do you have legs?')
                if legs.lower() == 'yes':
                    print('You are Palpatine, unlimited powwwaaaa')
                else:
                    print('You are Darth Vader, breathing noises')
    else:
        droid = input('Are you made of metal? ')
        if droid.lower() == "yes":
            garbage_can = input('Do you resemble a garbage can? ')
            if garbage_can.lower() == 'yes':
                print('You are R2D2')
            else:
                print("Oh My. Oh no. C-3PO")
        else:
            walking_carpet = input('Have you been called a walking carpet? ')
            if walking_carpet.lower() == 'yes':
                print('You are Chewbacca')
            else:
                print('You are probably Jabba the Hutt')







