import pandas as pd
import numpy as np

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)  # This will display all columns
    pd.set_option('display.width', None)  # This will display the full width of the dataframe
    # =====================================================================
    # Pandas Series
    g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])
    print(f"{g7_pop}\n")
    print(f"{g7_pop.name}\n")  # None

    g7_pop.name = "G7 Population in millions"
    print(f"{g7_pop.name}\n")
    print(f"{g7_pop}\n")
    print(f"{g7_pop.dtype}\n")

    print(f"{g7_pop.values}\n")
    print(f"{type(g7_pop.values)}\n")

    print(f"{g7_pop[[0, 1]]}\n")  # Accessing elements by index
    print(f'{g7_pop.index}\n')

    g7_pop.index = [
        'Canada',
        'France',
        'Germany',
        'Italy',
        'Japan',
        'United Kingdom',
        'United States',
    ]
    print(f"{g7_pop}\n")

    g7_pop_series = pd.Series({
        'Canada': 35.467,
        'France': 63.951,
        'Germany': 80.94,
        'Italy': 60.665,
        'Japan': 127.061,
        'United Kingdom': 64.511,
        'United States': 318.523
    }, name='G7 Population in millions')
    print(f"{g7_pop_series}\n")

    # It is the same with the previous one with the difference that the index is sorted
    # pd.Series(
    #     [35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523],
    #     index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom',
    #            'United States'],
    #     name='G7 Population in millions')

    g7_pop_diff = pd.Series(g7_pop, index=['France', 'Germany', 'Italy', 'Spain'])
    print(f"{g7_pop_diff}\n")

    # =====================================================================
    # Indexing
    print(f"{g7_pop['Canada']}\n")
    print(f"{g7_pop[['Italy', 'France']]}\n")
    print(f"{g7_pop['France':'Italy']}\n")  # Slicing: from France to Italy

    # iloc: integer location
    print(f"{g7_pop.iloc[0]}\n")
    print(f"{g7_pop.iloc[[0, 1]]}\n")  # Accessing elements by index: index 0 and 1
    print(f"{g7_pop.iloc[1:3]}\n")  # Slicing: from index 1 to 3 (exclusive)

    # =====================================================================
    # Boolean Arrays (conditional selection)
    print(f"{g7_pop > 70}\n")
    print(f"{g7_pop[g7_pop > 70]}\n")

    print(f"{g7_pop.std()}\n")  # Standard deviation

    print(f"{g7_pop[(g7_pop > g7_pop.mean() - g7_pop.std() / 2) | 
                    (g7_pop > g7_pop.mean() + g7_pop.std() / 2)]}\n")

    # =====================================================================
    # Operations and Methods
    print(f"{g7_pop}\n")
    print(f"{g7_pop * 10 ** 6}\n")

    print(f"{g7_pop.mean()}\n")
    print(f"{np.log(g7_pop)}\n")
    print(f"{g7_pop['France':'Italy'].mean()}\n")

    # =====================================================================
    # Modifying Series
    print(f"{g7_pop}\n")

    g7_pop['Canada'] = 40.5
    g7_pop.iloc[-1] = 500

    print(f"{g7_pop}\n")

    print(f"{g7_pop[g7_pop < 70]}\n")
    g7_pop[g7_pop < 70] = 99.99

    print(f"{g7_pop}\n")
