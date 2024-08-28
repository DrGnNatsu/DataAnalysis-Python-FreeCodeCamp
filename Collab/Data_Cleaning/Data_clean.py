import numpy as np
import pandas as pd

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)  # This will display all columns
    pd.set_option('display.width', None)  # This will display the full width of the dataframe

    # =============================================================================
    falsy_value = (0, False, None, '', [], {})
    # For Python, all the values above are considered "falsy":
    # Values that evaluate to False are considered Falsy. All other values are considered Truthy.
    print(f"{"Falsy values":-^30}")
    # Numpy has a special "nullable" value for numbers which is np.nan. It's NaN: "Not a number"
    print(f"{np.nan}\n")

    # The np.nan value is kind of a virus. Everything that it touches becomes np.nan:
    print(f"{np.nan + 1}\n")
    a = np.array([1, 2, 3, np.nan, np.nan, 4])
    print(f"{[i for i in a]}\n")
    print(f"{a.sum()}\n")
    print(f"{a.mean()}\n")
    print(f"{a.max()}\n")

    # This is better than regular None values, which in the previous examples would have raised an exception.
    print(f"{"Using None":-^30}")
    a = np.array([1, 2, 3, np.nan, None, 4], dtype='float')
    print(f"{[i for i in a]}\n")
    print(f"{a.sum()}\n")
    print(f"{a.mean()}\n")

    # Numpy also supports an "Infinite" type
    print(f"{"Infinite":-^30}")
    print(f"{np.inf}\n")

    # Which also behaves as a virus:
    print(f"{np.inf / np.inf}\n")
    b = np.array([1, 2, 3, np.inf, np.nan, 4])
    print(f"{[i for i in b]}\n")
    print(f"{b.sum()}\n")

    # Check for NaN or Inf values
    print(f"{"Checking for NaN or Inf":-^30}")
    print(f"{np.isnan(np.nan)}\n")
    print(f"{np.isinf(np.inf)}\n")

    # And the joint operation can be performed with np.isfinite.
    print(f"{np.isfinite(np.inf), np.isfinite(np.nan)}\n")

    print(f"{np.isnan(np.array([1, 2, 3, np.nan, np.inf, 4]))}\n")
    print(f"{np.isinf(np.array([1, 2, 3, np.nan, np.inf, 4]))}\n")
    print(f"{np.isfinite(np.array([1, 2, 3, np.nan, np.inf, 4]))}\n")

    # Filtering them out (np.nan and np.inf)
    print(f"{"Filtering out NaN and Inf":-^30}")
    a = np.array([1, 2, 3, np.nan, np.inf, 4])

    print(f"{a[~np.isnan(a)]}\n")
    print(f"{a[np.isfinite(a)]}\n")
    print(f"{a[np.isfinite(a)].sum()}\n")
    print(f"{a[np.isfinite(a)].mean()}\n")
