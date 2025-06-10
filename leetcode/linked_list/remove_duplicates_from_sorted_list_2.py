"""Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous = dummy

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                previous.next = head.next
            else:
                previous = previous.next
                head = head.next
        return dummy.next



def check(res):
    while res:
        print(res.val)
        res = res.next
    print('-'.ljust(20))


a = ListNode(1, ListNode(1, ListNode(3, ListNode(4, ListNode(5)))))
a1 = ListNode(1, ListNode(3, ListNode(3, ListNode(4, ListNode(5)))))
a2 = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(5)))))
res= Solution().deleteDuplicates(a)
# check(res)
# res= Solution().deleteDuplicates(a1)
# check(res)
#
# res= Solution().deleteDuplicates(a2)
# check(res)
