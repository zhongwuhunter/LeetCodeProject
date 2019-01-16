
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4.
# 输出: 1->4->3->2->5->NULL
#


from BaseLinkedList import  *



def reverseBetwwen(list, m, n):

    dummy = Node(-1)
    dummy.next = list.head
    cur = dummy
    pre = None
    front = None
    last = None
    index = 0

    for index in range(index, m-1):
        cur = cur.next

    pre = cur
    last = cur.next

    index = m;
    for index in range(index, n+1):
        cur = pre.next
        pre.next = cur.next
        cur.next = front
        front = cur

    cur = pre.next
    pre.next = front
    last.next = cur

    return dummy.next




def  cus_bw(list, m, n):
    dummy = Node(-1)
    dummy.next = list.head

    cur = dummy
    pre = None

    last = None # last 是m，因为最后面才赋值m 所以取名last
    front = None
    index = 0

    for index in range(index, m-1):
        cur = cur.next

    pre = cur
    last = cur.next
    index = m

    for index in range(index, n+1):
        cur = pre.next
        pre.next = cur.next
        cur.next = front
        front = cur


    cur = pre.next
    pre.next = front
    last.next = cur

    return dummy.next



def test():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
    list.append(6)
    list.append(7)
    list.append(8)

    # node =  reverseBetwwen(list, 2, 7)
    node = cus_bw(list, 2, 7)
    while node is not None:
        print(node.data)
        node = node.next

test()