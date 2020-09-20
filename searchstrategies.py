"""
searchstrategies

Module to provide implementations of g and h for various search strategies.
In each case, the functions are class methods as we don't need an instance
of the class.  

If you are unfamiliar with Python class methods, Python uses a function
decorator (indicated by an @ to indicate that the next method is a class
method).  Example:

class SomeClass:
    @classmethod
    def foobar(cls, arg1, arg2):
        "foobar(arg1, arg2) - does ..."
        
        code... class variables are accessed as cls.var (if needed)
        return computed value

A caller would import SomeClass and then call, e.g. :  
    SomeClass.foobar("hola","amigos")

Contains g and h functions for:
BreadFirst - breadth first search
DepthFirst - depth first search
Manhattan - city block heuristic search.  To restrict the complexity of
    this, you only need handle heuristics for puzzles with a single solution
    where the blank is in the bottom right, e.g.:
        123
        456
        78
    When multiple solutions are allowed, the heuristic becomes a little more
    complex as the city block distance must be estimated to each possible solution
    state. 
"""

import math
from basicsearch_lib02.queues import PriorityQueue
from basicsearch_lib02.searchrep import Node


class BreadthFirst:
    """BreadthFirst - breadth first searcH
    ∀𝑛 𝑔′(𝑛) = depth(n) and h′(n)=k (k=0)"""

    @classmethod
    def g(cls, childnode):
        """"g - cost from initial state to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
        return childnode.depth


    @classmethod
    def h(cls, searchnode):
        """h - heuristic value"""
        return 0


class DepthFirst:
    """DepthFirst - depth first search
    ∀𝑛 𝑔′(𝑛) = k and h′(n)=−depth(n) (k=0)"""

    @classmethod
    def g(cls, parentnode):
        """"g - cost from initial state to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
        return -(BreadthFirst.g(parentnode))

    @classmethod
    def h(cls, searchnode):
        """h - heuristic value"""
        return 0


class Manhattan:
    """Manhattan - A* heuristic with manhattan distance, and a cost of 2. """

    @classmethod
    def g(cls, parentnode):
        """"g - cost from initial state to childnode
        constrained such that the last edge of the search space
        moves from parentnode to childnode via the specified action
        """
        return BreadthFirst.g(parentnode)

    @classmethod
    def h(cls, child_state):
        """h - heuristic value. Manhattan distance. The sum of distance of each tile from
        it's goal position.
        # TODO: make sure searchnode.state is a tuple/list. ex: [2,1,3,6,4,5,7,.,8]
        # TODO: Here I assume searchnode is an object of Node class. """
        diff = 0
        for ii in range(0, len(child_state.state)):
            if child_state.state[ii] != '.':
                """ find the manhattan distance to the correct location. """
                N = len(child_state.state)
                N_side = math.sqrt(N)
                x_true = child_state.state[ii] % N_side
                y_true = math.floor(((child_state.state[ii] - 1) / N_side)) + 1
                x_curr = (ii+1) % N_side
                y_curr = math.floor((ii/N_side)) + 1

                if x_true == 0:
                    x_true = N_side
                if x_curr == 0:
                    x_curr = N_side

                diff += abs(x_true - x_curr) + abs(y_true - y_curr)
        return diff