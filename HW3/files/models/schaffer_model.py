#From Class Discussion 8/26/2014
from __future__ import division
import sys,re,random,math
import numpy as np

from model_base import *

sys.dont_write_bytecode = True

class Schaffer(Model):
  n = 1
  smin = -10
  smax = 10
  XVar = [random.uniform(smin, smax) for i in range (0, 1)]
  XVarMax = XVar
  eMax = 0
  eMin = 0
  slices = 10
  
  def Energy(self):
    f1 = self.XVar[0]*self.XVar[0]
    f2 = (self.XVar[0]-2)*(self.XVar[0]-2)
    return (math.fabs(f1+f2) - self.eMin) / (self.eMax - self.eMin)
    
  def RawEnergy(self):
    f1 = self.XVar[0]*self.XVar[0]
    f2 = (self.XVar[0]-2)*(self.XVar[0]-2)
    return math.fabs(f1+f2)
    
  def __init__(self):
    self.Baseline(10000)
    self.XVar = self.XVarMax