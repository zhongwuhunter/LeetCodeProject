

from BaseLinkedList import  *


def reverseLinkedList(head):

    pre = None
    current = head


    while current is not None:
        next = current.next
        current.next = pre
        pre = current
        current = next


    return pre





def test():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
    list.append(6)
    list.append(7)

    head = list.head
    node = reverseLinkedList(head)

    while node is not None:
        print(node.data)
        node = node.next



test()
























