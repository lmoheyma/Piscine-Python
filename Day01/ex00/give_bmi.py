def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
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
    underLimit = []
    for element in bmi:
        underLimit.append(element > limit)
    return underLimit
