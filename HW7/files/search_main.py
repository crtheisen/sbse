import sys
from datetime import datetime
import random

sys.dont_write_bytecode = True

from models import *
from searchers import *
from utils import *
from options import *
from sk import *

myOpt = Options()

#Inspired by vivekaxl's display function
def display(model, searcher, startTime, scores, r):
  print "==============================================================="
  print "Model Name: ", model.__name__
  print "Searcher Name: ", searcher.__class__.__name__
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
  r = 30
  for klass in modelList:
    classScoreList = []
    for searcher in searcherList:
      fullScoreList = []
      startTime = datetime.now()
      scores = []
      mySearcher = searcher()
      random.seed(myOpt.seed)
      for _ in range(r):
        myKlass = klass()
        result, valid = mySearcher.run(myKlass)
        if valid == True:
          scores.append(result)
      display(klass, mySearcher, startTime, scores, len(scores))
      fullScoreList.append(searcher.__name__)
      for x in scores:
        fullScoreList.append(x)
      if scores:
        classScoreList.append(fullScoreList)
    print "Scott-Knott for", klass.__name__
    rdivDemo(classScoreList)
    print "\n"

modelList = [Schaffer, Kursawe, ZDT1, ZDT3, Viennet3, Schwefel, Osyczka]
searcherList = [DE, PSO, SA, MWS, GA]
#modelList = [Osyczka]
#searcherList = [SA]

main(modelList, searcherList)