#From Class Discussion 8/26/2014
from __future__ import division
import sys,re,random,math
import numpy as np
sys.dont_write_bytecode = True

from model_base import *
from options import *

class ZDT1(Model):
  smin = 0
  smax = 1
  n = 30
  XVar = [random.uniform(smin, smax) for i in range (0, n)]
  XVarMax = XVar
  eMax = 0
  eMin = 0
  
  def Energy(self):
    X = self.XVar
    f1 = X[0]
    g = 1+9*(np.sum([X[i] for i in range (1, self.n)])/(self.n-1))
    f2 = g*(1-np.sqrt(X[0]/g))
    return ((f1+f2) - self.eMin) / (self.eMax - self.eMin)
    
  def RawEnergy(self):
    X = self.XVar
    f1 = X[0]
    g = 1+9*(np.sum([X[i] for i in range (1, self.n)])/(self.n-1))
    f2 = g*(1-np.sqrt(X[0]/g))
    return (f1+f2)
    
  def __init__(self):
    self.Baseline(10000)
    self.XVar = self.XVarMax