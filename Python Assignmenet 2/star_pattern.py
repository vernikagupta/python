# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:31:22 2020

@author: verni
"""

# take user_input an odd no
# loop till user_input//2 and print *
# 


user_input = int(input("Enter no of lines: "))
user_input_half = user_input//2
i = 1
j = user_input_half

while(i <= user_input):
    if i <= (user_input_half+1):
        print('*' * i)
        i = i+1
     
    elif (i > user_input_half+1):
        print('*' * j)
        j = j-1
        i = i+1