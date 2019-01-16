# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
#  o(n)

from BaseLinkedList import  *


def cus_partition(list, number):
    header1 = Node(-1)
    header2 = Node(-1)

    header3 = header1
    header4 = header2

    node = list.head

    while node is not None:
        if node.data < number:
            header1.next = node
            node = node.next;
            header1 = header1.next
            header1.next = None
        else:
            header2.next = node
            node = node.next;
            header2 = header2.next
            header2.next = None



    header1.next = header4.next

    return header3.next


def partition(list, number):
    head1 = Node(-1)
    head2 = Node(-1)
    prev1 = head1
    prev2 = head2

    cur = list.head

    while cur is not  None:
        if cur.data < number:
            prev1.next = cur
            cur = cur.next
            prev1 = prev1.next
            prev1.next = None
        else:
            prev2.next = cur
            cur = cur.next
            prev2 = prev2.next
            prev2.next = None

    prev1.next = head2.next
    ret = head1.next
    return ret


def test():
    list = LinkedList()
    list.append(1)
    list.append(8)
    list.append(2)
    list.append(7)
    list.append(4)
    list.append(6)
    list.append(5)


    node = cus_partition(list, 6)

    while node is not None:
        print(node.data)
        node = node.next


test()

















