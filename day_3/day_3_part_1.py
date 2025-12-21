from utils import read_file_line_by_line

if __name__ == "__main__":
    ret = []
    inp = read_file_line_by_line("../inputs/day_3_part_1.txt")

    for line in inp:
        biggest_first = -1
        biggest_second = -1
        for index, num in enumerate(line):
            curr_num = int(num)
            if curr_num > biggest_first and index != len(line) - 1:
                biggest_first = curr_num
                biggest_second = -1
                continue
            if curr_num > biggest_second:
                biggest_second = curr_num
        try:
            ret.append(int(f"{biggest_first}{biggest_second}"))
        except ValueError:
            print("hello")
    print(sum(ret))
