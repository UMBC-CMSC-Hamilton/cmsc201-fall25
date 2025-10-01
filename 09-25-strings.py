"""
    Strings - collection of characters

        ASCII - 8 bit code that determines what character it is
            65 -> A
            97 -> a
            32 -> space
            48 -> 0

                128 or 256 ASCII characters

                Unicode - 16 bit code
                    2 ^ 16 = 65536 total options
        Unicode
"""

print('\u2660', '\u2665', '\u2663', '\u2666')
print('\U0001F0D2')  # if you need the 32 bit stuff you have to put the 3 0's in front in general

"""

    The three methods.
        strip()
            removes whitespace from before and after text
            removes whitespace characters from the front and back until it encounters non-whitespace
                \r \n \t [spaces]
        split()
            if no arguments it splits on whitespace
            converts a string into a list of strings
            finds any instance of whitespace and then separates it into strings.  
                scans through any whitespace at the start and ignores it
                don't NEED to strip() before split() in general
                
            if there is an argument it splits on whatever it is, does actually go by block, not by character
        join()
            inverse function to split
            join takes a list of strings AND a separator and gives you back a single string.

"""

the_something = input('Say something: ')
print(the_something)
print(the_something.strip())

new_string = "   \n\n\n\n\t\t\t\t\t\t  hello \t\t\t\r\r\r\t\t\n\n\n\n\n        "
print(new_string)
print(new_string.strip())

something_else = input('Tell me something else: ').strip()
print(something_else)

heading = '==============================================Section Heading============================================'
print(heading.strip('='))

another = '=x=x=x=x=x=x=x=x=x=x=x=x=x=Something Good=x=x=x=x=x=x=x=x=x=x'
print(another.strip('x='))  # it strips by character, not by expression not looking for x=, x or =

story = input('Tell me a story: ')
print(story)
print(story.split())

command = input('Enter the command: ')
split_command = command.split()
if split_command[0] == 'something':
    print("We will do something")
    if len(split_command) == 3:  # always check to make sure that there's enough stuff in those indices before you access
        print('That is a good command')
    else:
        print('No, I dont want to do that.  ')

a_string = 'cabxabrabab'  # if abab it's going to give you an empty string as part of the list
print(a_string.split('ab'))

b_string = 'happyrobottwitterhappysadhappy'
print(b_string.split('happy'))

cpp_string = 'BaseObject::OtherThing::SubThing::ReallyCoolThing'
print(cpp_string.split('::'))

print('      xyzaaaaaaaaa'.strip('a '))
print('the tea is that we got away with it'.split('t '))

words = ['True', 'blah', 'fire', 'time', 'clock']
# separator goes first
print(" ".join(words))
print(" :: ".join(words))

letters = 'axyajoiefjlakdsiazaaahahaskaasjfoa'
split_stuff = letters.split('a')
print(split_stuff)
print('a'.join(split_stuff) == letters)

sentence = 'The quick      fox    jumped    over the     lazy     brown dog. '
more_words = sentence.split()
print(more_words)
print(' '.join(more_words))

print(sentence.split(' '))

the_message = input('WHat is the message: ')

threes = []
current = ''
for i in range(len(the_message)):
    if i > 0 and i % 3 == 2:
        current += the_message[i]
        threes.append(current)
        current = ''
    else:
        current += the_message[i]

print(threes)

"""
    Slices = python specific feature that allows you to take substrings by index
    
    a_string[start: stop]
    a_string[start: stop: step]
    
        start is inclusive, stop is exclusive [does not include it]
    
"""
#           0123456789
a_string = 'QWERTYUIOP'
print(a_string[2: 6], a_string[3: 9])

list_of_things = []
for i in range(len(the_message) // 3):
    list_of_things.append(the_message[3 * i: 3 * (i + 1)])
print(list_of_things)

print(a_string[4:200000])

print(a_string[:3])  # a_string[0:3] inserts the zero by default
print(a_string[3:])  # a_string[3: len(a_string)] inserts the length by default
print(a_string[:])  # autopopulates both terms 0 len(a_string)

my_list = [3, 1, 9, 2, 4, 2, 2, 4, 4, 3, 2, 5, 3, 3, 5, 3, 3, 5, 3, 4]
print(my_list[8: 15])
not_copy_of_list = my_list  # this makes a reference where now both variables can modify the same list
my_list[0] = 91
print(my_list)
print(not_copy_of_list)  # it's a reference

copy_of_list = my_list[:]
# copy_of_list = list(my_list)
my_list[0] = 14
print(my_list)
print(copy_of_list)


print(the_message[::-1]) # you can have negative step sizes and reverse the list, weird 2 or 3 step sizes and skip elements
a_list = ['a', 1, 'b', 2, 'c', 3, 'd', 5]
print(a_list[::2], a_list[1::2])


