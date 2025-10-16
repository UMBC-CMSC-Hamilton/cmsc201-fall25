"""
    What is a dictionary in python?

        You'll learn what these things are in CMSC 341.

        what if instead of having a list where you use indices what if you can use anything that is a "key"
            keys are immutable
            integer - good
            strings - good
            floats - be very careful with floats, floating point issues [roundoff error]
            bools - not super useful, usually not, but possible
        Elements are stored as "key: value" pairs
"""

random_thing = {True: 4, False: 123, 'for': 4, 'while': 10, 3.12345: 5, 5 / 3: 'Hi', 1 / 3 * 5: 'silly'}
print(random_thing)

the_words = {'hello': 2, "turtle": 5, "only": 17, "really": 4}

# access a dictionary through the keys:
print(the_words['hello'], the_words['only'])

print(5 / 3 == 1 / 3 * 5, 1 / 3 * 5)

the_words['yellow'] = 22
the_words['fluff'] = 73
the_words['chicken'] = 11
print(the_words)
# there isn't actually any guarantee that you'll get the same order as you put them in.
# there's no actual "preferred order" in a dictionary

"""
    Like lists:
        use for loops to iterate through them.  Can't use a for-i loop exactly. 
"""

number_keys = {42: 'hi', 73: 'world', 81: 'purpose'}
for x in number_keys:
    print(x, number_keys[x])

print(len(number_keys))

# this just doesn't work sadly
# for i in range(len(number_keys)):
#     print(number_keys[i])

number_keys[57] = 'apple'
number_keys[69] = 'orange'

"""
How do you remove a key: value pair?

del the_dictionary[the_key]
"""

del number_keys[69]
print(number_keys)

"""
In order to delete from a dictionary using a for loop you'll probably need something like this:
    because dictionaries don't allow you to update (add or delete) while you're running a for each loop over their keys
"""

delete_me = []
for key in number_keys:
    if number_keys[key] == 'apple':
        delete_me.append(key)

for key in delete_me:
    del number_keys[key]

add_me = [(12, 'value'), (13, 'key'), (14, 'whatever')]
for key in number_keys:
    if number_keys[key] == 'world':
        t = (37, 'money')
        add_me.append(t)
        # tuple = immutable list

# L = [(a, b), (c, d), (e, f)]
# key = a, value = b
# key = c, value = d
# key = e, value = f
for key, value in add_me:
    number_keys[key] = value

print(number_keys)

"""
    What else can we do with dictionaries?
"""

ids = {
    1234: ['Eric', 'eric8'],
    2345: ['Thom', 'thom123'],
    8585: ['Sarah', 'sarah7']
}

if 4392 in ids:
    print('It is')
else:
    print('It isn\'t')

if 'money' in number_keys:
    print('It is')
else:
    print('It isn\'t')

number_keys[47] = 'whatever'
print(number_keys)
number_keys[47] = 'something else'
print(number_keys)

"""
In development make sure that the unique thing whatever it is becomes the key
    the rest of the data becomes part of the value
"""

"""
Sometimes [rarely] you just want the keys or the values
    you can use .keys() and .values() but keep in mind that you might have to cast to a list because they're immutable
    there is no problem in the course including projects that requires them.  
"""
print(number_keys.keys())
k = list(number_keys.keys())
k[3] = 24
print(k)
print(number_keys.values())

scores = {
    'eric8': [10, 20, 30],
    'robin': [10, 20, 30],
    'greg': [20, 30, 40],
    'jill': [25, 35, 46]
}

v = scores.values()
print(v)

nest = {
    4: {'t': 5, 's': 7, 'r': 19},
    7: {'a': 3, 'b': 29, 'c': 4},
}

for outer_key in nest:
    for inner_key in nest[outer_key]:
        print(outer_key, inner_key, nest[outer_key][inner_key])

rna = {'CAU': 'His', 'CAA': 'Gln'}
rna_sequence = 'CAUCAA'
for i in range(len(rna_sequence) // 3):
    print(rna[rna_sequence[3 * i: 3*(i + 1)]])