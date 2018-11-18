class Node:

    def __init__(self,val=None):
        self.left = None
        self.right = None
        self.data = val


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

def main():
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print "Preorder traversal of binary tree is"
print.Preorder(root)

print "\nInorder traversal of binary tree is"
print Inorder(root)

print "\nPostorder traversal of binary tree is"
print Postorder(root)

main()
