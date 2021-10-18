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

    def sample_action(self, obs, dq=False):
        """
        This method takes a state as input and returns an action sampled from this policy.

        Args:
            obs: current state

        Returns:
            An action (int).
        """
        if dq == False:
            x = random.random()
            if x > self.epsilon:
                if self.s_2_idx == None:
                    action = np.argmax(self.Q[obs])
                else:
                    action = np.argmax(self.Q[self.s_2_idx[obs]])
            else: action = random.randint(0, self.nA - 1)
            return action

        if dq == True:
            if self.s_2_idx == None:
                action_value = self.Q[obs]
            else:
                action_value = self.Q[self.s_2_idx[obs]]
            return action_value
