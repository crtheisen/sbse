import math
import random

Seed = 10
random.seed( Seed )

def expTime(rate):
     #Individual values in exponential distribution can be represented via:
     #x = ln(1-R)/(-lambda)
     #Can do this because of inversion method: this is arrived at via
     #integrating and inverting the exponential distribution:
     #F(y) = 1 - e^(-(lambda)y)
     #
     #Can use this function for both arrival rate and service rate. Mu = 1 for
     #entire project, so for service rate, we will always call expTime(1).
     return math.log(1.0 - random.uniform(1, 10000000)) / -rate
     
class Packet:
    #Packet Class. Returns arrival time, wait time, service time
    arrival = -1.0
    serviceStart = -1.0
    service = -1.0
    
    def getTotalTime(self):
        return (self.serviceStart+self.service)-self.arrival