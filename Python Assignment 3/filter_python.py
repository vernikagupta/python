# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 23:35:18 2020

@author: verni
"""

#def myfilter(function, sequence):
#    iter_obj = iter(sequence)
#    for element in iter_obj:
#        result = function(element)
#        if result == True:
#            print(element)


#def myfilter(function, sequence):
#    if function is None:
#        return [item for item in sequence if item]
#    else:
#        return [item for item in sequence if function(item)]
    

                
a = myfilter((lambda x: x==2), (1,2,3))
print(a)
        