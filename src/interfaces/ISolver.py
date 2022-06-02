import abc

from interfaces.IGame import IGame

class ISolver(abc.ABC):
  @abc.abstractmethod
  def solve(self) -> IGame:
    return
