"""
Math 590
Project 2
Fall 2019

p2stack.py

Partner 1: Fang Feng
Partner 2: Shu Yu Lee
Date: 11/04/2019
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 100.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=100):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        print(self.stack)
        print('Top: %d' % self.top)
        return ('numElems: %d' % self.numElems)

    """
    isFull function to check if the stack is full.
    """

    def isFull(self):
        return self.stack[-1] is not None


    """
    isEmpty function to check if the stack is empty.
    """
    def isEmpty(self):
        return self.numElems == 0

    """
    resize function to resize the stack by doubling its size.
    """
    def resize(self):
        new_stack = [None for x in range(0, self.numElems * 2)]
        new_stack[:self.numElems] = self.stack
        self.stack = new_stack
        return

    """
    push function to push a value onto the stack.
    """
    def push(self, val):
        if not val:
            return
        if self.isFull():
            self.resize()
        self.top += 1
        self.stack[self.top] = val
        self.numElems += 1


    """
    pop function to pop the value off the top of the stack.
    """
    def pop(self):
        if self.isEmpty():
            return None
        res = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        self.numElems -= 1
        return res


def test():
    stack = Stack(3)
    print(stack.isEmpty())
    stack.push(9)
    stack.push(3)
    print(stack.stack)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    stack.push(9)
    print(stack.pop())
    print(stack.stack)


if __name__ == '__main__':
    test()
