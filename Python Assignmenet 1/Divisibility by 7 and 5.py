# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 19:11:04 2020

@author: verni
"""

""" Program to find number between 2000 and 3200, that are divisible by 7 
    but not a multiple of 5"""
    

''' A number is divisible by 7 if square the last digit of number is 
    subtracted by remaining number is divisible by 7 and 
    A number is not divisible by 5 if last digit is not 0, 5'''
    

num = 2000

def divisible_by_7(number):
    if number < 0:
        return divisible_by_7(-number)
    
    elif number == 0 or number == 7:
        return number
    
    elif number < 10:
        return number
    
    return divisible_by_7(( number // 10 - 2 * ( number - number // 10 * 10 )))
    
    
while(num<=3200):
    if num % 10 not in [0,5]:
       output = divisible_by_7(num)
    if output == True:
        print(num, end=' ')
    num = num +1


   
