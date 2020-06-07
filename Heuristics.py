class Heuristic:
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
        # create a box around the current state of 5X5,
        # split it into 4 small boxes of 2x2 and 4 2x1 vectors between each 2x2 block.
        # count the number of visited cells in each block
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

        # calculate for each combination of 3 blocks vs 1 block. we are trying to get as close as possible to 3 fully
        # visited blocks to 1 unvisited block. return the max of those possibilities  ( to negate direction )
        return max(abs(up_left + left + down_left + up_right + up - down - right - down_right),
                   abs(up_left + left + down_left + down_right + down - up - right - up_right),
                   abs(down_left + up_right + down_right + down + right - up - left - up_left),
                   abs(up_left + up_right + down_right + up + right - down - left - down_left))


class Heuristic2:
    def estimate(self, problem, playing_agent):
        possible_forks = problem.get_nr_of_neighbor_unvisited_cell(1)
        dist_from_mid = problem.dist_from_mid(1)
        rival_dist_from_mid = problem.dist_from_mid(2)
        if dist_from_mid > rival_dist_from_mid:
            return possible_forks + 10
        elif rival_dist_from_mid > dist_from_mid:
            return possible_forks - 10
        else:
            return possible_forks
