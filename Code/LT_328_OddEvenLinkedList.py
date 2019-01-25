

from BaseLinkedList import  *



def oddEventList(head):

    if head is None:
        return None

    dummyHead1 = Node(-1)
    dummyHead2 = Node(-1)

    p1 = dummyHead1
    p2 = dummyHead2

    node = head

    flag = True
    while node is not None :
        if flag :
            p1.next = node
            p1 = p1.next
        else:
            p2.next = node
            p2 = p2.next
        flag = not flag
        node = node.next

    p2.next = None
    p1.next = dummyHead2.next

    res = dummyHead1.next

    return res




def test():
    list = LinkedList()
    # list.append(2)
    # list.append(1)
    # list.append(3)
    # list.append(5)
    # list.append(6)
    # list.append(4)
    # list.append(7)

    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
    list.append(6)

    node = oddEventList(list.head)

    while node is not None:
        print(node.data)
        node = node.next





test()



















