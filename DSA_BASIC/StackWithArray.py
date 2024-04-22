class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, data):
        self.stack.insert(0, data)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty, hence can't do pop operation")
        else:
            self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        retVal = ''
        for i in self.stack:
            retVal = retVal + str(i) + '->'

        retVal = retVal + 'NULL'
        return retVal

if __name__ == '__main__':
    stk = Stack()
    print(len(stk))
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.push(4)
    print(len(stk))
    print(stk)
    stk.pop()
    print(stk)
    stk.pop()
    print(stk)
    stk.pop()
    print(stk)
    stk.pop()
    print(stk)
    print(len(stk))
    stk.pop()       # It will throw exception