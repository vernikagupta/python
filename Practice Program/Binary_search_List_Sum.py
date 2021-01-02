# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 19:08:34 2020

@author: verni
"""

# Given a list of numbers and a number k, 
# return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, 
# return true since 10 + 7 is 17.

import time
from bisect import bisect_left


# Brute force approach
arr = [10, 15, 3, 7]
k = 17

for i in range(len(arr)):        # time complexity = O(n^2)
    for j in range(len(arr)):    
        if i!=j:
            if (arr[i] + arr[j]) == k:
                print(True)
    break

# Optimized solution 1 
    
'''This would take O(N2). Another way is to use a set to remember the numbers 
we've seen so far. Then for a given number, we can check if there is another number that,
if added, would sum to k. This would be O(N) since lookups of sets are O(1) each.'''

def sum_no(lst, k):
    seen = set()
    for num in lst:
        if k - num in seen:             # time complexity O(N)
            return True
        seen.add(num)
    return False

#sum_no(a, k)  

# Binary search method
'''Yet another solution involves sorting the list. 
We can then iterate through the list and run a binary search on K - lst[i].
Since we run binary search on N elements, 
this would take O(N log N) with O(1) space.'''


def binary_search(lst, target):
    lo = 0
    hi = len(lst)
    ind = bisect_left(lst, target, lo, hi)

    if 0 <= ind < hi and lst[ind] == target:
        return ind
    return -1
 

def two_sum(arr, k):
    arr.sort()
    for i in range(len(arr)):
         target = k - arr[i]
         j = binary_search(arr, target)
         
         # Check that binary search found the target and
         # that it's not in the same index
         # If it is in the same index, we can check lst[i + 1] 
         # and lst[i - 1] to see
         # if there's another number that's the same value as lst[i].
         if j==-1:
             continue
         elif j!=i:
             return True
         elif j + 1 < len(arr) and arr[j + 1] == target:
             return True
         elif j - 1 >= 0 and arr[j - 1] == target:
             return True
    
    return False

t0 = time.time()
b = two_sum(arr, k)
print(b)
t1 = time.time()
print(t1-t0)



