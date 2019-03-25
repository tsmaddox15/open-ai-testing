import gym
import Output
import sys


class Tee(object):
    def __init__(self, *files):
        self.files = files

    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()  # If you want the output to be visible immediately

    def flush(self):
        for f in self.files:
            f.flush()


env = gym.make('CartPole-v0')
for i_episode in range(200):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            break
env.close()
# Tee = Output.Tee()
f = open('out.txt', 'w')
original = sys.stdout
sys.stdout = Tee(sys.stdout, f)
print(sys.stdout)  # This will go to stdout and the file out.txt

# use the original
sys.stdout = original
print("This won't appear on file")  # Only on stdout
f.close()
