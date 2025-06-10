class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_node(self, value):
        self.next = value


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        temp = Node(value)
        temp.set_node(self.head)
        self.head = temp

    def push_to_end(self, value):
        if self.head:
            t = Node(value)
            last = self.head
            while last.next:
                last = last.next
            last.next = t
        else:
            self.push(value)

    def insert_into(self, value, ind):
        temp = Node(value)  # (value = 15, next = 30) # 15 -> 30
        if self.head:
            current = self.head # 10 -> 15 -> 30
            for _ in range(ind-1):
                current = current.next
            temp.next = current.next
            current.next = temp



# Example usage
linked_list = LinkedList()
linked_list.push(10)  # 1
linked_list.push(20)  # 0
linked_list.push_to_end(30)
linked_list.insert_into(15, 2)
while linked_list.head:
    print(linked_list.head.value)
    linked_list.head = linked_list.head.next
