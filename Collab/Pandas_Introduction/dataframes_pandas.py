import pandas as pd

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)  # This will display all columns
    pd.set_option('display.width', None)  # This will display the full width of the dataframe
    # =====================================================================
    # Pandas DataFrames
    df = pd.DataFrame({
        'Population': [35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523],
        'GDP': [1785387, 2833687, 3874437, 2167744, 4602367, 2950039, 17348075],
        'Surface Area': [9984670, 640679, 357114, 301336, 377930, 242495, 9525067],
        'HDI': [0.913, 0.888, 0.916, 0.873, 0.891, 0.907, 0.915],
        'Continent': ['America', 'Europe', 'Europe', 'Europe', 'Asia', 'Europe', 'America']
    }, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

    print(f"{df}\n")

    df.index = [
        'Canada',
        'France',
        'Germany',
        'Italy',
        'Japan',
        'United Kingdom',
        'United States',
    ]

    print(f"{df}\n")
    print(f"{df.columns}\n")
    print(f"{df.index}\n")
    print(f"{df.info}\n")
    print(f"{df.size}\n")  # Number of elements = rows * columns
    print(f"{df.shape}\n")  # (rows, columns)
    print(f"{df.describe()}\n")
    print(f"{df.dtypes}\n")
    print(f"{df.dtypes.value_counts()}\n")  # Count of each type of data

    # =====================================================================
    # Indexing, Selection and Slicing
    print(f"{df.loc['Canada']}\n")  # Accessing by label, using the index by name
    print(f"{df.iloc[-1]}\n")
    # Last row == United States, Accessing by index (using the position by number)
    print(f"{df.iloc[[0, 1, -1]]}")
    print(f"{df.iloc[1:3]}\n")
    print(f"{df.iloc[1:3, 3]}")
    # Slicing by index and take only the HDI column (3 is the index of column - HDI)
    print(f"{df.iloc[1:3, [0, 3]]}\n")
    # Slicing by index and take only the Population and HDI
    print(f"{df.iloc[1:3, 1:3]}\n")

    print(f"{df['Population']}\n")  # Accessing by column
    print(f"{df[['Population', 'GDP']]}\n")   # Accessing by columns: Population and GDP

    new_df = df['Population'].to_frame()
    print(f"{new_df}\n")  # Convert a Series to a DataFrame

    print(f"{df.loc['France':'Italy']}\n")  # Slicing by label: from France to Italy (inclusive)
    print(f"{df[1:3]}\n")  # Slicing by index: from 1 to 3 (exclusive) - Should not use this
    # Row level selection works better with loc and iloc
    # which are recommended over regular "direct slicing" (df[:]).

    print(f"{df.loc['France':'Italy', 'Population']}\n")
    # Slicing by label and take only the Population column
    print(f"{df.loc['France':'Italy', ['Population', 'GDP']]}\n")
    # Slicing by label and take only the Population and GDP columns

    # =====================================================================
    # Conditional Selection (Boolean Arrays)
    print(f"{df['Population'] > 70}\n")
    print(f"{df.loc[df['Population'] > 70]}\n")
    print(f"{df.loc[df['Population'] > 70, ['Population', 'GDP']]}\n")

    # =====================================================================
    # Dropping stuff
    print(f"{df.drop(['Canada'])}\n")  # Drop by label
    print(f"{df.drop(columns=['Population', 'HDI'])}\n")  # Drop by column

    print(f"{df.drop(['Italy', 'Canada'], axis=0)}\n")  # Drop by label == axis = 'columns'
    print(f"{df.drop(['Population', 'HDI'], axis=1)}\n")  # Drop by column == axis = 'rows'
    # axis = 0: Refers to operations along the rows(i.e., column - wise operations)
    # axis = 1: Refers to operations along the columns(i.e., row - wise operations)

    # =====================================================================
    # Operations
    print(f"{df[['Population', 'GDP']]}\n")
    print(f"{df[['Population', 'GDP']] / 100}\n")

    crisis = pd.Series([-1_000_000, -0.3], index=['GDP', 'HDI'])
    print(f"{crisis}\n")

    print(f"{df[['GDP', 'HDI']]}\n")
    print(f"{df[['GDP', 'HDI']] + crisis}\n")

    # =====================================================================
    # Modifying DataFrames
    langs = pd.Series(
        ['French', 'German', 'Italian'],
        index=['France', 'Germany', 'Italy'],
        name='Language'
    )

    print(f"{langs}\n")

    df['Language'] = langs
    print(f"{df}\n")

    df['Language'] = 'English'
    print(f"{df}\n")

    # Rename columns
    print(f"{df.rename(
        columns={
            'HDI': 'Human Development Index',
            'Annual Popcorn Consumption': 'APC'
        }, index={
            'United States': 'USA',
            'United Kingdom': 'UK',
            'Argentina': 'AR'
        })
    }\n")

    print(f"{df.rename(index=str.upper)}\n")

    print(f"{df.rename(index=lambda x: x.lower())}\n")

    # Dropping columns
    print(f"{df.drop(columns='Language', inplace=True)}\n")

    # Adding values
    print(f"{df._append(pd.Series({
        'Population': 3,
        'GDP': 5
        }, name='China'))}\n")
    # Append returns a new DataFrame: df.append(...) does not change df itself.
    print(f"{df}\n")

    # You can directly set the new index and values to the DataFrame:
    df.loc['China'] = pd.Series({'Population': 1_400_000_000, 'Continent': 'Asia'})
    print(f"{df}\n")

    # We can use drop to just remove a row by index:
    print(f"{df.drop('China')}\n")

    # More radical index changes
    print(f"{df.reset_index()}\n")
    print(f"{df.set_index('Population')}\n")  # Using the Population as the index

    # =====================================================================
    # Creating columns from other columns
    df['GDP Per Capita'] = df['GDP'] / df['Population']
    print(f"{df}\n")

    # =====================================================================
    # Statistical info
    print(f"{df.head()}\n")
    print(f"{df.describe()}\n")

    population = df['Population']
    print(f"{population}\n")
    print(f"{population.min()}\n")
    print(f"{population.max()}\n")
    print(f"{population.sum()}\n")
    print(f"{population.sum() / len(population)}\n")
    print(f"{population.mean()}\n")
    print(f"{population.std()}\n")
    print(f"{population.median()}\n")
    print(f"{population.describe()}\n")
    print(f"{population.quantile(.25)}\n")  # 25th percentile
    print(f"{population.quantile([.2, .4, .6, .8, 1])}\n")
