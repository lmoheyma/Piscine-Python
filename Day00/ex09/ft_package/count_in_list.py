def count_in_list(elements: list, to_find: str) -> int:
    """
    Returns the number of occurences of a string in a list
    """
    return sum(1 for c in elements if c == to_find)
