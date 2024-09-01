import pandas as pd

if __name__ == "__main__":
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    # Read data from Excel
    path = ("ipynb_file/unit-1-reading-data-with-python-and-pandas/"
            "lesson-5-reading-excel-files/files/products.xlsx")
    df = pd.read_excel(path)
    print(f"{df.head()}\n")

    # =============================================================================
    # First row behaviour with header parameter
    print(f"{"read_excel() parameters":-^50}\n")
    print(f"{pd.read_excel(path).head()}\n")

    print(f"{pd.read_excel(path, header=None).head()}\n")

    # =============================================================================
    # Adding index to our data using index_col parameter
    print(f"{"Adding index to our data using index_col parameter":-^50}\n")
    df = pd.read_excel(path, index_col=[0])
    print(f"{df.head()}\n")

    # =============================================================================
    # Selecting specific sheets
    print(f"{"Selecting specific sheets":-^50}\n")
    products = pd.read_excel(path,
                             sheet_name='Products',
                             index_col='product_id')
    print(f"{products.head()}\n")

    merchants = pd.read_excel(path,
                              sheet_name='Merchants',
                              index_col='merchant_id')
    print(f"{merchants.head()}\n")

    # =============================================================================
    # The ExcelFile class
    print(f"{"The ExcelFile class":-^50}\n")
    excel_file = pd.ExcelFile(path)
    print(f"{excel_file.sheet_names}\n")

    products = excel_file.parse('Products')
    print(f"{products.head()}\n")

    products = excel_file.parse(sheet_name='Products',
                                header=0,
                                index_col='product_id')
    print(f"{products.head()}\n")
    print(f"{products.dtypes}\n")

    merchants = excel_file.parse('Merchants',
                                 index_col='merchant_id')
    print(f"{merchants.head()}\n")
    print(f"{merchants.dtypes}\n")

    # =============================================================================
    # Save to Excel file
    print(f"{"Save to Excel file":-^50}\n")
    path_out = ("ipynb_file/unit-1-reading-data-with-python-and-pandas/"
                "lesson-5-reading-excel-files/files/out.xlsx")
    products.to_excel(path_out)
    print(f'{pd.read_excel(path_out).head()}')

    # We can specify the sheet name with sheet_name parameter:
    products.to_excel(path_out,
                      sheet_name='Products')

    products.to_excel(path_out,
                      index=None)
    print(f'{pd.read_excel(path_out).head()}')

    # =============================================================================
    # Position Data with start row and start col
    print(f"{"Position Data with start row and start col":-^50}\n")
    # In Excel file, the data will start at row 2 and column C
    products.to_excel(path_out,
                      sheet_name='Products',
                      startrow=1,
                      startcol=2)

    # =============================================================================
    # Saving multiple sheets
    print(f"{"Saving multiple sheets":-^50}\n")
    writer = pd.ExcelWriter(path_out)
    print(f"{writer}\n")

    with writer:
        products.to_excel(writer, sheet_name='Products')

    print(f'{pd.read_excel(path_out, sheet_name='Products').head()}')

