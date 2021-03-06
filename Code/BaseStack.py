

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return  0 == len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        else:
            return None

    def top(self):
        if self.isEmpty():
            return None
        else:
            # return self.items[0]
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)