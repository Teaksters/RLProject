import random
import numpy as np

class EpsilonGreedyPolicy(object):
    """
    A simple epsilon greedy policy.
    """
    def __init__(self, Q, epsilon, nA, s_2_idx=None):
        self.Q = Q
        self.epsilon = epsilon
        self.nA = nA
        self.s_2_idx = s_2_idx

    def sample_action(self, obs):
        """
        This method takes a state as input and returns an action sampled from this policy.

        Args:
            obs: current state

        Returns:
            An action (int).
        """
        x = random.random()
        if x > self.epsilon:
            if self.s_2_idx == None:
                action = np.argmax(self.Q[obs])
            else:
                action = np.argmax(self.Q[self.s_2_idx[obs]])
        else: action = random.randint(0, self.nA - 1)

        return action
