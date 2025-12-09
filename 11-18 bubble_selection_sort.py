import random
import time

"""
    What is 
        rm -rf in linux?
        rm = remove command
        -r = recursively this is the real problem, be careful
        

    Let's talk about sorting...

        Bubble sort:
            Idea:
                you scan the list and find adjacent elements and swap them if they're out of order
                [7, 4, 8, 9, 2, 5]
                [4, 7, 8, 2, 5, 9]
                [4, 7, 2, 5, 8, 9]
                [4, 2, 5, 7, 8, 9]
                [2, 4, 5, 7, 8, 9]
                one more time
"""

def swap(the_list, i, j):
    temp = the_list[i]
    the_list[i] = the_list[j]
    the_list[j] = temp


"""
    The idea is that you swap pairs of adjacent (elements in position i, i + 1)
        until you reach the end of the list.
    Keep doing that because one iteration through the list isn't enough to actually sort it.  
        you need up to n - 1 iterations.  
"""
def bubble_sort(the_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(the_list) - 1):
            if the_list[i] > the_list[i + 1]:
                swap(the_list, i, i + 1)
                swapped = True

    return the_list


def test_bubble_sort():
    print(bubble_sort([5, 3, 9, 1, 2, 4]))
    random_list = [random.randint(0, 20) for _ in range(20)]
    # the_sorted_list = random_list.sort()
    # print(the_sorted_list)
    print(random_list)
    bubble_sort(random_list)
    print(random_list)


"""
Idea of selection sort:
    scans the list, finds the min or max, puts the min or max in the right position
    scan again, find the second from max, put it in the second to last position
    scan again, find the third from the max, put it in the third to last position
    ...
    until you're down to one element. 
    Many fewer swaps than bubble sort.  

    [5, 7, 9, 1, 3, 4, 8] let's do the max version
    [5, 7, 8, 1, 3, 4, 9] i = 1
    [5, 7, 4, 1, 3, 8, 9] i = 2
    [5, 3, 4, 1, 7, 8, 9] i = 3
    [1, 3, 4, 5, 7, 8, 9] i = 4
           v
    [1, 3, 4, 5, 7, 8, 9] i = 5
        v
    [1, 3, 4, 5, 7, 8, 9] i = 6
     v
    [1, 3, 4, 5, 7, 8, 9] i = 7 [maybe don't need this]

    selection_sort = the find max sort / the find min sort
"""

"""
Count operations:
    i starts at 0 goes to n - 1 (n = len(the_list))
    i = 0: n times
    i = 1: n - 1 times
    i = 2: n - 2 times
    ...
    i = n - 1: 1 time.  
    
    n + (n - 1) + (n - 2) + (n - 3) + ... + 3 + 2 + 1
    sum_{i = 1}^{n} i = 1 + 2 + 3 + 4 + ... + n [Gauss Sum] = n(n + 1)/2
    
    1 + 2 + 3 + 4 + 5 + 6 = 6(7)/2
    |-------------------| = 7
        |-----------| = 7
            |---| = 7
            = 7 + 7 + 7 = 21 = 6(7)/2 = 42/ 2 = yes. 
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
        What is the sum of the pairs? 1 + 8, 2 + 7 ,3 + 6, 4 + 5 = 9
        How many pairs are there? 4 = 8/2
        8 * 9 / 2 what the formula says... is this true? 9 * 4 = 36, that works too wow.  
        
    1 + 2 + 3 + 4 + 5 + 6 + 7
    |-----------------------| = 8
        |---------------| = 8
            |-------| = 8
                | = 4 (huh?)
                
    How many pairs are there? 3.5 pairs
    3.5 = 7/2
    7*8/2 = 56/2 = 28
    8 + 8 + 8 + 4 = 28 wow it's the same.  
    
    1 + 2 + ... + (n - 1) + n
    |-----------------------| = n + 1
        |-------------| n + 1
             |---| n + 1
    How many pairs are there?
        n / 2 [if n is odd consider the middle element as a half pair]
        n(n + 1) / 2

    n(n + 1)/ 2 simplify a little -> ignore the + 1, we get n^2/ 2
    we multiply the size of the list by 10, but the number of operations increases by a factor of 100. 
    100 ^2 / 2 = 5,000
    1000^2 / 2 = 500,000
"""
def selection_sort(the_list):
    for i in range(len(the_list)):
        max_index = 0
        # len(the_list) - i makes sure we don't take the previous maximum again.
        for j in range(len(the_list) - i):
            if the_list[j] > the_list[max_index]:
                max_index = j
        # len(the_list) - 1 - i way to reverse through indices
        swap(the_list, max_index, len(the_list) - 1 - i)

    return the_list


