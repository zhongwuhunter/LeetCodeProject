
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 进阶:
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
#
# 示例:
# 输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出: 7 -> 8 -> 0 -> 7



from BaseLinkedList import  *
from BaseStack import  *

def addTowNumII(node1, node2) :

    stack1 = Stack()
    stack2 = Stack()

    while node1 is not None :
        stack1.push(node1.data)
        node1 = node1.next

    while node2 is not None :
        stack2.push(node2.data)
        node2 = node2.next

    flag = 0
    head = None
    while not stack1.isEmpty() or not stack2.isEmpty() or flag != 0 :
        if not stack1.isEmpty():
            flag = flag + stack1.pop()
        if not stack2.isEmpty():
            flag = flag + stack2.pop()

        node = Node(flag % 10)
        node.next = head
        head = node
        # 取整除 - 返回商的整数部分（向下取整）   1 == 13/10 或者  0 == 9/10
        flag = flag // 10

    return head



def test():
    list1 = LinkedList()
    list2 = LinkedList()

    list1.append(9)
    list1.append(2)

    list2.append(3)
    list2.append(4)

    node = addTowNumII(list1.head, list2.head)

    while node is not  None:
        print(node.data)
        node = node.next



test()












































