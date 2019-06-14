# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 23:21:45 2019

@author: Annu Poonia
"""

n=1
while(n<101):
    if(n%3==0 and n%5==0):
        print('fizzbuzz')
        n=n+1
    elif(n%3==0):
        print('fizz')
        n=n+1
    elif(n%5==0):
        print('buzz')
        n=n+1
    else:
        print(n)
        n=n+1
    