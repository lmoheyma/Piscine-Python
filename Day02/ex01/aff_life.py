from matplotlib import pyplot as plt
from load_csv import load


def aff_life(path: str) -> None:
    df = load(path)
    temp = df[df['country'] == 'France']
    temp = temp.set_index('country').T
    temp.reset_index(inplace=True)
    temp.columns = ['Year', 'Life Expectancy']
    temp['Year'] = temp['Year'].astype(int)
    temp['Life Expectancy'] = temp['Life Expectancy'].astype(float)
    plt.plot(temp['Year'], temp['Life Expectancy'])
    plt.title('France Life expectancy Projections')
    plt.xlabel('Year')
    plt.xticks(temp['Year'][::40], rotation=45)
    plt.ylabel('Life Expectancy')
    plt.tight_layout()
    plt.show()

def main():
    aff_life("life_expectancy_years.csv")
    return 0


if __name__ == "__main__":
    main()
