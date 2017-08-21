class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    @property
    def get_next(self):
        return self.next

    @property
    def get_data(self):
        return self.data

    def set_next(self, item):
        self.next = item

    def set_data(self, item):
        self.data = item


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    @property
    def is_empty(self):
        return not self.head

    @property
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next
        return count

    def search(self, node):
        current = self.head
        while current:
            if current.get_data == node:
                return True
            current = current.get_next
        return False

    def delete(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data == item:
                found = True
            else:
                previous = current
                current = current.get_next

        if not previous:
            self.head = current.get_next
        else:
            previous.set_next(current.get_next)


s = LinkedList()
s.push(12)
s.push(14)
s.push(15)
s.push(16)
s.push(17)
s.push(18)
print(s.delete(14))
