import hashlib
import math
import os
import time 
import datetime
import uuid
import random
from node import node
class tree():
    def __init__(self):
        self.root = None

    def build_tree(self, leaves):
        blank_node = node(None, None, "\0")
        while pow(2,math.ceil(math.log2(len(leaves)))) != len(leaves):
            leaves.append(blank_node)
        parents = self.make_parent(leaves)
        
        if len(parents) != 1:
            self.build_tree(parents)
        else :
           self.root = parents[0].hash
            #set the root
            
        
    def make_parent(self, leaves):
        parents = []
        i = 0
        while i < len(leaves):
            parent_node = node( None, None, hash_line(leaves[i], leaves[i+1]))
            parent_node.left = leaves[i]
            parent_node.right = leaves[i+1]
            i += 2
            parents.append(parent_node)
        return parents

def hash_line(hash_val1, hash_val2):
        val1 = hash_val1.hash 
        val2 = hash_val2.hash 
        cat_hash = val1 + val2
        hashF = hashlib.sha256(cat_hash.encode('utf-8')).hexdigest()
        return hashF

