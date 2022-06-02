from interfaces.ISolver import ISolver
from interfaces.IGame import IGame
from typing import Callable, List

class SolveGameUseCase:
  def __init__(self, game: IGame, solver: ISolver, create_game: Callable[[List[int]], IGame], print_steps: bool = False):
    self.game = game
    self.solver = solver
    self.print_steps = print_steps
    self.create_game = create_game

  def _print(self, game: IGame):
    new_game = self.create_game(self.game.initial_state)
    new_game.print_curr()
    print()

    for move in game.moves:
      new_game.move(move)
      new_game.print_curr()
      print()

  def execute(self):
    solved_game = self.solver.solve()
    print(len(solved_game.moves), end='\n\n')
    if (self.print_steps):
      self._print(solved_game)
