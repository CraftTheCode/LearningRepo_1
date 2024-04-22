class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def enqueue(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        self.size = self.size + 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty, hence can't do dequeue operation")
        else:
            tempNode = self.head
            self.head = self.head.next
            tempNode = None
            self.size = self.size - 1

    def peek(self):
        return self.head.data

    def size(self):
        return self.size

    def __len__(self):
        return self.size

    def __str__(self):
        currNode = self.head
        retVal = ''
        while currNode is not None:
            retVal = retVal + str(currNode.data) + '->'
            currNode = currNode.next
        retVal = retVal + 'NULL'
        return retVal


if __name__ == '__main__':
    print('TESTING QUEUE FUNCTIONS')
    queue = Queue()
    print(len(queue))
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(len(queue))
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
    print(len(queue))
    queue.dequeue()       # It will throw exception