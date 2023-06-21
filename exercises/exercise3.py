import pandas as pd 

db = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'
column_names = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

df = pd.read_csv(db, sep=';', encoding='ISO-8859-1', header=None, skiprows=6, skipfooter=4,
                 usecols=[0,1,2, 12, 22, 32, 42, 52, 62, 72], names=column_names, engine='python',
                 converters={'CIN': str})

df = df[df["petrol"].str.contains("-")==False]
df = df.astype({'petrol':'int64', 'diesel':'int64', 'gas':'int64', 'electro':'int64', 'hybrid':'int64', 'plugInHybrid':'int64', 'others':'int64'})

engine = sa.create_engine("sqlite:///cars.sqlite")
df.to_sql('cars', engine, if_exists='replace', index=False)





