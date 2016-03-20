# Author: Julian Bracero
# This module defines 12 methods that have the effect of rotating
# a rubik's cube. This is done by taking the cubelets on the face we
# wish to rotate, tranposing them to the origin of 3 dimensional space, then
# applying the appropriate rotation matrix to rotate the face, then we transpose
# the cubelets back to the correct postition in 3 dimensional space. For a more
# comprehensive description email me at julianbracero@gmail.com

def rotateFront(positionMatrix):
	#a Cubelet is a tuple pair (label, coordinatePos) 
	cubelets = []

	cubelets.append((positionMatrix[0][0][0], (-1,-1,0)))
	cubelets.append((positionMatrix[0][1][0], (-1,0,0)))
	cubelets.append((positionMatrix[0][2][0], (-1,1,0)))
	cubelets.append((positionMatrix[1][0][0], (0,-1,0)))
	cubelets.append((positionMatrix[1][2][0], (0,1,0)))
	cubelets.append((positionMatrix[2][0][0], (1,-1,0)))
	cubelets.append((positionMatrix[2][1][0], (1,0,0)))
	cubelets.append((positionMatrix[2][2][0], (1,1,0)))
	for cubelet in cubelets:
		xPos = cubelet[1][0]
		yPos = cubelet[1][1]
		zPos = cubelet[1][2]
		# The following is the product of the rotation matrix
		#  0 1 0 
		# -1 0 0
		#  0 0 1 
		# and the vector (xPos,yPos,zPos)
		#  PRODUCT == (yPos, -xPos,zPos)
		positionMatrix[(1+yPos)][(1+(-xPos))][zPos] = cubelet[0]



def rotateFrontInverted(positionMatrix):
	cubelets = []

	cubelets.append((positionMatrix[0][0][0], (-1,-1,0)))
	cubelets.append((positionMatrix[0][1][0], (-1,0,0)))
	cubelets.append((positionMatrix[0][2][0], (-1,1,0)))
	cubelets.append((positionMatrix[1][0][0], (0,-1,0)))
	cubelets.append((positionMatrix[1][2][0], (0,1,0)))
	cubelets.append((positionMatrix[2][0][0], (1,-1,0)))
	cubelets.append((positionMatrix[2][1][0], (1,0,0)))
	cubelets.append((positionMatrix[2][2][0], (1,1,0)))
	for cubelet in cubelets:
		xPos = cubelet[1][0]
		yPos = cubelet[1][1]
		zPos = cubelet[1][2]
		# The following is the product of the rotation matrix
		#  0 -1  0 
		#  1  0  0
		#  0  0  1 
		# and the vector (xPos,yPos,zPos)
		positionMatrix[(1+(-yPos))][(1+(xPos))][zPos] = cubelet[0]

def rotateBack(positionMatrix):
	cubelets = []

	cubelets.append((positionMatrix[0][0][2], (-1,-1,2)))
	cubelets.append((positionMatrix[0][1][2], (-1,0,2)))
	cubelets.append((positionMatrix[0][2][2], (-1,1,2)))
	cubelets.append((positionMatrix[1][0][2], (0,-1,2)))
	cubelets.append((positionMatrix[1][2][2], (0,1,2)))
	cubelets.append((positionMatrix[2][0][2], (1,-1,2)))
	cubelets.append((positionMatrix[2][1][2], (1,0,2)))
	cubelets.append((positionMatrix[2][2][2], (1,1,2)))
	for cubelet in cubelets:
		xPos = cubelet[1][0]
		yPos = cubelet[1][1]
		zPos = cubelet[1][2]
		# The following is the product of the rotation matrix
		#  0 1 0 
		# -1 0 0
		#  0 0 1 
		# and the vector (xPos,yPos,zPos)
		positionMatrix[(1+yPos)][(1+(-xPos))][zPos] = cubelet[0]

def rotateBackInverted(positionMatrix):
	cubelets = []

	cubelets.append((positionMatrix[0][0][2], (-1,-1,2)))
	cubelets.append((positionMatrix[0][1][2], (-1,0,2)))
	cubelets.append((positionMatrix[0][2][2], (-1,1,2)))
	cubelets.append((positionMatrix[1][0][2], (0,-1,2)))
	cubelets.append((positionMatrix[1][2][2], (0,1,2)))
	cubelets.append((positionMatrix[2][0][2], (1,-1,2)))
	cubelets.append((positionMatrix[2][1][2], (1,0,2)))
	cubelets.append((positionMatrix[2][2][2], (1,1,2)))
	for cubelet in cubelets:
		xPos = cubelet[1][0]
		yPos = cubelet[1][1]
		zPos = cubelet[1][2]
		# The following is the product of the rotation matrix
		#  0 1 0 
		# -1 0 0
		#  0 0 1 
		# and the vector (xPos,yPos,zPos)
		positionMatrix[(1+(-yPos))][(1+(xPos))][zPos] = cubelet[0]

