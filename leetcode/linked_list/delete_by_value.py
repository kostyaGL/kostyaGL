class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
a1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9,
                                                                                                              ListNode(
                                                                                                                  10))))))))))


def delete_node(head, value):
    current = head
    while current.next:
        if current.next.value == value:
            current.next = current.next.next
            return head
        current = current.next
    return current


ff= delete_node(a, 3)

while ff:
    print(ff.value)
    ff = ff.next
