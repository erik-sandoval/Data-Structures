class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # if value in self.storage:
        #     return

        self.storage.append(value)
        index = len(self.storage)-1
        self._bubble_up(index)

    def delete(self):
        if self.get_size() == 1:
            return self.storage.pop()
        deleted_val = self.storage[0]
        self.storage[0] = self.storage[-1]
        self.storage.pop()
        self._sift_down(0)
        return deleted_val

    def get_max(self):
        max = self.storage[0]
        for i in range(len(self.storage)):
            if self.storage[i] > max:
                max = self.storage[i]
        return max

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index < 1:
            return

        parent = (index-1)//2
        child = index

        if self.storage[parent] < self.storage[child]:
            self.storage[parent], self.storage[child] = self.storage[child], self.storage[parent]
            index = parent
            self._bubble_up(index)

    def _sift_down(self, index):
        child1 = 2 * index + 1
        child2 = 2 * index + 2

        max = child1
        if (child2 < self.get_size()):
            if (self.storage[max] < self.storage[child2]):
                max = child2
            if self.storage[index] < self.storage[max]:
                self.storage[index], self.storage[max] = self.storage[max], self.storage[index]
                return self._sift_down(index + 1)
            else:
                return
        if (child1 < self.get_size()):
            if self.storage[index] < self.storage[max]:
                self.storage[index], self.storage[max] = self.storage[max], self.storage[index]
                return self._sift_down(index + 1)
            else:
                return
