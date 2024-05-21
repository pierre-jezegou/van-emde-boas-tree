import math

class VanEmdeBoasTree:
    """
    Van Emde Boas Tree implementation.

    Attributes:
        u (int): The size of the universe.
        min (int): The minimum element in the tree.
        max (int): The maximum element in the tree.
        sqrt_u (int): The square root of the universe size.
        children (list): The array of child trees.
        aux (VanEmdeBoasTree): The auxiliary tree.

    Methods:
        is_empty(): Check if the tree is empty.
        high(x): Get the high bits of x.
        low(x): Get the low bits of x.
        index(i, j): Get the index from high bits i and low bits j.
        find_next(x): Find the next element after x.
        find_previous(x): Find the previous element before x.
        insert(x): Insert an element x into the tree.
        delete(x): Delete an element x from the tree.
    """

    def __init__(self, universe_size):
        """
        Initialize the VanEmdeBoasTree.

        Args:
            universe_size (int): The size of the universe.
        """
        self.u = universe_size
        self.min = self.u
        self.max = -1
        if self.u > 2:
            self.sqrt_u = int(math.ceil(math.sqrt(self.u)))
            self.children = [None] * self.sqrt_u
            self.aux = VanEmdeBoasTree(self.sqrt_u)
        else:
            self.children = [None, None]

    def is_empty(self):
        """
        Check if the tree is empty.

        Returns:
            bool: True if the tree is empty, False otherwise.
        """
        return self.max == -1

    def high(self, x):
        """
        Get the high bits of x.

        Args:
            x (int): The input number.

        Returns:
            int: The high bits of x.
        """
        return x // self.sqrt_u

    def low(self, x):
        """
        Get the low bits of x.

        Args:
            x (int): The input number.

        Returns:
            int: The low bits of x.
        """
        return x % self.sqrt_u

    def index(self, i, j):
        """
        Get the index from high bits i and low bits j.

        Args:
            i (int): The high bits.
            j (int): The low bits.

        Returns:
            int: The index.
        """
        return i * self.sqrt_u + j

    def find_next(self, x):
        """
        Find the next element after x.

        Args:
            x (int): The input number.

        Returns:
            int: The next element after x.
        """
        if x < self.min:
            return self.min
        if x >= self.max:
            return self.u
        if self.u == 2:
            return 1 if x == 0 and self.max == 1 else self.u
        i = self.high(x)
        lo = self.low(x)
        if self.children[i] is not None and not self.children[i].is_empty() and lo < self.children[i].max:
            offset = self.children[i].find_next(lo)
            return self.index(i, offset)
        j = self.aux.find_next(i)
        if j == self.sqrt_u:
            return self.u
        return self.index(j, self.children[j].min)

    def find_previous(self, x):
        """
        Find the previous element before x.

        Args:
            x (int): The input number.

        Returns:
            int: The previous element before x.
        """
        if x > self.max:
            return self.max
        if x <= self.min:
            return -1
        if self.u == 2:
            return 0 if x == 1 and self.min == 0 else -1
        i = self.high(x)
        lo = self.low(x)
        if not self.children[i].is_empty() and lo > self.children[i].min:
            offset = self.children[i].find_previous(lo)
            return self.index(i, offset)
        j = self.aux.find_previous(i)
        if j == -1:
            if self.min < x:
                return self.min
            return -1
        return self.index(j, self.children[j].max)

    def insert(self, x):
        """
        Insert an element x into the tree.

        Args:
            x (int): The element to insert.
        """
        if self.min == self.max and self.min == x:
            return
        if self.is_empty():
            self.min = self.max = x
            return
        if x < self.min:
            x, self.min = self.min, x
        if self.u > 2:
            i = self.high(x)
            lo = self.low(x)
            if self.children[i] is None:
                self.children[i] = VanEmdeBoasTree(self.sqrt_u)
            if self.children[i].is_empty():
                self.aux.insert(i)
            self.children[i].insert(lo)
        if x > self.max:
            self.max = x

    def delete(self, x):
        """
        Delete an element x from the tree.

        Args:
            x (int): The element to delete.
        """
        if self.min == self.max and self.min == x:
            self.min = self.u
            self.max = -1
            return
        if x == self.min:
            if self.u == 2:
                self.min = self.max if x == 0 else 1
                self.max = self.min
                return
            i = self.aux.min
            x = self.index(i, self.children[i].min)
            self.min = x
        i = self.high(x)
        lo = self.low(x)
        self.children[i].delete(lo)
        if self.children[i].is_empty():
            self.aux.delete(i)
        if x == self.max:
            if self.aux.is_empty():
                self.max = self.min
            else:
                i = self.aux.max
                self.max = self.index(i, self.children[i].max)

# Example usage:
veb = VanEmdeBoasTree(16)  # for a universe size of 16
elements = [1, 2, 3, 5, 8, 10]

for elem in elements:
    veb.insert(elem)

print("Find next of 3:", veb.find_next(3))  # Should return 5
print("Find next of 9:", veb.find_next(9))  # Should return 10
print("Find next of 10:", veb.find_next(10))  # Should return 16 (universe size, no successor)
print("Find previous of 10:", veb.find_previous(10))  # Should return 8

veb.delete(3)
print("Find next of 2 after deleting 3:", veb.find_next(2))  # Should return 5
