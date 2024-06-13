from matplotlib import pyplot as plt
from load_csv import load


def aff_life(campus: str, path: str) -> None:
	df = load(path)
	sub_df = df[df['country'] == 'France']
	print(sub_df)
	sub_df.plot()
	plt.show()

def main():
	aff_life("Paris", "life_expectancy_years.csv")
	return 0


if __name__ == "__main__":
	main()