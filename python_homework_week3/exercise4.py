class Exercise4:
    num: int

    def __init__(self):
        self.num = int(input("input:"))
        print("\n")
        assert(self.num == 0 or self.num == 1)
        if self.num == 0:
            self.num = 1
        else:
            self.num = 0
        print("result:" + str(self.num))