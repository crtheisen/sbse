#From Class Discussion 8/26/2014
from __future__ import division
import sys,re,random,math
import numpy as np
sys.dont_write_bytecode = True

kmax = 5000
cooling = .6

#Structure from SA Lecture
def say(x): 
  sys.stdout.write(str(x)); sys.stdout.flush()
        
rand = random.random

class ZDT1:
  smin = 0
  smax = 1
  n = 30
  XVar = [random.uniform(smin, smax) for i in range (0, n)]
  XVarMax = XVar
  eMax = 0
  eMin = 0
  slices = 10
  
  def Energy(self):
    X = self.XVar
    f1 = X[0]
    g = 1+9*(np.sum([X[i] for i in range (1, self.n)])/(self.n-1))
    f2 = g*(1-np.sqrt(X[0]/g))
    return (math.fabs(f1-f2) - self.eMin) / (self.eMax - self.eMin)
    
  def RawEnergy(self):
    X = self.XVar
    f1 = X[0]
    g = 1+9*(np.sum([X[i] for i in range (1, self.n)])/(self.n-1))
    f2 = g*(1-np.sqrt(X[0]/g))
    return math.fabs(f1-f2)

  def Neighbor(self):
    self.XVar[random.randint(0, self.n-1)] = random.uniform(self.smin, self.smax)
    
  def BestNeighbor(self):
    toChange = random.randint(0, self.n-1)
    toIncrement = (self.smax - self.smin) / self.slices
    curMax = 1
    maxVal = self.XVar[toChange]
    for i in xrange(self.slices):
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
    self.Baseline(10000)
    self.XVar = self.XVarMax