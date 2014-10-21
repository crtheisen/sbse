#Structure from SA Lecture
import sys,re,random,math
import copy
sys.dont_write_bytecode = True

from options import *
from utils import *
from analyzer import *

myOpt = Options()

#Structure from vivekaxl's DE
class DE:

  def threeOthers(self,frontier,one):
    #print "threeOthers"
    seen = [one]
    def other():
      #print "other"
      for i in xrange(len(frontier)):
        while True:
          k = random.randint(0,len(frontier)-1)
          #print "%d"%k
          if frontier[k] not in seen:
            seen.append(frontier[k])
            break
        return frontier[k]
    this = other()
    that = other()
    then = other()
    return this,that,then
  
  def trim(self,x,one)  : # trim to legal range
    return max(one.eMax, min(x, one.eMax))      

  def extrapolate(self,frontier,one):
    #print "Extrapolate"
    two,three,four = self.threeOthers(frontier,one)
    #print two,three,four
    solution=[]
    for d in xrange(one.n):
      x,y,z=two.XVar[d],three.XVar[d],four.XVar[d]
      if(random.random() < myOpt.de_cf):
        solution.append(self.trim(x + myOpt.de_f*(y-z), one))
      else:
        solution.append(one.XVar) 

    return solution

  def update(self,frontier):
    #print "update %d"%len(frontier)
    newF = []
    total,n=0,0
    for x in frontier:
      #print "update: %d"%n
      e = x.Energy()
      print x.XVar
      new = self.extrapolate(frontier,x)
      x.XVar = new
      print new
      eNew = x.Energy()
      if(eNew < e):
        newF.append(new)
      else:
        newF.append(x)
      total+=min(eNew, e)
      n+=1
    return total,n,newF
      
  def run(self, klass):
    #print "evaluate"
    de = klass
    frontier = []
    for i in range(myOpt.de_np):
      de.Chaos()
      frontier.append(copy.deepcopy(de)) #add a randomly generated model to list
    #print frontier
    for i in xrange(myOpt.de_max):
      total,n,frontier = self.update(frontier)
      self.model.evalBetter()
    for x in frontier:
      energy = self.model.evaluate(x)
      if(minR>energy):
        minR = energy
        solution=x  
    return energy, True

  def printOptions(self):
    print "DE Options:"
    print "Repeats:", myOpt.de_max, "Candidates:", myOpt.de_np
    print "Extrapolate:", myOpt.de_f, "Crossover:", de_cf
    print "Epsilon:", myOpt.de_epsilon