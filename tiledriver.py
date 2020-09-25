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

driver for graph search problem.
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


def driver(n=8, force_state=False, repeat=1, verbose=False, log_file=True, print_res=False):
    """
    step 3: save solutions in log.txt file. (Mario)
            Solution includes:
            * length of plan (DEPTH.)
            * number of nodes expanded (number of states explored?)
            * time running.

    :param print_res: If set to True, print overall stats from run.
    :param log_file: If set to True, results will be printed in log.txt.
    :param verbose: print results to screen. Default is False.
    :param repeat: integer number that indicates the number of random N-puzzles generated.
    :param force_state: If set True the problem will be solved using an initial state. Default is false.
    :param n: number of tiles in the n-puzzle. Default is 8.
    """

    # a puzzle and solve it using 3 search methods.
    search_algorithm_list = ["BFS", "DFS", "A*"]

    # list of N-puzzles generated
    games = []

    for _ in range(repeat):

        # check if input n is valid.
        if check_valid_n(n):

            if force_state:
                # generate the N-puzzle using a known initial state.
                problem = NPuzzle(n=n, force_state=force_state)
            else:
                problem = NPuzzle(n=n)

            if problem.solvable:
                # is the problem solvable? print to screen.
                if print_res:
                    print("\nIs the state solved?", problem.goal_test(problem.initial_state))

                # if the problem is solvable then append the problem to list.
                games.append(TileBoard(n))

                for ii in range(len(search_algorithm_list)):

                    # solve the same problem using BFS, DFS, and A*.
                    search_method = search_algorithm_list[ii]

                    # set the g and h functions in N-Puzzle.
                    if search_method == "BFS":
                        problem.g = lambda parent, action, node: BreadthFirst.g(parent=parent)
                        problem.h = lambda node: BreadthFirst.h(searchnode=node)
                    if search_method == "DFS":
                        problem.g = lambda parent, action, node: DepthFirst.g(parent=parent)
                        problem.h = lambda node: DepthFirst.h(searchnode=node)
                    if search_method == "A*":
                        problem.g = lambda parent, action, node: Manhattan.g(parent=parent)
                        problem.h = lambda node: Manhattan.h(node=node)

                    # call the search algorithm.
                    path, ii, time = graph_search(problem=problem, debug=False, verbose=verbose)

                    if print_res:
                        # print the type of search method.
                        print(search_method)
                        print("\nSolution in %s moves" % str(len(path)))
                        print("Number of nodes expanded = ", ii)
                        print("Computation time: %s (sec)\n" % time)
            else:
                print("Initial state is unsolvable. ")
        else:
            print("n is not valid.")


def check_valid_n(n):
    if math.sqrt(n+1).is_integer():
        return True
    else:
        return False


if __name__ == "__main__":
    driver(n=8, repeat=1, force_state=False, verbose=False, log_file=False, print_res=True)
