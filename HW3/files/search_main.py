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
  print "Searcher Name: ", searcher.__name__
  diff = (datetime.now() - startTime).total_seconds()
  print "Time to run (s): ", diff
  if r == 0:
    print "No valid runs!"
  else:
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
      random.seed(myOpt.seed)
      for _ in range(r):
        result, valid = searcher().run(myKlass)
        if valid == True:
          scores.append(result)
      display(klass, searcher, startTime, scores, len(scores))

modelList = [Fonseca, Schaffer, Kursawe, ZDT1]
searcherList = [SA, MWS]

main(modelList, searcherList)