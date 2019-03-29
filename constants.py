#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 01:11:46 2019

@author: Adamlkl
"""

FIT = 0
UNFIT = 1
EXERCISE = 0
RELAX = 1

'''
exeState = [[0.99,0.1],[0.2,0.8]]
relState = [[0.7,0.3],[0,1]]
exeReward = [[8,8],[0,0]]
relReward = [[10,10],[5,5]]
'''

baseRelaxTable = {
              'fit':{'fit':{'p':0.693,'r':10}, 'unfit':{'p':0.297,'r':10}, 'dead':{'p':0.01,'r':0}},
              'unfit':{'fit':{'p':0,'r':5}, 'unfit':{'p':0.99,'r':5}, 'dead':{'p':0.01,'r':0}},
              'dead':{'fit':{'p':0,'r':0}, 'unfit':{'p':0,'r':0}, 'dead':{'p':1,'r':0}}
              }
    
baseExerciseTable = { 
                  'fit':{'fit':{'p':0.891,'r':8}, 'unfit':{'p':0.09,'r':8}, 'dead':{'p':0.1,'r':0}},
                  'unfit':{'fit':{'p':0.18,'r':0}, 'unfit':{'p':0.72,'r':0}, 'dead':{'p':0.1,'r':0}},
                  'dead':{'fit':{'p':0,'r':0}, 'unfit':{'p':0,'r':0}, 'dead':{'p':1,'r':0}}
                 }