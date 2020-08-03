# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util, searchUtil

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # keep track of visited states
    closed = []
    # visit start state and push to stack
    fringe = util.Stack()
    node = searchUtil.SearchNode(problem.getStartState(), None, None)
    fringe.push(node)
    # depth-first search algorithm
    while (not fringe.isEmpty()):
        node = fringe.pop()
        if problem.isGoalState(node.getState()):
            break
        if node.getState() not in closed:
            closed.append(node.getState())
            for successor in problem.getSuccessors(node.getState()):
                fringe.push(searchUtil.SearchNode(successor[0], node, successor[1]))
    # retrace path
    moves = []
    while (node.getMove() is not None):
        moves.append(node.getMove())
        node = node.getPrevious()
    # reverse path
    moves.reverse()
    return moves

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # keep track of visited states
    closed = []
    # visit start state and push to stack
    fringe = util.Queue()
    node = searchUtil.SearchNode(problem.getStartState(), None, None)
    fringe.push(node)
    # depth-first search algorithm
    while (not fringe.isEmpty()):
        node = fringe.pop()
        if problem.isGoalState(node.getState()):
            break
        if node.getState() not in closed:
            closed.append(node.getState())
            for successor in problem.getSuccessors(node.getState()):
                fringe.push(searchUtil.SearchNode(successor[0], node, successor[1]))
    # retrace path
    moves = []
    while (node.getMove() is not None):
        moves.append(node.getMove())
        node = node.getPrevious()
    # reverse path
    moves.reverse()
    return moves

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # keep track of visited states
    closed = []
    # visit start state and push to stack
    fringe = util.PriorityQueue()
    node = searchUtil.SearchNode(problem.getStartState(), None, None)
    fringe.push(node, 1)
    # uniform cost algorithm
    while (not fringe.isEmpty()):
        node = fringe.pop()
        if problem.isGoalState(node.getState()):
            break
        if node.getState() not in closed:
            closed.append(node.getState())
            for successor in problem.getSuccessors(node.getState()):
                fringe.push(searchUtil.SearchNode(successor[0], node, successor[1]), successor[2])
    # retrace path
    moves = []
    while (node.getMove() is not None):
        moves.append(node.getMove())
        node = node.getPrevious()
    # reverse path
    moves.reverse()
    return moves

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
