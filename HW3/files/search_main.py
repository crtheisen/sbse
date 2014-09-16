import sys

sys.dont_write_bytecode = True

from fonseca_model import *
from schaffer_model import *
from kursawe_model import *
from ZDT1_model import *

from sim_anneal import *
from max_walk_sat import *

r = 1
for klass in [Fonseca, Schaffer, Kursawe, ZDT1]:
  print klass.__name__ + ":"
  for searcher in [SA, MWS]:
    #searcher(500, .6, 500, .00001).run(klass)
    n = 0.0
    for _ in range(r):
      n += searcher(500, .6, 500, .00001, False).run(klass)
      print searcher.__name__ + ':',  n/r
      
      
#TODOs (roughly prioritized)

#Implement models folder and searchers folder to import

# Actually implement the numerical analysis functions in searchers
#     -this includes saving of the seed. THIS IS REALLY IMPORTANT DO NOT FORGET

#Further abstraction of models; lots of repeated code

# Break out prints of the algorithm into a debug setting (can turn off/on as needed)
#     -this kind of works now, but I need to handle prints as well without ugly
#      if statements. It's bad and I should feel bad. Will be important for
#      checking if new models work!