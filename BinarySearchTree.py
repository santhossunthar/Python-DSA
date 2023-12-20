class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.counter = 1

class BST:
    def __init__(self):
        self.root = None

    def add(self, data):
        self.root = self._add(self.root, data)

    def _add(self, root, data):
        if root is None: return Node(data)

        if data <= root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                root.left = self._add(root.left, data)
        if data > root.data:
            if root.right is None:
                root.right = Node(data)
            else:
                root.right = self._add(root.right, data)

        return root
        
        return root

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, root, data):
        if root is None: return root

        if data == root.data: root.counter -= 1

        if data < root.data:
            root.left = self._delete(root.left, data)
        elif data > root.data:
            root.right = self._delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.data = self.findMinValue(root.right).data
            root.right = self._delete(root.right, root.data)

        return root
            
    def findMinValue(self, node):
        currentNode = node

        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode

    def inOrderTraversal(self):
        self._inOrderTraversal(self.root)

    def _inOrderTraversal(self, root):
        if root:
            self._inOrderTraversal(root.left)
            print(root.data)
            self._inOrderTraversal(root.right)

    def preOrderTraversal(self):
        self._preOrderTraversal(self.root)

    def _preOrderTraversal(self, root):
        if root:
            print(root.data)
            self._preOrderTraversal(root.left)
            self._preOrderTraversal(root.right)

bst = BST()
bst.add(3)
bst.add(1)
bst.add(5)
bst.add(3)
bst.add(7)
bst.add(6)
bst.add(5)
bst.add(5)
print(bst.inOrderTraversal())