from typing import Optional

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class ListNode:
    def __init__(self):
        self.head = None

    def add_value(self, value):
        temp = self.head
        node = Node(value)
        self.head = node
        self.head.next = temp


class Solution:

    def print_ll(self, merged_head):
        # Print the merged list
        current = merged_head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def mergeTwoLists(self, list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
        dummy = Node(0)
        cur = dummy
        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        return dummy.next


# Example usage:
# Create two sorted linked lists
ll = ListNode()
ll.add_value(5)
ll.add_value(3)
ll.add_value(10)
ll.add_value(6)

ll1 = ListNode()
ll1.add_value(2)
ll1.add_value(4)

# Merge the two lists
merged_head = Solution().mergeTwoLists(ll.head, ll1.head)

# Print the merged list
current = merged_head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
