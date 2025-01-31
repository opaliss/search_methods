'''
Queues: Stack, FIFOQueue, PriorityQueue
'''

import collections  # data containers
import bisect   # efficient sorted lists

class Queue:

    """Queue is an abstract class/interface. There are three types:
        Stack(): A Last In First Out Queue.
        FIFOQueue(): A First In First Out Queue.
        PriorityQueue(order, f): Queue in sorted order (default min-first).
    Each type supports the following methods and functions:
        q.append(item)  -- add an item to the queue
        q.extend(items) -- equivalent to: for item in items: q.append(item)
        q.pop()         -- return the top item from the queue
        len(q)          -- number of items in q (also q.__len())
        item in q       -- does q contain item?
    Note that isinstance(Stack(), Queue) is false, because we implement stacks
    as lists.  If Python ever gets interfaces, Queue will be an interface."""

    def __init__(self):
        raise NotImplementedError

    def extend(self, items):
        # append each item
        for item in items:
            self.append(item)


class PriorityQueue(Queue):

    """A queue in which the minimum (or maximum) element (as determined by f and
    order) is returned first. If order is min, the item with minimum f(x) is
    returned first; if order is max, then it is the item with maximum f(x).
    Also supports dict-like lookup."""

    def __init__(self, order=min, f=lambda x: x):
        """
        PriorityQueue
        :param order: Function used for ordering min/max
        :param f: Function applied to inserted nodes to determine f
        """
        self.A = []
        self.order = order
        self.f = f

    def append(self, item):
        """
        append(item)
        :param item:  Search state to add
        :return: None
        """
        bisect.insort(self.A, (self.f(item), item))

    def __len__(self):
        """
        len()
        :return: Number of items in queue
        """
        return len(self.A)

    def pop(self):
        """
        pop() - dequeue an item
        :return:  node with minimum or maximum f value depending on order
        """
        if self.order == min:
            return self.A.pop(0)[1]
        else:
            return self.A.pop()[1]

    def __contains__(self, item):
        # Implementation of in
        return any(item == pair[1] for pair in self.A)

    def __getitem__(self, key):
        # Support retrieval by indexing
        for _, item in self.A:
            if item == key:
                return item

    def __delitem__(self, key):
        # Support deletion by indexing, e.g. del queue[key]
        for i, (value, item) in enumerate(self.A):
            if item == key:
                self.A.pop(i)

