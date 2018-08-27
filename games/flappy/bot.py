import numpy as np


class Bot():
  def __init__(self):
    self.lr = 0.8
    self.discount = 0.9
    self.qtable = self.load_qtable()
    self.gameDump = 20

    #how many time launch bot to play game
    self.train_games = 5000

    #exploration parameters
    self.exp_min = -3
    self.exp_max = 3
    self.exp_interval = (self.exp_max - self.exp_min) / self.train_games
    self.sigmoid = lambda x: 1/(1+np.exp(-x))

  @staticmethod
  def init_qtable():
    pass

  def load_qtable(self):
    pass

  def dump_qtable(self):
    pass

  def act(self):
    pass

  def update(self):
    pass

  def map(self, x_dif, y_dif):
    pass

