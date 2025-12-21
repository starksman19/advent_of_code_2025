from typing import List


def read_file_line_by_line(file_path: str) -> List:
    ret = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            ret.append(line.strip())
    return ret


def read_file_one_line_coma_separated(file_path: str) -> List:
    with open(file_path, "r") as f:
        line = f.readline().strip()
    ret = [p.strip() for p in line.split(",")]
    return ret
