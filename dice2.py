#!/usr/bin/env python3
import logging
import os
#from statsd import StatsClient
import timeit
from time import time


statsd = StatsClient()
os.remove("dice2.log")
logging.basicConfig(filename='dice2.log',level=logging.DEBUG)

def score(dice):
	sum = 0
	for i in dice:
		sum+=i
	return sum

def rollEachFace(dice,sides,requiredscore,id):
	count = 0
	for i in range(0,id):
		while(dice[i]<=sides-1):
			total=score(dice)
			logging.debug(dice)
			if score==requiredscore:
				count+=1
			if(i>0):
				rollEachFace(dice,sides,requiredscore,i-1)
			dice[i]+=1
	return count





def rollDice(dice,requiredscore):
	match = 0
	count = 0
	for i in range(1,7):
		dice[0]=i
		for k in range(1,7):
			dice[1]=k
			for l in range(1,7):
				dice[2]=l
				logging.debug(dice)
				count +=1
				if(score(dice)==requiredscore):
					match+=1
					

	return [match,count]
def generatedice(number):
	dice=[]
	for i in range(0,number):
		dice.append(1)
	return dice

def listfaces(dice,face,requiredscore,index=99):
	match = 0
	count = 0
	if (index==99):
		index=len(dice)-1
	for i in range(1,face+1):
		dice[index]=i
		digit = index
		if(index ==0):
			logging.debug(dice)
			logging.debug(score(dice))
			count+=1
			if (score(dice)==requiredscore):
				match+=1
		elif(index > 0):
			match+=listfaces(dice,face,requiredscore,index=(index-1))['match']
			count+=listfaces(dice,face,requiredscore,index=(index-1))['count']
	return {'match':match,'count':count}


def rollDice2(requiredscore,numberofdice,face):
	
	dice=generatedice(numberofdice)
	match =listfaces(dice,face,requiredscore)
	return match


#print(rollDice([1,1,1],6))
t0=time()
print(rollDice2(10,5,6))
t1=time()
print('the function took %.2f seconds' % (t1-t0))
