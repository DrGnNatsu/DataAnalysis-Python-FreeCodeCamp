import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)  # This will display all columns
    pd.set_option('display.width', None)  # This will display the full width of the dataframe

    sales = pd.read_csv('data/sales_data.csv', parse_dates=['Date'])

    print(f"{sales.head()}\n")
    print(f"{sales.info()}\n")
    print(f"{sales.describe()}\n")
    print(f"{sales['Unit_Cost'].describe()}\n")
    print(f"{sales['Unit_Cost'].mean()}\n")  # Mean: is the average of the values
    print(f"{sales['Unit_Cost'].median()}\n")  # Median: is the middle value of the values

    sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14, 6))
    plt.show()

    sales['Unit_Cost'].plot(kind='density', figsize=(14, 6))
    plt.show()

    ax = sales['Unit_Cost'].plot(kind='density', figsize=(14, 6))  # kde
    ax.axvline(sales['Unit_Cost'].mean(), color='red')
    ax.axvline(sales['Unit_Cost'].median(), color='green')
    plt.show()

    ax = sales['Unit_Cost'].plot(kind='hist', figsize=(14, 6))
    ax.set_ylabel('Number of Sales')
    ax.set_xlabel('dollars')
    plt.show()

    print(sales['Age_Group'].value_counts())
    sales['Age_Group'].value_counts().plot(kind='pie', figsize=(7, 7))
    plt.show()

    ax = sales['Age_Group'].value_counts().plot(kind='bar', figsize=(14, 14))
    ax.set_ylabel('Number of Sales')
    plt.show()

    sales.plot(kind='scatter', x='Customer_Age', y='Revenue', figsize=(6, 6))
    plt.show()

    sales.plot(kind='scatter', x='Revenue', y='Profit', figsize=(6, 6))
    plt.show()

    ax = sales[['Profit', 'Age_Group']].boxplot(by='Age_Group', figsize=(10, 6))
    ax.set_ylabel('Profit')
    plt.show()

    boxplot_cols = ['Year', 'Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit']
    print(sales[boxplot_cols].info())
    sales[boxplot_cols].plot(kind='box', subplots=True, layout=(2, 3), figsize=(14, 8))
    plt.show()

    # Because the data is not clean, we need to clean it
    # We can not convert the column which have datatype object (String) to float or int
    object_columns = sales.select_dtypes(include=['object']).columns
    sales = sales.drop(columns=object_columns)

    corr = sales.corr()
    print(corr)
    fig = plt.figure(figsize=(8, 8))
    plt.matshow(corr, cmap='RdBu', fignum=fig.number)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.show()

    # =============================================================================================================
    sales['Revenue_per_Age'] = sales['Revenue'] / sales['Customer_Age']

    print(sales['Revenue_per_Age'].head())

    sales['Revenue_per_Age'].plot(kind='density', figsize=(14, 6))
    plt.show()

    sales['Revenue_per_Age'].plot(kind='hist', figsize=(14, 6))
    plt.show()

    # =============================================================================================================
    sales['Calculated_Cost'] = sales['Order_Quantity'] * sales['Unit_Cost']

    print(f"{sales['Calculated_Cost'].head()}\n")
    print(f"{(sales['Calculated_Cost'] != sales['Cost']).sum()}\n")

    sales.plot(kind='scatter', x='Calculated_Cost', y='Profit', figsize=(6, 6))
    plt.show()

    # =============================================================================================================
    sales['Calculated_Revenue'] = sales['Cost'] + sales['Profit']
    print(f"{sales['Calculated_Revenue'].head()}\n")
    print(f"{(sales['Calculated_Revenue'] != sales['Revenue']).sum()}\n")
    print(f"{sales.head()}")

    sales['Revenue'].plot(kind='hist', bins=100, figsize=(14, 6))
    plt.show()
    
    print(f"{sales['Unit_Price'].head()}\n")
    sales['Unit_Price'] *= 1.03
    print(f"{sales['Unit_Price'].head()}\n")

    # =============================================================================================================
    print(f"{sales.loc[sales['State'] == 'Kentucky']}\n")

    print(f"{sales.loc[sales['Age_Group'] == 'Adults (35-64)', 'Revenue'].mean()}\n")

    print(f"{sales.loc[(sales['Age_Group'] == 'Youth (<25)') | (sales['Age_Group'] == 'Adults (35-64)')].shape[0]}\n")

    print(f"{sales.loc[(sales['Age_Group'] == 'Adults (35-64)') & 
                       (sales['Country'] == 'United States'), 'Revenue'].mean()}\n")

    print(f"{sales.loc[sales['Country'] == 'France', 'Revenue'].head()}\n")
    sales.loc[sales['Country'] == 'France', 'Revenue'] *= 1.1
    print(f"{sales.loc[sales['Country'] == 'France', 'Revenue'].head()}\n")
