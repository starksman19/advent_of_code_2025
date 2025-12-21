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


class CyclicNumber2(CyclicNumber):
    def add(self, amount: int) -> int:
        times_zero = 0
        current = self.value

        if current == 0:
            first_zero = self.from_start_to_stop
        else:
            first_zero = self.from_start_to_stop - current

        if amount >= first_zero:
            times_zero += 1
            amount -= first_zero

            times_zero += amount // self.from_start_to_stop

        self.value = (
            self.value + (first_zero if times_zero > 0 else 0) + amount
        ) % self.from_start_to_stop

        return times_zero

    def sub(self, amount: int) -> int:
        times_zero = 0
        current = self.value

        if current == 0:
            first_zero = self.from_start_to_stop
        else:
            first_zero = current

        if amount >= first_zero:
            times_zero += 1
            amount -= first_zero

            times_zero += amount // self.from_start_to_stop

        self.value = (
            self.value - (first_zero if times_zero > 0 else 0) - amount
        ) % self.from_start_to_stop

        return times_zero
