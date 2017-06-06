# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 16:43:10 2017

@author: Narukurti Kavya
"""

# sum of the squares and square of the sum

i=0
num=[]
for i in range(0,101):
    num.append(i)
    i=i+1
    
print num


sum=0
#sum of squares
for i in range(len(num)):
    sum += num[i]**2
              
print sum

#square of sum
SUM=0
for i in range(len(num)):
    SUM += num[i]

print SUM**2

x= SUM**2 - sum
print x

    
    
    
    
    