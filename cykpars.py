import os
import numpy as np
from grammar import rules
import argparse

def findRules(charItem):
	#Empty list to collect the rules found for the
	#Specific charItem
	rulesFound = []
	#Iterate trough rules from grammar.py
	for i,j in rules.items():
		for rule in j:
			#if a rule is found add it to the end of the list
			#Double check for multiple rules
			if rule == charItem:
				rulesFound.append(i)
	return rulesFound

def initArray(tWORD):
	length = len(tWORD)
	height = length
	tArray = np.zeros([height, length], list)
	return tArray

def parseFirst(tWORD, array):
	#possibleProductions = {}
	length = len(tWORD)
	height = length

	#parse first row of array
	#do this seperatly because if one terminalsymbol
	#cant be deducted the word cant be build
	for i in range(length):
		findC = tWORD[i]
		foundC = findRules(findC)
		array[0][i] = foundC
		if(len(foundC) == 0):
			print("Word cant be build")
			print(array)
			#return 1
	#print(array)
	return array

def getDiag(array):
	return array


#MIGHT BE FINE
def getDown(array, possibleProductions, currentHeight, currentLength):
	print("getDown")

	for indexHeight in range(currentHeight):
		#if 0 dann ['0'] oder so
		print("tempSignal= ", indexHeight, "|", currentLength)
		tempSignal = array[indexHeight][currentLength]
		if(tempSignal == 0):
			print("No Production, ignore")
		else:
			print("tempSignal", tempSignal)
			print("array:", array[indexHeight][currentLength])
			possibleProductions.append(tempSignal)
	possibleProductions.reverse()
	print("---EXIT GETDOWN")
	return possibleProductions



def parse(tWORD, array, i):
	length = len(tWORD)
	currentHeight = i
	#The algorithm doesnt need to check every field in the array
	widthLength = length - i
	print("currentHeight", currentHeight)
	for currentLength in range(widthLength):
		print("----FOR LOOP----")
		print("currentLength", currentLength)
		possibleProductions = []
		possibleProductions = getDown(array, possibleProductions, currentHeight, currentLength)
		print("possible:", possibleProductions)
		array = getDiag(array)
	
	return array

def main():
	parser = argparse.ArgumentParser(description="CYK Parser in Python")
	group = parser.add_mutually_exclusive_group()
	parser.add_argument("WORD", type=str, help="word to parse")
	args = parser.parse_args()
	tWORD = args.WORD 

	#WORD = input("Enter the word to test \n")
	array = initArray(tWORD)
	array = parseFirst(tWORD, array)
	#array[1][0] = ['G']
	for i in range(1, len(tWORD)):
		print("main loop:", i)
		array = parse(tWORD, array, i)
	print(array)

if __name__ == "__main__":
	main()