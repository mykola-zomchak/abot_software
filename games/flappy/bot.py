import numpy as np
import json

class Bot():
  # size of square for mapping
  x_size = 20
  y_size = 10

  def __init__(self):
    self.lr = 0.8
    self.discount = 0.9
    self.qtable = self.load_qtable()
    self.game_dump = 20
    self.games_count = self.load_games_count()

    #how many time launch bot to play game
    self.train_games = 5000

    #exploration parameters
    self.exp_min = -3
    self.exp_max = 3
    self.exp_interval = (self.exp_max - self.exp_min) / self.train_games
    self.sigmoid = lambda x: 1/(1+np.exp(-x))

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.dump_qtable()
    self.write_game_count()


  @staticmethod
  def init_qtable():
    # x є [-40, 440], step = self.x_size
    # y є [-120, 440], step = self.y_size
    qtable = {}
    for x in range(-40, 440, Bot.x_size):
      for y in range(-120, 440, Bot.y_size):
        qtable[str(x)+'_'+str(y)] = [0, 0]

    with open("qvalues.json", 'w') as f:
      json.dump(qtable, f)
      print("Q table dump!")

  def write_game_count(self):
    with open("games_count.txt", 'w') as f:
      f.write(self.games_count)
      print("game number written")

  def load_games_count(self):
    with open("games_count.txt", 'r') as f:
      print("game number loaded")
      return int(f.readline())

  def load_qtable(self):
    with open("qvalues.json") as f:
      qtable = json.load(f)
      print("Q table load!")
      return qtable

  def dump_qtable(self, qtable):
    with open("qvalues.json") as f:
      json.dump(qtable, f)
      print("Q table dump!")

  def map(self, x_dif, y_dif):
    # x є [- 40, 440]
    # y є [-120, 440]
    x_dif = int(x_dif) - int(x_dif%self.x_size)
    y_dif = int(y_dif) - int(y_dif%self.y_size)
    return (str(x_dif) + '_' +str(y_dif))

  def action(self, x_dif, y_dif):
    pass

  def update(self):
    pass
