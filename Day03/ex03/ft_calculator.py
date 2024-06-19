class calculator:
    def __init__(self, vector):
        self.vector = vector
    def __add__(self, object) -> None:
        self.vector = [i + object for i in self.vector]
        print(self.vector)
    def __mul__(self, object) -> None:
        self.vector = [i * object for i in self.vector]
        print(self.vector)
    def __sub__(self, object) -> None:
        self.vector = [i - object for i in self.vector]
        print(self.vector)
    def __truediv__(self, object) -> None:
        try:
            self.vector = [i / object for i in self.vector]
            print(self.vector)
        except ZeroDivisionError:
            print("Error: Division By Zero!")
            exit(1)