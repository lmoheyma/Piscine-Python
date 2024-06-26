from matplotlib import pyplot as plt
from load_csv import load


def conv_m_to_f(value):
    """
    Convert a string in float
    If value end with M -> multiply by 100000
    Elif value end with k -> multiply by 1000
    Else it will return the value cast in float
    """
    if 'M' in value:
        return float(value.replace('M', '')) * 1_000_000
    elif 'k' in value:
        return float(value.replace('k', '')) * 1_000
    return float(value)


def aff_pop(path: str) -> None:
    """
    Calls the load function, loads the file life_expectancy_years.csv,
    and displays the country information of France versus Belgium
    """
    df = load(path)
    france_df = df[df['country'] == 'France']
    belgium_df = df[df['country'] == 'Belgium']
    france_df = france_df.set_index('country').T
    belgium_df = belgium_df.set_index('country').T
    france_df.reset_index(inplace=True)
    belgium_df.reset_index(inplace=True)
    france_df.columns = ['Year', 'Population']
    belgium_df.columns = ['Year', 'Population']
    france_df['Year'] = france_df['Year'].astype(int)
    belgium_df['Year'] = belgium_df['Year'].astype(int)
    france_df['Population'] = france_df['Population'].apply(conv_m_to_f)
    belgium_df['Population'] = belgium_df['Population'].apply(conv_m_to_f)
    france_df = france_df[(france_df['Year'] >= 1800)
                          & (france_df['Year'] <= 2050)]
    belgium_df = belgium_df[(belgium_df['Year'] >= 1800)
                            & (belgium_df['Year'] <= 2050)]
    plt.plot(france_df['Year'], france_df['Population'], label='France')
    plt.plot(belgium_df['Year'], belgium_df['Population'], label='Belgium')
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.xticks(france_df['Year'][::40], rotation=0)
    max_population = max(max(france_df['Population'][::20]),
                         max(belgium_df['Population'][::20]))
    y_ticks = [i * 2e7 for i in range(1, int(max_population / 2e7) + 1)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
    plt.ylabel('Population')
    plt.tight_layout()
    plt.legend(loc='lower right')
    plt.show()


def main():
    """
    Calls the aff_life function
    """
    aff_pop("population_total.csv")
    return 0


if __name__ == "__main__":
    main()
