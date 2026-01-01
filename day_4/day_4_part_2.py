from typing import List

from utils import read_file_line_by_line


def check_neighbours(i1: int, j1: int, grid1: List[List[str]]) -> int:
    how_many = 0
    possible_positions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    rows = len(grid1)
    cols = len(grid1[0])

    for di, dj in possible_positions:
        ni = i1 + di
        nj = j1 + dj

        if 0 <= ni < rows and 0 <= nj < cols:
            if grid1[ni][nj] == "@":
                how_many += 1
    ret = 1 if how_many < 4 else 0
    if ret == 1:
        grid[i1][j1] = "."
    return ret


if __name__ == "__main__":
    ret = 0
    ret_prev = None
    grid = []
    inp = read_file_line_by_line("../inputs/day_4_part_1.txt")

    for line in inp:
        grid.append(list(line))

    while ret_prev != ret:
        ret_prev = ret
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "@":
                    continue
                ret += check_neighbours(i, j, grid)
    print(ret)
