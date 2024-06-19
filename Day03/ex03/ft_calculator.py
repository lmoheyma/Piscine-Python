class calculator:
    """A class calculator that is able
    to do calculations (addition, multiplication,
    subtraction, division) of vector with a scalar."""
    def __init__(self, vector):
        """Constructor for calculator, with a vector
        as first parameter"""
        self.vector = vector
    def __add__(self, object) -> None:
        """Overload __add__ method to add the value
        of object to each element of the list
        using list comprehension"""
        self.vector = [i + object for i in self.vector]
        print(self.vector)
    def __mul__(self, object) -> None:
        """Overload __mul__ method to multiply
        each element of the list by the value of object
        using list comprehension"""
        self.vector = [i * object for i in self.vector]
        print(self.vector)
    def __sub__(self, object) -> None:
        """Overload __sub__ method to sub the value
        of object to each element of the list
        using list comprehension"""
        self.vector = [i - object for i in self.vector]
        print(self.vector)
    def __truediv__(self, object) -> None:
        """Overload __truediv__ method to div
        each element of the list by the value of object
        using list comprehension"""
        try:
            self.vector = [i / object for i in self.vector]
            print(self.vector)
        except ZeroDivisionError:
            print("Error: Division By Zero!")
            exit(1)