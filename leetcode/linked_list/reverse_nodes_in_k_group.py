"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000


Follow-up: Can you solve the problem in O(1) extra memory space?
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
a1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k) -> Optional[ListNode]:

        current = head
        for _ in range(k):
            if not current:
                return head
            current = current.next

        current = head
        prev = None
        for _ in range(k):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        head.next = self.reverseKGroup(current, k)
        return prev


a = (Solution().reverseKGroup(a, 2))
a1 = (Solution().reverseKGroup(a1, 3))


def print_list(head):
    current = head
    while current:
        print(
            f"Node value: {current.val}")
        current = current.next

print(print_list(a))
# print(print_list(a1))
