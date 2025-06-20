from abc import ABC, abstractmethod
from logging import Logger


class BaseTask(ABC):
    def __init__(self, logger: Logger):
        self.logger = logger

    @abstractmethod
    def run(self) -> None:
        pass
