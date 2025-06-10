"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.



Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
"""
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Create a mapping from original nodes to their copies
        mapp = {}
        cur = head
        while cur:
            mapp[cur] = Node(cur.val)
            cur = cur.next

        # Step 2: Assign next and random pointers for the copied nodes
        cur = head
        while cur:
            if cur.next:
                mapp[cur].next = mapp[cur.next]
            if cur.random:
                mapp[cur].random = mapp[cur.random]
            cur = cur.next

        return mapp[head]


# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Set next pointers
node1.next = node2
node2.next = node3
node3.next = node4

# Set random pointers
node1.random = node3  # node1's random points to node3
node2.random = node1  # node2's random points to node1
node3.random = node4  # node3's random points to node4
node4.random = node2  # node4's random points to node2

# Create a copy of the list
copied_head = Solution().copyRandomList(node1)


# Print the list to verify
def print_list(head: Node):
    current = head
    while current:
        random_val = current.random.val if current.random else None
        print(
            f"Node value: {current.val}, Next value: {current.next.val if current.next else None}, Random value: {random_val}")
        current = current.next


# Print the original and copied list to verify
print("Original list:")
print_list(node1)
print("\nCopied list:")
print_list(copied_head)

