from .models import Node

class LinkedListHelper:
    """Linked List Helper methods are here! All are static methods so they are ready to use"""

    @staticmethod
    def weave(arr):
        if not arr:
            return

        head, temp = None, None
        for a in arr:
            if not temp:
                head = Node(a)
                temp = head
            else:
                temp.next = Node(a)
                temp = temp.next
        return head
    
    @staticmethod
    def reverse(head):
        if (not head) or (not head.next):
            return head
        nexx, current, prev = head.next, head, None
        while current:
            current.next = prev
            current, prev = nexx, current
            if nexx:
                nexx = nexx.next
        return prev

    @staticmethod
    def traverse(head):
        print("traverse linkedlist: ", end=' ')
        if not head:
            return None

        temp = head
        while temp.next:
            print(temp.val, end=' ')
            temp = temp.next
        print(temp.val) #last node

        return temp #return last node