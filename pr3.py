# Student: Bryan Allen
# Class: CS456 Spring 2015
# Assignment: Project 3
# To Run: navigate to folder containing pr3.py in console/terminal and enter: python pr3.py

import re
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
	elif [x, y] in PAIRS or [y, x] in PAIRS:
		return SIMILAR
	else:
		return DIFFERENT
		
def buildOpt(x, y):
	if matrix[x][y].prev == None:
		return matrix[x][y].dir, matrix[x][y].score
	else:
		d = matrix[x][y].dir
		score = matrix[x][y].score
		
		t, s = buildOpt(matrix[x][y].prev[0], matrix[x][y].prev[1])
		
		d = t + d
		score += s
	return d, score

if __name__ == "__main__":
	MATCH = 2
	SIMILAR = 1
	DIFFERENT = -1
	GAP = -2
	VOWELS = ['a', 'e', 'i', 'o', 'u']
	PAIRS = (['b', 'p'], ['c', 'k'], ['c', 's'], ['d', 't'], ['e', 'y'], ['g', 'j'], ['g', 'k'], ['i', 'y'], ['k', 'q'], ['m', 'n'], ['s', 'z'], ['v', 'w'])
	
	# get input
	reg = re.compile('[a-z]+')
	
	s1 = ''
	r = reg.match(s1)
	while not r or not r.group() == s1:
		s1 = raw_input('string 1: ')
		r = reg.match(s1)
		
	s2 = ''
	r = reg.match(s2)
	while not r or not r.group() == s2:
		s2 = raw_input('string 2: ')
		r = reg.match(s2)
	
	# create matrix
	matrix = [[x for x in range(len(s2)+1)] for y in range(len(s1)+1)]
	
	# initialize matrix
	matrix[0][0] = Node(0, '', None)
	for i in range(1, len(s1)+1):
		matrix[i][0] = Node(i*GAP, 'H', [i-1, 0])
	for j in range(1, len(s2)+1):
		matrix[0][j] = Node(j*GAP, 'V', [0, j-1])
		
	# build matrix
	for i in range(1, len(s1)+1):
		for j in range(1, len(s2)+1):
			score = getScore(s1[i-1], s2[j-1])
			diag = matrix[i-1][j-1].score + score
			hori = matrix[i-1][j].score + GAP
			vert = matrix[i][j-1].score + GAP
			fullScore = max(diag, hori, vert)
			
			if fullScore == diag:
				dir = 'D'
				prev = [i-1, j-1]
			elif fullScore == hori:
				dir = 'H'
				prev = [i-1, j]
			else:
				dir = 'V'
				prev = [i, j-1]
			matrix[i][j] = Node(fullScore, dir, prev)
			
	# build optimal sequence
	opt, totalScore = buildOpt(len(s1), len(s2))
	
	# print optimal sequence and total score
	print ''
	print 'optimal sequence:', opt
	print 'total score:', totalScore
	print ''
	
	# print optimal strings
	opts1 = ''
	opts2 = ''
	k = 0
	for l in opt:
		if l == 'V':
			opts1 += '_'
		else:
			opts1 += s1[k]
			k += 1
	k = 0
	for l in opt:
		if l == 'H':
			opts2 += '_'
		else:
			opts2 += s2[k]
			k += 1
	print opts1
	print opts2
			