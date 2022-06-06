from interfaces.IGame import IGame, GameMoves
from interfaces.ISolver import ISolver

moves = [GameMoves.UP, GameMoves.DOWN, GameMoves.LEFT, GameMoves.RIGHT]

class IDS(ISolver):
  identifier = 'I'

  def __init__(self, game: IGame, config: dict):
    self.nodes = [game]
    self.config = config
    self.max_depth = 4
  
  def walk_subtree(self, subtree: IGame, depth = 0):
    if depth == self.max_depth:
      self.nodes.append(subtree)
      return
    
    if self.is_solution(subtree):
      return subtree

    for move in moves:
      if subtree.can_move(move):
        copy = subtree.copy()
        copy.move(move)
        solution = self.walk_subtree(copy, depth + 1)
        if solution != None and self.is_solution(solution):
          return solution

  def is_solution(self, game: IGame) -> bool:
    correct_positions = 0
    for i in range(1, 9):
      if game.state[i - 1] == i:
        correct_positions += 1
    return correct_positions == 8

  def solve(self) -> IGame:
    for node in self.nodes:
      possible_solution = self.walk_subtree(node)
      if possible_solution != None and self.is_solution(possible_solution):
        return possible_solution

export = IDS
