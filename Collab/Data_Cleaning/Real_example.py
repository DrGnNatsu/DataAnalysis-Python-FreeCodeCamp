import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    # =======================================================================================
    df = pd.read_csv(
        'ipynb_file/data/btc-eth-prices-outliers.csv',
        index_col=0,
        parse_dates=True
    )

    print(f"{"Loading Data":-^50}\n")
    print(f"{df.head()}\n")

    plt.clf()
    df.plot(figsize=(16, 9))
    plt.show()

    plt.clf()
    df.loc['2017-12': '2017-12-15'].plot(y='Ether', figsize=(16, 9))
    plt.show()

    # =======================================================================================
    df_na = df.loc['2017-12': '2017-12-15']
    print(f"{df_na['Ether'].isna().values.any()}\n")
    print(f"{df_na.loc[df_na['Ether'].isna()]}\n")

    df.loc['2017-12-06': '2017-12-12'] = df.loc['2017-12-06': '2017-12-12'].bfill()
    plt.clf()
    df.plot(figsize=(16, 9))
    plt.show()

    plt.clf()
    df['2017-12-25':'2018-01-01'].plot()
    plt.show()

    plt.clf()
    df['2018-03-01': '2018-03-09'].plot()
    plt.show()

    plt.clf()
    df_cleaned = df.drop(pd.to_datetime(['2017-12-28', '2018-03-04']))
    df_cleaned.plot(figsize=(16, 9))
    plt.show()

    # =======================================================================================
    # Cleaning Analysis
    print(f"{"Cleaning Analysis":-^50}\n")
    print(f"{df.mean()}\n")
    print(f"{df_cleaned.mean()}\n")

    print(f"{df.median()}\n")
    print(f"{df.mode()}\n")

    # =======================================================================================
    # Visualizing the distribution of the data
    plt.clf()
    df_cleaned.plot(kind='hist', y='Ether', bins=150)
    plt.show()

    plt.clf()
    df_cleaned.plot(kind='hist', y='Bitcoin', bins=150)
    plt.show()

    # =======================================================================================
    fig, ax = plt.subplots(figsize=(15, 7))
    plt.clf()
    sns.histplot(df_cleaned['Ether'], ax=ax, kde=True, stat='density')
    ax.set_xlim(0, 1500)

    fig, ax = plt.subplots(figsize=(15, 7))
    plt.clf()
    sns.displot(df_cleaned['Bitcoin'], rug=True, kde=True)
    ax.set_xlim(0, 25000)
    plt.show()

    fig, ax = plt.subplots(figsize=(15, 7))
    plt.clf()
    sns.kdeplot(df_cleaned['Ether'], fill=True, cut=0, ax=ax)
    sns.rugplot(df_cleaned['Ether'], ax=ax)
    plt.show()

    fig, ax = plt.subplots(figsize=(15, 7))
    plt.clf()
    sns.histplot(df_cleaned['Bitcoin'], cumulative=True, kde=True, stat='density')
    ax.set_xlim(0, 20000)
    plt.show()

    # =======================================================================================
    # Visualizing bivariate distributions
    plt.clf()
    sns.jointplot(x="Bitcoin", y="Ether", data=df_cleaned, size=9)
    plt.legend(['Pearsonr = 0.83; p = 2e-39'], loc='upper left')
    plt.show()

    plt.clf()
    fig, ax = plt.subplots(figsize=(15, 7))
    sns.regplot(x="Bitcoin", y="Ether", data=df_cleaned, ax=ax)
    plt.show()

    # =======================================================================================
    # Quantiles, quartiles and percentiles
    print(f"{"Quantiles, Quartiles and Percentiles":-^50}\n")
    print(f"{df_cleaned['Ether'].quantile(.25)}\n")

    fig, ax = plt.subplots(figsize=(15, 7))
    plt.clf()
    sns.displot(df_cleaned['Bitcoin'], bins=50, cumulative=True, kde=True, stat="density")
    plt.axhline(0.2, color='red')
    plt.axvline(df_cleaned['Bitcoin'].quantile(.2), color='red')
    plt.show()

    print(f"{df_cleaned['Bitcoin'].quantile(.5)}")
    print(f"{df_cleaned['Bitcoin'].median()}\n")

    fig, ax = plt.subplots(figsize=(15, 7))
    plt.clf()
    sns.displot(df_cleaned['Bitcoin'], bins=50, cumulative=True, kde=True, stat="density")
    plt.axhline(0.5, color='red')
    plt.axvline(df_cleaned['Bitcoin'].quantile(.5), color='red')
    plt.show()

    fig, ax = plt.subplots(figsize=(15, 7))
    plt.clf()
    sns.displot(df_cleaned['Bitcoin'], bins=50, cumulative=True, kde=True, stat="density")
    plt.axhline(0.5, color='red')
    plt.axvline(df_cleaned['Bitcoin'].median(), color='red')
    plt.show()

    # =======================================================================================
    # Dispersion
    print(f"{"Dispersion":-^50}\n")
    print(f"{"Range":-^50}\n")
    print(f"{df['Bitcoin'].max() - df['Bitcoin'].min()}\n")
    print(f"{df_cleaned['Bitcoin'].max() - df_cleaned['Bitcoin'].min()}\n")

    # Variance and Standard Deviation
    print(f"{"Variance and Standard Deviation":-^50}\n")
    print(f"{df['Bitcoin'].var()}\n")
    print(f"{df['Bitcoin'].std()}\n")
    print(f"{df_cleaned['Bitcoin'].std()}\n")

    # IQR: Inter-quartile Range
    print(f"{"IQR: Inter-quartile Range":-^50}\n")
    print(f"{df['Bitcoin'].quantile(.75) - df['Bitcoin'].quantile(.25)}\n")
    print(f"{df_cleaned['Bitcoin'].quantile(.75) - df_cleaned['Bitcoin'].quantile(.25)}\n")

    # =======================================================================================
    # Analytical Analysis of invalid values
    print(f"{"Analytical Analysis of invalid values":-^50}\n")
    upper_limit = df['Bitcoin'].mean() + 2 * df['Bitcoin'].std()
    lower_limit = df['Bitcoin'].mean() - 2 * df['Bitcoin'].std()
    print("Upper Limit: {}".format(upper_limit))
    print("Lower Limit: {}".format(lower_limit))

    fig, ax = plt.subplots(figsize=(15, 7))
    plt.clf()
    sns.displot(df['Bitcoin'], kde=True, stat="density")
    plt.axvline(lower_limit, color='red')
    plt.axvline(upper_limit, color='red')
    plt.show()

    # Using IQRs
    iqr = df['Bitcoin'].quantile(.75) - df['Bitcoin'].quantile(.25)
    print(f"Iqr: {iqr}\n")

    upper_limit = df['Bitcoin'].mean() + 2 * iqr
    lower_limit = df['Bitcoin'].mean() - 2 * iqr

    print("Upper Limit: {}".format(upper_limit))
    print("Lower Limit: {}".format(lower_limit))

    fig, ax = plt.subplots(figsize=(15, 7))
    plt.clf()
    sns.displot(df['Bitcoin'], kde=True, stat="density")
    plt.axvline(lower_limit, color='red')
    plt.axvline(upper_limit, color='red')
    plt.show()

    # Cleaning invalid values
    print(f"{"Cleaning invalid values":-^50}\n")
    upper_limit = df['Bitcoin'].mean() + 2 * df['Bitcoin'].std()

    df[df['Bitcoin'] < upper_limit].plot(figsize=(16, 7))
    plt.show()

    df.drop(df[df['Bitcoin'] > upper_limit].index).plot(figsize=(16, 7))
    plt.show()
