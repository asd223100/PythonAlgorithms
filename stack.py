class Stack:
    def __init__(self):
        self.stacks=[]
    def push(self,new_data):
        self.stacks.append(new_data)
    def pop(self):
        return self.stacks.pop()
