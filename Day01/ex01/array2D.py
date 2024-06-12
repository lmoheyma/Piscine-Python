def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes as parameters a 2D array,
    the function prints its shape,
    and returns a truncated version of the array
    based on the provided start and end arguments
    """
    if not isinstance(family, list):
        print("Type Error")
        exit(1)
    num_row = len(family)
    num_col = len(family[0])
    for i in range(num_row):
        if len(family[i]) != num_col:
            print("Arrays don't have the same size")
            exit(1)
    print(f"My shape is : ({num_row}, {num_col})")
    slicedArray = family[start:end]
    print(f"My new shape is : ({len(slicedArray)}, {len(slicedArray[0])})")
    return slicedArray
