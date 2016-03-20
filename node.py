# Author: Julian Bracero
# Simple node class that stores a cube configuration
class Node:
	def __init__( self, state, pathCostSoFar, parent=None ):
		self.state = state
		self.pathCost = pathCostSoFar + state.pathCost()
		self.parent = parent
