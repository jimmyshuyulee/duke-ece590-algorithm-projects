"""
Math 590
Project 3
Fall 2019

Partner 1: Shu Yu Lee
Partner 2: Fang Feng
Date: 11/15/2019
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
output a single list of vertex ranks corresponding to the negative cost cycle

INPUTS
currencies: a 2D list of the adjacency matrix representing the -log() value
of currency exchange rates
tol: the tolerance value for errors coming form decimal representation of
float numbers

OUTPUTS:
neg_cycle: a list representing the negative cost cycle in currencies
"""
def detectArbitrage(currencies, tol=1e-15):
    ##### Your implementation goes here. #####

    # Abstract the distance update portion of the code into a function,
    # since it will be used in the normal shortest path finding iterations
    # and the additional round to look for negative cost cycle
    def updateDist():
        for u in currencies.adjList:
            for neighbor in u.neigh:
                if neighbor.dist > u.dist + \
                    currencies.adjMat[u.rank][neighbor.rank] + tol:
                        neighbor.dist = u.dist + \
                            currencies.adjMat[u.rank][neighbor.rank]
                        neighbor.prev = u

    currencies.adjList[0].dist = 0;
    for i in range(len(currencies.adjList)-1):
        updateDist()
    # Distnce of every nodes after V-1 iterations
    correct_dist = [v.dist for v in currencies.adjList]
    updateDist()
    # Distnce of every nodes after V iterations
    new_dist = [v.dist for v in currencies.adjList]

    neg_cycle = []
    for i in range(len(correct_dist)):
        # look for the vertex which has its distance changes in the
        # additional iteration
        if correct_dist[i] - new_dist[i] > tol:
            current_vertex = currencies.adjList[i]
            # Traverse back to find the cycle
            while not current_vertex.rank in neg_cycle:
                neg_cycle.append(current_vertex.rank)
                current_vertex = current_vertex.prev
            # since our starting vertex may not be in the cycle, look for
            # the start of the cycle and cut off additional edges
            for j in range(len(neg_cycle)):
                if neg_cycle[j] == current_vertex.rank:
                    neg_cycle = neg_cycle[j:]
                    neg_cycle.append(current_vertex.rank)
                    # Make sure is in the correct order
                    return neg_cycle[::-1] 
    return neg_cycle
    ##### Your implementation goes here. #####

################################################################################

"""
rates2mat
return the adjacency matrix with the correctly weighted edges

INPUTS
rates: a 2D list of currency exchage rates

OUTPUTS
a 2D list of the correct adjacency matrix.
"""
def rates2mat(rates):
    ##### Your implementation goes here. #####
    # Currently this only returns a copy of the rates matrix.
    return [[-math.log(R) for R in row] for row in rates]
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
