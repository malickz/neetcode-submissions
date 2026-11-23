class MinStack:
    def __init__(self):
        self.main_stk = MainStack()
        self.min_stk = MainStack()

    def push(self, val: int) -> None:
        self.main_stk.push(val)
        if self.min_stk.is_empty() or val < self.min_stk.top():
            self.min_stk.push(val)
        else:
            self.min_stk.push(self.min_stk.top())

    def pop(self) -> None:
        self.min_stk.pop()
        return self.main_stk.pop()

    def top(self) -> int:
        if not self.main_stk.is_empty():
            return self.main_stk.top()
        return None
        

    def getMin(self) -> int:
        if not self.min_stk.is_empty():
            return self.min_stk.top()
        return None
        

class MainStack:

    def __init__(self):
        self.main_stk = []
    
    def top(self):
        if self.is_empty():
            return None
        return self.main_stk[-1]
    
    def is_empty(self):
        return len(self.main_stk) == 0
    
    def push(self, val):
        self.main_stk.append(val)
    
    def pop(self):
        if not self.is_empty():
            return self.main_stk.pop()
        return None

