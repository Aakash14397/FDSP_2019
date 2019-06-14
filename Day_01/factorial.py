# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:50:55 2019

@author: Annu Poonia
"""

# find factorial function from math module
import math
dir(math)
# how to use factorial function
help(math.factorial)
# take number from user only positive
fact=input("enter number>")
fact=int(fact)
fact_ans=math.factorial(fact)
print(fact_ans)


    