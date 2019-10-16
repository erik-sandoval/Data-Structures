class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return f"{self.value}, {self.prev}, {self.next}"
    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __str__(self):
        f"{self.head}, {self.tail}, {self.length}"

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

        return new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if self.length == 0:
            return None
        old_node = self.head
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = old_node.next
            self.head.prev = None
            old_node.next = None
        self.length -= 1
        return old_node.value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.head == None:
            return None
        old_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            old_node.prev = None
        self.length -= 1
        return old_node.value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return

        value = node.value
        self.delete(node)
        self.add_to_head(value)
        return value

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return

        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """
    Removes a node from the list and handles cases where
    the node was the head or the tail
    """

    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_index(self, index):

        if index > self.length or index < 1:
            return None
        if index == self.length:
            return self.tail.value
        if index <= self.length // 2:
            counter = 1
            node = self.head
            while (node.next):
                if counter == index:
                    return node.value
                node = node.next
                counter += 1
        else:
            counter = self.length - 1
            node = self.tail
            while node.prev:
                if counter == index:
                    return node.value
                node = node.prev
                counter -= 1
        return None

    def get_max(self):
        if self.head == None:
            return None
        max = self.head.value
        node = self.head
        while (node.next):
            if (node.value > max):
                max = node.value
            node = node.next
        if self.tail.value > max:
            max = self.tail.value
        return max
