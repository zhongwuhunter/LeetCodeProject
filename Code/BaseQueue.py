

class Queue:

    def __init__(self):
        self.items = []

    def empty(self):
        return 0 == len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.empty() :
            return None
        else:
            return self.items.pop(0)

    def front(self):
        if self.empty() :
            return None
        else:
            return self.items[0]


# def test():
#
#     q = Queue()
#     q.push(1)
#     q.push(2)
#     q.push(3)
#
#     print(q.pop())
#     print(q.pop())
#     print(q.pop())
#     print(q.pop())
#
#     print(q.front())


# test()


