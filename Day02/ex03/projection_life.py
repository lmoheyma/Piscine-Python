from load_csv import load
from matplotlib import pyplot as plt


def main():
    inflation = \
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy = load("life_expectancy_years.csv")
    inflation = inflation['1900']
    life_expectancy = life_expectancy['1900']
    plt.scatter(inflation, life_expectancy)
    print(inflation)
    plt.xscale('log')
    plt.xticks(ticks=[300, 1000, 10000], labels=["300", "1k", "10k"])
    plt.ylabel("Life Expectancy")
    plt.xlabel("Gross domestic product")
    plt.title("1900")
    plt.tight_layout()
    plt.show()
    return 0


if __name__ == "__main__":
    main()
