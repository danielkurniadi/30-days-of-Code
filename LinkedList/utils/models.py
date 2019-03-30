from .helpers import LinkedListHelper

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList(LinkedListHelper):
    def __init__(self, head=None):
        self.head = head
