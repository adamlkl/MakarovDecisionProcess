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
STATE = ['fit','unfit','dead']
ACTION = ['exercise','relax']
baseTable = {'relax':{
                      'fit':{'fit':[0.693,10], 'unfit':[0.297,10], 'dead':[0.01,0]},
                      'unfit':{'fit':[0,5], 'unfit':[0.99,5], 'dead':[0.01,0]},
                      'dead':{'fit':[0,0], 'unfit':[0,0], 'dead':[1,0]}
                     },
            'exercise':{
                          'fit':{'fit':[0.891,8], 'unfit':[0.009,8], 'dead':[0.1,0]},
                          'unfit':{'fit':[0.18,0], 'unfit':[0.72,0], 'dead':[0.1,0]},
                          'dead':{'fit':[0,0], 'unfit':[0,0], 'dead':[1,0]}
                      }
            }