def selection_sort_min(the_list):
    for i in range(len(the_list)):
        min_index = i  # need to skip up to the position i becaus everything before is sorted
        for j in range(i, len(the_list)):
            if the_list[min_index] > the_list[j]:
                min_index = j
        swap(the_list, min_index, i)
    return the_list


print(selection_sort_min([5, 9, 2, 4, 7, 8, 1]))
rand_list = [random.randint(0, 20) for _ in range(20)]
print(rand_list)
print(selection_sort_min(rand_list))


"""
Insertion Sort: Pull back sort
    takes elements at position i, asks how far can it be swapped back in the list.  
    pull back sort.  
"""
def insertion_sort(the_list):
    for i in range(len(the_list)):
        cur_pos = i
        while cur_pos > 0 and the_list[cur_pos - 1] > the_list[cur_pos]:
            swap(the_list, cur_pos - 1, cur_pos)
            cur_pos -= 1

    return the_list


def sort_test(the_sort):
    for n in [100, 1000, 10000, 100000, 10 ** 6, 10**7]:
        test_list = [random.randint(0, n) for _ in range(n)]
        start = time.process_time()
        the_sort(test_list)
        print(f'On size {n}, {the_sort.__name__} took {time.process_time() - start} seconds.')


# sort_test(insertion_sort)

"""
What do I ask on exams?

    i ask you to take one of the three sorts and do a few iterations
    
    do insertion sort on this list:
    [3, 9, 12, 4, 15, 8, 7, 13]
    [3, 9, 12, 4, 15, 8, 7, 13] i = 1
    [3, 9, 12, 4, 15, 8, 7, 13] i = 2
    [3, 4, 9, 12, 15, 8, 7, 13] i = 3
    [3, 4, 9, 12, 15, 8, 7, 13] i = 4
    [3, 4, 8, 9, 12, 15, 7, 13] i = 5
    [3, 4, 7, 8, 9, 12, 15, 13] i = 6
    [3, 4, 7, 8, 9, 12, 13, 15] i = 7
"""

""" 

Merge Sort 
    [4, 9, 2, 1, 3, 7, 6, 8]
    [4, 9, 2, 1] [3, 7, 6, 8]
    [4, 9] [2, 1] [3, 7] [6, 8]
    [4] [9] [2] [1] [3] [7] [6] [8]
    ([4, 9], [1, 2]) ([3, 7], [6, 8])
    [1, 2, 4, 9]  [3, 6, 7, 8]
    [1, 2, 3, 4, 6, 7, 8, 9]
    
                   | |    
    [1, 1, 1, 1, 1] [2, 2, 2, 2, 2]
    [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]

    Depends on which element is less, not which order they come in.      
    [1, 2, 3, 4, 10]
    [5, 6, 7, 8, 9]
    [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
                    |
    [1, 2, 2, 3, 4]
                 |
    [1, 2, 2, 4, 6, 7, 8, 9, 10]
    When we're done we have to take all the elements in the remaining list.  
    [1, 1, 2, 2, 2, 2, 3, 4, 4,   
"""

