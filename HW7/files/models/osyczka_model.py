#From Class Discussion 8/26/2014
from __future__ import division
import sys,re,random,math
import numpy as np

from model_base import *
from options import *

sys.dont_write_bytecode = True

class Osyczka(Model):
  n = 6
  smin = 0
  smax = 10
  XVar = [random.uniform(smin, smax) for i in range (0, n)]
  XVarMax = XVar
  eMax = 0
  eMin = 0
  
  #this is a horrible, horrible hack. But it works and I'm running out of time
  def Sanity(self):
    for i in [2,4]:
      if self.XVar[i] > 5:
        self.XVar[i] = 5
      elif self.XVar[i] < 1:
        self.XVar[i] = 1
    
    if self.XVar[3] > 6:
      self.XVar[3] = 6
    elif self.XVar[3] < 0:
      self.XVar[3] = 0
  
  def Energy(self):
    self.Sanity()
    X = self.XVar
    f1 = -25*(X[0] - 2)**2 - (X[1] - 2)**2 - (X[2] - 1)**2 - (X[3] - 4)**2 - (X[4] - 1)**2
    f2 = np.sum([X[i]**2 for i in range (0, 6)])
    return ((f1+f2) - self.eMin) / (self.eMax - self.eMin)
    
  def RawEnergy(self):
    self.Sanity()
    X = self.XVar
    f1 = -25*(X[0] - 2)**2 - (X[1] - 2)**2 - (X[2] - 1)**2 - (X[3] - 4)**2 - (X[4] - 1)**2
    f2 = np.sum([X[i]**2 for i in range (0, 6)])
    return (f1+f2)
    
  def __init__(self):
    self.Baseline(10000)
    self.XVar = self.XVarMax