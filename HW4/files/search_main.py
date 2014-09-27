import sys
from datetime import datetime
import random

sys.dont_write_bytecode = True

from models import *
from searchers import *
from utils import *
from options import *

myOpt = Options()

#Inspired by vivekaxl's display function
def display(model, searcher, startTime, scores, r):
  print "==============================================================="
  print "Model Name: ", model.__name__
  print "Searcher Name: ", searcher.name
  diff = (datetime.now() - startTime).total_seconds()
  myOpt.printGlobals()
  searcher.printOptions()
  print "Time to run (s): ", diff
  if r == 0:
    print "No valid runs!"
  else:
    print "Runs: ", r
    print "Average per run (s): ", diff/r
    print xtile(scores,width=25,show=" %1.5f")
  print "==============================================================="

def main(modelList, searcherList):
  r = 10
  for klass in modelList:
    for searcher in searcherList:
      startTime = datetime.now()
      scores = []
      myKlass = klass()
      mySearcher = searcher()
      random.seed(myOpt.seed)
      for _ in range(r):
        result, valid = mySearcher.run(myKlass)
        if valid == True:
          scores.append(result)
      display(klass, mySearcher, startTime, scores, len(scores))

modelList = [ZDT3, Viennet3]
searcherList = [MWS]

main(modelList, searcherList)