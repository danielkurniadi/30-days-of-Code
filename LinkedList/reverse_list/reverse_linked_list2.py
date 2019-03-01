from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))

from utils.models import (Node, LinkedList)
from utils.helpers import LinkedListHelper as llh

class Solution:
    def reverseBetween(self, A, n, m):
        if n > m:
            n, m = m, n
        if not A:
            return None
        left, start, end, right = self.cut(A, n, m)
        reverse_start = self.reverse(start)
        if left:
            left.next, start.next = reverse_start, right
        else:
            A, start.next = reverse_start, right
        return A
    
    def reverse(self, head):
        if (not head) or (not head.next):
            return head
        nexx, current, prev = head.next, head, None
        while current:
            current.next = prev
            current, prev = nexx, current
            if nexx:
                nexx = nexx.next
        return prev
    
    def cut(self, A, n, m):
        #find start
        if n==1:
            left, start = None, A
        else:
            left, start, i = A, A.next, 1
            while(i<n-1):
                start = start.next
                left = left.next
                i+=1
        #find end
        right, end, j = A.next, A, 0
        while(j<m-1):
            end = end.next
            right = right.next
            j += 1
        if left:
            left.next = None
        end.next = None
        return left, start, end, right
    
if __name__ == '__main__':
    solver = Solution()
    A = llh.weave([1, 2, 3])
    # left, start, end, right = solver.cut(A, 1, 5)
    # llh.traverse(start)
    # reverse = solver.reverse(start)
    # llh.traverse(reverse)
    B = solver.reverseBetween(A, 1, 2)
    llh.traverse(B)


