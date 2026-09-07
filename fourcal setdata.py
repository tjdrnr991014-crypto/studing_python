class FourCalStep1:
    pass

class FourCalStep2:
    def setdata(self, first, second):
        self.first = first
        self.second = second

class FourCalStep3:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second

        return result

    def mul(self):
        result = self.first * self.second

        return result

    def sub(self):
        result = self.first - self.second

        return result

    def div(self):
        result = self.first / self.second

        return result

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        return self.first / self.second

if __name__==("__main__"):
    a = FourCalStep1()
    print("1단계 type(a) :", type(a))

    a = FourCalStep2()
    b = FourCalStep2()
    a.setdata(4, 2)
    b.setdata(3, 7)
    print("2단계 a.first, b.first:", a.first, b.first)
    print("2단계 id(a) != id(b):", id(a) != id(b))

    a = FourCalStep3()
    b = FourCalStep3()

    a.setdata(4, 8)
    b.setdata(3, 7)
    print("3단계 a :", a.add(), a.sub(), a.mul(), a.div())
    print("3단계 b :", b.add(), b.sub(), a.mul(), a.div())

    try:
        FourCalStep3().add()
    except AttributeError as e:
        print("3단계 오류:", e)

    a = FourCal(4, 2)
    b = FourCal(3, 8)

    print("4단계 a :", a.add(), a.sub(), a.mul(), a.div())
    print("4단계 b :", b.add(), b.sub(), b.mul(), b.div())

    try:
        FourCal(4, 0).div()
    except ZeroDivisionError as e:
        print("나누기 오류:", e)