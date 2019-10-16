from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.size = 0
        self.dll = DoublyLinkedList()
        self.storage = {}
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage:
            return self.dll.move_to_front(self.storage[key])
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if key in self.storage:
            self.dll.delete(self.storage[key])
            self.storage[key] = self.dll.add_to_head(value)
            return

        if self.size == self.limit:
            old_node = self.dll.remove_from_tail()
            self.storage.pop(old_node, None)
            self.size -= 1

        self.storage[key] = self.dll.add_to_head(value)
        self.size += 1


# test = {}

# test[0] = 0
# test[2] = 2
# test[3] = 3
# test[4] = 4
# test[5] = 5
# test[1] = 1

# print(test)


# test[3] = 1

# print(test)
test = LRUCache(3)

test.set(1, 4)
test.set(2, 2)
test.set(3, 72)
test.set(4, 6)
test.set(8, 7)
test.set(8, 12)
test.set(8, 3434)
test.set(128, 3434)


print(test.storage[8].value)
print(test.size, len(test.storage))
print(test.dll.length)
