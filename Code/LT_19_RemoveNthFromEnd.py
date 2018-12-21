# 删除链表的倒数第N个节点
# 时间复杂度 O(n)
# 空间复杂度 O(1)
# 关键点 1 p,q 节点是 head的前一个节点， 这里为了应付链表 head 被删除的情况。所以先newnode 作为头节点
#2 因为循环关系 n+1 才能遍历到对应的位置
#3 注意 p, q 判断 None情况




from BaseSTL import  *







def removeNodeFromeEnd(list, n):
    head = list.head
    node = Node(0)
    node.next = head
    p = node
    q = node
    i = 0

    for i in range(i, n+1):
        if q is not None:
            q = q.next

    while q is not None:
        p = p.next
        q = q.next

    deleteNode = p.next
    if deleteNode is not None :
        p.next = deleteNode.next
    else:
        p.next = None

def test():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)

    removeNodeFromeEnd(list, 1)
    node = list.head

    while node is not None:
        print(node.data)
        node = node.next


test()




