'''
problemsearch - Functions for seaarching.
'''

from basicsearch_lib02.searchrep import (Node, print_nodes)
from basicsearch_lib02.queues import PriorityQueue
from basicsearch_lib02.timer import Timer
from basicsearch_lib02.tileboard import TileBoard
from explored import Explored
from searchstrategies import BreadthFirst, DepthFirst, Manhattan
       
def graph_search(problem, verbose=False, debug=False):
    """graph_search(problem, verbose, debug) - Given a problem representation
    (instance of basicsearch_lib02.representation.Problem or derived class),
    attempt to solve the problem.
    
    If debug is True, debugging information will be displayed.
    
    if verbose is True, the following information will be displayed:
        
        Number of moves to solution
        List of moves and resulting puzzle states
        Example:

         # TODO BEWARE: [Y,X], Y is flipped.

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


    while:
    node
    for each action of node:

    """
    initial_state = problem.initial_state
    set_explored = Explored()
    queue_nodes = PriorityQueue()
    queue_nodes.f = lambda child_node: BreadthFirst.g(child_node) + BreadthFirst.h(child_node)
    queue_nodes.append(item=Node(problem=problem, state=initial_state, parent=None, action=None))

    while True:
        # check if queue is empty
        if len(queue_nodes) == 0:
            # failure to find a solution.
            return False
        # current node
        current_node = queue_nodes.pop()
        if verbose:
            print(current_node.state)
        # add node state to explored.
        set_explored.add(current_node.state)
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
                    if verbose:
                        print("child = ")
                        print(child)
                    return child
