from utils import read_file_line_by_line


class CyclicNumber:
    def __init__(self, start: int, stop: int, value: int):
        self.start = start
        self.stop = stop
        self.value = value
        self.from_start_to_stop = self.stop - self.start + 1

    def add(self, amount: int):
        temp_val = self.value + amount
        rest = (temp_val - self.start) % self.from_start_to_stop

        if temp_val > self.stop:
            self.value = self.start + rest
        else:
            self.value = temp_val

    def sub(self, amount: int):
        temp_val = self.value - amount
        rest = (temp_val - self.start) % self.from_start_to_stop

        if temp_val < self.start:
            self.value = self.start + rest
        else:
            self.value = temp_val


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
