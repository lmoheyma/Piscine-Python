def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculte BMI value for each element of height list,
    with his weight associated value in weight list.
    Values can be int or float
    It returns a list of each BMI values
    """
    bmiList = []
    if len(height) != len(weight):
        print("Arrays don't have the same size")
        exit(1)

    for i in range(len(height)):
        if not isinstance(height[i], int | float) \
                or not isinstance(weight[i], int | float):
            print("Type Error")
            exit(1)
        bmi = weight[i] / (height[i] * height[i])
        bmiList.append(bmi)
    return bmiList


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Take a list in parameters and a limit
    Returns a list of bool,
    with True if element is above the limit, else False
    """
    underLimit = []
    for element in bmi:
        underLimit.append(element > limit)
    return underLimit
