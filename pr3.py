# Student: Bryan Allen
# Class: CS456 Spring 2015
# Assignment: Project 2
# Required Files: alphabet.txt
# To Run: navigate to folder containing pr2.py in console/terminal and enter: python pr2.py

import os, sys
class Node:
	def __init__(self, score=None, dir=None, prev=None):
		self.score = score
		self.dir = dir
		self.prev = prev
		
def getScore(x, y):
	if x == y:
		return MATCH
	elif x in VOWELS and y in VOWELS:
		return SIMILAR
	elif [x, y] in PAIRS:
		return SIMILAR
	else:
		return DIFFERENT

if __name__ == "__main__":
	MATCH = 2
	SIMILAR = 1
	DIFFERENT = -1
	GAP = -2
	VOWELS = ['a', 'e', 'i', 'o', 'u']
	PAIRS = (['b', 'p'], ['c', 'k'], ['c', 's'], ['d', 't'], ['e', 'y'], ['g', 'j'], ['g', 'k'], ['i', 'y'], ['k', 'q'], ['m', 'n'], ['s', 'z'], ['v', 'w'])
	
	#s1 = raw_input('string 1: ')
	#s2 = raw_input('string 2: ')
	s1 = 'selects'
	s2 = 'salekt'
	
	matrix = [[x for x in range(len(s2)+1)] for y in range(len(s1)+1)]
	
	#initialize
	matrix[0][0] = Node(0, '', None)
	for i in range(1, len(s1)):
		matrix[i][0] = Node(i*GAP, 'H', [i-1, 0])
	for j in range(1, len(s1)):
		matrix[0][j] = Node(j*GAP, 'V', [0, j-1])
		
	