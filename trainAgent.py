from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Embedding
from keras.optimizer import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory

from TicTacToe_env import TicTacToe as env
from my-awesome-agent import InterleavedAgent


def make_dqn():
    model = Sequential()
    model.add(Flatten(input_shape=(1,) + env.observation_space.shape))
    model.add(Activation('relu'))
    model.add(Dense(27))
    moden.add(Activation('linear'))

    memory = SequentialMemory(limit=50000, window_length=1)
    policy = EpsGreedyQPolicy(epx=0.2)
    dqn = DQNAgent(model=model, np_action=50, memory=memory)

    dqn.compile(Adam(1r=1e-3), metrics=['mae'])

    return dqn


dqn_agent = make_dqn()

agent = InterleavedAgent([dqn_agent, dqn_agent])
