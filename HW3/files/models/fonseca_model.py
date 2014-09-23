#From Class Discussion 8/26/2014
from __future__ import division
import sys,re,random,math
import numpy as np
sys.dont_write_bytecode = True

from model_base import *
from options import *

class Fonseca(Model):
  n = 3
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

  def __init__(self):
    self.Baseline(10000)
    self.XVar = self.XVarMax
