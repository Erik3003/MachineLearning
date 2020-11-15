#!/usr/bin/python3

#
# Unit-Tests fuer Gridworld
#
# direkt ./unit_test.py aufrufen
#
# tas 23.10.19
#

import environment
import agent
import logging
import sys
import stateinfo

logging.basicConfig(format='%(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
# oder z.B.:  .WARNING

env = environment.Environment()
agent = agent.Agent(env.action_count)

# -------------------------------------------------------------
# Hilfs-Routinen der untersten Ebenen in environment
# -------------------------------------------------
s =  env.coord2state(0, 3)
if  s != 3:
    logging.error("env.coord2state(): s = %d", s)
    sys.exit(0)

s =  env.coord2state(2, 1)
if  s != 35:
    logging.error("env.coord2state(): s = %d", s)
    sys.exit(0)

y, x = env.state2coord(5)
if  (y != 0) or (x != 5):
    logging.error("env.state2coord(): y = %d x = %d", y, x)
    sys.exit(0)

y, x = env.state2coord(17+4)
if  (y != 1) or (x != 4):
    logging.error("env.state2coord(): Y = %d x = %d", y, x)
    sys.exit(0)

s = env.perform_action(17+3, 0) #nach rechts
print(s)
if  s != 17+4:
     logging.error("env.perform_action(): s = %d", s)
     sys.exit(0)

s = env.perform_action(1, 1) #nach unten
print(s)
if  s != 1+17:
     logging.error("env.perform_action(): s = %d", s)
     sys.exit(0)

s = env.perform_action(17+3, 2) #nach links
if  s != 17+2:
    logging.error("env.perform_action(): s = %d", s)
    sys.exit(0)

s = env.perform_action(17+3, 3) #nach oben
if  s != 3:
     logging.error("env.perform_action(): s = %d", s)
     sys.exit(0)

s = env.perform_action(2*17+1, 0) #nach rechts in ein Hindernis
if  s != 2*17+1:    #no change
     logging.error("env.perform_action(): s = %d", s)
     sys.exit(0)

s = env.perform_action(2*17+0, 2) #nach links aus der gridworld
if  s != 2*17+0:    #no change
     logging.error("env.perform_action(): s = %d", s)
     sys.exit(0)

for i in range(0, 500):
    s = env.get_random_state()
    # print(s, end=' | ')
    y, x = env.state2coord(s)
    if env.gridworld[y, x] == 1:  # Hindernis ?
        logging.error("env.get_random_state(): y = %d  x = %d", y, x)
        sys.exit(0)

 # -------------------------------------------------------------
 # stateinfo.py
 # -------------------------------------------------

si = stateinfo.StateInfo(4)
si.set_testvalues()

#si.cal_actionvalue(1, 5)
#if  (si.actioncount[1] != 4) or (si.actionvalue[1] != 5):
#     logging.error("si.cal_actionvalue()")
#     sys.exit(0)

#si.cal_actionvalue(1, 30)
#if  (si.actioncount[1] != 5) or (si.actionvalue[1] != 10):
#     logging.error("si.cal_actionvalue()")
#     sys.exit(0)sys.exit(0

action = si.policy_greedy_q_based()
if action != 1:
    logging.error("policy_greedy_q_based()")
    sys.exit(0)

action = si.policy_epsilon_greedy_q_based(0)
if action != 1:
    logging.error("policy_epsilon_greedy_q_based() 1")
    sys.exit(0)

action = si.policy_epsilon_greedy_q_based(1)
if action == 1:
    logging.error("policy_epsilon_greedy_q_based() 2")
    sys.exit(0)

count = [0,0,0,0]
for i in range(1,1000):
    action = si.policy_epsilon_greedy_q_based(0.2)
    count[action] = count[action] + 1
if not( count[1] in range(700, 900)):
    logging.error("policy_epsilon_greedy_q_based() 3")
    print(count)
    sys.exit(0)

maxval = si.get_max_actionvalue()
if maxval != 5:
    logging.error("get_max_actionvalue()")
    sys.exit(0)

sys.exit(0)

 # -------------------------------------------------------------
 # Routinen der obersten Ebene in environment
 # -------------------------------------------------

env.state = 4 # links neben Ziel
s, reward, done, infos = env.step(0) # nach rechts in Ziel
if s != 5:
    logging.error("env.step(): wrong state s = %d  reward = %d  done = %d  infos = %s", s,  reward, done, infos )
    sys.exit(0)
if reward != 1:
    logging.error("env.step(): wrong reward s = %d  reward = %d  done = %d  infos = %s", s,  reward, done, infos )
    sys.exit(0)
if done != True:
    logging.error("env.step(): wrong done s = %d  reward = %d  done = %d  infos = %s", s,  reward, done, infos )
    sys.exit(0)

env.state = 2*17+1 # links neben Hindernis
s, reward, done, infos = env.step(2) # nach links (also ok)
if s != 2*17+0:
    logging.error("env.step(): wrong state s = %d  reward = %d  done = %d  infos = %s", s,  reward, done, infos )
    sys.exit(0)
if reward != 0:
    logging.error("env.step(): wrong reward s = %d  reward = %d  done = %d  infos = %s", s,  reward, done, infos )
    sys.exit(0)
if done != False:
    logging.error("env.step(): wrong done s = %d  reward = %d  done = %d  infos = %s", s,  reward, done, infos )
    sys.exit(0)

env.state = 2*17+1 # links neben Hindernis
s, reward, done, infos = env.step(0) # nach rechts (ins Hindernis)
if s != 2*17+1:
    logging.error("env.step(): wrong state s = %d  reward = %d  done = %d  infos = %s", s,  reward, done, infos )
    sys.exit(0)
if reward != -10:
    logging.error("env.step(): wrong reward s = %d  reward = %d  done = %d  infos = %s", s,  reward, done, infos )
    sys.exit(0)
if done != False:
    logging.error("env.step(): wrong done s = %d  reward = %d  done = %d  infos = %s", s,  reward, done, infos )
    sys.exit(0)

print()
print ("!!!!!!!!! alle Unit Tests ok !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print()
