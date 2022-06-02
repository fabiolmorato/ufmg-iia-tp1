import sys

from domain.EightPuzzle import EightPuzzle
from domain.SolverLoader import SolverLoader

from usecases.SolveGameUseCase import SolveGameUseCase

class TP1:
  def __init__(self):
    self.solver_loader = SolverLoader()
    self.solver_loader.load_from_directory('src/solvers')
    self.should_print = False
    self.args = self.get_args()
    self.prepare()

  def get_args(self):
    return sys.argv[1:]

  def prepare(self):
    self.get_initial_state()
    self.get_solver_identifier()
    self.get_should_print()

  def get_initial_state(self):
    config = self.args[1:10]
    values = [int(x) for x in config]
    self.game_initial_state = values
  
  def get_solver_identifier(self):
    self.solver_identifier = self.args[0]
  
  def get_should_print(self):
    if (len(self.args) > 10):
      self.should_print = self.args[10] == 'PRINT'
  
  def run(self):
    game = EightPuzzle(self.game_initial_state)
    solver_class = self.solver_loader.get_solver(self.solver_identifier)
    solver = solver_class(game)
    solve_game_use_case = SolveGameUseCase(game, solver, EightPuzzle, self.should_print)
    solve_game_use_case.execute()

if __name__ == '__main__':
  TP1().run()
