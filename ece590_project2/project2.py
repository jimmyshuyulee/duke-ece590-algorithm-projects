"""
Math 590
Project 2
Fall 2019

project2.py

Partner 1: Fang Feng
Partner 2: Shu Yu Lee
Date: 11/04/2019
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
Path finding function
A function which allows us to use different data structure to implement 
a path searching algorithm. If we use a stack, it gives a DFS algorithm, 
and using queue gives a BFS algorithm,

INPUTS
maze: A Maze object representing the maze.
dataStructure: The data structure used to store the vertices in
               this path finding algorithm

OUTPUTS
path: The path from maze.start to maze.exit obtained by DFS.
"""
def pathFinding(maze, dataStructure):
    for vertex in maze.adjList:
        vertex.visited = False
    maze.start.visited = True
    dataStructure.push(maze.start)
    while not dataStructure.isEmpty():
        current = dataStructure.pop()
        for neighbor in current.neigh:
            if not neighbor.visited:
                # We mark the vertex as visited before putting it into the DS
                neighbor.visited = True
                neighbor.prev = current
                dataStructure.push(neighbor)
    current = maze.exit
    path = [maze.exit.rank]
    # A path cannot start from a unreachable path, so if current.prev is None,
    # current must be exit and this exit is not reachable form start
    while current != maze.start or current.prev is not None:
        current = current.prev
        path.append(current.rank)
    return path[::-1]  #reverse the path so it is from start to exit

"""
DFS function
Use a stack to store the vertices

INPUTS
maze: A Maze object representing the maze.

OUTPUTS
path: The path from maze.start to maze.exit obtained by DFS.
"""
def dfs(maze):
    return pathFinding(maze, Stack())

"""
BFS function
Use a queue to store the vertices

INPUTS
maze: A Maze object representing the maze.

OUTPUTS
path: The path from maze.start to maze.exit obtained by BFS.
"""
def bfs(maze):
    return pathFinding(maze, Queue())

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The shortest path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    if alg == 'BFS':
        return bfs(maze)
    return dfs(maze)

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
