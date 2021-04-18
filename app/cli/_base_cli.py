from abc import ABC
from abc import abstractmethod


class _BaseCli(ABC):
    @abstractmethod
    def run_command(self, *args, **kwargs):
        pass
