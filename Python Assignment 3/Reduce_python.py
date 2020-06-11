# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 23:29:29 2020

@author: verni
"""

''' Implement Reduce function of python
Reduce function in python is 
reduce(function, iterable)
reduce function will take first two values of iterable and apply function
then function will apply on result and 3rd value,
this will continue until a single value is returned
after iterating over all values
'''

def myreduce(function, sequence):
    iter_obj = iter(sequence)
    value = next(iter_obj)
    for element in iter_obj:
        value = function(value, element)
    return value

sum = myreduce((lambda x,y: x+y), [1,2,3])
print(sum)