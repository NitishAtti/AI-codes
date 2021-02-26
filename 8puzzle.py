import numpy as np
import math
import scipy.linalg

class Puzzle:
	def __init__(self,state,parent=None):
		self.state=state
		self.emptyIndex = (np.where(self.state==0)[0][0],np.where(self.state==0)[1][0])
		self.parent=parent
	def __str__(self):
		return str(self.state)

goal = np.array ([
	[1,2,3],
	[4,0,5],
	[6,7,8]])

def getPossibleMoves(puzzleObject):
	possiblStates=[]
	x=puzzleObject.emptyIndex[0]
	y=puzzleObject.emptyIndex[1]
	possX=[x-1,x+1]
	possY=[y-1,y+1]
	for i in possX:
		if (i<0 or i>2):
			possX.remove(i)
	for i in possY:
		if (i<0 or i>2):
			possY.remove(i)
	movableIndices=[]
	for i in possX:
		movableIndices.append((i,y))
	for i in possY:
		movableIndices.append((x,i))
	possibleStates=[]
	for movableIndex in movableIndices:
		newState=puzzleObject.state.copy()
		newState[puzzleObject.emptyIndex]=newState[movableIndex]
		newState[movableIndex]=0
		possibleStates.append(Puzzle(state=newState,parent=puzzleObject))
	return possibleStates

def heuristicMisplaced(state):
	h=0
	goalBase=[]
	for i in range(3):
		for j in range(3):
			if((i,j) != (1,1)):
				goalBase.append((i,j))
	for i in range(1,9):
		p=np.where(state==i)
		index=(p[0][0],p[1][0])
		if(index!=goalBase[i-1]):
			h=h+1
	if(np.where(state==0)[0][0] != 1 or np.where(state==0)[1][0] !=1):
		h=h+1
	return h

def heuristicManhattan(state):
	h=0
	goalBase=[]
	for i in range(3):
		for j in range(3):
			if((i,j) != (1,1)):
				goalBase.append((i,j))
	for i in range(1,9):
		p=np.where(state==i)
		index=(p[0][0],p[1][0])
		h=h+abs(goalBase[i-1][0]-index[0]) + abs(goalBase[i-1][1]-index[1])
	h=h+abs(1-np.where(state==0)[0][0]) + abs(1-np.where(state==0)[1][0])
	return h

def checkGoalState(state):
	for i,j in zip(state,goal):
		for k,l in zip(i,j):
			if(k!=l):
				return False
	return True 

def goalInFrontier(frontier):
	for i in frontier:
		if(checkGoalState(i.state)):
			return i
	return None

def doesPathExist(puzzleObject):
	found=False
	frontier=[]
	visited=[]
	n=0

	while(not found):
		n=n+1
		visited.append(puzzleObject.state)
		frontier.extend(getPossibleMoves(puzzleObject))
		for i in visited:
			for j in frontier:
				if(np.array_equal(j.state,i)):
					frontier.remove(j)
					break
		p=goalInFrontier(frontier)
		if(p!=None):
			print("yes")
			found=True
		else:
			#print(visited)
			puzzleObject=frontier[0]
	print("found")


def getPath(puzzleObject):
	frontier=[]
	visited=[]
	path=[]
	n=0
	init=puzzleObject
	found=False

	while (not found):
		print(n)
		n=n+1
		visited.append(puzzleObject.state)
		frontier.extend(getPossibleMoves(puzzleObject))
		for i in visited:
			for j in frontier:
				if(np.array_equal(j.state,i)):
					frontier.remove(j)
					break
		p=goalInFrontier(frontier)
		if(p!=None):
			found=True
			while(p.parent!=None):
				path.append(p)
				p=p.parent
			path.append(init)
		else:
			min=math.inf
			next=None
			for i in frontier:
				if(heuristicManhattan(i.state)<min):
					min=heuristicManhattan(i.state)
					next=i
			puzzleObject=next
	path.reverse()
	for i in path:	
		print(i)

init=np.array([
	[1,2,4],
	[8,3,7],
	[6,5,0]],dtype=float)
g=[
	np.array([
	[1,2,3],
	[4,5,0],
	[6,7,8]]),
	np.array([
	[1,2,3],
	[0,4,5],
	[6,7,8]]),
	np.array([
	[1,0,3],
	[4,2,5],
	[6,7,8]]),
	np.array([
	[1,2,3],
	[4,7,5],
	[6,0,8]])
	]

puzzleObject=Puzzle(init)
getPath(puzzleObject)

def removeTwoBack(two_back,possible_moves):
	if(two_back is not None):
		for i in possible_moves:
			if i.state == two_back:
				possible_moves.remove(i)


def check(puzzleObject):
	init=puzzleObject
	two_back=None
	possible_moves=getPossibleMoves(init)
	removeTwoBack(two_back,possible_moves)
	for i in possible_moves:
		two_back=init
		possible_moves=getPossibleMoves(i)
		removeTwoBack(two_back,possible_moves)
		
	n=0
	while (checkattain(visited,init)==False):
		n+=1
		moves=getPossibleMoves(init)

#getPath(puzzleObject)