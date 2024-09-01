import pandas as pd

if __name__ == "__main__":
    pd.set_option('display.max_columns', 10)
    pd.set_option('display.max_rows', None)
    # =============================================================================
    # Parsing raw HTML string
    print(f"{"Parsing raw HTML string":-^50}\n")
    html_string = """
<table>
    <thead>
      <tr>
        <th>Order date</th>
        <th>Region</th> 
        <th>Item</th>
        <th>Units</th>
        <th>Unit cost</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1/6/2018</td>
        <td>East</td> 
        <td>Pencil</td>
        <td>95</td>
        <td>1.99</td>
      </tr>
      <tr>
        <td>1/23/2018</td>
        <td>Central</td> 
        <td>Binder</td>
        <td>50</td>
        <td>19.99</td>
      </tr>
      <tr>
        <td>2/9/2018</td>
        <td>Central</td> 
        <td>Pencil</td>
        <td>36</td>
        <td>4.99</td>
      </tr>
      <tr>
        <td>3/15/2018</td>
        <td>West</td> 
        <td>Pen</td>
        <td>27</td>
        <td>19.99</td>
      </tr>
    </tbody>
</table>
"""
    dfs = pd.read_html(html_string)
    print(f"{len(dfs)}\n")
    df = dfs[0]
    print(f"{df}\n")
    print(f"{df.shape}\n")
    print(f"{df.loc[df['Region'] == 'Central']}\n")
    print(f"{df.loc[df['Units'] > 35]}\n")

    # =============================================================================
    print(f"{pd.read_html(html_string)[0]}\n")
    print(f"{pd.read_html(html_string, header=0)[0]}\n")

    # =============================================================================
    # Simple example
    html_url = "https://www.basketball-reference.com/leagues/NBA_2019_per_game.html"
    nba_tables = pd.read_html(html_url)
    print(f"{len(nba_tables)}\n")
    nba = nba_tables[0]
    print(f"{nba.head()}\n")

    # =============================================================================
    # Complex example
    import requests

    html_url = "https://en.wikipedia.org/wiki/The_Simpsons"
    r = requests.get(html_url)

    wiki_tables = pd.read_html(r.text, header=0)
    print(f"{len(wiki_tables)}\n")

    simpsons = wiki_tables[1]
    print(f"{simpsons.head()}\n")

    print(f"{simpsons.drop([0, 1], inplace=True)}\n")
    print(f"{simpsons.set_index('Season', inplace=True)}\n")

    print(f"{simpsons['No. ofepisodes'].unique()}\n")

    simpsons = simpsons.loc[simpsons['No. ofepisodes'] != 'TBA']

    min_season = simpsons['No. ofepisodes'].min()
    print(f"{min_season}\n")
    print(f"{simpsons.loc[simpsons['No. ofepisodes'] == min_season]}\n")

    # =============================================================================
    # Save to CSV file
    print(f"{simpsons.head()}")
    simpsons.to_csv("out.csv")
    print(f"{pd.read_csv('out.csv', index_col='Season').head()}\n")



