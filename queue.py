"""
    Basic queue class implemented in a list
    Insert at position zero, remove from end of list
"""
# Completed implementation of a queue ADT
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

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

