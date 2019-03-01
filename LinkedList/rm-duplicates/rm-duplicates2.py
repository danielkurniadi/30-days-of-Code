from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))

from utils.models import (Node, LinkedList)
from utils.helpers import LinkedListHelper

# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    """ Given a sorted linked list, delete all duplicate numbers, leaving only distinct numbers from the original list
    """
    # @param A : head node of linked list
    # @return an integer
    def deleteDuplicates(self, A):
        dups = set()
        uniques = set()
        head = A
        while head:
            a = head.val
            if a in uniques:
                uniques.remove(a)
                dups.add(a)
            if a not in dups:
                uniques.add(a)
            head = head.next
        print("uniques", uniques)
        head, current = None, None
        for b in sorted(list(uniques)):
            if not head:
                head = ListNode(b)
                current = head
                continue
            current.next = ListNode(b)
            current = current.next
        return head

if __name__ == '__main__':
    arr1 = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3]
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
    for i, input in enumerate([head1, head2, head3, head4, head5, head6]):
        x = solver.deleteDuplicates(input)
        LinkedListHelper.traverse(x)