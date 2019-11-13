"""
Math 590
Project 3
Fall 2019

Partner 1:
Partner 2:
Date:
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage
"""
def detectArbitrage(currencies, tol=1e-15):
    ##### Your implementation goes here. #####
    currencies.adjList[0].dist = 0;
    for i in range(len(currencies.adjList)-1):
        for u in currencies.adjList:
            for neighbor in u.neigh:
                if neighbor.dist > u.dist + \
                    currencies.adjMat[u.rank][neighbor.rank] + tol:
                        neighbor.dist = u.dist + \
                            currencies.adjMat[u.rank][neighbor.rank]
                        neighbor.prev = u
    correct_dist = [v.dist for v in currencies.adjList]
    for u in currencies.adjList:
        for neighbor in u.neigh:
            if neighbor.dist > u.dist + \
                currencies.adjMat[u.rank][neighbor.rank] + tol:
                    neighbor.dist = u.dist + \
                        currencies.adjMat[u.rank][neighbor.rank]
                    neighbor.prev = u
    new_dist = [v.dist for v in currencies.adjList]

    neg_cycle = []
    for i in range(len(correct_dist)):
        if correct_dist[i] - new_dist[i] > tol:
            current_vertex = currencies.adjList[i]
            while not current_vertex.rank in neg_cycle:
                neg_cycle.append(current_vertex.rank)
                current_vertex = current_vertex.prev
            for j in range(len(neg_cycle)):
                if neg_cycle[j] == current_vertex.rank:
                    neg_cycle = neg_cycle[j:]
                    neg_cycle.append(current_vertex.rank)
                    return neg_cycle[::-1]
    return neg_cycle
    ##### Your implementation goes here. #####

################################################################################

"""
rates2mat
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
