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
        times_passed = 0

        temp_val = self.value + amount

        while temp_val > self.stop:
            temp_val -= self.from_start_to_stop
            times_passed += 1

        self.value = temp_val

        if self.value == 0:
            times_passed += 1

        return times_passed

    def sub(self, amount: int) -> int:
        times_passed = 0

        temp_val = self.value - amount

        while temp_val < self.start:
            temp_val += self.from_start_to_stop
            times_passed += 1

        self.value = temp_val

        if self.value == 0:
            times_passed += 1

        return times_passed

