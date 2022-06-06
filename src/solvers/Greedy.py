from interfaces.IGame import IGame, GameMoves
from interfaces.ISolver import ISolver
from typing import Tuple, List

_abs = abs

x_coords = [0, 1, 2, 0, 1, 2, 0, 1, 2]
y_coords = [0, 0, 0, 1, 1, 1, 2, 2, 2]

moves = [GameMoves.UP, GameMoves.DOWN, GameMoves.LEFT, GameMoves.RIGHT]

class Greedy(ISolver):
  identifier = 'G'

  def __init__(self, game: IGame, config: dict):
    self.game = game.copy()
    self.config = config

  def expected_coordinate(self, value: int) -> Tuple[int, int]:
    return (y_coords[value], x_coords[value])
  
  def steps_to_point(self, point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return _abs(x1 - x2) + _abs(y1 - y2)
  
  def evaluate_solution_distance(self, game: IGame):
    total_score = 0

    for i in range(3):
      for j in range(3):
        value = game.state[i * 3 + j]
        expected_coords = self.expected_coordinate(value - 1)
        actual_coords = (i, j)
        steps_to_expected = self.steps_to_point(expected_coords, actual_coords)
        total_score += steps_to_expected
    
    return total_score
  
  def evaluate_state(self, state: List[int]) -> int:
    score = 8
    for i in range(9):
      if state[i] == 0:
        continue
      if state[i] == i + 1:
        score -= 1
    return score

  def h(self, game: IGame):
    if self.config['alternate_heuristic']:
      return self.evaluate_state(game.state)
    else:
      return self.evaluate_solution_distance(game)
  
  def choose_next_best_state(self) -> str:
    best_move = None
    best_score = float('inf')
    for move in moves:
      if self.game.can_move(move):
        copy = self.game.copy()
        copy.move(move)
        score = self.h(copy)
        if score < best_score:
          best_move = move
          best_score = score
        
    return best_move
  
  def solve(self) -> IGame:
    score = self.evaluate_state(self.game.state)
    last_move = None
    opposing = {GameMoves.UP: GameMoves.DOWN, GameMoves.DOWN: GameMoves.UP, GameMoves.LEFT: GameMoves.RIGHT, GameMoves.RIGHT: GameMoves.LEFT}
    
    while score != 0:
      move = self.choose_next_best_state()
      if move == None:
        return self.game
      if last_move != None and move == opposing[last_move]:
        return self.game
      self.game.move(move)
      last_move = opposing[move]
      score = self.evaluate_state(self.game.state)
    
    return self.game

export = Greedy
