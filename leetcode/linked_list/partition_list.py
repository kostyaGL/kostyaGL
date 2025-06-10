"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.



Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]


Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))


def print_list(head):
    current = head
    while current:
        print(
            f"Node value: {current.val}")
        current = current.next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        s = ListNode(0)
        b = ListNode(0)
        small_lst = s
        big_lst = b

        while head is not None:
            if head.val < x:
                small_lst.next = head
                small_lst = small_lst.next
            else:
                big_lst.next = head
                big_lst = big_lst.next
            head = head.next

        small_lst.next = b.next
        big_lst.next = None

        return s.next


res = Solution().partition(a, 3)
print_list(res)
