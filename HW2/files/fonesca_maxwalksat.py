#From Class Discussion 8/26/2014
from __future__ import division
import sys,re,random,math
import numpy as np
sys.dont_write_bytecode = True

maxTries = 500
maxChanges = 500
#threshold; well, how close do we want to get?
threshold = .000001
cooling = 1


#Structure from SA Lecture
def say(x): 
  sys.stdout.write(str(x)); sys.stdout.flush()
        
rand = random.random

class FonescaMWS:
  smin = -4
  smax = 4
  XVar = [random.uniform(smin, smax) for i in range (0, 3)]
  XVarMax = XVar
  eMax = 0
  eMin = 0
  slices = 10
  
  def Energy(self):
    f1 = (1-math.e**(-np.sum([self.XVar[i]-(1/np.sqrt(i+1))**2 for i in range (0, 3)])))
    f2 = (1-math.e**(-np.sum([self.XVar[i]+(1/np.sqrt(i+1))**2 for i in range (0, 3)])))
    return (math.fabs(f1+f2) - self.eMin) / (self.eMax - self.eMin)
    
  def RawEnergy(self):
    f1 = (1-math.exp(-np.sum([self.XVar[i]-(1/np.sqrt(i+1))**2 for i in range (0, 3)])))
    f2 = (1-math.exp(-np.sum([self.XVar[i]+(1/np.sqrt(i+1))**2 for i in range (0, 3)])))
    return math.fabs(f1+f2)

  def Neighbor(self, toChange):
    self.XVar[toChange] = self.smin + (self.smax - self.smin) * random.uniform(0,1)
  
  def BestNeighbor(self, toChange):
    toIncrement = (self.smax - self.smin) / self.slices
    curMax = 1
    maxVal = self.XVar[toChange]
    for i in xrange(10):
      self.XVar[toChange] = self.smin + toIncrement
      x = self.Energy()
      if x < curMax:
        curMax = x
        maxVal = self.XVar[toChange]
    
  def Chaos(self):
    self.XVar[0] = random.uniform(self.smin, self.smax)
    self.XVar[1] = random.uniform(self.smin, self.smax)
    self.XVar[2] = random.uniform(self.smin, self.smax)
    
  def Baseline(self, numRuns):
    self.Chaos()
    self.eMax = self.eMin = self.RawEnergy()
    runs = 1
    while runs < numRuns:   
      self.Neighbor(random.randint(0,2))
      eNew = self.RawEnergy()
      if eNew > self.eMax: #find largest difference               
        self.eMax = eNew
        self.XVarMax = self.XVar
        #print self.XVarMax, eNew
      if eNew < self.eMin: #find smallest difference  
        self.eMin = eNew
        #print 'Min: ', self.XVar, eNew
      runs += 1
    print 'Baseline: ', self.eMin, ', ', self.eMax
  
  def EnergyChecker(self, x, y, z):
    self.XVar[0] = x
    self.XVar[1] = y
    self.XVar[2] = z
    print 'Energy @ ', x, ' ', y, ' ', z, ': ', self.Energy()
    
  def __init__(self):
    print '\nInitializing Fonesca (MaxWalkSat)...'
    self.Baseline(10000)
    self.XVar = self.XVarMax
    print 'Initialized.'
  
#Structure from MaxWalkSat Lecture
def MWS(probability):
  fon = FonescaMWS()
  XVarBest = fon.XVar
  eBest = e = 1       
  k = 1
  say(int(math.fabs(eBest-1)*100))
  say(' ')
  for i in xrange(maxTries): 
    fon.Chaos()
    for j in xrange(maxChanges):
      eNew = fon.Energy()
      if(eNew < threshold):
        #% means found a solution and quit
        say('%')
        eBest = eNew
        XVarBest = list(fon.XVar)
        print '\nQuitting...'
        return eBest, XVarBest
      else:
        #modify random part of solution
        if probability > random.uniform(0,1):
          fon.Neighbor(random.randint(0, 2))
          say('+')
        #maximize for some random
        else:
          fon.BestNeighbor(random.randint(0,2))
        say('.')
        if (i+1)*(j+1) % 40 == 0:
          print ''
          say(int(math.fabs(eNew-1)*100))
          say(' ')
    print ''
    return -1, XVarBest
  
for i in [0.25, 0.5, 0.75]:
  eBest, XVarBest = MWS(i)
  if eBest == -1:
    print 'No Best Found for prob = ', i
  else:
    print 'Found best - e: ', eBest, ' for prob = ', i
    print 'Variables: ', XVarBest[0], ', ', XVarBest[1], ', ', XVarBest[2]
