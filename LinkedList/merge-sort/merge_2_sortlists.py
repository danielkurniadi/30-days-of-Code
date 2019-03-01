from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))

from utils.models import (Node, LinkedList)
from utils.helpers import LinkedListHelper as llh

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if not A:
            return B
        if not B:
            return A
        C, current_c = None, None
        current_a, current_b = A, B
        while(current_a and current_b):
            # find which to merge
            if current_a.val <= current_b.val:
                c = current_a.val
                current_a = current_a.next
            else:
                c = current_b.val
                current_b = current_b.next
            if not C: #init C here
                C = Node(c)
                current_c = C
                continue
             #if already init C
            current_c.next = Node(c)
            current_c = current_c.next
        if(current_a):
            current_c.next = current_a
        if current_b:
            current_c.next = current_b
        return C

if __name__ == '__main__':
    solver = Solution()
    A = llh.weave([5, 8, 20])
    B = llh.weave([4, 11, 15])
    C = solver.mergeTwoLists(A, B)
    llh.traverse(C)