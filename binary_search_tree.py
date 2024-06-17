import random

UNIVERSE_SIZE = 16

class BSTNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = BSTNode(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = BSTNode(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.value == key:
            return root is not None
        if key < root.value:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

if __name__ == "__main__":
    elements = random.sample(range(UNIVERSE_SIZE), UNIVERSE_SIZE // 2)
    bst = BinarySearchTree()
    for element in elements:
        bst.insert(element)

    for elem in elements:
        bst.search(elem)