def put_together(a_list, b_list):
    """
        THis puts two sorted lists together into a sorted list

    :param a_list: both sorted lists
    :param b_list:
    :return: sorted list which is the merge of the two sorted lists
    """
    i = 0  # a index
    j = 0  # b index
    new_list = []
    while i < len(a_list) and j < len(b_list):
        if a_list[i] < b_list[j]:
            new_list.append(a_list[i])
            i += 1
        else:
            new_list.append(b_list[j])
            j += 1
    # only one of these two for loops is going to run, it's the one where we haven't taken
    # the remainder of the list
    for k in range(i, len(a_list)):
        new_list.append(a_list[k])
    for r in range(j, len(b_list)):
        new_list.append(b_list[r])
    return new_list


def merge_sort(the_list):
    if len(the_list) <= 1:
        return the_list
    middle = len(the_list) // 2
    first_half = the_list[0: middle]
    second_half = the_list[middle:]
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    # this takes two lists of size n/2 and gives us back one list of size n but takes n steps to do it.
    return put_together(first_half, second_half)


# sort_test(merge_sort)

L = [2, 9, 4, 8, 1, 5, 2, 3]
L.sort()  # this is a merge sort
print(L)

"""

            1024                        -> 1024
        512     512                     -> 2 * 512 = 1024
    256 256     256 256                 -> 4 * 256 = 1024
128 128 128 128 128 128 128 128         -> 8 * 128 = 1024
................................
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 x         [1024]

S = the number of times we have to divide the lists in half
n / 2^S = 1
n = 2^S
lg(n) = lg(2^S) = S lg(2) = S (1) = 1
n "=" in this example "=" 1024
Total cost:
Merge sort ALWAYS takes n lg (n) time.  
n * lg(n)


10^6 = n -> 10^6 * lg(10^6) = 10^6 * lg(10) * 6
10^7 = n -> 10^7 * lg(10^7) = 10^7 * lg(10) * 7

i want to know the ratio of time it'll take to do the 10 M calculation vs 1M calculation:

10^7 * lg(10) * 7
-----------------
10^6 * lg(10) * 6

= 10 * 1.167 = 11.67 times as long to do 10M vs 1 M
"""

"""
QuickSort - it says quick and it usually beats mergesort but there's a problem.  
"""

def quick_sort(the_list):
    # no difference
    if len(the_list) <= 1:
        return the_list

    # print(the_list)
    less_list = []
    greater_list = []  # greater than or equal to list
    # partition
    pivot = the_list[0] # this can be modified to fix things a little, but for now this.
    for i in range(1, len(the_list)):  # skip the pivot
        if the_list[i] < pivot:
            less_list.append(the_list[i])
        else:
            greater_list.append(the_list[i])

    #print(pivot, less_list, greater_list)
    less_list = quick_sort(less_list)
    greater_list = quick_sort(greater_list)
    # why did i put the pivot into a list?
    return less_list + [pivot] + greater_list


test = [4, 9, 3, 8, 1, 2, 4, 6]
print('\n\n\n')
print(quick_sort(test))

"""
Quick sort takes about n lg(n) time in the good cases ??? wait what do you mean?
"""

sort_test(quick_sort)

reverse_sorted = [x for x in range(990, 0, -1)]
print(reverse_sorted)
print(quick_sort(reverse_sorted))

"""

[7, 6, 5, 4, 3, 2, 1]
pivot = 7
[6, 5, 4, 3, 2, 1]  []
pivot = 6
[5, 4, 3, 2, 1]  []
pivot = 5
[4, 3, 2, 1] []
pivot = 4
[3, 2, 1] []
pivot = 3
[2, 1], []
pivot = 2
[1] []

size = n, n steps of n work, that's n^2 again... wait
that's not n lg(n)

Either you can pick the pivot as the median (requires the median function implementation)
or
Trust luck, pick a pivot at random.  


"""