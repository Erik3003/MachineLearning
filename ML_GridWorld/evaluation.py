#!/usr/bin/python3

#
# Darstellung der Runs
#  greift nur lesend auf agent und environent Objekte zu
#
#
# tas 12.10.2020
#

import scipy as sp
import numpy as np
import math as ma
import matplotlib.pylab as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import logging
import random
import copy

class Evaluation:

    # Konstruktor
    def __init__(self, agent, environent):
        logging.debug("init() ")
        self.agent = agent
        self.environent = environent

    def render(self):
        logging.debug("render(): stepcount: %d", self.environent.stepcount)

        plt.close('all')

        # ----- state value function zeichnen

        sv = np.zeros((self.environent.gw_y_count, self.environent.gw_x_count))
        sum_sv = 0
        for e in self.agent.stateinfos:
            y, x = self.environent.state2coord(e)
            statevalue = self.agent.stateinfos[e].statevalue
            sum_sv = sum_sv + statevalue
            sv[y, x] = statevalue

        if sum_sv == 0:  # ist der StateValue im Agent-Algorithmus ueberhaupt berechnet worden ?
            for e in self.agent.stateinfos:   # stattdessen dem maximalen ActionValue nehmen
                y, x = self.environent.state2coord(e)
                statevalue = self.agent.stateinfos[e].get_max_actionvalue()
                sv[y, x] = statevalue

        xgrid = np.arange(self.environent.gw_x_count, 0,-1)
        ygrid = np.arange(0, self.environent.gw_y_count, 1)
        xmesh, ymesh = np.meshgrid(xgrid, ygrid)

        # schoen waere: plot_surface(Y, X, ..... ), das klappt leider nicht
        #, cmap=cm.coolwarm, linewidth=0, antialiased=False)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        plt.contourf(xmesh, ymesh, sv, 20, cmap='RdGy')
        ## todo: x-Achse in der Beschriftung invertieren
        ax.view_init(30, 90)
        if sum_sv == 0:
            plt.title('max action value function')
        else:
            plt.title('state value function')
        plt.ylabel('y')
        plt.xlabel('x')
        # ax = fig.add_subplot(212, projection='3d')
        # ax.plot_wireframe(X, Y, self.gridworld)

        plt.matshow(sv)
        if sum_sv == 0:
            plt.title('max action value function')
        else:
            plt.title('state value function')
        plt.ylabel('y')
        plt.xlabel('x')

        # ---- quiver plot

        xgrid = np.arange(-1, self.environent.gw_x_count+1, 1)
        yinvgrid = np.arange(self.environent.gw_y_count+1, -1, -1)
        ygrid = np.arange(-1, self.environent.gw_y_count+1, 1)
        u = np.zeros((self.environent.gw_y_count+2, self.environent.gw_x_count+2))
        v = np.zeros((self.environent.gw_y_count+2, self.environent.gw_x_count+2))

        # Test
        #print (xgrid)
        #print (yinvgrid)
        #print (u)
        #print(v)
        #u[0,5] = 1  # u[y, x]
        #v[0,5] = 0
        #u[4,5] = 0
        #v[4,5] = -1
        #u[6,5] = -1
        #v[6,5] = 0
        #u[10,5] = 0
        #v[10,5] = 1

        for e in self.agent.stateinfos:
            y, x = self.environent.state2coord(e)
            policy = self.agent.stateinfos[e].policy_greedy_q_based()
            if policy == 0:
                u[y+1,x+1] = 1
                v[y+1,x+1] = 0
            if policy == 1:
                u[y+1,x+1] = 0
                v[y+1,x+1] = -1
            if policy == 2:
                u[y+1,x+1] = -1
                v[y+1,x+1] = 0
            if policy == 3:
                u[y+1,x+1] = 0
                v[y+1,x+1] = 1

        fig, ax = plt.subplots()
        q = plt.quiver(xgrid, yinvgrid, u, v, pivot='mid', width=0.011,
               scale=3 / 0.15)
        plt.yticks(ygrid, yinvgrid)
        plt.title('policy')
        plt.ylabel('y')
        plt.xlabel('x')

        # den Weg der Episode einzeichnen
        gw = copy.copy(self.environent.gridworld)

        for e in self.agent.episode:
            s = e.getstate()
            y, x = self.environent.state2coord(s)
            gw[y, x] = 2
            # Sartstate kennzeichnen
            s =  self.agent.episode[0].getstate()
            y, x = self.environent.state2coord(s)
            gw[y, x] = 4
            # Endstate
            gw[self.environent.destinationPos[0], self.environent.destinationPos[1]] = 4

        # matshow macht sein eigenes (naechstes) Fenster auf:
        plt.matshow(gw)

        # und zum Schluss fuer alles:
        plt.draw()
        # plt.show()
        plt.pause(0.1)
