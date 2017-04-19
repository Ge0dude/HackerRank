#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:12:32 2017

@author: brendontucker
"""

from itertools import combinations

a = [1, 3, 2, 6, 1, 2]
k = 3


sumCount = 0
combos = list(combinations(a, 2))


for x in combos:
    if sum(x[0:2]) % k == 0:
        #for testing purposes print(x)
        sumCount += 1