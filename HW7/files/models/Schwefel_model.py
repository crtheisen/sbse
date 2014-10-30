#From Class Discussion 8/26/2014
from __future__ import division
import sys,re,random,math
import numpy as np
sys.dont_write_bytecode = True

from model_base import *
from options import *

class Schwefel(Model):
  smin = -3
  smax = 3
  n = 10
  XVar = [random.uniform(smin, smax) for i in range (0, n)]
  XVarMax = XVar
  eMax = 0
  eMin = 0
    
  def Energy(self):
    temp = self.RawEnergy()
    return (temp - self.eMin) / (self.eMax - self.eMin)
    
  #From vivekaxl's structure   
  def RawEnergy(self):
    temp = np.sum([(self.MA(n) - self.MB(self.XVar,n))**2 for n in xrange(self.n)]) + self.f_bias
    return temp

  def MA(self,n):
    t = self.alpha
    return np.sum(self.A[n][j]*math.sin(t[j])+self.B[n][j]*math.cos(t[j]) for j in xrange(self.n))

  def MB(self,x,n):
    return np.sum([self.A[n][j]*math.sin(s) + self.B[n][j]*math.cos(s) for j,s in enumerate(x)])
    
  def __init__(self):
    self.f_bias=-460
    self.objf=1
    randInt = lambda x: random.randint(-x,x)
    randFloat = lambda x: random.uniform(-x,x)
    self.A = [[randInt(100) for _ in xrange(self.n)] for _ in xrange(self.n)] 
    self.B = [[randInt(100) for _ in xrange(self.n)] for _ in xrange(self.n)] 
    self.alpha = [randFloat(math.pi) for _ in xrange(self.n)]
    self.Baseline(10000)
    self.XVar = self.XVarMax