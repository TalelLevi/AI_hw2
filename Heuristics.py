class Heuristic:
    def estimate(self, problem, playing_agent):  # TODO fix heuristic func
        # possible_forks = problem.get_nr_of_neighbor_unvisited_cell(1)
        # return possible_forks
        if problem.get_dist_from_rival() <= 15:
            # check if path exists if yes do something.
            return 18 + problem.get_nr_of_neighbor_unvisited_cell(1)
        up_left = 0
        up_right = 0
        down_left = 0
        down_right = 0

        right = 0
        left = 0
        up = 0
        down = 0

        for i in range(-2, 3):
            for j in range(-2, 3):
                cell = (problem.loc[0] + i, problem.loc[1] + j)
                if not problem.in_board(cell) or problem.board[cell] == -1:
                    if i < 0 and j < 0:
                        down_left += 1
                    elif i < 0 and j > 0:
                        down_right += 1
                    elif i > 0 and j < 0:
                        up_left += 1
                    elif i > 0 and j > 0:
                        up_right += 1
                    elif i == 0:
                        if j == -1 or j == -2:
                            left += 1
                        elif j == 1 or j == 2:
                            right += 1
                    elif j == 0:
                        if i == -1 or j == -2:
                            down += 1
                        elif i == 1 or i == 2:
                            up += 1

        return max(abs(up_left + left + down_left + up_right + up - down - right - down_right),
                   abs(up_left + left + down_left + down_right + down - up - right - up_right),
                   abs(down_left + up_right + down_right + down + right - up - left - up_left),
                   abs(up_left + up_right + down_right + up + right - down - left - down_left))



class Heuristic2:
    def estimate(self, problem, playing_agent):
        if problem.get_dist_from_rival() <= 15:
            # check if path exists if yes do something.
            return 18 + problem.get_nr_of_neighbor_unvisited_cell(1)
        up_left = 0
        up_right = 0
        down_left = 0
        down_right = 0

        right = 0
        left = 0
        up = 0
        down = 0

        for i in range(-2, 3):
            for j in range(-2, 3):
                cell = (problem.loc[0] + i, problem.loc[1] + j)
                if not problem.in_board(cell) or problem.board[cell] == -1:
                    if i < 0 and j < 0:
                        down_left += 1
                    elif i < 0 and j > 0:
                        down_right += 1
                    elif i > 0 and j < 0:
                        up_left += 1
                    elif i > 0 and j > 0:
                        up_right += 1
                    elif i == 0:
                        if j == -1 or j == -2:
                            left += 1
                        elif j == 1 or j == 2:
                            right += 1
                    elif j == 0:
                        if i == -1 or j == -2:
                            down += 1
                        elif i == 1 or i == 2:
                            up += 1

        return max(abs(up_left + left + down_left + up_right + up - down - right - down_right),
                   abs(up_left + left + down_left + down_right + down - up - right - up_right),
                   abs(down_left + up_right + down_right + down + right - up - left - up_left),
                   abs(up_left + up_right + down_right + up + right - down - left - down_left))

        # return max(abs(up_left + left + down_left + up_right + up + down - down_right - right),
        #            abs(up_left + left + down_left + down_right + down + up - up_right - right),
        #            abs(down_left + up_right + down_right + up + down + right - up_left - left),
        #            abs(up_left + up_right + down_right + up + down + right - down_left - left))






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
