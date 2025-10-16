"""
Python has a built in file opening function, called open

    Why do we need files outside of the python program?
        You have data that you need to store, and you want that data to survive the restart/shudown of the program itself.

file_object = open('filename', mode)

r = read mode

w = write mode

a = append mode

when you open a file, the operating system gives you a "handle = code" that tells the operating system what file is opened
    and where in the file you are currently reading from (cursor inside the file)
Why do we close files?
    if we leave them open and your program shuts down, ends, or crashes, it's possible that the file handle will be
    left open, stay allocated.  OS may not know that it's not in use anymore
    if you reopen the program, then it may actually not give you permission to read or write from that file.
    Happens with write mode more than read mode.
"""

stuff_file = open('stuff.txt', 'r')  # opens a file
print(stuff_file.read())
stuff_file.close()  # close a file

# future life stuff, not 201 necessary
stuff_file = open('stuff.txt', 'r')  # opens a file
x = stuff_file.read(50)
print(x, len(x))
x = stuff_file.read(50)
print(x, len(x))
stuff_file.close()  # close a file

"""
    All the ways you can read through a file:
    
    .read() = reads the entire file

    .readline() = reads a single line    
        reads until a \n but does not strip the \n

    .readlines() = read all of the lines and put them into a list
        more like .read() than .readline in a way reads the entire file.  
        splits('\n')         

    for each loop will do it.  
    for line in my_file:
        print(line)
"""


# future life stuff, not 201 necessary
stuff_file = open('stuff.txt', 'r')  # opens a file
x = stuff_file.readline()
print(x, list(x))
print(stuff_file.readline().strip())
print(stuff_file.readline(), end='')
stuff_file.close()  # close a file


test_file = open('test.dat')
dimen = test_file.readline()
row, col = dimen.split()
row = int(row)
col = int(col)
print(row, col)
for i in range(row):
    print(test_file.readline())

the_line = test_file.readline()
while the_line:  # if the readline returns EMPTY not just \n but totally empty, then it's at the end.
    # do more stuff
    the_line = test_file.readline()

test_file.close()

test_file = open('test.dat')
dimen = test_file.readline()
row, col = dimen.split()
row = int(row)
col = int(col)
print(row, col)
print(test_file.readlines())  # the newline is not stripped, you have to do that (if you need to)
test_file.close()



test_file = open('test.dat')
for line in test_file:
    print(line, end='')
print('reading again')
print(test_file.readline())
print('Done reading')
test_file.close()


"""
how do we write into a file?
    .write()  # takes a string
    .writelines()  # takes a list
    
    ==> neither one will add the \n character so you have to do it.  
    
    DO NOT OPEN A FILE IN WRITE MODE IF YOU NEED THAT DATA
    IT WILL ERASE THE FILE AND PUT THE CURSOR AT THE START
"""
if False:
    new_file = open('new_file.txt', 'w')
    write_string = input('>> ')
    while write_string != 'quit':
        new_file.write(write_string + '\n')
        write_string = input('>> ')
    new_file.close()


    with open('music_file.txt', 'w') as music_file:
        music_stuff = []
        music = input('Enter Music: ')
        while music:
            music_stuff.append(music + '\n')
            music = input('Enter Music: ')

        music_file.writelines(music_stuff)
    # once you leave the with statement it closes your file for you


"""
What is append mode?
    you open the file with write permissions but instead of blanking the file out you set the cursor at the end and you can add
"""

with open('new_file.txt', 'a') as new_file:
    write_string = input('>> ')
    while write_string != 'quit':
        new_file.write(write_string + '\n')
        write_string = input('>> ')

"""
What is a log file?
    
    When you write a big program, things go wrong.
    If you have 1000 people running your program you're not there when bad things happen.
    Files that just log what's going on.  
    Log files are the biggest example of an append mode

"""

