import json
#import random
import numpy as np

class Bot:

  def __init__(self):
    self.gameCNT = 0
    self.DUMPING_N = 100
    self.lr = 0.1
    self.load_qvalues()
    self.gamma = 0.9
    #self.step = 0.0001
    #self.x = -2
    self.moves = []
   # print(self.x)

  def epsilon(self):
    return 1/(1+np.exp(self.x))

  def action(self, xdif, ydif, vely):

    self.last_state = self.perform_state(xdif, ydif, vely)
    if self.last_state not in self.qvalues:
      self.qvalues[self.last_state] = [0, 0]

    #print(self.epsilon())

    #if random.uniform(0, 1) >= self.epsilon():
    #  if random.uniform(0,1 ) >= self.epsilon():
    #     self.last_action = 1
    #  else:
    #     self.last_action = 0
    #else:
    if self.qvalues[self.last_state][0] > self.qvalues[self.last_state][1]:
	    self.last_action = 0
    else:
	    self.last_action = 1


    return self.last_action

  def perform_state(self, xdif, ydif, vely):
    state = str(int(xdif)) + '_'
    state += str(int(ydif)) + '_'
    state += str(int(vely))
    return state

  def update_qvalues(self, xdif, ydif, vely, reward):
    new_state = self.perform_state(xdif, ydif, vely)

    if self.last_state not in self.qvalues:
      self.qvalues[self.last_state] = [0, 0]

    if new_state not in self.qvalues:
      self.qvalues[new_state] = [0, 0]

    self.qvalues[self.last_state][self.last_action] \
      += self.lr*(reward + self.gamma*self.qvalues[new_state][self.last_action] \
                  - self.qvalues[self.last_state][self.last_action])

    self.gameCNT+= 1

    self.dump_qvalues()

   # self.x -= self.step

  def load_qvalues(self):
    self.qvalues = {}
    try:
      fil = open('qvalues.json', 'r')
    except IOError:
      return
    self.qvalues = json.load(fil)
    fil.close()


  def dump_qvalues(self):
    if self.gameCNT % self.DUMPING_N == 0:
      fil = open('qvalues.json', 'w')
      json.dump(self.qvalues, fil)
      fil.close()
      print('Q-values updated on local file.')
