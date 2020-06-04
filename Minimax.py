def utility(problem, playing_agent):
    if playing_agent:
        rival_possible_move = problem.get_nr_of_neighbor_unvisited_cell(2)
        if rival_possible_move > 0:
            return float('-inf')
    else:
        rival_possible_move = problem.get_nr_of_neighbor_unvisited_cell(1)
        if rival_possible_move > 0:
            return float('inf')
    return 0


def estimate(problem, playing_agent):  # TODO fix heuristic func
    if playing_agent:
        possible_forks = problem.get_nr_of_neighbor_unvisited_cell(1)
    else:
        possible_forks = problem.get_nr_of_neighbor_unvisited_cell(2)
    route_length = problem.get_length_of_route()
    dist_from_rival = problem.get_dist_from_rival()
    return 6 * route_length + 3 * possible_forks + dist_from_rival


def heuristic(problem, playing_agent):
    return estimate(problem, playing_agent)


class Minimax:
    Maximizer = True
    Minimizer = False
    single_leaf = 1

    def __init__(self, heuristic_function, alpha_beta_pruning=False, ordered_alpha_beta=False,
                 minimax_value_by_move=None):
        self.ordered_alpha_beta = ordered_alpha_beta
        self.alpha_beta_pruning = alpha_beta_pruning
        self.heuristic_function = heuristic_function
        self.last_iteration_minimax_val = minimax_value_by_move
        self.is_root = True

    def solve_problem(self, problem, depth, playing_agent, alpha=float('-inf'), beta=float('inf')):
        """

        :param alpha:
        :param beta:
        :param problem:
        :param depth: if depth is a number then the function will act as depth restricted minmax otherwise if depth is
                        None then the function will act as a standard minmax
        :param playing_agent:
        :return:
        """
        if problem.is_goal(playing_agent):
            return None, utility(problem, playing_agent), self.single_leaf
        if depth == 0:
            return None, self.heuristic_function(problem, playing_agent), self.single_leaf
        # generate legal moves ( order if needed )
        legal_moves = problem.legal_moves(playing_agent)
        best_move = legal_moves[0]
        curr_nr_of_leaves = 0
        possible_end_states = 0
        tree_root_update_sons_minimax_value = False
        if self.ordered_alpha_beta and self.is_root:
            nr_of_legal_moves = len(legal_moves)
            legal_moves = sorted(legal_moves,
                                 key=lambda tup: self.last_iteration_minimax_val[tup],
                                 reverse=True)
            self.last_iteration_minimax_val.clear()
            tree_root_update_sons_minimax_value = True
            self.is_root = False

        # Maximizer
        if playing_agent == self.Maximizer:
            best_minmax_value = float("-inf")
            for move in legal_moves:
                problem.execute_move(playing_agent, move)
                _, current_minmax_value, leaves = self.solve_problem(problem, depth - 1, self.Minimizer, alpha, beta)
                problem.undo_move(playing_agent, move)

                curr_nr_of_leaves += leaves
                if current_minmax_value > best_minmax_value:
                    best_minmax_value = current_minmax_value
                    best_move = move
                    possible_end_states = leaves
                elif current_minmax_value == best_minmax_value and possible_end_states < leaves:
                    best_move = move
                    possible_end_states = leaves
                if self.alpha_beta_pruning:
                    alpha = max(current_minmax_value, alpha)
                    if beta <= alpha != float('inf'):
                        return None, float('inf'), curr_nr_of_leaves
                # we only order the sons of the tree root so here we save the last moves to use for next iteration
                if tree_root_update_sons_minimax_value:
                    self.last_iteration_minimax_val[move] = current_minmax_value
                    self.is_root = True if nr_of_legal_moves == len(self.last_iteration_minimax_val) else False
            return best_move, best_minmax_value, curr_nr_of_leaves

        # Minimizer
        else:  # playing_agent == self.Minimizer
            best_minmax_value = float("inf")
            for move in legal_moves:
                problem.execute_move(playing_agent, move)
                _, current_minmax_value, leaves = self.solve_problem(problem, depth - 1, self.Maximizer, alpha, beta)
                problem.undo_move(playing_agent, move)

                curr_nr_of_leaves += leaves
                if current_minmax_value < best_minmax_value:
                    best_minmax_value = current_minmax_value
                    best_move = move
                    possible_end_states = leaves
                elif current_minmax_value == best_minmax_value and possible_end_states < leaves:
                    best_move = move
                    possible_end_states = leaves
                if self.alpha_beta_pruning:
                    beta = min(current_minmax_value, beta)
                    if alpha >= beta != float('-inf'):
                        return None, float('-inf'), curr_nr_of_leaves
            return best_move, best_minmax_value, curr_nr_of_leaves
