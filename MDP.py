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
        self.nV = {}
        
    def calculateQ(self, state, action, n):
        #if(len(self.qvalues[action][state])<n):
        q = -1
        if n==0:
            for s in const.STATE:
                print(const.baseTable[action][state][s][0])
                q += const.baseTable[action][state][s][0]*const.baseTable[action][state][s][1]
                
        else: 
            q = self.calculateQ(state, action, 0) + self.gamma*(const.baseTable[action][state]['fit'][0]*self.getV('fit', n-1)+const.baseTable[action][state]['unfit'][0]*self.getV('unfit', n-1))
            #self.qvalues[action][state][n]=q
        #return self.qvalues[action][state][n]
        return q
    
    def getV(self, state, n):
        if n<len(self.nV):
            self.nV[n]= max(self.calculateQ(state,'exercise',n),self.calculateQ(state,'relax',n))
        return self.nV[n]
            
    def getsth(self, action, state):
        return const.baseTable[action][state]['fit'][0]
    
def main():
    inputs = sys.argv
    if(len(inputs)!=4):
        print('Input error!!!')
    else:
        n = int(inputs[1])
        initial_state = inputs[2]
        gamma = float(inputs[3])
        
        mdp = MDP(gamma)
        print(mdp.calculateQ(initial_state,'exercise',n))
        print(mdp.calculateQ(initial_state,'relax',n))
    
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