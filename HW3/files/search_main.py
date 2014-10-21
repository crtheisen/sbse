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
def display(model, searcher, startTime, scores, r, prob):
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
  r = 10
  for klass in modelList:
    classScoreList = []
    for searcher in searcherList:
      for loopTemp in [.25, .5, .75]:
        fullScoreList = []
        startTime = datetime.now()
        scores = []
        myKlass = klass()
        mySearcher = searcher()
        random.seed(myOpt.seed)
        for _ in range(r):
          result, valid = mySearcher.run(myKlass, loopTemp)
          if valid == True:
            scores.append(result)
        display(klass, mySearcher, startTime, scores, len(scores), loopTemp)
        fullScoreList.append(searcher.__name__)
        for x in scores:
          fullScoreList.append(x)
        if scores:
          classScoreList.append(fullScoreList)
        if mySearcher.__class__.__name__ == "SA":
          break
    print "Scott-Knott for", klass.__name__
    rdivDemo(classScoreList)
      

modelList = [Fonseca, Schaffer, Kursawe, ZDT1]
searcherList = [SA, MWS]
#modelList = [ZDT1]
#searcherList = [SA, MWS]

main(modelList, searcherList)