import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)  # This will display all columns
    pd.set_option('display.width', None)  # This will display the full width of the dataframe

    conn = sqlite3.connect('data/sakila.db')

    df = pd.read_sql('''
        SELECT
            rental.rental_id, rental.rental_date, rental.return_date,
            customer.last_name AS customer_lastname,
            store.store_id,
            city.city AS rental_store_city,
            film.title AS film_title, film.rental_duration AS film_rental_duration,
            film.rental_rate AS film_rental_rate, film.replacement_cost AS film_replacement_cost,
            film.rating AS film_rating
        FROM rental
        INNER JOIN customer ON rental.customer_id == customer.customer_id
        INNER JOIN inventory ON rental.inventory_id == inventory.inventory_id
        INNER JOIN store ON inventory.store_id == store.store_id
        INNER JOIN address ON store.address_id == address.address_id
        INNER JOIN city ON address.city_id == city.city_id
        INNER JOIN film ON inventory.film_id == film.film_id
        ;
    ''', conn, index_col='rental_id', parse_dates=['rental_date', 'return_date'])

    # ===============================================================================================================
    print(f"{df.head()}\n")
    print(f"{df.shape}\n")
    print(f"{df.info()}\n")
    print(f"{df.describe()}\n")

    # ===============================================================================================================
    print(f"{df['film_rental_rate'].describe()}\n")
    print(f"{df['film_rental_rate'].mean()}\n")
    print(f"{df['film_rental_rate'].median()}\n")

    print(f"{df['film_rental_rate'].plot(kind='box', vert=False, figsize=(14, 6))}\n")
    plt.show()

    print(f"{df['film_rental_rate'].plot(kind='density', figsize=(14, 6))}\n")
    plt.show()

    ax = df['film_rental_rate'].value_counts().plot(kind='bar', figsize=(14, 6))
    ax.set_ylabel('Number of Rentals')
    plt.show()

    # ===============================================================================================================
    print(f"{df['film_rating'].value_counts()}\n")
    df['rental_store_city'].value_counts().plot(kind='pie', figsize=(6, 6))
    plt.show()

    ax = df['rental_store_city'].value_counts().plot(kind='bar', figsize=(14, 6))
    ax.set_ylabel('Number of Rentals')
    plt.show()

    # ===============================================================================================================
    df['rental_gain_return'] = df['film_rental_rate'] / df['film_replacement_cost'] * 100
    print(f"{df['rental_gain_return'].head()}\n")

    df['rental_gain_return'].plot(kind='density', figsize=(14, 6))
    print(f"{df['rental_gain_return'].mean().round(2)}\n")
    print(f"{df['rental_gain_return'].median().round(2)}\n")
    plt.show()

    ax = df['rental_gain_return'].plot(kind='density', figsize=(14, 6))  # kde
    ax.axvline(df['rental_gain_return'].mean(), color='red')
    ax.axvline(df['rental_gain_return'].median(), color='green')
    plt.show()

    print(f"{df['film_title'].value_counts().mean()}\n")

    # ===============================================================================================================
    print(f"{df.loc[df['customer_lastname'] == 'HANSEN']}\n")
    print(f"{df['film_replacement_cost'].max()}\n")
    print(f"{df.loc[df['film_replacement_cost'] == df['film_replacement_cost'].max(), 'film_title'].unique()}\n")
    print(f"{df.loc[(df['film_rating'] == 'PG') | (df['film_rating'] == 'PG-13')].shape[0]}\n")
