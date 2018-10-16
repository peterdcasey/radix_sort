"""
    Basic queue class implemented in a list
    Insert at position zero, remove from end of list
"""
# Completed implementation of a queue ADT
class Queue:
    def __init__(self):
        self.items = []
        self.next = -1
        self.count = 0

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.count += 1
        self.items.append(item)

    def dequeue(self):
        self.count -= 1
        self.next += 1
        return self.items[self.next]

    def size(self):
        return self.count

    def clear(self):
        self.items = []
        self.next = -1
        self.count = 0

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(3)
    q.enqueue(7)
    print('size', q.size())
    print('front', q.dequeue())
    print('front', q.dequeue())
    print('size', q.size())
    q.clear()
    print('size', q.size())

