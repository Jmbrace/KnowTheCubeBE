# Author: Julian Bracero
# This class represents a Rubik's cube 

import copy
from rotator import *
import math

class RubixCube():

	def __init__ ( self, state, howWeGotHere = ""):
		self.state = state
		self.howWeGotHere = howWeGotHere

	def isGoalState ( self , goal):
		return ( goal.state == self.state ) 

	def pathCost ( self ):
		return 1
	# This method generates a list of Rubiks cube objects, all of which can be reached by
	# rotating a single face 90 degrees
	def getNextStates ( self ):
		list = []
		# Front rotation
		posMatrix = copy.deepcopy(self.state)
		rotateFront(posMatrix)
		successorState = RubixCube(posMatrix, "F")
		list.append(successorState)

		# Front inverted rotation
		posMatrix = copy.deepcopy(self.state)
		rotateFrontInverted(posMatrix)
		successorState = RubixCube(posMatrix,"Fn")
		list.append(successorState)

		# Front inverted rotation
		posMatrix = copy.deepcopy(self.state)
		rotateBack(posMatrix)
		successorState = RubixCube(posMatrix, "B")
		list.append(successorState)


		posMatrix = copy.deepcopy(self.state)
		rotateBackInverted(posMatrix)
		successorState = RubixCube(posMatrix, "Bn")
		list.append(successorState)


		posMatrix = copy.deepcopy(self.state)
		rotateRight(posMatrix)
		successorState = RubixCube(posMatrix, "R")
		list.append(successorState)


		posMatrix = copy.deepcopy(self.state)
		rotateRightInverted(posMatrix)
		successorState = RubixCube(posMatrix, "Rn")
		list.append(successorState)


		posMatrix = copy.deepcopy(self.state)
		rotateLeft(posMatrix)
		successorState = RubixCube(posMatrix, "L")
		list.append(successorState)


		posMatrix = copy.deepcopy(self.state)
		rotateLeftInverted(posMatrix)
		successorState = RubixCube(posMatrix, "Ln")
		list.append(successorState)


		posMatrix = copy.deepcopy(self.state)
		rotateTop(posMatrix)
		successorState = RubixCube(posMatrix, "T")
		list.append(successorState)


		posMatrix = copy.deepcopy(self.state)
		rotateTopInverted(posMatrix)
		successorState = RubixCube(posMatrix, "Tn")
		list.append(successorState)


		posMatrix = copy.deepcopy(self.state)
		rotateBottom(posMatrix)
		successorState = RubixCube(posMatrix, "Bot")
		list.append(successorState)


		posMatrix = copy.deepcopy(self.state)
		rotateBottomInverted(posMatrix)
		successorState = RubixCube(posMatrix, "Botn")
		list.append(successorState)
		return list

	def toString ( self ):
		return self.howWeGotHere

	def computeHueristic ( self, hueristicHelper ):
		row = 0
		col = 0
		depth = 0
		sum = 0;
		for arrays in self.state:
			col = 0
			for array in arrays:
				depth = 0
				for cubelet in array:
					# sum = sum + math.sqrt(pow((row - hueristicHelper[cubelet][0]),2)  + pow((col - hueristicHelper[cubelet][1]),2) + pow((depth - hueristicHelper[cubelet][2]),2))
					sum = sum + abs(row - hueristicHelper[cubelet][0]) + abs(col - hueristicHelper[cubelet][1]) + abs(depth - hueristicHelper[cubelet][2]);
					depth = depth + 1
				col = col + 1
			row = row +1
		return sum

	def __eq__(self, other):
		return self.state == other.state