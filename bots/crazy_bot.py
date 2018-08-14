from types import FunctionType

from action_executor import *
from bots.bot import Bot
import random

from models.field import Field


class CrazyBot(Bot):
    actions = [go_left, go_right, go_up, go_down]

    def make_action(self, parsed: Field):
        random.choice(self.actions)()
