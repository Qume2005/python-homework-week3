from math import hypot

class Exercise7:
    result: float

    def __init__(self):
        point1_x = float(input("point1_x:"))
        print("\n")
        point1_y = float(input("point1_y:"))
        print("\n")
        point2_x = float(input("point2_x:"))
        print("\n")
        point2_y = float(input("point2_y:"))
        print("\n")
        self.result = hypot(point1_y - point2_y, point1_x - point2_x)
        print("result:" + str(self.result))