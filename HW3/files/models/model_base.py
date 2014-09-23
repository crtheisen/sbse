#From Class Discussion 8/26/2014
from __future__ import division
import sys,re,random,math
import numpy as np
sys.dont_write_bytecode = True
        
from options import *
myOpt = Options()
rand = random.random

class Model:
  #Default Values overwritten by subclass; should have better defaults, but...
  n = 1
  smin = 1
  smax = 1
  XVar = [random.uniform(smin, smax) for i in range (0, n)]
  XVarMax = XVar
  eMax = 0
  eMin = 0
  
  def Energy(self):
    print "Energy Class Undefined!"
    
  def RawEnergy(self):
    print "RawEnergy Class Undefined!"

  def Neighbor(self):
    self.XVar[random.randint(0, self.n-1)] = random.uniform(self.smin, self.smax)
    
  def BestNeighbor(self):
    toChange = random.randint(0, self.n-1)
    toIncrement = (self.smax - self.smin) / myOpt.mws_slices
    curMax = 1
    maxVal = self.XVar[toChange]
    for i in xrange(myOpt.mws_slices):
      self.XVar[toChange] = self.smin + toIncrement
      x = self.Energy()
      if x < curMax:
        curMax = x
        maxVal = self.XVar[toChange]
    
  def Chaos(self):
    for vars in self.XVar:
      vars = random.uniform(self.smin, self.smax)
    
  def Baseline(self, numRuns):
    self.Chaos()
    self.eMax = self.eMin = self.RawEnergy()
    runs = 1
    while runs < numRuns:   
      self.Neighbor()
      eNew = self.RawEnergy()
      if eNew > self.eMax: #find largest difference               
        self.eMax = eNew
        self.XVarMax = self.XVar
        #print self.XVarMax, eNew
      if eNew < self.eMin: #find smallest difference  
        self.eMin = eNew
        #print 'Min: ', self.XVar, eNew
      runs += 1
    #print 'Baseline: ', self.eMin, ', ', self.eMax
    
  def __init__(self):
    print "Default init Shouldn't be used!"