#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 10:29:02 2017

@author: brendontucker

learned from http://stackoverflow.com/questions/1518522/
python-most-common-element-in-a-list
"""
from itertools import groupby
types = [4, 4, 4, 5, 3, 1, 1, 1]




import itertools
import operator

def most_common(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  print('SL:', SL)
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    print ('item %r, count %r, minind %r' % (item, count, min_index))
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]
  
print(most_common(types))

'''understanding enumerate better'''

seasons = ['Dry', 'Spring', 'Summer', 'Fall', 'Winter', 'Rainy', 
'Wet', 'Dry', 'Dry']
#creates a list of tuples 
#enumExample = list(enumerate(seasons, start = 12)) 




