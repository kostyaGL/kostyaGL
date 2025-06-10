"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
a1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = dummy
        for _ in range(left - 1):
            current = current.next
        nxt = current.next
        for _ in range((right - left)):
            temp = nxt.next
            nxt.next = temp.next
            temp.next = current.next
            current.next = temp
        return dummy.next


a = (Solution().reverseBetween(a, 2, 4))
a1 = (Solution().reverseBetween(a1, 2, 9))


def print_list(head):
    current = head
    while current:
        print(
            f"Node value: {current.val}")
        current = current.next

print(print_list(a))
print(print_list(a1))

"""
[1,2,3,4,5] -> [1,2,3,4,5]
[1,2,3,4,5,6,7,8,9,10] -> [1,9,8,7,6,5,4,3,2,10]

[1,2,3,4,5,6,7,8,9,10] -> 
"""
