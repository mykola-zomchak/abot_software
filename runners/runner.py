from abc import ABC, abstractmethod

from bots.bot import Bot
from executors.executor import Executor
from parsers.image_parser import ImageParser
from screenshooter import ScreenShooter


class Runner(ABC):
    shooter = ScreenShooter()

    @abstractmethod
    def run(self, game: Executor, parser: ImageParser, bot: Bot): pass
