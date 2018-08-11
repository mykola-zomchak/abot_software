from types import FunctionType

from action_executor import *
from bots.bot import Bot
import random


class CrazyBot(Bot):

    def __init__(self):
        self.actions = [go_left, go_right, go_up, go_down]

    def get_action(self) -> FunctionType:
        return random.choice(self.actions)
