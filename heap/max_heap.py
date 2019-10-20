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
        pass

    def get_size(self):
        pass

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

heap.insert(11)
heap.insert(12)
heap.insert(13)
heap.insert(110)
