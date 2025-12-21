from typing import List

from utils import read_file_one_line_coma_separated


def part1(inp: List[str]) -> List[int]:
    ret = []
    for ran in inp:
        numbers = ran.split("-")
        for i in range(int(numbers[0]), int(numbers[1]) + 1):
            str_len = len(str(i))
            if str_len % 2 == 1:
                continue
            else:
                if str(i)[: str_len // 2] == str(i)[str_len // 2 :]:
                    ret.append(i)
    return ret


def get_all_dividers(n: int):
    return [i for i in range(2, n + 1) if n % i == 0]


def part2(inp: List[str]) -> List[int]:
    ret = []
    for ran in inp:
        numbers = ran.split("-")
        for i in range(int(numbers[0]), int(numbers[1]) + 1):
            str_len = len(str(i))
            dividers = get_all_dividers(str_len)
            for divider in dividers:
                part_len = str_len // divider
                parts = [str(i)[j * part_len : (j + 1) * part_len] for j in range(divider)]
                if len(set(parts)) == 1:
                    ret.append(i)
                    break
    return ret


if __name__ == "__main__":
    inpu = read_file_one_line_coma_separated("../inputs/day_2_part_1.txt")
    print(sum(part1(inpu)))
    print(sum(part2(inpu)))
