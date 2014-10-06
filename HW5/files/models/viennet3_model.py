#From Class Discussion 8/26/2014
from __future__ import division
import sys,re,random,math
import numpy as np
sys.dont_write_bytecode = True

from model_base import *
from options import *

class Viennet3(Model):
  smin = -3.0
  smax = 3
  n = 2
  XVar = [random.uniform(smin, smax) for i in range (0, n)]
  XVarMax = XVar
  eMax = 0
  eMin = 0
  
  def Energy(self):
    X = self.XVar
    f1 = 0.5*X[0]**2 + X[1]**2 + math.sin(X[0]**2+X[1]**2)
    f2 = (3*X[0]-2*X[1]+4)**2/8 + (X[0]-X[1]+1)**2/27 + 15
    f3 = 1/(X[0]+X[1]+1) - 1.1*math.e**(-X[0]**2-X[1]**2)
    return (math.fabs(f1+f2+f3) - self.eMin) / (self.eMax - self.eMin)
    
  def RawEnergy(self):
    X = self.XVar
    f1 = 0.5*X[0]**2 + X[1]**2 + math.sin(X[0]**2+X[1]**2)
    f2 = (3*X[0]-2*X[1]+4)**2/8 + (X[0]-X[1]+1)**2/27 + 15
    f3 = 1/(X[0]+X[1]+1) - 1.1*math.e**(-X[0]**2-X[1]**2)
    return math.fabs(f1+f2+f3)
    
  def __init__(self):
    self.Baseline(10000)
    self.XVar = self.XVarMax