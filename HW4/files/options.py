#From Class Discussion 8/26/2014
from __future__ import division
import sys,re,random,math
import numpy as np
sys.dont_write_bytecode = True

class Options:
  #Globals
  debug = False
  seed = 1
  
  #MaxWalkSat options
  mws_prob = 0.75
  mws_maxTries = 500
  mws_maxChanges = 500
  mws_threshold = .000001
  mws_slices = 10
  
  #Simulated Annealing options
  sa_kmax = 500
  sa_cooling = .6
  
  def printGlobals(self):
    print "Seed:", self.seed