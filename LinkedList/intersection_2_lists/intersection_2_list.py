from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))
from utils.models import Node

class Solution:
    """ 
        Problem statement: 
        Assuming no cycle in linked list 1 and 2, find the intersection in linked list 1 and 2. If there isn't, 
    
    """
    def getIntersectionNode(self, A, B):
        """
        @param A : head node of linked list 1
        @param B : head node of linked list 2
        @return: the intersection node in the linked list
        """
        self.hashSet = {}
        # traverse linked list 1
        current = A
        while not current:
            if not id(current) in hashSet:
                self.hashSet[id(current)] = 1
            else: 
                return current
        # traverse linked list 2
        current = B
        while not current:
            if not id(current) in hashSet:
                self.hashSet[id(current)] = 1
            else :
                return current
        # no intersection
        return None
        

        