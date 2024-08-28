import pandas as pd

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)  # This will display all columns
    pd.set_option('display.width', None)  # This will display the full width of the dataframe

    df = pd.DataFrame({
        'Sex': ['M', 'F', 'F', 'D', '?'],
        'Age': [29, 30, 24, 290, 25],
    })

    print(f"{'Original DataFrame':-^50}\n")
    print(f"{df}\n")

    # =============================================================================
    # Finding Unique Values
    print(f"{'Finding Unique Values':-^50}\n")
    print(f"{df['Sex'].unique()}\n")
    print(f"{df['Sex'].value_counts()}\n")
    print(f"{df['Sex'].replace('D', 'F')}\n")
    print(f"{df['Sex'].replace({'D': 'F', 'N': 'M'})}\n")
    print(f"{df.replace({
        'Sex': {
            'D': 'F',
            'N': 'M'
        },
        'Age': {
            290: 29
        }
    })}\n")
    print(f"{df[df['Age'] > 100]}")

    df.loc[df['Age'] > 100, 'Age'] = df.loc[df['Age'] > 100, 'Age'] / 10
    print(f"{df}")

    # =============================================================================
    # Duplicates
    print(f"{'Duplicates':-^50}\n")
    ambassadors = pd.Series([
        'France', 'United Kingdom', 'United Kingdom', 'Italy', 'Germany', 'Germany', 'Germany',],
        index=[
        'Gérard Araud',
        'Kim Darroch',
        'Peter Westmacott',
        'Armando Varricchio',
        'Peter Wittig',
        'Peter Ammon',
        'Klaus Scharioth'
    ])

    print(f"{ambassadors}\n")
    # Check for duplicates: if the values appear more than ance, the first occurrence is not considered a duplicate
    print(f"{ambassadors.duplicated()}\n")
    # "last" considers the first occurrence as not duplicated
    print(f"{ambassadors.duplicated(keep='last')}\n")
    # "False" is assigned to the first occurrence is considered as duplicated
    print(f"{ambassadors.duplicated(keep=False)}\n")

    # =============================================================================
    # Duplicates in DataFrames
    print(f"{'Duplicates in DataFrames':-^50}\n")
    players = pd.DataFrame({
        'Name': [
            'Kobe Bryant',
            'LeBron James',
            'Kobe Bryant',
            'Carmelo Anthony',
            'Kobe Bryant',
        ],
        'Pos': [
            'SG',
            'SF',
            'SG',
            'SF',
            'SF'
        ]
    })

    print(f"{players}\n")
    # Conceptually, "duplicated" means "all the column values should be duplicates
    print(f"{players.duplicated()}\n")  # == print(f"{players.duplicated(subset=['Name', 'Pos'])}\n")
    print(f"{players.duplicated(subset=['Name'])}\n")
    print(f"{players.duplicated(subset=['Name'], keep='last')}\n")

    print(f"{players.drop_duplicates()}\n")
    print(f"{players.drop_duplicates(subset=['Name'])}\n")
    print(f"{players.drop_duplicates(subset=['Name'], keep='last')}\n")

    # =============================================================================
    # Text Handling
    # Splitting Columns
    df = pd.DataFrame({
        'Data': [
            '1987_M_US _1',
            '1990?_M_UK_1',
            '1992_F_US_2',
            '1970?_M_   IT_1',
            '1985_F_I  T_2'
        ]
    })

    print(f"{'Splitting Columns':-^50}\n")
    print(f"{df}\n")
    print(f"{df['Data'].str.split('_')}\n")  # split the string by '_'
    print(f"{df['Data'].str.split('_', expand=True)}\n")  # expand=True: return a DataFrame
    print(f"{df['Data'].str.split('_', expand=True, n=2)}\n")  # n=2: split the first two occurrences

    df = df['Data'].str.split('_', expand=True)
    df.columns = ['Year', 'Sex', 'Country', 'No Children']
    print(f"{df}\n")
    print(f"{df['Year'].str.contains('\?')}\n")  # check if the string contains a question mark
    print(f"{df['Country'].str.contains('U')}\n")  # strip the whitespace characters
    print(f"{df['Country'].str.strip()}\n")  # strip the whitespace characters
    print(f"{df['Country'].str.replace(' ', '')}\n")  # replace ' ' with ''

    # replace '1970?' with '1970'
    # Explanation of the Regular Expression `r'(?P<year>\d{4})\?'`

    # 1. Raw String Literal (`r'...'`): - The `r` before the string indicates a raw string literal in Python.
    # This means that backslashes are treated as literal characters and not as escape characters.

    # 2. Named Group (`(?P<year>...)`): - `(?P<year>...)` is a named capturing group in the regular expression.
    # -`?P<year>`: The `P<year>` part names the group "year". This allows you to reference this group by name in the
    # replacement string or in the code. - `\d{4}`: This part of the named group matches exactly four digits,
    # representing a year.

    # 3. Literal Question Mark (`\?`): - `\?` matches a literal question mark character. The backslash is used to
    # escape the question mark, which is a special character in regular expressions.

    print(f"{df['Year'].str.replace(r'(?P<year>\d{4})\?', lambda m: m.group('year'), regex=True)}")
