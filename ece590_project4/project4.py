"""
Math 590
Project 4
Fall 2019

Partner 1: Shu Yu Lee
Partner 2: Fang Feng
Date: 12/04/2019
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p4priorityQueue import *

################################################################################

"""
Prim's Algorithm

INPUTS
adjList: adjacency list storing every vertices of the graph
adjMat: adjacency matrix storing the weight of each edges
"""
def prim(adjList, adjMat):
    ##### Your implementation goes here. #####
    adjList[0].cost = 0
    Q = PriorityQueue(adjList)
    while not Q.isEmpty():
        v = Q.deleteMin()
        v.visited = True;
        for neighbor in v.neigh:
            if not neighbor.visited:
                # Update the cost for neighbors
                if neighbor.cost > adjMat[v.rank][neighbor.rank]:
                    neighbor.cost = adjMat[v.rank][neighbor.rank]
                    neighbor.prev = v
    return

################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.

INPUTS
adjList: adjacency list storing every vertices of the graph
edgeList: a sorted list of all the edges in the graph

OUTPUTS
X: a list of edges included in the MST
"""
def kruskal(adjList, edgeList):
    ##### Your implementation goes here. #####
    for v in adjList:
        makeset(v)
    X = []

    for e in edgeList:
        u, v = e.vertices
        if not find(u).isEqual(find(v)):
            X.append(e)
            union(u, v)
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.

INPUTS
v: a Vertex object
"""
def makeset(v):
    ##### Your implementation goes here. #####
    v.pi = v
    v.height = 0
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

INPUTS
v: a Vertex object

OUTPUTS:
the root of the set which v belongs to
"""
def find(v):
    ##### Your implementation goes here. #####
    while not v.isEqual(v.pi):
        v = v.pi
    return v.pi

"""
union: this function will union the sets of vertices v and u.

INPUTS
u: a Vertex object to be unioned
v: a Vertex object to be unioned
"""
def union(u,v):
    ##### Your implementation goes here. #####
    ru = find(u)
    rv = find(v)

    if ru == rv:
        return

    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height:
        ru.pi = rv
    else:
        ru.pi = rv
        rv.height += 1
    return

################################################################################

"""
TSP

INPUTS
adjList: adjacency list storing every vertices of the graph
start: the Vertex object of the starting point

OUTPUTS
tour: a list of vertex ranks storing in the order of tour visit
"""
def tsp(adjList, start):
    ##### Your implementation goes here. #####
    tour = []
    for v in adjList:
        v.visited = False
    stack =[]
    start.visited = True
    stack.append(start)
    while len(stack) > 0:
        # the top of the stack is the last element
        v = stack[len(stack) -1]
        stack.pop()
        tour.append(v.rank)
        for neighbor in v.mstN:
            if not neighbor.visited:
                neighbor.visited = True
                stack.append(neighbor)
    tour.append(start.rank)
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p4tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
