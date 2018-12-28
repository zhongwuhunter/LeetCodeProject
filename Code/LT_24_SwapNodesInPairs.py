# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 示例:
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
#
# 说明:
# 你的算法只能使用常数的额外空间。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

from BaseLinkedList import  *


list = LinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)


dummyHead = list.head
dummyHead.next = Node(10)








def swapNode(list):
    dummyHead = Node(0)
    dummyHead.next = list.head
    p = dummyHead

    while p.next is not None and p.next.next is not None:

        node1 = p.next
        node2 = node1.next
        next = node2.next

        node2.next = node1
        node1.next = next
        # 关键步骤 p.next 第一次的时候 等于 dummyHead.next = node2 ,也就是node2变成list的head
        p.next = node2
        p = node1

    ret = dummyHead.next
    return ret





def test():
    head = swapNode(list)
    list.head = head
    list.printAll()
    # while head is not None:
    #     print(head.data)
    #     head = head.next

test()