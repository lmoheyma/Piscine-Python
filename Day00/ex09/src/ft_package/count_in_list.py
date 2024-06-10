def count_in_list(elements: list, to_find: str) -> int:
	return sum(1 for c in elements if c == to_find)