import numpy as np
import pandas as pd

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)  # This will display all columns
    pd.set_option('display.width', None)  # This will display the full width of the dataframe

    # =============================================================================
    # Pandas utility functions
    print(f"{"Pandas utility functions":-^50}\n")
    print(f"{pd.isnull(np.nan)}\n")
    print(f"{pd.isnull(None)}\n")
    print(f"{pd.notnull(np.nan)}\n")
    print(f"{pd.notnull(None)}\n")

    print(f"{pd.isna(np.nan)}\n")
    print(f"{pd.isna(None)}\n")
    print(f"{pd.notna(np.nan)}\n")
    print(f"{pd.notna(None)}\n")
    # isnull() and isna() are that isnull() is an alias for isna()

    # These functions also work with Series and DataFrames
    print(f"{pd.isnull(pd.Series([1, np.nan, 7]))}\n")
    print(f"{pd.notnull(pd.Series([1, np.nan, 7]))}\n")

    # The infinite values are not considered as missing values
    print(f"{pd.isnull(pd.DataFrame({
        'A': [1, np.nan, 7],
        'B': [np.nan, 2, 8],
        'C': [3, np.inf, 9]
    }))}\n")

    # =============================================================================
    # Pandas Operations with Missing Values
    # Pandas manages missing values more gracefully than numpy.
    # nans will no longer behave as "viruses", and operations will just ignore them completely
    print(f"{"Pandas Operations with Missing Values":-^50}\n")
    print(f"{pd.Series([1, np.nan, 7]).sum()}\n")
    print(f"{pd.Series([1, np.nan, 7]).mean()}\n")
    print(f"{pd.Series([1, np.nan, 7]).count()}\n")

    # =============================================================================
    # Filtering Missing Data
    print(f"{"Filtering Missing Data":-^50}\n")
    s = pd.Series([1, 2, 3, np.nan, np.nan, 4])
    print(f"{s.notnull()}\n")
    print(f"Number of not null value: {pd.notnull(s).sum()}\n")
    print(f"{s[s.notnull()]}\n")

    # =============================================================================
    # Dropping Null Values
    print(f"{"Dropping Null Values":-^50}\n")
    print(f"{s}\n")
    print(f"{s.dropna()}\n")

    # =============================================================================
    # Dropping Null Values in DataFrames
    print(f"{"Dropping Null Values in DataFrames":-^50}\n")
    df = pd.DataFrame({
        'Column A': [1, np.nan, 30, np.nan],
        'Column B': [2, 8, 31, np.nan],
        'Column C': [np.nan, 9, 32, 100],
        'Column D': [5, 8, 34, 110],
    })

    print(f"{df}\n")
    print(f"{df.shape}\n")
    print(f"{df.info()}\n")
    print(f"{df.isna()}\n")
    print(f"{df.isnull().sum()}\n")

    # The default dropna() behavior will drop all the rows in which any null value is present
    print(f"{"dropna()":-^50}\n")
    print(f"{df.dropna()}\n")
    print(f"{df.dropna(axis=1)}\n")  # axis='columns' also works

    # In this case, any row or column that contains at least one null value will be dropped.
    # Which can be, depending on the case, too extreme. You can control this behavior with the "how" parameter.
    print(f"{"dropna(how=)":-^50}\n")
    print(f"{df}\n")
    print(f"{df.dropna(how='all')}\n")  # drop rows where all values are null
    print(f"{df.dropna(how='any')}\n")  # default behavior
    # You can also use the "thresh" parameter to indicate a threshold (a minimum number)
    # of non-null values for the row/column to be kept
    print(f"{df.dropna(thresh=3)}")  # drop rows that have less than 3 non-null values
    print(f"{df.dropna(thresh=3, axis=1)}")    # drop columns that have less than 3 non-null values

    # =============================================================================
    # Filling Null Values
    print(f"{"Filling Null Values":-^50}\n")
    print(f"{s}\n")
    print(f"{s.fillna(0)}\n")
    print(f"{s.fillna(s.mean())}\n")

    # Filling null with contiguous values
    print(f"{s.fillna(method='ffill')}\n")  # forward fill: propagate the previous value forward
    print(f"{s.fillna(method='bfill')}\n")  # backward fill: propagate the next value backward

    # This can still leave null values at the extremes of the Series/DataFrame:
    # Because there is no previous (or next) value to use for filling
    print(f"{pd.Series([np.nan, 1, 2, np.nan, np.nan, 3]).fillna(method='ffill')}\n")
    # Because there is no next value to use for filling

    # =============================================================================
    # Filling Null Values in DataFrames
    print(f"{"Filling Null Values in DataFrames":-^50}\n")
    print(f"{df}\n")

    print(f"{df.fillna({'Column A': 0, 'Column B': 99, 'Column C': df['Column C'].mean()})}\n")
    print(f"{df.fillna(method='ffill', axis='columns')}\n")  # axis='columns' == axis=1
    print(f"{df.fillna(method='ffill', axis='rows')}\n")  # axis='rows' == axis=0

    # =============================================================================
    # Checking if there are NAs
    print(f"{"Checking if there are NAs":-^50}\n")

    print(f"{s}\n")
    print(f"{s.dropna().count()}\n")

    # print(f"{s.count()}\n") == print(f"{s.dropna().count()}\n") == below
    missing_values = len(s.dropna()) != len(s)
    print(f"{missing_values}\n")

    # More Pythonic solution "any" and "all" methods
    # The methods any and all check if either there's any True value in a Series or all the values are True.
    print(f"{"any() and all() method":-^50}\n")
    print(f"{pd.Series([True, False, False]).any()}\n")
    print(f"{pd.Series([True, False, False]).all()}\n")
    print(f"{pd.Series([True, True, True]).all()}\n")

    # The isnull() method returned a Boolean Series with True values wherever there was a nan:
    print(f"{s}\n")
    print(f"{s.isnull()}\n")

    # So we can just use the "any" method with the boolean array returned:
    print(f"{pd.Series([1, np.nan]).isnull().any()}\n")
    print(f"{pd.Series([1, 2]).isnull().any()}\n")
    print(f"{s.isnull().all()}\n")

    # A more strict version would check only the values of the Series:
    print(f"{s.isnull().values}\n")
    print(f"{s.isnull().values.any()}\n")




