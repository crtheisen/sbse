#From Class Discussion 8/26/2014
from __future__ import division
import sys,re,random,math
import numpy as np
sys.dont_write_bytecode = True

from model_base import *

class Kursawe(Model):
  n = 3
  smin = -5
  smax = 5
  XVar = [random.uniform(smin, smax) for i in range (0, 3)]
  XVarMax = XVar
  eMax = 0
  eMin = 0
  a = 0.8
  b = 3
  slices = 10
  
  def Energy(self):
    X = self.XVar
    f1 = np.sum([-10*math.exp(-0.2*(np.sqrt(X[i]**2+X[i]**2))) for i in range (0, 3-1)])
    f2 = np.sum([math.fabs(X[i])**self.a + 5*np.sin(X[i])**self.b for i in range (0, 3)])
    return (math.fabs(f1-f2) - self.eMin) / (self.eMax - self.eMin)
    
  def RawEnergy(self):
    X = self.XVar
    f1 = np.sum([-10*math.exp(-0.2*(np.sqrt(X[i]**2+X[i]**2))) for i in range (0, 3-1)])
    f2 = np.sum([math.fabs(X[i])**self.a + 5*np.sin(X[i])**self.b for i in range (0, 3)])
    return math.fabs(f1-f2)
    
  def __init__(self):
    self.Baseline(10000)
    self.XVar = self.XVarMax
