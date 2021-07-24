import gym
env = gym.make('Asteroids-v0')
favorites = [
    'Asteroids-v4',
    'FrozenLake8x8-v0',
]

env.reset()
for _ in range(100):
    env.render()
    env.step(env.action_space.sample()) # take a random action
env.close()