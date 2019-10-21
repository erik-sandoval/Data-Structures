class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.frequency = 0

    def __str__(self):
        return f"value: {self.value}, left: {self.left}, right: {self.right}"

    # Insert the given value into the tree
    def insert(self, value):

        if self.value == value:
            self.frequency += 1
            return

        if value > self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
                self.right.frequency += 1
            else:
                self.right.insert(value)

        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
                self.left.frequency += 1
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if self.value == target:
            return True
        if target < self.value:
            if self.left == None:
                return False
            return self.left.contains(target)
        if target > self.value:
            if self.right == None:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        max = self.value
        if not self.right:
            return max
        if self.value > max:
            max = self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        visited = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            visited.append(node.value)
            helper(node.right)

        helper(node)

        return visited

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        queue = []
        visited = []

        if not node.value:
            return []

        queue.append(node)
        while (len(queue) > 0):
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            visited.append(queue[0].value)
            del queue[0]
        return visited

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        visited = []

        def helper(node):
            if node.left:
                helper(node.left)
            visited.append(node.value)
            if node.right:
                helper(node.right)

        helper(node)

        return visited

    # STRETCH Goals -------------------------
    # Note: Research may be required

    def pre_order_dft(self, node):
        visited = []

        def helper(node):
            visited.append(node.value)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)

        helper(node)
        return visited

    def post_order_dft(self, node):
        visited = []

        def helper(node):
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
            visited.append(node.value)

        helper(node)
        return visited


bss = BinarySearchTree(4)

bss.insert(8)
bss.insert(5)
bss.insert(7)
bss.insert(6)
bss.insert(3)
bss.insert(2)
bss.insert(9)

print(bss.dft_print(bss))
