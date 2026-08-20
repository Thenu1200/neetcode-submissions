import math
class MinStack:

    def __init__(self):
        self.stack = []
        self.minlist = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minlist:
            self.minlist.append(val)
        else:
            self.minlist.append(min(val, self.minlist[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minlist.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minlist[-1]
