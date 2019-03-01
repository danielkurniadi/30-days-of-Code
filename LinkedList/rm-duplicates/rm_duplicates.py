from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))

from utils.models import (Node, LinkedList)
from utils.helpers import LinkedListHelper

class Solution:
    """ Given a sorted linked list, delete all duplicate numbers, leaving only distinct numbers from the original list
    """
    # @param A : head node of linked list
    # @return an integer
    def deleteDuplicates(self, A):
        if (not A) or (not A.next):
            return A
        current, prev = A.next, A
        while current.next:
            # if duplicate found
            if current.val == current.next.val:
                # remove it by skip it
                prev.next = current.next
                current, prev = current.next, prev
                continue
            current, prev = current.next, current
        if A.next.val == A.val:
            A = A.next
        return A


if __name__ == '__main__':
    arr1 = [1, 1, 1, 1, 1, 1,  2, 2, 2, 3]
    arr2 = [1, 2, 3, 3, 3, 3, 3]
    arr3 = [-6, 3, 7, 9, 9, 10, 10]
    arr4 = [7, 8, 9, 9, 9]
    arr5 = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4]
    arr6 = [1, 2, 2, 5, 5, 6, 6, 6, 6, 6]

    head1 = LinkedListHelper.weave(arr1)
    head2 = LinkedListHelper.weave(arr2)
    head3 = LinkedListHelper.weave(arr3)
    head4 = LinkedListHelper.weave(arr4)
    head5 = LinkedListHelper.weave(arr5)
    head6 = LinkedListHelper.weave(arr6)

    solver = Solution()
    for idx, input in enumerate([head1, head2, head3, head4, head5, head6]):
        A = solver.deleteDuplicates(input)
        print("Result {}: ".format(idx), LinkedListHelper.traverse(A))