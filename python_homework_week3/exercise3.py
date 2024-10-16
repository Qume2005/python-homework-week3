class Exercise3:
    who: str
    when: str
    where: str
    what: str

    def __init__(self):
        self.who = input("谁？")
        print("\n")
        self.when = input("什么时间？")
        print("\n")
        self.where = input("什么地点？")
        print("\n")
        self.what = input("做了什么？")
        print("\n")
        print(self.who + "于" + self.when + "在" + self.where + self.what)