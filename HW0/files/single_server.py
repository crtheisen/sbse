from Queue import *
import matplotlib.pyplot as plt
import numpy as np

from sim_definitions import expTime, Packet, Seed

def single_basic():
	B = 5
	N = 200000
	rate = 0.5
	mu = 1
	total = 0

	list = []
	for x in xrange(1, N):
		total = total + 1
		list.append(expTime(rate));
	hist, bins = np.histogram(list, bins=200, normed=True)
	width = 0.7 * (bins[1] - bins[0])
	center = (bins[:-1] + bins[1:]) / 2
	plt.bar(center, hist, align='center', width=width)
	plt.show()
	print 'Total:', total
	print 'Average Arrival Time:', sum(list)/N
	print 'Seed:', Seed

def single_queueing(rate, N, mu):
	currentTime = 0
	totalLeft = N
	q = Queue()
	lost = 0.0
	minWait = 9999999
	maxWait = 0
	serverBusy = 0

	list = []
	while totalLeft > 0:

		oldTime = currentTime
		nextArrival = currentTime + expTime(rate)
		nextDeparture = currentTime + expTime(mu)
		currentTime = min(nextArrival, nextDeparture)

		if nextArrival < nextDeparture and not(q.full()):
			totalLeft = totalLeft - 1
			packet = Packet()
			packet.arrival = currentTime
			q.put(packet)
		if nextArrival >= nextDeparture and not(q.empty()):
			item = q.get()
			currentWait = currentTime-item.arrival
			if currentWait < minWait:
				minWait = currentWait
			elif currentWait > maxWait:
				maxWait = currentWait
			list.append(currentTime-item.arrival)
		if not(q.empty()):
			serverBusy = serverBusy + (currentTime - oldTime)
			
	print 'Parameters - Seed:', Seed, 'Rate:', rate, 'Mu:', mu, 'Number:', N
	print 'End Time of Simulation:', currentTime
	print 'Wait Times - Average:', sum(list)/N,
	print 'Server Utilization: ', serverBusy/currentTime
	print 'Percentage lost: ', (lost/(N+lost))*100, '%'
	print ''
	
def single_queueing_B(rate, B, N, mu):
	
	currentTime = 0
	totalLeft = 0
	lost = 0.0
	##Queue size plus the service position, so B+1
	q = Queue(maxsize=B+1)
	serverBusy = 0
	minWait = 9999999
	maxWait = 0

	list = []
	while totalLeft < N:
	
		oldTime = currentTime
		nextArrival = currentTime + expTime(rate)
		if q.empty():
			currentTime = nextArrival
			nextDeparture = nextArrival + 1
		else:
			nextDeparture = currentTime + expTime(mu)
			currentTime = min(nextArrival, nextDeparture)
			
		if nextArrival < nextDeparture:
			if q.full():
				lost = lost + 1.0
			else:
				packet = Packet()
				packet.arrival = currentTime
				q.put(packet)		

		elif nextArrival >= nextDeparture:
			item = q.get()
			list.append(currentTime-item.arrival)
			currentWait = currentTime-item.arrival
			if currentWait < minWait:
				minWait = currentWait
			elif currentWait > maxWait:
				maxWait = currentWait
			totalLeft = totalLeft + 1
		
		if not(q.empty()):
			serverBusy = serverBusy + (currentTime - oldTime)
	
	print 'Parameters - Seed:', Seed, 'Rate:', rate, 'Mu:', mu, 'Number:', N
	print 'End Time of Simulation:', currentTime
	print 'Wait Times - Average (B=', B, ')', sum(list)/N
	print 'Server Utilization: ', serverBusy/currentTime
	print 'Percentage lost: ', (lost/(N+lost))*100, '%'
	print ''