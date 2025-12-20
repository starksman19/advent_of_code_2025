from typing import List


def read_file_line_by_line(file_path: str) -> List:
    ret = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            ret.append(line.strip())
    return ret
