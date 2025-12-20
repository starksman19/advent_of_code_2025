from day_1.cyclic_numbers import CyclicNumber
from utils import read_file_line_by_line

if __name__ == "__main__":
    ret = 0
    inp = read_file_line_by_line("../inputs/day_1_part_1.txt")
    cyclic_number = CyclicNumber(0, 99, 50)

    for val in inp:
        if val[0] == "R":
            cyclic_number.add(int(val[1:]))
        else:
            cyclic_number.sub(int(val[1:]))

        if cyclic_number.value == 0:
            ret += 1
    print(ret)
