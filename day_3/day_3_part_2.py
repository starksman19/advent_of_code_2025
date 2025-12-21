from typing import Tuple

from utils import read_file_line_by_line


def find_first_biggest_index(str_nums: str) -> Tuple[int, str]:
    max_val_str = 0
    ret_index = None
    for index, val in enumerate(str_nums):
        if int(val) > max_val_str:
            max_val_str = int(val)
            ret_index = index
    return ret_index, str(max_val_str)


if __name__ == "__main__":
    ret = []
    inp = read_file_line_by_line("../inputs/day_3_part_1.txt")

    desired_len = 11
    for line in inp:
        str_nums = []
        temp_line = line
        for i in range(desired_len, -1, -1):
            str_len = len(temp_line)
            max_index = str_len - i
            index_to_start_next, value = find_first_biggest_index(temp_line[:max_index])
            temp_line = temp_line[index_to_start_next + 1 :]
            str_nums.append(value)

        ret.append(int("".join(str_nums)))
    print(sum(ret))
