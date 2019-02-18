# 给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4) (逆序存储)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


from BaseLinkedList import  *

l1 = LinkedList()
l1.append(2)
l1.append(4)
l1.append(3)
l2 = LinkedList()
l2.append(5)
l2.append(6)
l2.append(6)

p1 = l1.head
p2 = l2.head

dummyHead = LinkedList()
# 这里添加一个-1的节点不是必须的，指数保证了这个链表的存在，其实这个-1节点没用
dummyHead.append(-1)


def addTowNums(node1, node2, dummyHead):
    cur = dummyHead.head
    carried = 0
    while node1 is not None or node2 is not  None:
        num1 = 0
        num2 = 0
        if node1 is not None:
            num1 = node1.data

        if node2 is not None:
            num2 = node2.data

        value = (num1 + num2 + carried)
        carried = int(value / 10)
        number = value % 10

        cur.next = Node(number)
        cur = cur.next

        if node1 is not None:
            node1 = node1.next
        if node2 is not None:
            node2 = node2.next

    if carried != 0:
        cur.next = Node(1)

    return dummyHead.head.next

def start():
    ret = addTowNums(p1, p2, dummyHead)
    while (ret is not None):
        print(ret.data)
        ret = ret.next

start()













