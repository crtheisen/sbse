#Structure from SA Lecture
import sys,re,random,math
sys.dont_write_bytecode = True
  
class MWS:
  maxTries = 500
  maxChanges = 500
  cooling = .6
  threshold = .000001
  debug = False
  
  def say(self, x): 
    if self.debug:
      sys.stdout.write(str(x)); sys.stdout.flush()

  def specificRun(self, probability, klass):
    fon = klass()
    XVarBest = fon.XVar
    eBest = e = 1       
    k = 1
    self.say(int(math.fabs(eBest-1)*100))
    self.say(' ')
    for i in xrange(self.maxTries): 
      fon.Chaos()
      for j in xrange(self.maxChanges):
        eNew = fon.Energy()
        if(eNew < self.threshold):
          #% means found a solution and quit
          self.say('%')
          eBest = eNew
          XVarBest = list(fon.XVar)
          #print '\nQuitting...'
          return eBest, XVarBest
        else:
          #modify random part of solution
          if probability > random.uniform(0,1):
            fon.Neighbor()
            self.say('+')
          #maximize for some random
          else:
            fon.BestNeighbor()
          self.say('.')
          if (i+1)*(j+1) % 40 == 0:
            #print ''
            self.say(int(math.fabs(eNew-1)*100))
            self.say(' ')
      #print ''
      return -1, XVarBest
      
  def run(self, klass):
    theBest = 0.0
    totalFound = 0
    for i in [0.25, 0.5, 0.75]:
      eBest, XVarBest = self.specificRun(i, klass)
      if eBest == -1:
        #print 'No Best Found for prob = ', i
        self.say('')
      else:
        #print 'Found best - e: ', eBest, ' for prob = ', i
        #print 'Variables: '
        for vars in XVarBest:
          self.say(vars)
          self.say(", ")
        #print "\n"
        theBest += eBest
        totalFound += 1
    if totalFound != 0:
      return theBest/totalFound
    else:
      return 2
        
  def __init__(self, newMaxTries, newCooling, newMaxChanges, newT, newDebug):
    self.maxTries = newMaxTries
    self.cooling = newCooling
    self.maxChanges = newMaxChanges
    self.threshold = newT
    self.debug = newDebug