"""
    Basic queue class implemented in a list
    Insert at position zero, remove from end of list
"""
# Completed implementation of a queue ADT
class Queue:
    """
    List implementation of queue
    """
    def __init__(self):
        self.items = []
        self.next = -1      # pointer one behind next item to retrieve
        self.count = 0

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """
        Enqueue items at the end of the list
        :param item:
        :return:
        """
        self.count += 1
        self.items.append(item)

    def dequeue(self):
        """
        Dequeue items from lst[next], index moves +1 through
          this list leaving wasted space behind
        :return:
        """
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
    q.enqueue(5)
    q.enqueue(7)
    print('size', q.size())
    print('front', q.dequeue())
    print('front', q.dequeue())
    print('size', q.size())
    q.clear()
    print('size', q.size())

