from time import time
from Minimax import Minimax


class RBMinmax:

    def __init__(self, heuristic_function_type, alpha_beta_pruning=False, ordered_alpha_beta=False):
        self.ordered_alpha_beta = ordered_alpha_beta
        self.alpha_beta_pruning = alpha_beta_pruning
        self.heuristic_function_type = heuristic_function_type

    def estimate_next_iteration(self, nr_of_leaves, last_iteration_time):
        return last_iteration_time * (9 * nr_of_leaves - 2) / (3 * nr_of_leaves - 2)

    def solve(self, time_limit, problem):
        start_time = time()
        depth = 1
        last_iteration_minimax_val = {move: 0 for move in problem.get_viable_moves()}
        algo = Minimax(heuristic_function=self.heuristic_function_type().estimate,
                       alpha_beta_pruning=self.alpha_beta_pruning,
                       ordered_alpha_beta=self.ordered_alpha_beta,
                       minimax_value_by_move=last_iteration_minimax_val)
        move, _, leaves = algo.solve_problem(problem=problem, depth=depth, playing_agent=1)
        last_iteration_time = time() - start_time
        next_iteration_max_time = self.estimate_next_iteration(leaves, last_iteration_time)
        time_until_now = time() - start_time
        while time_until_now + next_iteration_max_time < time_limit:
            depth += 1
            iteration_start_time = time()
            move, _, leaves = algo.solve_problem(problem=problem, depth=depth, playing_agent=1)
            last_iteration_time = time() - iteration_start_time
            next_iteration_max_time = self.estimate_next_iteration(leaves, last_iteration_time)
            time_until_now = time() - start_time
        print(f'the depth is {depth}')
        return move # TODO return to move
