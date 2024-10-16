class Exercise6:
    shoe_size: float
    result: float

    def __init__(self):
        self.shoe_size = float(input("shoe_size?"))
        print("\n")
        self.result = self.shoe_size * 2 - 10
        print("result:" + str(self.result))
        