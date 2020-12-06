import agent_q_learning as agent
import logging

logging.basicConfig(format='%(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', level=logging.WARNING)


count_episode_done = 0
reward = 0
for i_episode in range(10000):
    state = tuple(env.reset())
    agent.reset()

    for steps in range(50):
        action = agent.step(state, reward)
        state, reward, done, info = env.step(action)
        state = tuple(state)
        if i_episode % 100 == 0:
            env.render()

        if done:
            agent.done(state, reward)
            count_episode_done += 1
            print("----- Episode done", i_episode, "success count:", count_episode_done, "  finished")
            break

    print("Episode", i_episode, "finished")

env.close()
