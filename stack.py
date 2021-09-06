class Stack:
    def __init__(self):
        self.stacks = []

    def push(self, new_data):
        self.stacks.append(new_data)

    def pop(self):
        return self.stacks.pop()

    def size(self):
        return len(self.stacks)

    def is_empty(self):
        return self.stacks == []
