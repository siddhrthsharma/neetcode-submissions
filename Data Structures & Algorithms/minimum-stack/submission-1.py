class MinStack:
    # create a stack that keeps track of the min
        # when we add, we only add the minimum of the top element and the new element
    # when asked for getMin -> return top of minStack
    # when popping, just pop from other stack as normal
        # but if top of minStack (current minimum value)
        # pop out of the minStack as well
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.minStack) >= 1:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
