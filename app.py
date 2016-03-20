# Author: Julian Bracero
# This is a python flask REST service that takes Rubik's cube initial state
#  and goal state and performs an iterative deepenig Astar search to find the 
# optimal solution
from datetime import timedelta
from functools import update_wrapper
from flask import Flask, jsonify, make_response, request, current_app
from rubixCube import RubixCube
from heapq import heappush, heappop
import ast
from node import Node
from rotator import *
import sys
import time

app = Flask(__name__)

solution = ""

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route('/solve/<init_config>/<goal_state>', methods=['GET'])
@crossdomain(origin="*")
def getSolution(init_config,goal_state):
	global solution
	solution = ""
	# computeSolution(init_config,goal_state)
	Idfs(init_config, goal_state)
	# startProblem = RubixCube( prepareArrayForProblem(init_config, False, []) )
	# solution = startProblem.state
	return jsonify({'initial_state': init_config,'goal_state': goal_state, 'solution': solution})

def Idfs(initial_state, goal_state):
	start_time = time.clock()
	print "Idfs is executing at time" , time.clock(), "sec(s)"
	startProblem = RubixCube( prepareArrayForProblem(initial_state, False, []) )
	hueristicHelper = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	goalProblem = RubixCube( prepareArrayForProblem(goal_state, True, hueristicHelper) )
	bound = 1
	node = Node(startProblem, 0)
	while True:
		solution = search(node, 0, goalProblem, bound,hueristicHelper)
		if solution < 0:
			end_time = time.clock()
			print "IDFS completed at time" ,  end_time, "sec(s)", "\nTime difference of", end_time - start_time
			return solution
		if solution == sys.maxint:
			return []
		bound = solution

def search(node, cost, goalProblem, bound,hueristicHelper):
	total_cost = cost + node.state.computeHueristic(hueristicHelper)
	if total_cost > bound:
		return total_cost
	if node.state == goalProblem:
		buildSolution(node)
		return -1
	min = sys.maxint
	successors = node.state.getNextStates()
	for child in successors:
		t = search(Node(child, node.pathCost,node),cost + child.computeHueristic(hueristicHelper) ,goalProblem,bound,hueristicHelper)
		if t < 0:
			return t 
		if t < min:
			min = t 
	return min


#This is the Kosher A* implementation, it is unused for now since IDFS outclasses A* in general
def computeSolution(initial_state, goal_state):
	start_time = time.clock()
	print "Astar is executing at time" , time.clock(), "sec(s)"
	startProblem = RubixCube( prepareArrayForProblem(initial_state, False, []) )
	hueristicHelper = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	goalProblem = RubixCube( prepareArrayForProblem(goal_state, True, hueristicHelper) )
	#This heap will serve a a priority queue for our search algorithm
	heap = [] 
	initialHueristic = startProblem.computeHueristic(hueristicHelper)
	heappush( heap, (0 + initialHueristic, Node(startProblem, -1) ))
	counter = 0
	while len( heap ) != 0 : 
		currentCube = heappop(heap)[1]
		if currentCube.state == goalProblem:
			end_time = time.clock()
			print "Astar completed at time" ,  end_time, "sec(s)", "\nTime difference of", end_time - start_time
			return buildSolution(currentCube)
		else:
			# print "we have checked" ,counter , "nodes"
			successors = currentCube.state.getNextStates()
			for nextState in successors:
				if notYetExplored(nextState, currentCube):
					hueristicValue = nextState.computeHueristic(hueristicHelper)
					heappush(heap, (currentCube.pathCost + hueristicValue, Node(nextState, currentCube.pathCost, currentCube) ))
					counter = counter + 1
	return []

# This method preps the hueristicHelper, hueristicHelper is a hash array that stores a
# cublets correct position in the array, so that the manhattan distance can quickly look 
# up where a cubelet should be
def prepareArrayForProblem(array, isGoal, hueristicHelper):
	arr = ast.literal_eval(array)
	list = [[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]];
	row = 0
	col = 0
	depth = 0
	index = 0
	for element in arr:
		if isGoal:
			hueristicHelper[index] = [row,col,depth]
		list[row][col][depth] = element
		col = col + 1
		if col > 2:
			row = row + 1
			col = 0
			if row > 2:
				depth = depth + 1
				row = 0
		index = index +1
	return list

def notYetExplored(state, node):# This function will traverse the path to the root to prevent cycles
	while node is not None:
		if state == node.state:
			return False
		node = node.parent
	return True

def buildSolution(node):
	pathToSolution = []
	pathCost = node.pathCost
	pathToSolution.append(node.state)
	node = node.parent
	while node is not None:
		pathToSolution.append(node.state)
		node = node.parent
	pathToSolution.reverse()
	global solution
	for i in pathToSolution:
		if len(solution) > 0:
			solution = solution + ", " +i.toString()
		else:
			solution = " "
		print i.toString()

if __name__ == '__main__':
	app.run(debug=True)