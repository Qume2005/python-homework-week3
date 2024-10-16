from math import sqrt

class Exercise1:
    a_0: float
    a_1: float
    a_2: float

    def __init__(self):
        self.a_0 = float(input("a_0:"))
        print("\n")
        self.a_1 = float(input("a_1:"))
        print("\n")
        self.a_2 = float(input("a_2:"))
        print("\n")
        delta = self.a_1 ** 2 - self.a_2 * self.a_0 * 4
        assert(delta >= 0)
        delta_sqrt = sqrt(delta)
        x_1 = (-self.a_1 - delta_sqrt) / (self.a_2 * 2)
        x_2 = (-self.a_1 + delta_sqrt) / (self.a_2 * 2)
        print("x_1: " + str(x_1) + " x_2 " + str(x_2))