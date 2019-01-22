

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
        countTmp = 0;
        res1D = []
        while count > 0 :
            res1D.append(q.front().val)
            if q.front().left is not None:
                q.push(q.front().left)
                countTmp += 1
            if q.front().right:
                q.push(q.front().right)
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
    tree.insert2()
    root = tree.root
    res = zigzagLevelOrder(root)

    for vct in res :
        for val in vct:
            print(val)


test()
































