import gym
from gym import spaces
import numpy as np

class CustomEnv(gym.Env):

  metadata = {'render.modes': ['human']}
  N_DISCRETE_ACTIONS = 2
  def __init__(self):
    # called at the beginning to set up the env
    super(CustomEnv, self).__init__()
    # action space is two variables:
    # agent can provide left/right acceleration 
    # and turning velocity
    self.action_space = spaces.Box(low=-1, high=1, shape=(2))
    # observation space atm is two variables:
    # agent can see the x, y displacement of the 
    # ball relative to the racket
    self.observation_space = spaces.Box(low=-1, high=1, shape=(2), dtype=np.uint8)

  def step(self, action):
    # Execute one time step within the environment
    pass
  def reset(self):
    # Reset the state of the environment to an initial state
    pass
  def render(self, mode='human', close=False):
    # Render the environment to the screen
    pass
