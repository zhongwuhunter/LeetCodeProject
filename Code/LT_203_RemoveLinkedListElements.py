# 删除链表中等于给定值 val 的所有节点。
#
# 示例:
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
# 时间复杂度: O(n)
# 空间复杂度: O(1)


from BaseLinkedList import  *




def removeElements(head, val):

    ret = head

    dummyHead = Node(0)
    dummyHead.next = head
    currentNode = dummyHead


    while currentNode.next is not None:
        if currentNode.next.data == val:
            currentNode.next = currentNode.next.next
        else:
            currentNode = currentNode.next


    return dummyHead.next


def removeElementsEes(head, val):
    if head is None:
        return None

    head.next = removeElementsEes(head, val)
    if head.val == val :
        return head.next
    else:
        return head




def test():
    list = LinkedList()
    list.append(1)
    list.append(3)
    list.append(2)
    list.append(10)
    list.append(22)
    list.append(2)
    list.append(12)

    node = removeElementsEes(list.head, 12)

    tempNode = node
    while tempNode is not None:
        print(tempNode.data)
        tempNode = tempNode.next


    # ListNode* removeElements(ListNode* head, int val) {
    #     if (!head) return NULL;
    #     head->next = removeElements(head->next, val);
    #     return head->val == val ? head->next : head;
    # }

















