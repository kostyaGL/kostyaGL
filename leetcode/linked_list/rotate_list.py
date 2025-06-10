"""
Given the head of a linked list, rotate the list to the right by k places.



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]


Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    current = head
    while current:
        print(
            f"Node value: {current.val}")
        current = current.next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        last_element = head
        length = 1
        while last_element.next:
            length += 1
            last_element = last_element.next

        k = k % length
        last_element.next = head

        temp = head
        for _ in range(length - k - 1):
            temp = temp.next

        answer = temp.next
        temp.next = None
        return answer


a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

res = Solution().rotateRight(a, 2)
print_list(res)
