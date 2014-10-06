#Structure from SA Lecture
import sys,re,random,math
import copy
sys.dont_write_bytecode = True

from options import *
from utils import *
from analyzer import *

myOpt = Options()

#Structure from:
#http://www.cleveralgorithms.com/nature-inspired/evolution/genetic_algorithm.html
class GA:

  def Mutate(self, child, pMut):
    for x in range(0, len(child.XVar)):
      if(random.random() < pMut):
        child.specificMutate(x)
    return child

  def Crossover(self, parent1, parent2, crossover):
    #BECAUSE REASONS OK TODO
    return parent1, parent2
    
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
          child1, child2 = self.Crossover(parent1, parent2, myOpt.ga_crossover)
          children.append(self.Mutate(child1, pMutate))
          children.append(self.Mutate(child2, pMutate))
        eBest, population = self.GetBestSolutions(children)
        k += 1
        eList.append(eBest)
      #some "is significantly better" termination logic here
  
    return min(eList), True

  def printOptions(self):
    print "GA Options:"
    print "popSize:", myOpt.ga_pop_size, "Crossover:", myOpt.ga_crossover 
    print "Gens:", myOpt.ga_gen_list