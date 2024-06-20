# from statistics import median


def median(values: tuple) -> int:
	print(values)
	length = len(values)
	# index += 1
	if length % 2 == 0:
		median1 = values[length // 2]
		print(median1)
		median2 = values[length // 2 - 1]
		print(median2)
		return (median1 + median2) / 2
	else:
		return values[length // 2]

def ft_statistics(*args: any, **kwargs: any) -> None:
	# print(args, type(args), len(args))
	length = len(args)
	sortedTuple = sorted(args)
	for key, value in  kwargs.items():
		match value:
			case 'mean':
				print(f"mean: {sum(args) / length}")
			case 'quartile':
				mid = len(sortedTuple) // 2
				
				if len(sortedTuple) % 2 == 0:
					print(f"quartile: {[median(sortedTuple[:mid]), median(sortedTuple[mid:])]}")
				else:
					print(f"quartile: {[median(sortedTuple[:mid]), median(sortedTuple[mid + 1:])]}")
			case 'std':
				print()
			case 'var':
				print()
			case _:
				print("ERROR")
