class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.size = 0
        self.head = None

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size = self.size + 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty, hence can't do pop operation")
        else:
            tempNode = self.head
            self.head = self.head.next
            tempNode = None
            self.size = self.size - 1

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty, hence can't do pop operation")
        else:
            return self.head.data

    def __len__(self):
        return self.size

    def __str__(self):
        currNode = self.head
        retVal = ''
        while currNode is not None:
            retVal = retVal + str(currNode.data) + '->'
            currNode = currNode.next
        retVal = retVal + 'None'
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