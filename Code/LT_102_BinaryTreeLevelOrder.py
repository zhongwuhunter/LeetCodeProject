# 二叉树的层次遍历
# 给定二叉树: [3,9,20,null,null,15,7],
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


from  BaseTree import  *
from  BaseQueue import  *

def levelOrder(root):
    res = []
    if root is None :
        return res

    q = Queue()
    q.push((root, 0))

    while not q.empty():
        tup = q.front()
        node = tup[0]
        level = tup[1]
        q.pop()

        if ( level == len(res) ):
            res.append([])

        res[level].append(node.val)
        if node.left is not None :
            q.push((node.left, level+1))
        if node.right is not None:
            q.push((node.right, level + 1))

    return res


def test():

    tree =  BinaryTree()
    tree.insert2()
    root = tree.root
    res = levelOrder(root)

    for vct in res :
        for val in vct:
            print(val)









test()





























































