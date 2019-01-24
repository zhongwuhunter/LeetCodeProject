

from  BaseTree import  *
from  BaseQueue import  *


def zigzagLevelOrder(root):

    res2D = []
    q = Queue()

    if root is None:
        return

    q.push(root)
    level = 1
    count = 1
    countTmp = 0
    while not q.empty():
        countTmp = 0
        res1D = []
        while count > 0 :
            frontNode =  q.front()
            res1D.append(frontNode.val)
            if frontNode.left is not None:
                anode = frontNode.left
                q.push(anode)
                countTmp += 1
            if frontNode.right  is not None:
                anode = frontNode.right
                q.push(anode)
                countTmp += 1

            q.pop()
            count -= 1;

        if level == 2 :
            res1D.reverse()

        count = countTmp
        res2D.append(res1D)
        level += 1

    return  res2D





def test():
    tree =  BinaryTree()
    tree.insert3()
    root = tree.root
    res = zigzagLevelOrder(root)

    for vct in res :
        for val in vct:
            print(val)


test()
































