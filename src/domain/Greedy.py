from interfaces.IGame import IGame, GameMoves
from interfaces.ISolver import ISolver
from typing import List

moves = [GameMoves.UP, GameMoves.DOWN, GameMoves.LEFT, GameMoves.RIGHT]

class Greedy(ISolver):
  def __init__(self, game: IGame):
    self.game = game.copy()
  
  def evaluate_state(self, state: List[int]) -> int:
    score = 0
    for i in range(9):
      if state[i] == 0:
        continue
      if state[i] == i + 1:
        score += 1
    return score
  
  def choose_next_best_state(self) -> str:
    best_move = None
    best_score = 0
    for move in moves:
      if self.game.can_move(move):
        copy = self.game.copy()
        copy.move(move)
        score = self.evaluate_state(copy.state)
        if score > best_score:
          best_move = move
          best_score = score
        
    return best_move
  
  def solve(self) -> IGame:
    score = self.evaluate_state(self.game.state)
    last_move = None
    opposing = {GameMoves.UP: GameMoves.DOWN, GameMoves.DOWN: GameMoves.UP, GameMoves.LEFT: GameMoves.RIGHT, GameMoves.RIGHT: GameMoves.LEFT}
    
    while score != 8:
      move = self.choose_next_best_state()
      if move == None:
        return self.game
      if last_move != None and move == opposing[last_move]:
        return self.game
      self.game.move(move)
      last_move = opposing[move]
      score = self.evaluate_state(self.game.state)
    
    return self.game
