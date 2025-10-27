""" bst.py

Student: Marcus Steiner
Mail: marcus.steiner.3581@student.uu.se
Reviewed by: Anna Seiderer
Date reviewed: 9/10 - 2024
"""


from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k): #
        return self._contains(self.root, k) is not None
    
    def _contains(self, n, k):
        if n is None:
            return n
        elif n.key is k:
            return n
        elif k < n.key:
            n = self._contains(n.left, k)
        else:
            n = self._contains(n.right, k)
        return n

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                 #            
        return self._height(self.root)
    
    def _height(self, n):
        if n is None:
            return 0
        elif self._height(n.left) < self._height(n.right):
            return 1 + self._height(n.right)
        else:
            return 1 + self._height(n.left)

    def remove(self, key): #
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      #
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
        elif k > r.key:
            r.right = self._remove(r.right, k)
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                _right_tree = r.right               # Find the smallest key in the right subtree
                while _right_tree.left is not None: # Find the smallest key in the right subtree
                    _right_tree = _right_tree.left  # Find the smallest key in the right subtree
                _right_tree_num = _right_tree.key   # Find the smallest key in the right subtree
                r.key = _right_tree_num             # Put that key in this node
                r.right = self._remove(r.right, _right_tree_num)    # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above

    def __str__(self):                #
        return f"<{', '.join(str(n) for n in self)}>"

    def to_list(self):                      #      
        return [n for n in self]

    def to_LinkedList(self):                 #
        lst = LinkedList()
        for x in self:
            lst.insert(x)
        return lst


def random_tree(n):     # Didn't use
    pass


def main():
    t = BST()
    for x in [5, 10, 12, 8, 3, 6, 4, 1, 2, 11]:
        t.insert(x)
    # t.print()
    # print()

    # print('size  : ', t.size())
    # for k in [0, 1, 2, 5, 9]:
    #     print(f"contains({k}): {t.contains(k)}")
    
    # print('height  : ', t.height())
    
    # print(str(t))
    
    # print(t.to_list())
    
    # print(t.to_LinkedList())
    
    # t.remove(10)
    
    # t.print()


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size?
When calculating the size of the tree it's a good idea to use __iter__.

2. computing height?
I wouldn't use __iter__ for calculating the height, I think its a lot of bonus steps

3. contains?
When checking if the tree contains a specific number you can use __iter__ but i don't think it's the fastest.

4. insert?
No, inserting is not something i would use __iter__ for

5. remove?
Yea it would work but not the fastest, it's the same as contains function

"""
