'''
Created on 18 Sep 2018

@author: Aaron
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
<<<<<<< HEAD
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
=======

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
>>>>>>> eef10420e28eb84ac0102052f38cbf32ac563367
    
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