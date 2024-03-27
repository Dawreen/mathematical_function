from abc import ABC, abstractmethod


class math_fun(ABC):

    @abstractmethod
    def exec(n: int) -> int:
        pass

    @abstractmethod
    def print(self) -> tuple:
        pass

    @abstractmethod
    def graph(self):
        pass