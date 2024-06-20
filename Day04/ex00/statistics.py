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


def ft_statistics(*args: any, **kwargs: any) -> None:
	length = len(args)
	if length == 0:
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
					print(f"quartile: {[sortedTuple[length // 4], sortedTuple[length // 4 * 3]]}")
				case 'std':
					print(f"std: {sum(args) - }")
				case 'var':
					print(f"var: ")
				case _:
					print("ERROR")
