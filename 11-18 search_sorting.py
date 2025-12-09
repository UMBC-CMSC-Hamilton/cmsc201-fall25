import random
import time

"""

We're going to start with linear search and then binary search.

We want to talk about efficiency.  How fast do these algorithms run versus each other?

What is linear search?
    Linear search is the idea that we scan through a list looking for a specific element, and if we find it, we return it
        or True (that we found it) or the index (sometimes the index)

    If the list is of size n, how many steps could it take?
        if we get lucky 1,
        if we get unlucky... that took n steps to do.  
    if n is small we don't really care, but when n grows large, we start to care because searching 
        n total things can be quite a lot.
        
    Average number of steps is going to be about n/2.  If we run the search on 100 lists with 100 different
    elements to find, then on average we expect to find the element at about the middle position.        
"""

def linear_search(the_list, the_element):
    for i in range(len(the_list)):
        if the_list[i] == the_element:
            return True

    return False



lucky = [1, 2, 4, 6, 8, 9]
unlucky = [2, 9, 4, 2, 13, 29, 71, 36]
print(linear_search(unlucky, 36))

"""
binary search - specific requirement: the list must be sorted

Idea:
    What if we look at the "middle" element.  
"""

sorted_list = [3, 9, 12, 16, 17, 32, 54, 68, 92]
# middle element is 17
# look at:
# [3, 9, 12, 16]  len = 4 and 4 / 2 = 2 => index 2
# middle element is... 12
# [3, 9] len = 2, 2//2 = 1, look at index 1, we see 9... we win, return True


"""
Search for 215

  0   1   2    3   4  5 
[ 13, 29, 32, 45, 51, 97, 103, 145, 215, 291 ] len = 10 // 2 => 5

215 > 97 look to the larger side (right side)
[103, 145, 215, 291] len == 4 // 2 == 2 index
215 == 215 found it return True


Now look for 141
[ 13, 29, 32, 45, 51, 97, 103, 145, 215, 291 ] len = 10 // 2 => 5 element is 97
141 > 97 go right
[ 103, 145, 215, 291 ] len == 4 // 2 = 2 (index); 215 element 
141 < 215 go left
[ 103, 145 ] len == 2 // 2 => index = 1, element 145
141 < 145 go left
[ 103 ] len == 1 // 2 == 0 => index 0, element 103
103 != 141
return False

sum_{i = 0}^{infinity} a^i = a^0 + a^1 + a^2 + a^3 + a^4 + ....
sum_{i = 0}^{infinity} (1/2)^i = 1 + 1/2 + 1/4 + 1/8 + 1/16 + 1/32 + 1/64 + 1/128 + .... = 2

1 + 1/2 + 1/4 + 1/8 + 1/16 + 1/32 + 1/64 + .... = 2

n + n/2 + n/4 + n/8 + n/16 + ... = 2n operations (not great). 

Actual performance:
1 operation per division (when it's working right)
16 => 8 => 4 => 2 => 1 (5 operations)
32 => 16 => 8 => 4 => 2 => 1 (6 operations)

214 => 107 => 53 => 26 => 13 => 7 => 3 => 1

list size = n
find the number of times we can divide it by 2 until it's 'close to 1'.  

n / 2^steps = 1
lg(n) = lg(2^steps)
lg(n) = log_2(n) = steps
"""

def binary_search(the_list, the_element):
    if not the_list:
        return False

    print(the_list)

    middle_index = len(the_list) // 2
    if the_element < the_list[middle_index]: # go to the smaller side of the list
        return binary_search(the_list[0: middle_index], the_element)
    elif the_element > the_list[middle_index]:
        return binary_search(the_list[middle_index + 1: ], the_element)
    else:
        return True


def binary_search_index(the_list, start, end, the_element):
    if end <= start:
        return False
    middle_index = (start + end) // 2
    print(start, middle_index, end, the_list[middle_index])
    if the_list[middle_index] == the_element:
        return True
    elif the_element < the_list[middle_index]:
        return binary_search_index(the_list, start, middle_index, the_element)
    else: #trichotomy
        return binary_search_index(the_list, middle_index + 1, end, the_element)



def binary_search_supercool(the_list, the_element):
    return binary_search_index(the_list, 0, len(the_list), the_element)


test_list = [random.randint(0, 20) for _ in range(10)]
test_list.sort()

print(test_list)
x = int(input('What to find? '))
while x != -1:
    print(binary_search_supercool(test_list, x))
    x = int(input('What to find? '))


big_list = [random.randint(0, 10000000) for _ in range(10000000)]
start = time.process_time_ns()
print(linear_search(big_list, 100000000 + 1))
print(f'That took {time.process_time_ns() - start}')

big_list.sort()
start = time.process_time_ns()
print(binary_search_supercool(big_list, 100000000 + 1))
print(f'That took {time.process_time_ns() - start}')

