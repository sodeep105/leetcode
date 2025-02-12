from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        copy = {}
        node = head
        
        # First pass: Copy all nodes
        while node:
            copy[node] = Node(node.val)
            node = node.next
           
        # Second pass: Assign next and random pointers
        node = head
        while node:
            copy[node].next = copy.get(node.next)
            copy[node].random = copy.get(node.random)
            node = node.next

        return copy[head]  # Return the copied head
