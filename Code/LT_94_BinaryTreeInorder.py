

from  BaseTree import  *
from  BaseStack import  *


def inorderTraversal(root):
    res = []
    s  = Stack()
    p = root

    while p is not None or not s.isEmpty() :
        while p is not  None :
            s.push(p)
            p = p.leftNode
        p = s.top()
        s.pop()
        res.append(p.key)
        p = p.rightNode

    return res



def test():
    tree = BinaryTree();
    tree.insert1()
    tree.inorder(tree.root)
    # list = inorderTraversal(tree.root)
    # for key in list:
    #     print(key)


test()