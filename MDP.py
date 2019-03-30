#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 01:06:07 2019

@author: Adamlkl
"""

import constants as const
import sys

class MDP:
    
    def __init__(self,gamma):
        self.gamma = gamma
        self.qvalues = {'exercise':{'fit':{},'unfit':{},'dead':{}},
                        'relax':{'fit':{},'unfit':{},'dead':{}}
                        }
        self.nV = {}
        
    def calculateQ(self, state, action, n):
        if n not in self.qvalues[action][state]:
            q = 0
            if n==0:
                for s in const.STATE:
                    q = q + const.baseTable[action][state][s][0]*const.baseTable[action][state][s][1]
                    self.qvalues[action][state][n]=q
            else: 
                q = self.calculateQ(state, action, 0) + self.gamma*(const.baseTable[action][state]['fit'][0]*self.getV('fit', n-1)+const.baseTable[action][state]['unfit'][0]*self.getV('unfit', n-1))
                self.qvalues[action][state][n]=q
            return q
        
        else: 
            return self.qvalues[action][state][n]            
    
    def getV(self, state, n):
        v = max(self.calculateQ(state,'exercise',n),self.calculateQ(state,'relax',n))
        return v
            
    def getsth(self, action, state):
        return const.baseTable[action][state]['fit'][0]
    
    def calculateAllQ(self, state, action, n):
        for i in range(n+1):
            q = self.calculateQ(state, action, i)
            print 'n=%d %s: %.15f' %(i, action, q)
        
def main():
    inputs = sys.argv
    if(len(inputs)!=4):
        print('Input error!!!')
    else:
        n = int(inputs[1])
        initial_state = inputs[2]
        gamma = float(inputs[3])
        
        mdp = MDP(gamma)
        # print "1: %.15f" %(mdp.calculateQ(initial_state,'exercise',n))
        # print "2: %.15f" %(mdp.calculateQ(initial_state,'relax',n))
        mdp.calculateAllQ(initial_state,'exercise',n)
        mdp.calculateAllQ(initial_state,'relax',n)
    
if __name__ == '__main__':
    main()