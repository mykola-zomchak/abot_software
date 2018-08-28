import numpy as np
import json
import random

class Bot():
  # size of square for mapping
  x_size = 20
  y_size = 10

  def __init__(self):

    self.lr = 0.8
    self.discount = 0.9
    self.load_qtable()
    self.game_dump = 20

    self.history = []
    self.last_state = "420_40"
    self.last_action = 0

    self.reward = {0:1, 1:-1000}

    #how many times launch bot to play game
    self.train_games = 5000

    #exploration parameters
    self.load_games_count()
    self.exp_min = -3
    self.x = self.exp_min
    self.exp_max = 3
    self.exp_interval = (self.exp_max - self.exp_min) / self.train_games
    self.sigmoid = lambda x: 1/(1+np.exp(-x))

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.dump_qtable()
    self.write_game_count()
    #print(self.qtable)

  @staticmethod
  def init_qtable():
    # x є [-40, 440], step = self.x_size
    # y є [-300, 440], step = self.y_size
    qtable = {}
    for x in range(-40, 440, Bot.x_size):
      for y in range(-300, 440, Bot.y_size):
        qtable[str(x)+'_'+str(y)] = [0, 0]

    with open("qvalues.json", 'w') as f:
      json.dump(qtable, f)
      print("Q table init!")

  def write_game_count(self):
    if self.games_count % self.game_dump == 0:
      f = open("games_count.txt", 'w')
      f.write(str(self.games_count))
      f.close()
      print("game number written")

  def load_games_count(self):
    with open("games_count.txt", 'r') as f:
      print("game number loaded")
      self.games_count = int(f.readline())

  def load_qtable(self):
    f = open("qvalues.json")
    self.qtable = json.load(f)
    print("Q table load!")


  def dump_qtable(self):
    if self.games_count % self.game_dump == 0:
      #print(self.qtable)
      f = open('qvalues.json', 'w')
      json.dump(self.qtable, f)
      f.close()
      print("Q table dump!")


  def map(self, x_dif, y_dif):
    # x є [- 40, 440]
    # y є [-140, 440]
    x_dif = int(x_dif) - (int(x_dif) % self.x_size)
    y_dif = int(y_dif) - (int(y_dif) % self.y_size)
    return (str(x_dif) + '_' +str(y_dif))

  def action(self, x_dif, y_dif):
    state = self.map(x_dif, y_dif)
    self.history.append([self.last_state, self.last_action, state])


    #exploration/exploitation trade-off
    rand = random.uniform(0.5, 1)
    if rand > self.sigmoid(self.x):
      action = 1 if rand > 0.975 else 0
    else:
      #it`s like np.argmax, but we have just two cases
      action = 0 if self.qtable[state][0] >= self.qtable[state][1] else 1

    self.last_action = action
    self.last_state = state

    return action

  def update(self):
    #print("update")
    #print(self.qtable)
    history = list(reversed(self.history))

    high_death_flag = True if int(history[0][2].split('_')[1]) > 120 else False

    t = 1
    for exp in history:
      state = exp[2]
      prev_state = exp[0]
      action = exp[1]

      # Select reward
      if t == 1 or t == 2:
        cur_reward = self.reward[1]
      elif high_death_flag and action:
        cur_reward = self.reward[1]
        high_death_flag = False
      else:
        cur_reward = self.reward[0]

      max = self.qtable[state][0] if self.qtable[state][0] >= self.qtable[state][1] else self.qtable[state][1]

      self.qtable[prev_state][action] = self.qtable[prev_state][action] \
                                        + self.lr*(cur_reward + self.discount*max - self.qtable[prev_state][action])
      t+=1
      #print(cur_reward)

    #print(self.qtable)

    self.x += self.exp_interval*self.games_count
    #print("x=",self.x)
    self.games_count +=1
    self.dump_qtable()
    self.write_game_count()
    self.history = []

if __name__ == "__main__":
  Bot.init_qtable()
