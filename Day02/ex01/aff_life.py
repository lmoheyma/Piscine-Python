from matplotlib import pyplot as plt
from load_csv import load


def aff_life(campus: str, path: str) -> None:
	df = load(path)
	# print(df)
	temp = df[df['country'] == 'France']
	xValues = temp.columns[1:]
	print(xValues)
	xValues = xValues.astype(str)
	yValues = temp.iloc[0, 1:].values
	df.plot(xValues, yValues, label='france', title='France life expectancy Projections')
	plt.show()

def main():
	aff_life("Paris", "life_expectancy_years.csv")
	return 0


if __name__ == "__main__":
	main()