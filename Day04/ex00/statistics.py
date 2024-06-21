def median(values: tuple) -> int:
    length = len(values)
    if length % 2 == 0:
        median1 = values[length // 2]
        print(median1)
        median2 = values[length // 2 - 1]
        print(median2)
        return (median1 + median2) / 2
    else:
        return values[length // 2]


def variance(values: tuple) -> float:
    mean = sum(values) / len(values)
    return sum((xi - mean) ** 2 for xi in values) / len(values)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    The function takes in *args a quantity of unknown
    number and make the Mean, Median,
    Quartile (25% and 75%), Standard Deviation
    and Variance according to the **kwargs ask.
    """
    length = len(args)
    if length == 0:
        for items in kwargs.items():
            print("ERROR")
    sortedTuple = sorted(args)
    for key, value in kwargs.items():
        if length != 0:
            match value:
                case 'mean':
                    print(f"mean: {sum(args) / length}")
                case 'median':
                    print(f"median: {median(sortedTuple)}")
                case 'quartile':
                    print(f"quartile: \
{[sortedTuple[length // 4], sortedTuple[length // 4 * 3]]}")
                case 'std':
                    print(f"std: {variance(args) ** 0.5}")
                case 'var':
                    mean = sum(args) / len(args)
                    print(f"var: \
{sum((xi - mean) ** 2 for xi in args) / len(args)}")
                case _:
                    print(end="")
