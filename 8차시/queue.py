class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self, queue) == 0:
            print("Queue is empty")
            return -1
        else:
            return self.queue.pop(0)
        
    def printQueue(self):
        print(self.queue)

if __name__=="__main__":
    queue_list = Queue()
    queue_list.enqueue(1)
    queue_list.enqueue(2)
    queue_list.printQueue()
    print(queue_list.dequeue())
    print(queue_list.dequeue())