from sortedcontainers import SortedList

class NewString:
    def __init__(self) -> None:
        self.bst = SortedList()
    
    def read(self, idx):
        return self.bst[idx][1]
    
    def insert(self, idx, ch):
        if idx > len(self.bst):
            raise NotImplementedError
        if not self.bst:
            key = 0
        elif idx == 0:
            key = self.bst[0][0] - 1
        elif idx == len(self.bst):
            key = self.bst[-1][0] + 1
        else:
            key = (self.bst[idx - 1][0] + self.bst[idx][0]) / 2
        self.bst.add((key, ch))

    def delete(self, idx):
        if idx >= len(self.bst):
            raise NotImplementedError
        del self.bst[idx]

s = NewString()
s.insert(0, "a")
s.insert(1, "1")
s.insert(2, "2")
s.insert(3, "3")
s.insert(0, "b")
print(s.read(0))
print(s.read(1))
print(s.read(2))
s.delete(2)
print(s.read(2))
print(s.read(3))

# ba123