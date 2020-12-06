#!/usr/bin/python3

class StrucStep:
    # container fuer das Tripel s(t), r(t), und der sich ergebenden action a(t)
    #   eines steps, s. Abb. Sutton (Auflage 1##) S. 52

    def __init__(self, state, reward, action):
        self.state = state      # von environement im step t geliefert
        self.reward = reward    #          "            "
        self.action = action    # im agent im step t berechnet

    def getstate(self):
        return self.state

    def getreward(self):
        return self.reward

    def getaction(self):
        return self.action
