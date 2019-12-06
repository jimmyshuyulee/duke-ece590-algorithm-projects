"""
Math 590
Project 2
Fall 2019

p2queue.py

Partner 1: Fang Feng
Partner 2: Shu Yu Lee
Date: 11/04/2019
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 100.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        print(self.queue)
        print('Front: %d' % self.front)
        print('Rear: %d' % self.rear)
        return ('numElems: %d' % self.numElems)

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        # If front and rear point to the same element, the queue is either
        # empty or full. We can make sure the queue is full by checking that 
        # the pointed element is not None
        return self.front == self.rear and self.queue[self.rear] is not None

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        # If front and rear point to the same element, the queue is either
        # empty or full. We can make sure the queue is empty by checking that 
        # the pointed element is None
        return self.front == self.rear and self.queue[self.rear] is None

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        new_queue = [None for x in range(0, self.numElems * 2)]
        new_queue[: self.numElems - self.front] = self.queue[self.front:]
        new_queue[self.numElems - self.front: self.numElems] = self.queue[: self.front]
        self.queue = new_queue
        self.first = 0
        self.rear = self.numElems
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        if val is None:
            return
        if self.isFull():
            self.resize()
        self.queue[self.rear] = val
        # if rear is currently at the end of the list, set it to 0
        if self.rear == len(self.queue) -1:
            self.rear = 0
        else:
            self.rear += 1
        self.numElems += 1
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        if self.isEmpty():
            return
        res = self.queue[self.front]
        self.queue[self.front] = None
        # if front is currently at the end of the list, set it to 0
        if self.front == len(self.queue) - 1:
            self.front = 0
        else:
            self.front += 1
        self.numElems -= 1
        return res


def test():
    stack = Queue(3)
    print(stack.isEmpty())
    stack.push(1)
    print(stack)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    stack.push(9)
    print(stack.pop())
    print(stack)


if __name__ == '__main__':
    test()
