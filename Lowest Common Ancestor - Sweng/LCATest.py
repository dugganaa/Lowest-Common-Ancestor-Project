'''
Created on 28 Sep 2018

@author: Aaron
'''
import unittest
import LCA


class LCATest(unittest.TestCase):
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
        self.assertEqual(LCA.findLCA(root, 3, 4), 1)
        self.assertEqual(LCA.findLCA(root, 2, 4), 2)