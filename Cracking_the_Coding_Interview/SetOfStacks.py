# CCI_3.3
class SetOfStacks(object):
    def __init__(self):
        self.data = [[]]
        self.cap = 5
    def push(self,item):
        if len(self.data[len(self.data)-1]) == self.cap:
            self.data.append([item])
        else:
            self.data[len(self.data)-1].append(item)
    def pop(self):
        if len(self.data[len(self.data)-1]) == 1:
            return self.data.pop()[0]
        else:
            self.data[len(self.data)-1].pop()
    def peek(self):
        return self.data[len(self.data)-1][len(self.data[len(self.data)-1])-1]
    def isEmpty(self):
        return self.data == [[]]