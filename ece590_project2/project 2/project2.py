"""
Math 590
Project 2
Fall 2019

project2.py

Partner 1:Fang Feng
Partner 2:
Date:
"""

# Import math and other p2 files.
import math
from p2tests import *


def dfs(maze):
    for vertex in maze.adjList:
        vertex.visited = False
    stack = Stack()
    maze.start.visited = True
    stack.push(maze.start)
    while not stack.isEmpty():
        current = stack.pop()
        for neighbor in current.neigh:
            if not neighbor.visited:
                neighbor.visited = True
                neighbor.prev = current
                stack.push(neighbor)
    current = maze.exit
    path = [maze.exit.rank]
    while current != maze.start or current.prev is not None:
        current = current.prev
        path.append(current.rank)
    return path[::-1]


def bfs(maze):
    for vertex in maze.adjList:
        vertex.visited = False
    queue = Queue()
    maze.start.visited = True
    queue.push(maze.start)
    while not queue.isEmpty():
        current = queue.pop()
        for neighbor in current.neigh:
            if not neighbor.visited:
                neighbor.visited = True
                neighbor.prev = current
                queue.push(neighbor)
    current = maze.exit
    path = [maze.exit.rank]
    while current != maze.start or current.prev is not None:
        current = current.prev
        path.append(current.rank)
    return path[::-1]


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
    testMazes(True)
