



class TreeNode:
    val = None
    data= None
    left = None
    right = None

    def __init__(self, val):
        self.val = val

# 二叉树搜索树
class BinarySearchTree:
    root = None

    def insert(self, val):
        node = TreeNode(val)
        currentNode = self.root
        while True :
            if currentNode is None :
                self.root = node
                return
            else:
                if val > currentNode.val :
                    if currentNode.right is None:
                        currentNode.right = node
                        return
                    else:
                        currentNode = currentNode.right
                else:
                    if currentNode.left is None:
                        currentNode.left = node
                        return
                    else:
                        currentNode = currentNode.left



    def inorder(self, node):
        if node is not None :
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)



# 普通二叉树
class BinaryTree():
    root = None

    def insert1(self):
        self.root = TreeNode(1)
        current = self.root
        current.right = TreeNode(2)
        current = current.right
        current.left = TreeNode(3)
        current = current.left
        current.left = TreeNode(4)
        current.right = TreeNode(5)

    def insert2(self):
        self.root = TreeNode(3)
        current = self.root
        current.left = TreeNode(9)
        current.right = TreeNode(20)

        current = current.left
        current.left = TreeNode(15)
        current.right = TreeNode(7)

    def insert3(self):
        self.root = TreeNode(3)
        current = self.root
        current.left = TreeNode(9)
        current.right = TreeNode(20)

        current = current.right
        current.left = TreeNode(15)
        current.right = TreeNode(7)

    def inorder(self, node):
        if node is not None :
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)

# def test():
#     # tree = BinarySearchTree();
#     # tree.insert(100)
#     # tree.insert(80)
#     # tree.insert(150)
#     # tree.insert(50)
#     # tree.insert(90)
#     # tree.insert(60)
#     # tree.insert(70)
#     # tree.insert(40)
#     # tree.insert(30)
#
#     tree = BinaryTree()
#     tree.insert3()
#
#     tree.inorder(tree.root)
#
# test()









