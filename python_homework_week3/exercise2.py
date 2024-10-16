class Exercise2:
    total: float
    index: int
    annual_interest_rate: float

    def __init__(self):
        self.index = 0;
        self.total = float(input("principal:"))
        print("\n")
        self.annual_interest_rate = float(input("annual interest rate:"))
        print("\n")
        self.next()
        self.next()
        self.next()
        self.next()
        self.next()

    def next(self):
        self.index += 1
        self.total *= 1.2
        print("year" + str(self.index) + ": " + str(self.total))
        return self