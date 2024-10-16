class Exercise5:
    result: float

    def __init__(self):
        self.result = float(input("tem?"))
        print("\n")
        self.result = self.result * (9 / 5) + 32
        print("\n")
        print("result:" + str(self.result))