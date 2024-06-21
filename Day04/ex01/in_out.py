def square(x: int | float) -> int | float:
    """Calculate the square of arguement
    and return it"""
    return x * x


def pow(x: int | float) -> int | float:
    """Calculate the pow of arguement by himself
    and return it"""
    return x ** x


def outer(x: int | float, function) -> object:
    """A function that takes as argument a number
    and a function, it returns an object that when
    called returns the result of the arguments
    calculation."""
    def inner() -> float:
        """
        Apply the function given in argument and apply it
        to the first argument.
        Usage of a nonlocal variable to keep the result in memory
        after multiple function call.
        """
        nonlocal x
        x = function(x)
        return x
    return inner
