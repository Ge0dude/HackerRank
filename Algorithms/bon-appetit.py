#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 07:38:42 2017

@author: brendontucker
"""

n = 4
k = 1
foodList = [3, 10, 2, 9]
charged = 12


if k == len(foodList):
    realCost = sum(foodList[0:k]) / 2
else:
    realCost = ( sum(foodList[0:k]) + sum(foodList[k+1:]) ) / 2

realCost = int(realCost)                     
if charged == realCost:
    print('Bon Appetit')
else:
    print(charged - realCost)