class Queue:
    def __init__(self):
        self.queues = []

    def enqueue(self, new_data):
        self.queues.insert(0, new_data)

    def dequeue(self):
        if self.size():
            return self.queues.pop()
        return 'empty'

    def size(self):
        return len(self.queues)


q = Queue()
q.enqueue(1)
q.enqueue(5)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

