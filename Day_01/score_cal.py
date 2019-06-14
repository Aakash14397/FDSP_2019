# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:32:40 2019

@author: Annu Poonia
"""

# PUT THE SCORE OF ASSIGNMENT
A1=input("enter the marks>")
A2=input("enter the marks>")
A3=input("enter the marks>")
# PUT THE SCORE OF EXAM
E1=input("enter the marks>")
E2=input("enter the marks>")
# cal weighted score
weighted_score=(A1+A2+A3)*0.1 + (E1+E2)*0.35
print(weighted_score)