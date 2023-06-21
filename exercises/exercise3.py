import pandas as pd 

db = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'
column_names = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid','others']

df = pd.read_csv(db, sep=';', encoding='ISO-8859-1', header=None, skiprows=range(0, 7), skipfooter=4,
                 usecols=[0, 1, 2, 12, 22, 32, 42, 52, 62, 72], names=column_names, engine='python', na_values='.', thousands=',',dtype={'CIN': str})

df = df[df["petrol"].str.contains("-")==False]

df = df[df['CIN'].str.contains(r'^\d{5}$', regex=True)]



df = df.astype({col: 'int64' for col in ['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']})



df.to_sql('cars', 'sqlite:///cars.sqlite', if_exists='replace', index=False)





