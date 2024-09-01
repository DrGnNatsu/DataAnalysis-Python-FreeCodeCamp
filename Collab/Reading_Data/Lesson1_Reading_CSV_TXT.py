import pandas as pd

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', False)
    # Read CSV file
    file_path = ("ipynb_file/unit-1-reading-data-with-python-and-pandas"
                 "/lesson-1-reading-csv-and-txt-files/files/btc-market-price.csv")

    # =============================================================================
    # Reading data with Python
    with open(file_path, 'r') as reader:
        for index, line in enumerate(reader.readlines()):
            # read just the first 10 lines
            if index < 10:
                print(f"{index}, {line}")
            else:
                break

    # =============================================================================
    # Reading data with Pandas
    # the read_csv() method
    csv_url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
    print(f"{pd.read_csv(csv_url).head()}\n")

    df = pd.read_csv(file_path)
    print(f"{df.head()}\n")

    # =============================================================================
    # header parameter
    df = pd.read_csv(file_path, header=None)
    print(f"{df.head()}\n")

    # =============================================================================
    # na_values parameter
    # noinspection PyTypeChecker
    df = pd.read_csv(file_path, header=None, na_values=['', '?', '-'])
    print(f"{df.head()}\n")

    # =============================================================================
    # names parameter
    # noinspection PyTypeChecker
    df = pd.read_csv(file_path, names=['Timestamp', 'Price'],
                     header=None, na_values=['', '?', '-'])
    print(f"{df.head()}\n")

    # =============================================================================
    # dtype parameter
    # noinspection PyTypeChecker
    df = pd.read_csv(file_path, header=None, na_values=['', '?', '-'],
                     names=['Timestamp', 'Price'], dtype={'Price': 'float'})
    print(f"{df.head()}\n")
    print(f"{df.dtypes}\n")
    print(f"{pd.to_datetime(df['Timestamp']).head()}\n")

    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    print(f"{df.head()}\n")
    print(f"{df.dtypes}\n")

    # =============================================================================
    # parse_dates parameter
    # noinspection PyTypeChecker
    df = pd.read_csv(file_path, header=None, na_values=['', '?', '-'],
                     names=['Timestamp', 'Price'], dtype={'Price': 'float'},
                     parse_dates=[0])

    print(f"{df.head()}\n")
    print(f"{df.dtypes}\n")

    # =============================================================================
    # index_col parameter: set the Timestamp column as the index
    # noinspection PyTypeChecker
    df = pd.read_csv(file_path, header=None, na_values=['', '?', '-'],
                     names=['Timestamp', 'Price'], dtype={'Price': 'float'},
                     parse_dates=[0], index_col=[0])

    print(f"{df.head()}\n")
    print(f"{df.dtypes}\n")

    # =============================================================================
    # Custom data delimiters using sep() parameter
    example_file_path = ("ipynb_file/unit-1-reading-data-with-python-and-pandas"
                         "/lesson-1-reading-csv-and-txt-files/files/exam_review.csv")

    exam_df = pd.read_csv(example_file_path, sep='>')

    print(f"{exam_df.head()}\n")
    print(f"{exam_df[['math_score', 'french_score']].dtypes}\n")

    exam_df = pd.read_csv(example_file_path, sep='>', decimal=',')
    print(f"{exam_df.head()}\n")
    print(f"{exam_df[['math_score', 'french_score']].dtypes}\n")

    print(f"{pd.read_csv(example_file_path, sep='>', thousands=',').head()}\n")

    # =============================================================================
    # Excluding specific rows
    exam_df = pd.read_csv(example_file_path, sep='>', skiprows=2)
    print(f"{exam_df.head()}\n")

    # =============================================================================
    # Get rid of blank lines
    exam_df = pd.read_csv(example_file_path, sep='>', skip_blank_lines=False)
    print(f"{exam_df.head()}\n")

    # =============================================================================
    # Loading specific columns
    # Below code is equal to the following code: pd.read_csv('exam_review.csv', usecols=[0, 1, 2], sep='>')
    exam_df = pd.read_csv(example_file_path,
                          usecols=['first_name', 'last_name', 'age'],
                          sep='>')
    print(f"{exam_df.head()}\n")

    # =============================================================================
    exam_test_1 = pd.read_csv(example_file_path,
                              sep='>',
                              usecols=['last_name'])
    print(f"{type(exam_test_1)}\n")

    # =============================================================================
    # Save to CSV
    exam_df.to_csv("ipynb_file/unit-1-reading-data-with-python-and-pandas"
                   "/lesson-1-reading-csv-and-txt-files/files/out.csv", index=None)
    print(f"{pd.read_csv("ipynb_file/unit-1-reading-data-with-python-and-pandas"
                         "/lesson-1-reading-csv-and-txt-files/files/out.csv").head()}\n")
