from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))

from utils.models import (Node, LinkedList)
from utils.helpers import LinkedListHelper

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        if not A:
            return 0
        if not A.next:
            return 1
        self.result = False
        self.lPalinRecursive(A, A)
        return self.result
    
    def lPalinRecursive(self, left, right):
        if not right:
            return left
        # we are in the middle and have successfully verified all strings
        left = self.lPalinRecursive(left, right.next)
        if not left:
            return None
        if (left is right) or (right.next is left):
            self.result = True
        if left.val != right.val:
            return None
        return left.next

if __name__ == '__main__':
    arr1 = [1, 2, 1]
    arr2 = [1, 2, 3]
    arr3 = [6, 3, 7, 3, 6]
    arr4 = [7, 8, 9, 9, 9, 8]
    arr5 = [1, 2, 3, 4, 3, 2, 1]
    arr6 = [1, 2, 2, 1]

    head1 = LinkedListHelper.weave(arr1)
    head2 = LinkedListHelper.weave(arr2)
    head3 = LinkedListHelper.weave(arr3)
    head4 = LinkedListHelper.weave(arr4)
    head5 = LinkedListHelper.weave(arr5)
    head6 = LinkedListHelper.weave(arr6)

    solver = Solution()
    for idx, input in enumerate([head1, head2, head3, head4, head5, head6]):
        print("Is Linked List {} Palindromic?: ".format(idx), solver.lPalin(input))