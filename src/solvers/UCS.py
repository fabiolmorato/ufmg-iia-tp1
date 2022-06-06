from interfaces.IGame import IGame, GameMoves
from interfaces.ISolver import ISolver

moves = [GameMoves.UP, GameMoves.DOWN, GameMoves.LEFT, GameMoves.RIGHT]

class Node:
  def __init__(self, game: IGame, value: int):
    self.game = game
    self.value = value

class UCS(ISolver):
  identifier = 'U'

  def __init__(self, game: IGame):
    self.queue = [Node(game, 0)]
  
  def is_solution(self, game: IGame) -> bool:
    correct_positions = 0
    for i in range(1, 9):
      if game.state[i - 1] == i:
        correct_positions += 1
    return correct_positions == 8
  
  def solve(self) -> IGame:
    while True:
      node = self.queue[0]
      game = node.game

      if self.is_solution(game):
        return game
        
      for move in moves:
        if game.can_move(move):
          copy = game.copy()
          copy.move(move)
          self.queue.append(Node(copy, node.value + 1))

      del self.queue[0]
      self.queue.sort(key = lambda x: x.value, reverse = False)

export = UCS
