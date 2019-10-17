class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"value: {self.value}, left: {self.left}, right: {self.right}"

    # Insert the given value into the tree
    def insert(self, value):

        if self.value == value:
            return

        if value > self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
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
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bss = BinarySearchTree(4)

bss.insert(3)
bss.insert(5)
bss.insert(7)
bss.insert(1)
bss.insert(32)

print(bss.contains(1))
