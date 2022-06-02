import abc
from typing import List

class IGame(abc.ABC):
  __metaclass__ = abc.ABCMeta

  @property
  @abc.abstractmethod
  def initial_state(self) -> List[int]:
    return

  @property
  @abc.abstractmethod
  def moves(self) -> str:
    return

  @abc.abstractmethod
  def copy(self):
    return
  
  @abc.abstractmethod
  def print_curr(self):
    return

  @abc.abstractmethod
  def can_move(self, direction: str):
    return
  
  @abc.abstractmethod
  def move(self, direction: str):
    return