def rotateRight(positionMatrix):
	cubelets = []

	cubelets.append((positionMatrix[0][2][0], (-1,1,-1)))
	cubelets.append((positionMatrix[0][2][1], (-1,1,0)))
	cubelets.append((positionMatrix[0][2][2], (-1,1,1)))
	cubelets.append((positionMatrix[1][2][0], (0,1,-1)))
	cubelets.append((positionMatrix[1][2][2], (0,1,1)))
	cubelets.append((positionMatrix[2][2][0], (1,1,-1)))
	cubelets.append((positionMatrix[2][2][1], (1,1,0)))
	cubelets.append((positionMatrix[2][2][2], (1,1,1)))
	for cubelet in cubelets:
		xPos = cubelet[1][0]
		yPos = cubelet[1][1]
		zPos = cubelet[1][2]
		# The following is the product of the rotation matrix
		#  0 1 0 
		# -1 0 0
		#  0 0 1 
		# and the vector (xPos,yPos,zPos)
		positionMatrix[(zPos)+1][(yPos) + 1][-xPos+1] = cubelet[0]

def rotateRightInverted(positionMatrix):
	cubelets = []

	cubelets.append((positionMatrix[0][2][0], (-1,1,-1)))
	cubelets.append((positionMatrix[0][2][1], (-1,1,0)))
	cubelets.append((positionMatrix[0][2][2], (-1,1,1)))
	cubelets.append((positionMatrix[1][2][0], (0,1,-1)))
	cubelets.append((positionMatrix[1][2][2], (0,1,1)))
	cubelets.append((positionMatrix[2][2][0], (1,1,-1)))
	cubelets.append((positionMatrix[2][2][1], (1,1,0)))
	cubelets.append((positionMatrix[2][2][2], (1,1,1)))
	for cubelet in cubelets:
		xPos = cubelet[1][0]
		yPos = cubelet[1][1]
		zPos = cubelet[1][2]
		# The following is the product of the rotation matrix
		#  0 1 0 
		# -1 0 0
		#  0 0 1 
		# and the vector (xPos,yPos,zPos)
		positionMatrix[(-zPos)+1][yPos + 1][xPos+1] = cubelet[0]

def rotateLeft(positionMatrix):
	cubelets = []

	cubelets.append((positionMatrix[0][0][0], (-1,-1,-1)))
	cubelets.append((positionMatrix[0][0][1], (-1,-1,0)))
	cubelets.append((positionMatrix[0][0][2], (-1,-1,1)))
	cubelets.append((positionMatrix[1][0][0], (0,-1,-1)))
	cubelets.append((positionMatrix[1][0][2], (0,-1,1)))
	cubelets.append((positionMatrix[2][0][0], (1,-1,-1)))
	cubelets.append((positionMatrix[2][0][1], (1,-1,0)))
	cubelets.append((positionMatrix[2][0][2], (1,-1,1)))
	for cubelet in cubelets:
		xPos = cubelet[1][0]
		yPos = cubelet[1][1]
		zPos = cubelet[1][2]
		# The following is the product of the rotation matrix
		#  0 1 0 
		# -1 0 0
		#  0 0 1 
		# and the vector (xPos,yPos,zPos)
		positionMatrix[(zPos)+1][(yPos) + 1][-xPos+1] = cubelet[0]

def rotateLeftInverted(positionMatrix):
	cubelets = []

	cubelets.append((positionMatrix[0][0][0], (-1,-1,-1)))
	cubelets.append((positionMatrix[0][0][1], (-1,-1,0)))
	cubelets.append((positionMatrix[0][0][2], (-1,-1,1)))
	cubelets.append((positionMatrix[1][0][0], (0,-1,-1)))
	cubelets.append((positionMatrix[1][0][2], (0,-1,1)))
	cubelets.append((positionMatrix[2][0][0], (1,-1,-1)))
	cubelets.append((positionMatrix[2][0][1], (1,-1,0)))
	cubelets.append((positionMatrix[2][0][2], (1,-1,1)))
	for cubelet in cubelets:
		xPos = cubelet[1][0]
		yPos = cubelet[1][1]
		zPos = cubelet[1][2]
		# The following is the product of the rotation matrix
		#  0 1 0 
		# -1 0 0
		#  0 0 1 
		# and the vector (xPos,yPos,zPos)
		positionMatrix[(-zPos)+1][(yPos) + 1][xPos+1] = cubelet[0]

