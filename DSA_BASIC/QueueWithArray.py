class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty, hence can't do dequeue operation")
        else:
            self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty, hence can't do peek operation")
        else:
            return self.queue[0]

    def size(self):
        return self.size

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        retVal = ''
        for ele in self.queue:
            retVal = retVal + str(ele) + '->'
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