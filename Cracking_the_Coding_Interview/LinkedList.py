class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None
    def append(self,value):
        new = Node(value)
        current = self
        while current.next:
            current = current.next
        current.next = new