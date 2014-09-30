#From Class Discussion 8/26/2014
from __future__ import division
import sys,re,random,math
import numpy as np
sys.dont_write_bytecode = True

from model_base import *
from options import *

class DTLZ7(Model):
  smin = -4.0
  smax = 4
  n = 20
  XVar = [random.uniform(smin, smax) for i in range (0, n)]
  XVarMax = XVar
  eMax = 0
  eMin = 0
  
  def Energy(self):
    X = self.XVar
    n = self.n
    f1 = 1 - math.exp(-np.sum([(X[i] - 1/math.sqrt(i+1))**2 for i in range (0, n)]))
    f2 = 1 - math.exp(-np.sum([(X[i] + 1/math.sqrt(i+1))**2 for i in range (0, n)]))
    return (math.fabs(f1-f2) - self.eMin) / (self.eMax - self.eMin)
    
  def RawEnergy(self):
    X = self.XVar
    n = self.n
    f1 = 1 - math.exp(-np.sum([(X[i] - 1/math.sqrt(i+1))**2 for i in range (0, n)]))
    f2 = 1 - math.exp(-np.sum([(X[i] + 1/math.sqrt(i+1))**2 for i in range (0, n)]))
    return math.fabs(f1-f2)
    
  def __init__(self):
    self.Baseline(10000)
    self.XVar = self.XVarMax