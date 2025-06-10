class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
a1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9,
                                                                                                              ListNode(
                                                                                                                  10))))))))))


def delete_node(head, index):
    current = head
    if index == 0:
        current = current.next
        return current
    for i in range(index):
        if not current.next:
            raise Exception('out of range')
        if i == index-1:
            current.next = current.next.next
        else:
            current = current.next
    return head


ff= delete_node(a, 0)

while ff:
    print(ff.value)
    ff = ff.next
