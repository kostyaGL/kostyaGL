class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


a = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
a1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9,
                                                                                                              ListNode(
                                                                                                                  10))))))))))


def is_polindrome(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    current = slow
    rev = None
    while current:
        next_node = current.next
        current.next = rev
        rev = current
        current = next_node
    while rev and head:
        if head.value != rev.value:
            return False
        rev = rev.next
        head = head.next

    return True




ff= is_polindrome(a)
print(ff)