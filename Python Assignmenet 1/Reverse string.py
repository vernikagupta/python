# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 19:11:04 2020

@author: verni
"""

""" Take user's first and last name and print in reverse order
    separated by space"""
    
user_name = input("Enter first and last name separated by space ").split(' ')

reverse_name = [name[::-1]for name in user_name]
print(" ".join(reverse_name))
    

