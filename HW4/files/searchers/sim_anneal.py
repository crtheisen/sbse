#Structure from SA Lecture
import sys,re,random,math
sys.dont_write_bytecode = True

from options import *
myOpt = Options()

class SA:
  
  def say(self, x): 
    if myOpt.debug:
      sys.stdout.write(str(x)); sys.stdout.flush()

  def run(self, klass):
    sa = klass
    XVarBest = sa.XVar
    eBest = e = 1
    #print 'start energy: ', eBest           
    k = 1
    self.say(int(math.fabs(eBest-1)*100))
    self.say(' ')
    while k < myOpt.sa_kmax:   
      sa.Neighbor()
      eNew = sa.Energy()
      if eNew < eBest:               
        eBest = eNew
        XVarBest = list(sa.XVar)
        self.say('!')
  
      if eNew < e:                 
        e = eNew     
        self.say('+')       
      #Probability Check from SA Lecture
      elif math.exp(-1*(eNew-e)/(k/myOpt.sa_kmax**myOpt.sa_cooling))<random.uniform(0,1):
      #P function should be between 0 and 1
      #more random hops early, then decreasing as time goes on
        sa.Chaos()
        self.say('?')        
      self.say('.')
      k = k + 1
      if k % 50 == 0 and k != myOpt.sa_kmax:
        #print ''
        self.say(int(math.fabs(eBest-1)*100))
        self.say(' ')

    if myOpt.debug:
      #print '\nFound best - e: ', eBest
      #print 'Variables: '
      for vars in XVarBest:
        self.say(vars)
        self.say(", ")
      #print "\n"
    return eBest, True
    
  def printOptions():
    print "SA Options:"
    print "KMAX: ", myOpt.sa_kmax, "Cooling: ", myOpt.mws_cooling