the_string = input('Enter a string: ')
letters = input('Enter allowed letters: ')
letter_list = letters.split()
the_biggest = ''
for x in the_string:
    if x.lower() > the_biggest and x.lower() in letter_list:
        the_biggest = x.lower()

print(the_biggest)

"""
+2 input the strings
+2 use split to get the letters in the list
+3 for loop over the first list (doesn't matter if it's a for each or for i)
    technically they could use a while loop too but why?
+3 correct condition for the max checking. 
+1 Set the maximum
+1 Output the result [doesn't really have to match exactly] 

"""


n = int(input('Input an Integer: '))
steps = 0
current = 1
while current < n:
    steps += 1
    current *= 3

print(f'It took {steps} steps to reach {current} > {n}')


"""
+2 input an integer (input and cast)
+2 declare initial variables
+4 use a while loop (2 for the loop, 2 for a correct condition)
+2 increment a step and multiply the other variable
+2 output the result
"""


s = ''
i = 1
while i < 20:   # here's a commnet
    s += 'a'
    i *= 2
print ( s )

# here's another comment
