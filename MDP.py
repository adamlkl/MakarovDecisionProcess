#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 01:06:07 2019

@author: Adamlkl
"""

import constants as const
import sys

class MDP:
    
    class StateTable:
            
        def __init__(self, eP, rP, eR, eR, condition):
            self.eP = eP
            self.rP = rP
            self.eR = eR
            self.rR = rR
            self.condition = condition
            self.state = const.FIT if self.condition == 'fit' else const.UNFIT
            
    def __init__(self, n, startState, gamma):
        self.n = n 
        self.gamma = gamma
        
        self.fitState = State(const.exeState, relState, exeReward, relReward, 'fit')
        self.unfitState = State(const.exeState, relState, exeReward, relReward, 'unfit')
        self.startState = fitState if startState == 'fit' else self.unfitState
        
        
def main():
    inputs = sys.argv
    if(len(inputs)!=3):
        print('Input error!!!')
    else:
        mdp = MDP(inputs[1],inputs[2],inputs[3])
    
if __name__ == '__main__':
    main()