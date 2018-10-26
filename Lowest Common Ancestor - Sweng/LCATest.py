'''
Created on 28 Sep 2018

@author: Aaron
'''
import unittest
import LCA
from _overlapped import NULL

class LCATest(unittest.TestCase):
    '''
    def test_findlca(self):
        root = LCA.Node(1) 
        root.left = LCA.Node(2) 
        root.right = LCA.Node(3) 
        root.left.left = LCA.Node(4) 
        root.left.right = LCA.Node(5) 
        root.right.left = LCA.Node(6) 
        root.right.right = LCA.Node(7) 
        
        self.assertEqual(LCA.findLCA(root, 4, 5), 2)
        print("Should receive findLCA(root, 4, 5) 2. Answer received: " + str(LCA.findLCA(root, 4, 5)))
        
        self.assertEqual(LCA.findLCA(root, 4, 6), 1)
        print("Should receive findLCA(root, 4, 6) 1. Answer received: " + str(LCA.findLCA(root, 4, 6)))
        
        self.assertEqual(LCA.findLCA(root, 3, 4), 1)
        print("Should receive findLCA(root, 3, 4) 1. Answer received: " + str(LCA.findLCA(root, 3, 4)))
        
        self.assertEqual(LCA.findLCA(root, 2, 4), 2)
        print("Should receive findLCA(root, 2, 4) 2. Answer received: " + str(LCA.findLCA(root, 2, 4)))
    '''
    def test_findlca(self):
        nodeA = LCA.Node('A')
        nodeB = LCA.Node('B')
        nodeC = LCA.Node('C')
        nodeD = LCA.Node('D')
        nodeE = LCA.Node('E')
        nodeF = LCA.Node('F')
        nodeA.left = nodeB
        nodeA.right = nodeC
        nodeB.left = nodeD
        nodeB.right = nodeC
        nodeC.left = nodeD
        nodeC.right = nodeE
        nodeE.left = nodeF
        nodes = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF]
        
        
        self.assertEqual(LCA.findLCA(nodes, nodeD, nodeC), nodeB.key)
        print("Should receive findLCA(nodes, nodeD, nodeC), B. Answer received: " + str(LCA.findLCA(nodes, nodeD, nodeC)))
        
        self.assertEqual(LCA.findLCA(nodes, nodeD, nodeF), nodeC.key)
        print("Should receive findLCA(nodes, nodeD, nodeF), C. Answer received: " + str(LCA.findLCA(nodes, nodeD, nodeF)))
        
        self.assertEqual(LCA.findLCA(nodes, nodeB, nodeF), nodeA.key)
        print("Should receive findLCA(nodes, nodeB, nodeF), A. Answer received: " + str(LCA.findLCA(nodes, nodeB, nodeF)))
        
        self.assertEqual(LCA.findLCA(nodes, nodeA, nodeE), None)
        print("Should receive findLCA(nodes, nodeA, nodeE), None. Answer received: " + str(LCA.findLCA(nodes, nodeA, nodeE)))
        
    
            
            
        
