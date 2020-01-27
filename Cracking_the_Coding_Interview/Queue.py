class Queue(object):
    def __init__(self):
        self.data = []
    def enqueue(self,item):
        self.data.append(item)
    def dequeue(self):
        return self.data.pop(0)
    def peek(self):
        return self.data[0]
    def isEmpty(self):
        return self.data == []