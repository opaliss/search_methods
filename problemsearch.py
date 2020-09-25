'''
problemsearch - Functions for seaarching.
'''

from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue
from basicsearch_lib02.timer import Timer
from basicsearch_lib02.tileboard import TileBoard
from explored import Explored
import math


def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.
    
    If debug is True, debugging information will be displayed.
    
    if verbose is True, the following information will be displayed:
        
        Number of moves to solution
        List of moves and resulting puzzle states
        Example:

            Solution in 25 moves        
            Initial state
                  0        1        2    
            0     4        8        7    
            1     5        .        2    
            2     3        6        1    
            Move 1 -  [0, -1]
                  0        1        2    
            0     4        8        7    
            1     .        5        2    
            2     3        6        1    
            Move 2 -  [1, 0]
                  0        1        2    
            0     4        8        7    
            1     3        5        2    
            2     .        6        1    
            
            ... more moves ...
            
                  0        1        2    
            0     1        3        5    
            1     4        2        .    
            2     6        7        8    
            Move 22 -  [-1, 0]
                  0        1        2    
            0     1        3        .    
            1     4        2        5    
            2     6        7        8    
            Move 23 -  [0, -1]
                  0        1        2    
            0     1        .        3    
            1     4        2        5    
            2     6        7        8    
            Move 24 -  [1, 0]
                  0        1        2    
            0     1        2        3    
            1     4        .        5    
            2     6        7        8    
        
        If no solution were found (not possible with the puzzles we
        are using), we would display:
        
            No solution found
    
    Returns a tuple (path, nodes_explored, elapsed_s) where:
    path - list of actions to solve the problem or None if no solution was found
    nodes_explored - Number of nodes explored (dequeued from frontier)
    elapsed_s is the elapsed wall clock time performing the search
    """
    timer = Timer()  # start the timer.
    initial_state = problem.initial_state
    set_explored = Explored()   # create a hashtable.
    queue_nodes = PriorityQueue()  # queue with frontier nodes.
    queue_nodes.append(item=Node(problem=problem, state=initial_state, parent=None, action=None))
    list_of_expanded_nodes = []
    path = None
    ii = 0  # number of nodes expanded.

    while True:
        ii += 1
        # check if queue is empty
        if len(queue_nodes) == 0:
            # failure to find a solution.
            return None
        # current node
        current_node = queue_nodes.pop()
        # add node state to explored.
        set_explored.add(current_node.state)
        # add current node to list.
        list_of_expanded_nodes.append(current_node.state)
        #  check for all valid moves:
        for action in TileBoard.get_actions(current_node.state):
            # action [y, x]
            child = current_node.state.move(offset=action)
            # if child is not explored then add to frontier.
            if set_explored.exists(child) is False:
                set_explored.add(child)
                # add to queue.
                added_to_queue = Node(problem=problem, state=child, parent=current_node, action=action)
                queue_nodes.append(item=added_to_queue)
                if problem.goal_test(child):
                    child_node = Node(problem=problem, state=child, parent=current_node, action=action)
                    path = Node.solution(child_node)
                    if verbose:
                        print("\nSolution in %s moves" % str(len(path)))
                        print("Number of nodes expanded = ", len(list_of_expanded_nodes))
                        print("Final depth = ", child_node.depth)
                        print("Computation time: %s (sec)\n" % timer.elapsed_s())
                        for ii in range(0, len(path)):
                            if ii == 0:
                                print("Initial state=")
                                print(initial_state)
                                print("\n")
                                next_node = initial_state
                            if ii == len(path) - 1:
                                print("Final child node=")
                            print("Action = ", path[ii])
                            next_node = next_node.move(offset=path[ii])
                            print(next_node)
                            print("\n")
                    return path, list_of_expanded_nodes, timer.elapsed_s()


