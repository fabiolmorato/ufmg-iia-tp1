import sys

from domain.EightPuzzle import EightPuzzle
from domain.Greedy import Greedy

from usecases.SolveGameUseCase import SolveGameUseCase

def main(argv):
  initial_state = [1, 2, 3, 4, 0, 5, 7, 8, 6]
  game = EightPuzzle(initial_state)
  solver = Greedy(game)
  usecase = SolveGameUseCase(game, solver, EightPuzzle, True)
  usecase.execute()

if __name__ == '__main__':
  main(sys.argv)
