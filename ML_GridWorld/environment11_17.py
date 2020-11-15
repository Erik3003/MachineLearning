#!/usr/bin/python3

import scipy as sp
import numpy as np
import math as ma
import matplotlib.pylab as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import logging
import random
import copy

class Environment:

    # Konstruktor
    def __init__(self):
        logging.debug("init() ")

        # Gridworld aufbauen
        self.gw_x_count = 17
        self.gw_y_count = 11
        self.destinationPos = [0, 5]         # [y, x]
        self.gridworld = np.zeros((self.gw_y_count, self.gw_x_count))
        # Ziel eintragen
        self.gridworld[self.destinationPos[0], self.destinationPos[1]] = 2
        # Hindernisse aufbauen
        self.gridworld[3, 4:9] = 1
        self.gridworld[3, 10:13] = 1
        self.gridworld[2:9, 2] = 1
        print(self.gridworld)

        # Actions festlegen, richtet sich nach der Indizierung der gridworld
        #   und der Ausgabe via plt.matshow(self.gridworld)
        self.action_count = 4                # 0: right 1: down 2: left 3: up

        # States festlegen
        #   state ist der flat-Index der gridworld, Berechnung s. perform_ation()
        self.start_state = self.coord2state(self.gw_y_count-1,6)
        self.end_state = self.coord2state(self.destinationPos[0],self.destinationPos[1])
        self.state = self.start_state

        self.start_reward = -1  # dummy wert
        self.stepcount = 0

    def reset(self, mode):
        self.stepcount = 0

        if mode == 'random':
             self.start_state = self.get_random_state()

        if mode == 'fix':
              self.start_state = self.start_state

        self.state = self.start_state
        logging.debug("reset(): return: state: %d reward: %d ", self.state, self.start_reward)
        return self.state, self.start_reward

    def get_action_space(self):
        return self.action_count

    def step(self, action):
        logging.debug("step() ")

        reward = -1     # Standard
        done = False
        info = "nix"

        new_state = self.perform_action(self.state, action)

        if new_state == self.state:  # action lief auf Hindernis o. aus der gridworld
            reward =  -10  # -0.1

        if new_state == self.end_state:
            done = True
            reward = 0

        self.state = new_state

        self.stepcount = self.stepcount + 1
        logging.debug("step(): return: state: %d reward: %d done: %d", self.state, reward, done )

        return self.state, reward, done, info

    def close(self):
        logging.debug("close() ")

    def perform_action(self, s, a):
        # liefert bei ausfuehrbarer action a den neuen State
        #   oder den alten State, falls ausserhalb gridworld oder auf Hinderniss
        logging.debug("perform_action(state:%d, action:%d) ", s, a)

        valid = True

        y, x = self.state2coord(s)
        #Action ausführen
        if (a == 0):
            x = x+1
        if (a == 1):
            y = y+1
        if (a == 2):
            x = x-1
        if (a == 3):
            y = y-1
        # innerhalb der Gridworld ?
        if (x<0) or (x>=self.gw_x_count):
            valid = False
        if (y<0) or (y>=self.gw_y_count):
            valid = False
        # Hinderniss ?
        if valid and (self.gridworld[y, x]  == 1):
            valid = False

        if valid:
            s = self.coord2state(y, x)
            s_ret = s
        else:
            s_ret = s    # den alten Wert

        logging.debug("perform_action(): return: state: %d ", s_ret)

        return s_ret

    def state2coord(self, s):
        # wandelt states in gridworld Koordinaten. ohne Ueberpruefung auf Gueltigkeit
        y = ma.floor(s / self.gw_x_count)
        x = s % self.gw_x_count
        return y, x

    def coord2state(self, y, x):
        s = y * self.gw_x_count + x
        return s

    def get_random_state(self):
        # liefert einen zufaelligen, gueltigen state, z.B. fuer den Start
        # Hindernisse sind in der gridworld Matrix mit 1 belegt

        x = random.randrange(self.gw_x_count)
        y = random.randrange(self.gw_y_count)
        while self.gridworld[y,x] == 1:  # while Hindernis
            x = random.randrange(self.gw_x_count)
            y = random.randrange(self.gw_y_count)

        return self.coord2state(y, x)
