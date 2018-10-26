'''
Created on 18 Sep 2018

@author: Aaron
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def findPaths(start, end, path):
    path = path + [start.key]
    if (start.left == None and start.right == None):
        return []
    if start.key == end.key:
        return [path]
    paths = []
    if (start.left != None and start.right!= None):
        newpaths1 = findPaths(start.left, end, path)
        newpaths2 = findPaths(start.right, end, path)
        for y in newpaths1:
            paths = paths + [y]
        for y in newpaths2:
            paths = paths + [y]
    if (start.left == None and start.right!= None):
        newpaths = findPaths(start.right, end, path)
        for y in newpaths:
            paths = paths + [y]
    if (start.left != None and start.right == None):
        newpaths = findPaths(start.left, end, path)
        for y in newpaths:
            paths = paths + [y]       
    
    return paths

def findLCA(nodes, n1, n2):
    shortestPath = 0
    ancestors = []
    nodes.remove(n1)
    nodes.remove(n2)
    for x in nodes:
        tempPath = []
        paths1 = findPaths(x, n1, tempPath)
        short1 = []
        for y in paths1:
            if (len(short1) == 0 or len(y) < len(short1)):
                short1 = y
        paths2 = findPaths(x, n2, tempPath)
        short2 = []
        for y in paths2:
            if (len(short2) == 0 or len(y) < len(short2)):
                short2 = y        
        runningLen = len(short1) + len(short2)
        if ((shortestPath >= runningLen or shortestPath == 0)and (len(short1) != 0 and (len(short2) != 0))):
            shortestPath = runningLen
            ancestors.append(short1[0])   