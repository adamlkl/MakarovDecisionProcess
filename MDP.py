#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 01:06:07 2019

@author: Adamlkl
"""

import constants as const
import sys

class MDP:
    
    # TODO
    ''' 
        - add dead state 
        - reconstruct state tables 
        - change functions 
        - make dynamic 
    '''    
    def __init__(self,gamma):
        self.gamma = gamma
        self.qvalues = {'exercise':{'fit':[],'unfit':[],'dead':[]},
                        'relax':{'fit':[],'unfit':[],'dead':[]}
                        }
        
    def calculateQ(self, state, action, n):
        if(len(q)<n):
            if n==0:
                    q = const.baseExerciseTable[action][state]['fit'][0]*const.baseExerciseTable[action][state]['fit'][1]+const.baseExerciseTable[action][state]['unfit'][0]*const.baseExerciseTable[action][state]['ununfit'][1]
            else: 
                    q = q + self.gamma*calculateQ(state, action, n-1)
            self.qvalues[n]=q
            return q
        else:
            return qvalues[action][state][n]
    
    def v(self, state, n):
        return max(calculateQ(state,'exercise',n),calculateQ(state,'relax',n))
    
    def getReward(self):
    
    def getProbability(self):
        
def main():
    inputs = sys.argv
    if(len(inputs)!=3):
        print('Input error!!!')
    else:
        mdp = MDP(inputs[3])
        print(mdp.calculateQ(inputs[1],'exercise',inputs[2]))
        print(mdp.calculateQ(inputs[1],'relax',inputs[2]))
    
if __name__ == '__main__':
    main()
    
'''
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
'''