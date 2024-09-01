import pandas as pd
import sqlite3

if __name__ == "__main__":
    pd.set_option('display.max_columns', 15)
    pd.set_option('display.max_rows', None)
    # =============================================================================
    data_path = ("ipynb_file/unit-1-reading-data-with-python-and-pandas/"
                 "lesson-11-reading-data-from-relational-databases/files/chinook.db")
    conn = sqlite3.connect(data_path)
    # Once we have a Connection object, we can then create a Cursor object.
    # Cursors allow us to execute SQL queries against a database:
    cur = conn.cursor()
    query = 'SELECT * FROM employees LIMIT 5;'
    print(f"{cur.execute(query)}\n")
    # To fetch the results of a query, we can use the fetchall() method:
    results = cur.fetchall()
    print(f"{results}\n")
    # df = pd.read_sql_query(query, conn)
    df = pd.DataFrame(results)
    print(f"{df.head()}\n")

    cur.close()
    conn.close()

    # =============================================================================
    # Using pandas read_sql() method
    print(f"{"pd.read_sql()":-^50}\n")
    conn = sqlite3.connect(data_path)
    df = pd.read_sql(query, conn)
    print(f"{df.head()}\n")

    df = pd.read_sql(query, conn,
                     index_col='EmployeeId',
                     parse_dates=['BirthDate', 'HireDate'])
    print(f"{df.head()}\n")
    print(f"{df.info()}\n")
    print(f"{df['ReportsTo'].isna().sum()}\n")
    print(f"{df['ReportsTo'].mean()}\n")
    print(f"{df['ReportsTo'] > 1.75}\n")

    df['City'] = df['City'].astype('category')
    print(f"{df.info()}\n")

    conn.close()
    # =============================================================================
    # Using pandas read_sql_query() method
    print(f"{"pd.read_sql_query()":-^50}\n")
    conn = sqlite3.connect(data_path)
    df = pd.read_sql_query(query, conn)
    print(f"{df.head()}\n")

    df = pd.read_sql_query(query, conn,
                            index_col='EmployeeId',
                            parse_dates=['BirthDate', 'HireDate'])
    print(f"{df.head()}\n")

    # =============================================================================
    # Using pandas read_sql_table() method
    print(f"{"pd.read_sql_table()":-^50}\n")
    # read_sql_table is a useful function, but it works only with SQLAlchemy,
    # a Python SQL Toolkit and Object Relational Mapper.
    # This is just a demonstration of its usage where we read the whole employees table.

    # from sqlalchemy import create_engine
    # engine = create_engine('sqlite:///chinook.db')
    #
    # connection = engine.connect()
    # df = pd.read_sql_table('employees', con=connection)
    # print(f"{df.head()}\n")
    #
    # df = pd.read_sql_table('employees', con=connection,
    #                        index_col='EmployeeId',
    #                        parse_dates=['BirthDate', 'HireDate'])
    # print(f"{df.head()}\n")
    #
    # connection.close()

    # =============================================================================
    # Create tables from DataFrames
    print(f"{"Create tables from DataFrames":-^50}\n")
    print(f"{df.head()}\n")
    df.to_sql('employees2', conn)
    print(f"{pd.read_sql_query('SELECT * FROM employees2 LIMIT 5;', conn)}\n")
    # pd.read_sql_query('DROP TABLE employees2;', conn)

    # =============================================================================
    # Custom behaviour
    print(f"{"Custom behaviour":-^50}\n")
    pd.DataFrame().to_sql('employees2',
                          conn,
                          if_exists='replace')
    print(f"{pd.read_sql_query('SELECT * FROM employees2;', conn).head()}")

    df.to_sql('employees2',
              conn,
              if_exists='replace')
    print(f"{pd.read_sql_query('SELECT * FROM employees2;', conn).head()}")

    conn.close()

