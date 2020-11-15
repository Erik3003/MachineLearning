#!/usr/bin/python3

 # state ist der Index unter dem dieses Element
 # in das dictionary abgespeichert wird
 #

import logging
import random

class StateInfo:

    def __init__(self, action_count):
        logging.debug("__init__()")
        self.action_count = action_count
        self.statevalue = 0     # V, wird nicht in allen Alogrithemn verwendet
        self.actionvalues = [0 for x in range(action_count)]
        # wird nur bei Mittelungen benoetigt (z.B.: MC):
        self.actioncounts =  [0 for x in range(action_count)]

    def get_max_actionvalue(self):
        maxval = max(self.actionvalues)
        return maxval

    def policy_random(self):
        action = random.randrange(self.action_count)
        return action

    def policy_greedy_q_based(self):
        action = self.actionvalues.index(max(self.actionvalues))
        logging.debug("policy_greedy_q_based(): %d", action)
        return action

    def policy_epsilon_greedy_q_based(self, epsilon):
        # Achtung: darf natuerlich nur verwendet werden, wenn die
        # actionvalue Werte auch gesetzt werden, epsilon = 1 bedeutet
        # nicht, dass ein random Wert geliefert wird 
        x = random.random()  # 0 - 1
        greedyaction =  self.policy_greedy_q_based()
        if x < epsilon:
            action = greedyaction
            while action == greedyaction:
                action = random.randrange(self.action_count)
        else:
            action = greedyaction
        logging.debug("policy_epsilon_greedy_q_based(%d): %d", epsilon, action)
        return action

    def set_testvalues(self):
        logging.debug("set_testvalues()")
        self.statevalue = 0     # Statevalue
        self.actioncounts = [1, 3, 1, 2]
        self.actionvalues = [2, 5, 1, 2]
        self.policy = 2
