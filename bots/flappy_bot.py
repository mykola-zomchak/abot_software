from bots.bot import Bot
from models.field import  Field
from action_executor import  go_up
import random

class FlappyBot(Bot):

    def make_action(sef, parsed: Field):
        rd = random.uniform(0, 1)
        if rd >= 0.5:
          go_up()
