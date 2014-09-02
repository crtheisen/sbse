from single_server import single_basic, single_queueing, single_queueing_B
from multi_server import *
from multi_server_b import *
import sys


total = len(sys.argv)
if total != 2:
	print 'Usage: python', str(sys.argv[0]), '<problem_number>'
	exit(0)
	
problem = str(sys.argv[1])

if problem == '1':
	print 'Problem 1:'
	single_basic()
	
elif problem == '2':
	print 'Problem 2:'
	my_rate = .2
	while my_rate <= .951:
		single_queueing(my_rate, 200000, 1)
		my_rate = my_rate + .15
		
elif problem == '3':
	print 'Problem 3:'
	my_B = 10
	while my_B <= 50:
		single_queueing_B(.95, my_B, 200000, 1)
		my_B = my_B + 5
		
elif problem == '4a':
	#1: 3(lambda) arrival, 3 servers rate mu
	my_lambda = .1
	while my_lambda <= .91:
		single_queueing_3_server(my_lambda, 10000, 200000, 1)
		my_lambda = my_lambda + .1

elif problem == '4b':	
	#2: 3(lambda) arrival, 1 server rate 3*mu
	my_lambda = .1
	while my_lambda <= .91:
		single_queueing(3*my_lambda, 200000, 3*1)
		my_lambda = my_lambda + .1

elif problem == '4c':
	#3: 3 queue lambda arrival, 1 server rate 3*mu (priority)
	my_lambda = .1
	while my_lambda <= .91:
		three_queueing_single_server_priority(my_lambda, 10000, 200000, 3*1)
		my_lambda = my_lambda + .1

elif problem == '4d':	
	#4: 3 queue lambda arrival, 1 server rate 3*mu (Longest Queue First)
	my_lambda = .1
	while my_lambda <= .91:
		three_queueing_single_server_LQF(my_lambda, 10000, 200000, 3*1)
		my_lambda = my_lambda + .1
	
elif problem == '5a':
	#1: 3(lambda) arrival, 3 servers rate mu
	my_B = 10
	while my_B <= 50:
		single_queueing_3_server_b(3*0.9, my_B, 200000, 1)
		my_B = my_B + 5

elif problem == '5b':	
	#2: 3(lambda) arrival, 1 server rate 3*mu
	my_B = 10
	while my_B <= 50:
		single_queueing_B(3*0.9, my_B, 200000, 3*1)
		my_B = my_B + 5

elif problem == '5c':
	#3: 3 queue lambda arrival, 1 server rate 3*mu (priority)
	my_B = 10
	while my_B <= 50:
		three_queueing_single_server_priority_b(0.9, my_B, 200000, 3*1)
		my_B = my_B + 5

elif problem == '5d':	
	#4: 3 queue lambda arrival, 1 server rate 3*mu (Longest Queue First)
	my_B = 10
	while my_B <= 50:
		three_queueing_single_server_LQF_b(0.9, my_B, 200000, 3*1)
		my_B = my_B + 5
		
elif problem == 'custom':
	#Use this space to construct custom queries for testing.
	three_queueing_single_server_LQF_b(0.9, 10, 200000, 3*1)
	
else:
	print 'Invalid Problem Specified. Exiting.'
	print 'Usage: python', str(sys.argv[0]), '<problem_number>'
