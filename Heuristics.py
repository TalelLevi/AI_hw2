class Heuristic:
    def estimate(self, problem, playing_agent):  # TODO fix heuristic func
        possible_forks = problem.get_nr_of_neighbor_unvisited_cell(1)
        # route_length = problem.get_length_of_route()
        # dist_from_rival = problem.get_dist_from_rival()
        return possible_forks


class Heuristic2:
    def estimate(self, problem, playing_agent):
        possible_forks = problem.get_nr_of_neighbor_unvisited_cell(1)
        if problem.get_dist_from_rival() <= 10:
            return 1000 + possible_forks

        up_left = 0
        up_right = 0
        down_left = 0
        down_right = 0

        right = 0
        left = 0

        right_visited_cells_around = 0
        left_visited_cells_around = 0
        for i in range(-2, 3):
            for j in range(-2, 3):
                cell = (problem.loc[0] + i, problem.loc[1] + j)
                if 0 <= cell[0] < len(problem.board) and 0 <= cell[1] < len(problem.board[0]):
                    if i < 0 or i == 0 and j > 0:
                        if problem.board[cell] == -1:
                            left_visited_cells_around += 1

                    else:
                        if problem.board[cell] == -1:
                            right_visited_cells_around += 1

        return abs(left_visited_cells_around - right_visited_cells_around)

        # unvisited_cells_around = 0
        # for i in range(-2, 3):
        #     for j in range(-2, 3):
        #         cell = (problem.loc[0] + i, problem.loc[1] + j)
        #         if 0 <= cell[0] < len(problem.board) and 0 <= cell[1] < len(problem.board[0]) and problem.board[cell] == -1:
        #             unvisited_cells_around += 1

        # possible_forks = problem.get_nr_of_neighbor_unvisited_cell(1)
        # rival_possible_forks = problem.get_nr_of_neighbor_unvisited_cell(2)
        # close_to_middile = problem.dist_from_edge(1)
        # rival_close_to_middle = problem.dist_from_edge(2)
        # dist_to_rival = problem.get_dist_from_rival()
        # return possible_forks - 10 * rival_possible_forks - close_to_middile + rival_close_to_middle - 10 * dist_to_rival
