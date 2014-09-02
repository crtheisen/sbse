#From Class Discussion 8/26/2014
from __future__ import division
import sys,re,random,math
sys.dont_write_bytecode = True

kmax = 100000 #100000 run trial for max

rand = random.random

low = 100

def say(x): 
  sys.stdout.write(str(x)); sys.stdout.flush()
  
def Energy(x):
	ans = math.fabs((x*x) - (x-2)*(x-2))
	return ans

def Neighbor(x):
	return random.uniform(-10, 10)

def eMax():
	s = random.uniform(-10, 10) #random start
	e = Energy(s)  
	sBest = s
	eBest = e             
	k = 1
	while k < kmax:   
		sNew = Neighbor(s)
		eNew = Energy(sNew)
		if eNew > eBest: #find largest difference               
			sBest = sNew 
			eBest = eNew
		k = k + 1
	
	print 'Found eMax - s:', sBest, ' e: ', eBest
	
def eMin():
	s = random.uniform(-10, 10) #random start
	e = Energy(s)  
	sBest = s
	eBest = e             
	k = 1
	while k < kmax:   
		sNew = Neighbor(s)
		eNew = Energy(sNew)
		if eNew < eBest: #find smallest difference               
			sBest = sNew 
			eBest = eNew
		k = k + 1
	
	print 'Found eMin - s:', sBest, ' e: ', eBest
	
eMax()
eMin()
		          