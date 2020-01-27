# CCI_3.6
import Queue
class shelter(object):
    def __init__(self):
        self.cats = Queue.Queue()
        self.dogs = Queue.Queue()
        self.order = 0
    def enqueue(self, name, type):
        if type == 'dog':
            self.dogs.enqueue([name,self.order])
            self.order += 1
        elif type == 'cat':
            self.cats.enqueue([name,self.order])
            self.order += 1
    def dequeueCat(self):
        if not self.cats.isEmpty():
            return self.cats.dequeue()[0]
    def dequeueDog(self):
        if not self.dogs.isEmpty():
            return self.dogs.dequeue()[0]
    def dequeueAny(self):
        if not self.cats.isEmpty():
            catorder = self.cats.peek()[1]
        else: catorder = order + 1
        if not self.dogs.isEmpty():
            dogorder = self.dogs.peek()[1]
        else: dogorder = order + 1
        if catorder <= dogorder and not cats.isEmpty():
            return self.cats.dequeue()[0]
        elif not dogs.isEmpty():
            return self.dogs.dequeue()[0]