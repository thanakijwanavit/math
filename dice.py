#!/usr/bin/env python3
import logging
logging.basicConfig(filename='dice.log',level=logging.ERROR)
def sumdice(diceValue):
	sum=0
	for i in diceValue:
		sum += i
	return sum
def tryEachSide(diceface,diceValue,outcome,diceID):
	totaloutcome=0
	for i in range(1,diceface+1):
		diceValue[diceID]=i
		logging.error(diceValue)
		logging.debug("i is %s" % i)
		logging.debug("diceface is %s" % diceface)
		score = sumdice(diceValue)
		logging.info('the total score is %s' %score)
		nextDigit = diceID -1
#		if i == 6:
#			diceValue[diceID]=1
#			continue
		if score == outcome:
			totaloutcome+=1
#		if i == 1:
		while(nextDigit>=0):
#			if(nextDigit==0):
#				break
#			diceValue[nextDigit]=1
			totaloutcome+=tryEachSide(diceface,diceValue,outcome,nextDigit)
#			logging.error(nextDigit)
			logging.error('diceID is %s nextDigit is %s' % (diceID,nextDigit))
			nextDigit-=1
	return totaloutcome

def createDice(numberOfDice):
	diceValue = []
	for i in range (0,numberOfDice):
		diceValue.append(1)
	return diceValue

def numberOfOutcome(diceface,outcome,numberOfDice):
	diceValue = createDice(numberOfDice)
	totaloutcome = 0
	for die in range(1,numberOfDice):
		totaloutcome += rollEachOne(numberOfDice,diceValue,diceface,outcome,die)
	return totaloutcome

def rollEachOne(numberOfDice,diceValue,diceface,outcome,die):
	totaloutcome = 0
	'''
	for k in range(1,diceface+1):
				diceValue[die+1]=k
				logging.warning('k is %s' % k)
				logging.warning('diceValue is %s' % diceValue)
	'''
	totaloutcome += tryEachSide(diceface,diceValue,outcome,die)
	return totaloutcome


print(tryEachSide(6,[1,1,1],10,2))
#print(sumdice([1,2,3]))
