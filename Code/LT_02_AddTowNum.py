#
#  两个数字相加  整数非0， 用于超大数字
#  时间复杂度 O(n)
#  空间复杂度 O(n)
#
from BaseSTL import  *

l1 = LinkedList()
l1.append(8)
l1.append(4)
l1.append(3)
l2 = LinkedList()
l2.append(5)
l2.append(6)
l2.append(1)
p1 = l1.head
p2 = l2.head

dummyHead = LinkedList()
# 这里添加一个-1的节点不是必须的，指数保证了这个链表的存在，其实这个-1节点没用
dummyHead.append(-1)



def addTowNums(p1, p2, dummyHead):
    cur = dummyHead.head
    carried = 0
    while (p1 is not None or p2 is not None):

        a = 0
        b = 0
        if p1 is not None:
            a = p1.data
            p1 = p1.next

        if p2 is not None:
            b = p2.data
            p2 = p2.next

        value = a + b + carried
        cur.next = Node(value%10)
        carried = int(value/10)
        cur = cur.next

    if (0 != carried):
        cur.next = Node(1)
    else:
        cur.next = None

    ret = dummyHead.head.next

    return ret






ret = addTowNums(p1, p2, dummyHead)
while (ret is not None):
    print(ret.data)
    ret = ret.next











