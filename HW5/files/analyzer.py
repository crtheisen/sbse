#Structure from SA Lecture
import sys,re,random,math
sys.dont_write_bytecode = True
  
from options import *
from utils import *
from sk import *

myOpt = Options()

class Analyzer:
  n = 50
  old = [1 for i in range (0, n)]
  new = [1 for i in range (0, n)]
  era_lives = myOpt.era_lives;

  def bettered(self, new, old):

    def quartiles(value):
      return value*.25, value*.5, value*.75
      
    def betterifless():
      p1, median1, p3 = quartiles(new)
      IQR1=p3-p1
      p1, median2, p3 = quartiles(old)
      IQR2=p3-p1
      return median1<median2, IQR1<IQR2
      
    def same(): return a12(new, old)<=0.56
    
    betterMedian, betterIQR = betterifless()
    return betterMedian, betterIQR, same()
      
  def EraStop(self, lst):
    self.old = self.new
    self.new = lst
    out = False
    betterMedian = False
    betterIQR = False
    same = False
    
    #print self.old
    #print self.new
    oldQ1, oldMedian, oldQ3 = quartiles(self.old)
    newQ1, newMedian, newQ3 = quartiles(self.new)
    if newMedian < oldMedian:
      betterMedian = True
    if newQ3 - newQ1 < oldQ3 - oldQ1:
      betterIQR = True
    if a12(self.new, self.old) <= myOpt.a12_test:
      same = True
    
    #worsed
    if (same and not betterIQR) or (not same and not betterMedian):
      out = False
    #bettered
    elif (not same and betterMedian):
      out = True
    
    if out:
      self.era_lives += 1
    else:
      self.era_lives -= 1
    if self.era_lives == 0:
      print "Early Era Termination!"
      return True
    else:
      return False
      
#from menzies code
def median(lst,ordered=False):
  if not ordered: lst= sorted(lst)
  n = len(lst)
  p = n//2
  if n % 2: return lst[p]
  q = p - 1
  q = max(0,min(q,n))
  return (lst[p] + lst[q])/2
  
def quartiles(lst):
  q1 = lst[int(len(lst)*.25)]
  med = median(lst, False)
  q3 = lst[int(len(lst)*.5)]
  return q1, med, q3