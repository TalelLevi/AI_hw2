class Heuristic:
    def estimate(self, problem, playing_agent):  # TODO fix heuristic func
        possible_forks = problem.get_nr_of_neighbor_unvisited_cell(1)
        # route_length = problem.get_length_of_route()
        dist_from_rival = problem.get_dist_from_rival()
        return 3 * possible_forks + dist_from_rival


class Heuristic2:
    def estimate(self, problem, playing_agent):
        possible_forks = problem.get_nr_of_neighbor_unvisited_cell(1)
        if problem.get_dist_from_rival() <= 10:
            return 1000 + possible_forks

        unvisited_cells_around = 0
        for i in range(-3, 4):
            for j in range(-3, 4):
                if 0 <= i < len(problem.board) and 0 <= j < len(problem.board[0]) and problem.board[i][j] == -1:
                    unvisited_cells_around += 1
        return unvisited_cells_around


        # possible_forks = problem.get_nr_of_neighbor_unvisited_cell(1)
        # rival_possible_forks = problem.get_nr_of_neighbor_unvisited_cell(2)
        # close_to_middile = problem.dist_from_edge(1)
        # rival_close_to_middle = problem.dist_from_edge(2)
        # dist_to_rival = problem.get_dist_from_rival()
        # return possible_forks - 10 * rival_possible_forks - close_to_middile + rival_close_to_middle - 10 * dist_to_rival

