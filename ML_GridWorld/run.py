#!/usr/bin/python3

#
# Manager fuer Reinforcement-Examples Gridworld
#
#  direkt ./run.py aufrufen
#
# tas 02.11.2018, 9.11.2020
#

import environment11_17 as environment
# import environment4_4 as environment
# import agent                                       # in work
# import agent_first_visit_mc_estimating_v as agent  # in work
# import agent_tabular_td0_estimating_v as agent     # in work
import agent_q_learning as agent

import evaluation
import logging

# logging.basicConfig(format='%(lstateinfosevelname)-8s [%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', level=logging.WARNING)

env = environment.Environment()
agent = agent.Agent(env.get_action_space())
evaluation = evaluation.Evaluation(agent, env)    # liest nur aus den Objekten

count_episode_done = 0
for i_episode in range(1000):
    state, reward = env.reset('fix')  # random or fix
    agent.reset()

    for t in range(60):   #60):    # Achtung: sehr kritischer Parameter -> ca. 2 * laengster Weg
        action = agent.step(state, reward)
        state, reward, done, info = env.step(action)

        if done:
            agent.done(state, reward)

            # jetzt noch etwas Statistik und Darstellung:
            count_episode_done += 1
            print("----- Episode done", i_episode, "success count:", count_episode_done, "  finished after", t+1,  " timesteps")
            if i_episode % 500 == 0:
                evaluation.render()
            break

    print("Episode", i_episode, "finished after", t+1,  " timesteps")

evaluation.render()
env.close()
in1 = input("Script wird mit bel. Eingabe beendet !!!!!!!!!! ")
