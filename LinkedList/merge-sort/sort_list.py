from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))

from utils.models import (Node, LinkedList)
from utils.helpers import LinkedListHelper as llh

class Solution:
    # @param A: unsorted LinkedList
    # @return : sorted LinkedList
    def sortList(self, A):
        if not A.next:
            # print(A.val)
            return A
        left, right = self.cut_middle(A)
        left, right = self.sortList(left), self.sortList(right)
        return self.mergeTwoLists(left, right)

    def cut_middle(self, A):
        if not A:
            return None

        slow_pt, fast_pt, prev = A, A, None
        while (fast_pt) and (fast_pt.next):
            fast_pt = fast_pt.next.next
            prev, slow_pt = slow_pt, slow_pt.next
        prev.next = None
        return A, slow_pt

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
    A = llh.weave([-16, 91, 10, -17, 18, 63, 133, 9, 103, -88, -29, -11, 14, -88, 87, 179])
    A_sorted = solver.sortList(A)
    llh.traverse(A_sorted)