'''
Created on Feb 8, 2018

@author: mroch
'''


class Explored(object):
    "Maintain an explored set.  Assumes that states are hashable."

    def __init__(self):
        "__init__() - Create an empty explored set."
        self.hash_table = set()

    def exists(self, state):
        """
        exists(state) - Has this state already been explored?
        :param state:  Hashable problem state
        :return: True if already seen, False otherwise.
        """
        return hash(state) in self.hash_table

    def add(self, state):
        """
        add(state) - Add a given state to the explored set
        :param state:  A problem state that is hashable, e.g. a tuple
        :return: None
        """
        self.hash_table.add(hash(state))
        return None
