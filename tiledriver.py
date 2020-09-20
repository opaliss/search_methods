"""
We the undersigned promise that we have in good faith attempted
to follow the principles of pair programming. Although we were free to discuss
ideas with others, the implementation is our own. We have shared a common workspace and
taken turns at the keyboard for the majority of the work that we are submitting.
Furthermore, any non programming portions of the assignment were done independently.
We recognize that should this not be the case,
we will be subject to penalties as outlined in the course syllabus.

Pair Programmer #1: Opal Issan, 09/15/2020
Pair Programmer #2: Mario Inzunza, 09/15/2020

driver for graph search problem

"""

from statistics import (mean, stdev)  # Only available in Python 3.4 and newer
import math
from npuzzle import NPuzzle
import random
from tileboard import TileBoard
from basicsearch_lib02.timer import Timer
from searchstrategies import (BreadthFirst, DepthFirst, Manhattan)
from problemsearch import graph_search
from basicsearch_lib02.searchrep import *
import collections


def driver(n, force_state=False):
    """
    # TODO OPAL:
                * newtonraphson.py. - DONE.
                * Double check g,h BFS, DFS, A*. + TEST. -DONE.

    # TODO TOGETHER: STEP 2.
                * problemsearch.py
                * npuzzle.py

    # TODO MARIO:
                * step 3 - not yet ready.. tbd.
                * outline step 2.
                * step 1.

    step 1: create 31 puzzles. for now: create 1.
        input :
            * n - where sqrt(n) = int. - create a function to make sure this holds. -DONE
            * what is the range of n?
            * get 31 n values from random generator.
            * check if board is solvable. TileBoard.solvable() -DONE

    step 2: solve the puzzle using BFS. Later on: DFS, A*.
            * TODO: EDIT THE MOST IMPORTANT FILE: graph_search.
            * verbose: make our lives better. print the current state in a human readable way.
            * time the calculation.
            * record the length/ depth.
            * record the number of nodes expanded.
            * return the tuple of graph_search and save it for step 3.

    step 3: save solutions in log.txt file. (Mario)
            Solution includes:
            * length of plan (DEPTH.)
            * number of nodes expanded (number of states explored?)
            * time running.


    # TODO: QUESTIONS FOR PROFESSOR ROCH:
    1. Is n = 16 always?
    2. Can you explain the comments in graph_search? why are there repeated numbers?
     do we need to account for this?
    3. Is there a range for n? if so, what is it?
    4. What is the empty space and period in graph_search comments?
    5. Is coordinate system in graph_search comments correct?

    # TODO: COMMENTS TO SELF:
    1. force_state is great for debugging.
    2. Beware of the coordinate system used in graph_search.

    # TODO: TESTING:
    1. first, test for n = 4.
    2. When implementing always add debug param and verbose to print behind the scenes.
    """

    # Generate 31 puzzles with 4, 9, or 16 squares
    games = []
    for _ in range(n):
        board_height = random.randint(2, 4)
        game_size = board_height ** 2 - 1
        if check_valid_n(game_size):
            problem = NPuzzle(n=game_size)
            if problem.solvable:
                print(problem)
                print("Is the state solved?", problem.goal_test(problem.initial_state))
                games.append(TileBoard(game_size))
                graph_search(problem=problem, debug=True, verbose=True)
            else:
                print("initial state is unsolvable. ")
        else:
            print("n is not valid.")


def check_valid_n(n):
    if math.sqrt(n+1).is_integer():
        return True
    else:
        return False


if __name__ == "__main__":
    driver(n=1)
