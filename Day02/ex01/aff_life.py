from matplotlib import pyplot as plt
from load_csv import load


def aff_life(path: str) -> None:
    """
    Calls the load function, loads the file life_expectancy_years.csv,
    and displays the country information of France.
    """
    df = load(path)
    france_df = df[df['country'] == 'France']
    france_df = france_df.set_index('country').T
    france_df.reset_index(inplace=True)
    france_df.columns = ['Year', 'Life Expectancy']
    france_df['Year'] = france_df['Year'].astype(int)
    france_df['Life Expectancy'] = france_df['Life Expectancy'].astype(float)
    plt.plot(france_df['Year'], france_df['Life Expectancy'])
    plt.title('France Life expectancy Projections')
    plt.xlabel('Year')
    plt.xticks(france_df['Year'][::40], rotation=0)
    plt.ylabel('Life Expectancy')
    plt.tight_layout()
    plt.show()


def main():
    """
    Calls the aff_life function
    """
    aff_life("life_expectancy_years.csv")
    return 0


if __name__ == "__main__":
    main()
