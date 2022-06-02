from interfaces.IGame import IGame
from typing import List

class EightPuzzle(IGame):
  def __init__(self, initial_state: List[int], moves: List[str] = []):
    self._initial_state = [x for x in initial_state]
    self.state = initial_state
    self.zero_position = self.state.index(0)
    self._moves = [m for m in moves]
  
  @property
  def initial_state(self) -> List[int]:
    return self._initial_state
  
  @property
  def moves(self) -> List[str]:
    return self._moves

  def copy(self):
    return EightPuzzle([x for x in self.state], [m for m in self.moves])
  
  def print_curr(self):
    for i in range(3):
      for j in range(3):
        value = self.state[i * 3 + j]
        print(' ' if value == 0 else value, end = ' ')
      print()
  
  def can_move(self, direction: str) -> bool:
    if direction == 'up':
      return self.zero_position not in [0, 1, 2]
    elif direction == 'down':
      return self.zero_position not in [6, 7, 8]
    elif direction == 'left':
      return self.zero_position not in [0, 3, 6]
    elif direction == 'right':
      return self.zero_position not in [2, 5, 8]
    else:
      return False
  
  def move(self, direction: str):
    if not self.can_move(direction):
      raise Exception('Cannot move in that direction')
    
    if direction == 'up':
      self.state[self.zero_position] = self.state[self.zero_position - 3]
      self.zero_position -= 3
      self.state[self.zero_position] = 0
    elif direction == 'down':
      self.state[self.zero_position] = self.state[self.zero_position + 3]
      self.zero_position += 3
      self.state[self.zero_position] = 0
    elif direction == 'left':
      self.state[self.zero_position] = self.state[self.zero_position - 1]
      self.zero_position -= 1
      self.state[self.zero_position] = 0
    elif direction == 'right':
      self.state[self.zero_position] = self.state[self.zero_position + 1]
      self.zero_position += 1
      self.state[self.zero_position] = 0

    self.moves.append(direction)
