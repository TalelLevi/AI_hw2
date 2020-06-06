class Heuristic:
    def estimate(self, problem, playing_agent):  # TODO fix heuristic func
        # possible_forks = problem.get_nr_of_neighbor_unvisited_cell(1)
        # # route_length = problem.get_length_of_route()
        # # dist_from_rival = problem.get_dist_from_rival()
        # return possible_forks
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
        up = 0
        down = 0

        right_visited_cells_around = 0
        left_visited_cells_around = 0
        for i in range(-2, 3):
            for j in range(-2, 3):
                cell = (problem.loc[0] + i, problem.loc[1] + j)
                if i < 0 and j < 0:
                    if 0 <= cell[0] < len(problem.board) and 0 <= cell[1] < len(problem.board[0]):
                        if problem.board[cell] == -1:
                            down_left += 1
                    else:
                        down_left += 1

                elif i < 0 and j > 0:
                    if 0 <= cell[0] < len(problem.board) and 0 <= cell[1] < len(problem.board[0]):
                        if problem.board[cell] == -1:
                            down_right += 1
                    else:
                        down_right += 1

                elif i > 0 and j < 0:
                    if 0 <= cell[0] < len(problem.board) and 0 <= cell[1] < len(problem.board[0]):
                        if problem.board[cell] == -1:
                            up_left += 1
                    else:
                        up_left += 1

                elif i > 0  and j > 0:
                    if 0 <= cell[0] < len(problem.board) and 0 <= cell[1] < len(problem.board[0]):
                      if problem.board[cell] == -1:
                         up_right += 1
                    else:
                        up_right += 1

                else:
                    if 0 <= cell[0] < len(problem.board) and 0 <= cell[1] < len(problem.board[0]):
                        if i == 0 and problem.board[cell] == -1:
                            if j == -1 or j == -2:
                                left += 1
                            elif j == 1 or j == 2:
                                right += 1
                        elif j == 0 and problem.board[cell] == -1:
                            if i == -1 or j == -2:
                                down += 1
                            elif i == 1 or i == 2:
                                up += 1
                    else:
                        if i == 0:
                            if j == -1 or j == -2:
                                left += 1
                            elif j == 1 or j == 2:
                                right += 1
                        elif j == 0:
                            if i == -1 or j == -2:
                                down += 1
                            elif i == 1 or i == 2:
                                up += 1

        return max(abs(up_left + down_left + up_right + down + up + left - down_right - right),
                   abs(up_left + down_left + down_right + down + up + left - up_right - right),
                   abs(down_left + up_right + down_right + up + down + right - up_left - left),
                   abs(up_left + up_right + down_right + up + down + right - down_left - left))

        # return max(abs(up_left+down_left+left+down - (up_right+down_right+right+up)),
        #            abs(up_left+down_left+left+up - (up_right+down_right+right+down)),
        #            abs(up_right+up_left+up+right - (down_left+down_right+down+left)),
        #            abs(up_right+up_left+up+left - (down_left+down_right+down+right)))

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

#
# class Heuristic3:
#     def estimate(self, problem, playing_agent):
#         max = 0
#         if problem.loc[0] + 1 < len(problem.board) and problem.loc:
