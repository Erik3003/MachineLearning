import agent_q_learning as agent
import gym
import logging
import numpy as np

logging.basicConfig(format='%(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', level=logging.WARNING)


env = gym.make("Acrobot-v1")
low = env.observation_space.low
high = env.observation_space.high
print(low)
print(high)
agent = agent.Agent(env.action_space.n)
clustering_multiplier = [5, 5, 5, 5, 4, 4]

count_episode_done = 0
reward = -1
for i_episode in range(10000):
    state = tuple(np.asarray((env.reset() + high) * clustering_multiplier).astype(int))
    agent.reset()

    for steps in range(300):
        action = agent.step(state, reward)
        state, reward, done, info = env.step(action)
        state = tuple(np.asarray((state + high) * clustering_multiplier).astype(int))
        if i_episode % 100 == 0:
            env.render()

        if done:
            agent.done(state, reward)
            count_episode_done += 1
            print("----- Episode done", i_episode, " in ", steps, " steps")
            break

    print("Episode", i_episode, "finished, success count:", count_episode_done)

env.close()
