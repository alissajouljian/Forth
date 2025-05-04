class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise Exception("Stack underflow")
        return self.items.pop()

    def peek(self):
        if not self.items:
            raise Exception("Stack is empty")
        return self.items[-1]

    def __len__(self):
        return len(self.items)


