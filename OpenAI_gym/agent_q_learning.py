#!/usr/bin/python3

#
# agent
#
# Q Learning   (nach Sutton Aufl.1 S. 149)
#
#
# tas 22.11.2019
#
#
# Doku:
#
#
from array import array

import numpy as np
import logging
import strucstep
import random
import stateinfo


class Agent:

    # Konstruktor
    def __init__(self, action_count):
        #logging.debug("init() ")
        self.action_count = action_count
        # 4_4 gridworld, start fix o. random: 100 Episoden, laenge: 60
        # gamma: 0.99-0.7, alpha: 0.5, epsilon 0.2 sehr gut
        # 17_11 gridworld, start fix o. random: 3000 Episoden, laenge: 60
        # gamma: 0.99-0.7, alpha: 0.5, epsilon 0.2 sehr gut
        self.discountrate = 0.99  # gamma
        self.alpha = 0.6# alpha
        self.epsilon = 0.02# fuer epsilon greedy policy (epsilon = Anteil random)
        self.stateinfos = {}
        self.oldstate = -1
        self.oldaction = -1

    def reset(self):
        #logging.debug("reset() ")
        self.episode = []
        self.firststep = True
        return

    def step(self, state, reward):
        state = tuple(np.array(state, dtype=np.uint8))
        #logging.debug("step(): state: %d, reward: %d", state, reward)
        # stateinfo dictionary pflegen
        if bool(self.stateinfos.get((state))):
            # print("state bekannt") # state schon bekannt ?
            si = self.stateinfos[state]  # ja
        else:
            si = stateinfo.StateInfo(self.action_count)  # Eintrag neu anlegen
            self.stateinfos[state] = si

        # oldstate, oldaction anlegen
        if self.firststep:
            self.firststep = False
            self.oldstate = state
            action = si.policy_random()
            self.oldaction = action
            return action

        # jetzt kann es losgehen
        old_si = self.stateinfos[self.oldstate]
        old_q_sa = old_si.actionvalues[self.oldaction]
        max_q_sa = si.get_max_actionvalue()

        old_q_sa = old_q_sa + self.alpha * (reward + self.discountrate * max_q_sa - old_q_sa)
        old_si.actionvalues[self.oldaction] = old_q_sa

        # naechste Action
        action = si.policy_epsilon_greedy_q_based(self.epsilon)

        self.oldstate = state
        self.oldaction = action

        # nur zum Zeichnen in environment.render()
        triple = strucstep.StrucStep(state, reward, action)
        self.episode.append(triple)

        #logging.debug("step(): return action: %d ", action)
        return action

    def done(self, state, reward):
        # eine Episode ist beendet
        # logging.warning("done(): state: %d, reward: %d", state, reward)
        #print("Log : Done()")
        self.step(state, reward)

        return

    def close(self):
        logging.debug("close() ")
