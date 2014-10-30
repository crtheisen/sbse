#Structure from SA Lecture
import sys,re,random,math,operator
import copy
sys.dont_write_bytecode = True
import numpy

from options import *
from utils import *
from analyzer import *

myOpt = Options()

#inspiration and help from: http://deap.gel.ulaval.ca/doc/dev/examples/pso_basic.html
#Also took ideas From WeiFoo
class PSO:

  phi = myOpt.pso_phi2 + myOpt.pso_phi1
  K = 2/(abs(2 - (phi) -math.sqrt(phi **2) -4*phi))
  
  def trim(self,x,one)  : # trim to legal range
    if x < one.smin:
      return one.smin
    elif x > one.smax:
      print "too big"
      return one.smax
    return x  
  
  def velocity(self,v, p, l, g):
    newVel = []
    for i in range(p.n):
      newVel.append(self.K*(myOpt.pso_w*v[i]+myOpt.pso_phi1*rand()*(l.XVar[i]-p.XVar[i])+myOpt.pso_phi2*rand()*(g.XVar[i]-p.XVar[i])))
    return [self.trim(i,p) for i in newVel] # velocity should be in the range

  def move(self, v, p):
    newPos = [v[i] + p.XVar[i] for i in range(p.n)]
    return [self.trim(i,p) for i in newPos] # velocity should be in the range
    
  def run(self, klass):
      
    vel = []
    pos = []
    lBestSet = []
    
    gBestItem = copy.deepcopy(klass)
    gBestItem.Chaos()
       
    gBest = 1 

    #init all 4 states
    for i in range(myOpt.pso_n):
     
      #velocities; start 0
      vel.append([0 for _ in range(klass.n)])
      
      #position;
      temp = copy.deepcopy(klass)
      temp.Chaos()
      pos.append(temp)
      
      #local best; start at just the current loc
      lBestSet.append(temp)
      
      #global best; check as we go
      temp2 = pos[i].Energy()
      if temp2 < gBest:
        gBest = temp2
        gBestSet = pos[i]

    #Our Swarm
    for _ in range(myOpt.pso_repeats):
      if gBest < myOpt.pso_epsilon:
        break
      for k in range(myOpt.pso_n):
      
        vel[k] = self.velocity(vel[k], pos[k], lBestSet[k], gBestItem)
        #pos[k] = self.move(vel[k], pos[k])
        pos[k].XVar = self.move(vel[k], pos[k])
        
        eCurrent = pos[k].Energy()
        eLocal = lBestSet[k].Energy()  
        
        if eCurrent < eLocal:
          lBestSet[k] = pos[k]
          
        if eCurrent < gBest:
          gBest = eCurrent
          gBestItem = pos[k]
          
    return gBest, True

  def printOptions(self):
    print "PSO Options:"