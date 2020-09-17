from basicsearch_lib02.tileboard import TileBoard
from basicsearch_lib02.searchrep import Problem
import math


class NPuzzle(Problem):
    """
    NPuzzle - Problem representation for an N-tile puzzle
    Provides implementations for Problem actions specific to N tile puzzles.
    """

    def __init__(self, n, force_state=None, **kwargs):
        """"__init__(n, force_state, **kwargs)
        
        NPuzzle constructor.  Creates an initial TileBoard of size n.
        If force_state is not None, the puzzle is initialized to the
        specified state instead of being generated randomly.
        
        The parent's class constructor is then called with the TileBoard
        instance any remaining arguments captured in **kwargs.

        # Note on **kwargs:
        # **kwargs is Python construct that captures any remaining arguments
        # into a dictionary.  The dictionary can be accessed like any other
        # dictionary, e.g. kwargs[“keyname”], or passed to another function
        # as if each entry was a keyword argument:
        #    e.g. foobar(arg1, arg2, …, argn, **kwargs).
        """
        self.n_side = int(math.sqrt((n + 1)))
        self.initial_state = TileBoard(n=n)
        self.solvable = self.initial_state.solvable

    def actions(self, state):
        "actions(state) - find a set of actions applicable to specified state"
        return state.get_actions()

    def result(self, state, action):
        "result(state, action)- apply action to state and return new state"
        return state.move(offset=action)

    def goal_test(self, state):
        "goal_test(state) - Is state a goal?"
        return state.solved()

    def __str__(self):
        state = self.initial_state.state_tuple()
        string = str(state[: self.n_side])
        for ii in range(1, self.n_side):
            string += "\n"
            string += str(state[ii * self.n_side: (ii + 1) * self.n_side])
        return string
