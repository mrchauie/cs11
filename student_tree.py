class Node:
    """An Node of the Binary Tree.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()

    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res

    # Preorder traversal
    # Root -> Left ->Right
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res

    # Postorder traversal
    # Left ->Right -> Root
    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res


#test
root = Node('tu')
root.insert('f')
root.insert('r')
root.insert('i')
root.insert('n')
root.insert('ta')
root.insert('u')


print(root.preorderTraversal(root))