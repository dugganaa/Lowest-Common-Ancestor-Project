'''
Created on 18 Sep 2018

@author: Aaron
'''
from pip.__main__ import path
from pathlib import Path

'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''

<<<<<<< HEAD


<<<<<<< HEAD

=======
>>>>>>> parent of adc648a... Recommitting to dag
=======
'''
>>>>>>> f5ce7abb5d6bba6a7ef9c0ff3f3c8ecddfe2b0c3
class Node:
    def __init__(self, name, colour, count, parents, children):
        self.name = name
        self.colur = colour
        self.count = count
        self.parents = parents
        self.children = children 
'''
def findPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = findPath(graph, node, end, path)
            if newpath: return newpath
    return None
    
def findLCA(root, n1, n2):
    path1 = []
    path2 = []
    
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2 )):
        return -1
    
    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]
