# CCI_3.2
class minstack(object):
    def __init__(self):
        self.data = []
    def push(self,item):
        if self.isEmpty():
            newmin = item
        else:
            newmin = min(item,self.data[len(self.data)-1][1])
        self.data.append([item,newmin])
    def pop(self):
        return self.data.pop()[0]
    def peek(self):
        return self.data[len(self.data)-1][0]
    def min(self):
        return self.data[len(self.data)-1][1]
    def isEmpty(self):
        return self.data == []