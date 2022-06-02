from interfaces.IGame import IGame, GameMoves
from interfaces.ISolver import ISolver

moves = [GameMoves.UP, GameMoves.DOWN, GameMoves.LEFT, GameMoves.RIGHT]

class BFS(ISolver):
  def __init__(self, game: IGame):
    self.queue = [game]

  def check_game_solved(self, game):
    correct_positions = 0
    for i in range(8):
      if game.state[i] == i + 1:
        correct_positions += 1
    return correct_positions == 8
  
  def solve(self):
    for game in self.queue:
      if self.check_game_solved(game):
        self.queue = []
        return game
      for move in moves:
        if game.can_move(move):
          copy = game.copy()
          copy.move(move)
          self.queue.append(copy)
