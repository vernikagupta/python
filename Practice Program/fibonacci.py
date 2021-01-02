# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 10:44:58 2020

@author: verni
"""

'''Fibonacci series is 0,1,1,2,3,5,8,13,21...
Now objective is to find fibonacci series no as per user entry
Means if user say n=7 then answer is 8
because 8 is 7th fibonacci no'''


def fib(no):
    if no<=0:
        return("incorrect input")
    elif no==1:
        return no
    else:
        return fib(no-1) + fib(no-2)
    

print(fib(9))

# Python Program for How to check if a given number is Fibonacci number?

'''A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square'''

def isFib(no):
    s1 = math.sqrt(5 * (no*no) + 4)
    s2 = math.sqrt(5 * (no*no) - 4)
    
