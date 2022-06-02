from interfaces.IGame import IGame
from interfaces.ISolver import ISolver
from typing import List

class Greedy(ISolver):
  def __init__(self, game: IGame):
    self.game = game
  
  def evaluate_state(self, state: List[int]) -> int:
    score = 0
    for i in range(9):
      if state[i] == 0:
        continue
      if state[i] == i + 1:
        score += 1
    return score
  
  def choose_next_best_state(self) -> str:
    possible_moves = ['up', 'down', 'left', 'right']
    best_move = None
    best_score = 0
    for move in possible_moves:
      if self.game.can_move(move):
        copy = self.game.copy()
        copy.move(move)
        score = self.evaluate_state(copy.state)
        if score > best_score:
          best_move = move
          best_score = score
    return best_move
  
  def solve(self):
    score = self.evaluate_state(self.game.state)
    
    while score != 8:
      move = self.choose_next_best_state()
      self.game.move(move)
      score = self.evaluate_state(self.game.state)
