class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        index = len(self.storage)-1
        self._bubble_up(index)

    def delete(self):
        pass

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
        pass


heap = Heap()

heap.insert(6)
heap.insert(8)
heap.insert(10)
heap.insert(9)
heap.insert(1)
heap.insert(9)
heap.insert(9)
heap.insert(5)
heap.insert(3000)

print(heap.get_max())
print(heap.get_size())
# print(heap.storage)
# print(range(len(heap.storage)))
