



class TreeNode:
    val = None
    data= None
    leftNode = None
    rightNode = None

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
                    if currentNode.rightNode is None:
                        currentNode.rightNode = node
                        return
                    else:
                        currentNode = currentNode.rightNode
                else:
                    if currentNode.leftNode is None:
                        currentNode.leftNode = node
                        return
                    else:
                        currentNode = currentNode.leftNode



    def inorder(self, node):
        if node is not None :
            self.inorder(node.leftNode)
            print(node.val)
            self.inorder(node.rightNode)



# 普通二叉树
class BinaryTree():
    root = None

    def insert1(self):
        self.root = TreeNode(1)
        current = self.root
        current.rightNode = TreeNode(2)
        current = current.rightNode
        current.leftNode = TreeNode(3)
        current = current.leftNode
        current.leftNode = TreeNode(4)
        current.rightNode = TreeNode(5)

    def insert2(self):
        self.root = TreeNode(3)
        current = self.root
        current.leftNode = TreeNode(9)
        current.rightNode = TreeNode(20)

        current = current.leftNode
        current.leftNode = TreeNode(15)
        current.rightNode = TreeNode(7)

    def inorder(self, node):
        if node is not None :
            self.inorder(node.leftNode)
            print(node.val)
            self.inorder(node.rightNode)

# def test():
#     tree = BinarySearchTree();
#     tree.insert(100)
#     tree.insert(80)
#     tree.insert(150)
#     tree.insert(50)
#     tree.insert(90)
#     tree.insert(60)
#     tree.insert(70)
#     tree.insert(40)
#     tree.insert(30)
#
#     tree.inorder(tree.root)
#
# test()









