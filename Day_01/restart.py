# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:57:38 2019

@author: Annu Poonia
"""

# In RESTART REPLACE "R" BY "$" EXCEPT FIRST "R"
newstr='RESTART'
newst='R'
newstr1=newstr[1:].replace('R','$')
print(newstr+newstr1)