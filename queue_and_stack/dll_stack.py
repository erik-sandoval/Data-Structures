from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        return self.storage.add_to_head(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        return self.size


stack = Stack()

stack.push(33)
stack.push(44)
stack.push(55)
stack.push(22)

print(stack.pop())

print(stack.storage.head.value)
