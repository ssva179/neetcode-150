#pseudocode
#keep track of min
#during push if we find a smaller value that curr min we append
#during pop we check if the og stack pop is == min pop this way we
#get rid of values accordingly on bod stacks
#for top and get min we just return the top of both stacks
class MinStack:

    def __init__(self):
        self.stack = []
        self.trackMin =[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.trackMin:
            if self.trackMin[-1] >= val:
                self.trackMin.append(val)
        else:
                self.trackMin.append(val)
        

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.trackMin[-1]:
                self.trackMin.pop()
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            null

    def getMin(self) -> int:
        if self.trackMin:
            return self.trackMin[-1]
            
        else: 
            return null
