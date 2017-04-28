#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 16:04:20 2017

@author: brendontucker
"""


from collections import Counter

types = [4, 4, 4, 5, 3, 1, 1, 1]
birds = Counter(types)
print(birds.most_common(1)[0][0])