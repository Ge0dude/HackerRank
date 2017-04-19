#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 08:37:49 2017

@author: brendontucker
"""

n = 5
s = [1, 2, 1, 3, 2]
d = 3
m = 2
   
#function version        
def getWays(s, d, m):
    start = 0
    end = len(s)
    countIterater = start + m
    sumCounter = 0
    
    
    
    while countIterater <= end + 1:
        if sum(s[start:countIterater]) == d:
            sumCounter += 1
            start += 1
            countIterater += 1
        else:
            start += 1
            countIterater += 1
            
    return sumCounter
    
print(getWays(s, d, m))




#local testing version
'''
start = 0
end = len(s)
countIterater = start + m
sumCounter = 0



while countIterater <= end + 1:
    if sum(s[start:countIterater]) == d:
        sumCounter += 1
        start += 1
        countIterater += 1
    else:
        start += 1
        countIterater += 1
'''     