def rotateTop(positionMatrix):
	cubelets = []

	cubelets.append((positionMatrix[0][0][0], (0,-1,-1)))
	cubelets.append((positionMatrix[0][0][1], (0,-1,0)))
	cubelets.append((positionMatrix[0][0][2], (0,-1,1)))
	cubelets.append((positionMatrix[0][1][0], (0,0,-1)))
	cubelets.append((positionMatrix[0][1][2], (0,0,1)))
	cubelets.append((positionMatrix[0][2][0], (0,1,-1)))
	cubelets.append((positionMatrix[0][2][1], (0,1,0)))
	cubelets.append((positionMatrix[0][2][2], (0,1,1)))

	for cubelet in cubelets:
		xPos = cubelet[1][0]
		yPos = cubelet[1][1]
		zPos = cubelet[1][2]
		# The following is the product of the rotation matrix
		#  0 1 0 
		# -1 0 0
		#  0 0 1 
		# and the vector (xPos,yPos,zPos)
		positionMatrix[xPos][(zPos+1)][(-yPos)+1] = cubelet[0]

def rotateTopInverted(positionMatrix):
	cubelets = []

	cubelets.append((positionMatrix[0][0][0], (0,-1,-1)))
	cubelets.append((positionMatrix[0][0][1], (0,-1,0)))
	cubelets.append((positionMatrix[0][0][2], (0,-1,1)))
	cubelets.append((positionMatrix[0][1][0], (0,0,-1)))
	cubelets.append((positionMatrix[0][1][2], (0,0,1)))
	cubelets.append((positionMatrix[0][2][0], (0,1,-1)))
	cubelets.append((positionMatrix[0][2][1], (0,1,0)))
	cubelets.append((positionMatrix[0][2][2], (0,1,1)))

	for cubelet in cubelets:
		xPos = cubelet[1][0]
		yPos = cubelet[1][1]
		zPos = cubelet[1][2]
		# The following is the product of the rotation matrix
		#  0 1 0 
		# -1 0 0
		#  0 0 1 
		# and the vector (xPos,yPos,zPos)
		positionMatrix[xPos][(-zPos+1)][(yPos)+1] = cubelet[0]

def rotateBottom(positionMatrix):
	cubelets = []

	cubelets.append((positionMatrix[2][0][0], (2,-1,-1)))
	cubelets.append((positionMatrix[2][0][1], (2,-1,0)))
	cubelets.append((positionMatrix[2][0][2], (2,-1,1)))
	cubelets.append((positionMatrix[2][1][0], (2,0,-1)))
	cubelets.append((positionMatrix[2][1][2], (2,0,1)))
	cubelets.append((positionMatrix[2][2][0], (2,1,-1)))
	cubelets.append((positionMatrix[2][2][1], (2,1,0)))
	cubelets.append((positionMatrix[2][2][2], (2,1,1)))

	for cubelet in cubelets:
		xPos = cubelet[1][0]
		yPos = cubelet[1][1]
		zPos = cubelet[1][2]
		# The following is the product of the rotation matrix
		#  0 1 0 
		# -1 0 0
		#  0 0 1 
		# and the vector (xPos,yPos,zPos)
		positionMatrix[xPos][(zPos+1)][(-yPos)+1] = cubelet[0]

def rotateBottomInverted(positionMatrix):
	cubelets = []

	cubelets.append((positionMatrix[2][0][0], (2,-1,-1)))
	cubelets.append((positionMatrix[2][0][1], (2,-1,0)))
	cubelets.append((positionMatrix[2][0][2], (2,-1,1)))
	cubelets.append((positionMatrix[2][1][0], (2,0,-1)))
	cubelets.append((positionMatrix[2][1][2], (2,0,1)))
	cubelets.append((positionMatrix[2][2][0], (2,1,-1)))
	cubelets.append((positionMatrix[2][2][1], (2,1,0)))
	cubelets.append((positionMatrix[2][2][2], (2,1,1)))

	for cubelet in cubelets:
		xPos = cubelet[1][0]
		yPos = cubelet[1][1]
		zPos = cubelet[1][2]
		# The following is the product of the rotation matrix
		#  0 1 0 
		# -1 0 0
		#  0 0 1 
		# and the vector (xPos,yPos,zPos)
		positionMatrix[xPos][(-zPos+1)][(yPos)+1] = cubelet[0]




