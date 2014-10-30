#Structure from SA Lecture
import sys,re,random,math
import copy
sys.dont_write_bytecode = True

from options import *
from utils import *
from analyzer import *

import itertools

myOpt = Options()

#Structure from:
#http://www.cleveralgorithms.com/nature-inspired/evolution/genetic_algorithm.html
class GA:

  def Mutate(self, child, pMut):
    for x in range(0, len(child.XVar)):
      if(random.random() < pMut):
        child.specificMutate(x)
    return child

  #Based on WeiFoo's crossover
  def Crossover(self, parent1, parent2, crossovers):
    def what(lst):
      return lst[0] if isinstance(lst, list) else lst
    child = parent1
    if rand()> myOpt.ga_crossover:
      return parent1
    else:
      index = sorted([random.randint(0, parent1.n - 1) for _ in xrange(crossovers)])
      child.XVar = parent1.XVar[:]
      child.XVar[index[0]:index[1]] = parent2.XVar[index[0]:index[1]]
    return child
    
  def SelectParents(self, pop): #all possible parents
    temp = []
    for x in pop:
      for y in pop:
        if x != y:
          temp.append([x, y])
    return temp
        
  def GetBestSolutions(self, pop):
    eMin = 1
    temp = []
    temp2 = []
    seen = []
    for x in pop:
      if x.Energy() not in seen:
        temp.append([x.Energy(), x])
        seen.append(x.Energy())
    temp.sort(key = lambda x: x[0])
    for x in range (0, 50):
      temp2.append(temp[x][1])
      #print temp[x]
    return temp[0][0], temp2

  def run(self, klass):
    ga = klass
    pMutate = 1.0/len(ga.XVar)
    XVarBest = ga.XVar
    #print 'start energy: ', eBest           
    k = 1
    eList = []
    population = []
    analyze = Analyzer()
    stop = False
    
    for i in range(myOpt.ga_pop_size):
      ga.Chaos()
      population.append(copy.deepcopy(ga)) #add a randomly generated model to list
  
    for gens in myOpt.ga_gen_list:
      eBest = 1
      while k < gens:
        parents = self.SelectParents(population) #all possible pairings of parents
        children = []
        for parent1, parent2 in parents:
          child = self.Crossover(parent1, parent2, 2)
          children.append(self.Mutate(child, pMutate))
        eBest, population = self.GetBestSolutions(children)
        k += 1
        eList.append(eBest)
      #some "is significantly better" termination logic here
  
    return min(eList), True

  def printOptions(self):
    print "GA Options:"
    print "popSize:", myOpt.ga_pop_size, "Crossover:", myOpt.ga_crossover 
    print "Gens:", myOpt.ga_gen_list