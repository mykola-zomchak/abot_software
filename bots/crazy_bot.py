from types import FunctionType

from action_executor import *
from bots.bot import Bot
from field import Field
import random


class CrazyBot(Bot):

    def __init__(self):
        self.actions = [go_left, go_right, go_up, go_down]

    def get_action(self, field: Field) -> FunctionType:
        return random.choice(self.actions)
