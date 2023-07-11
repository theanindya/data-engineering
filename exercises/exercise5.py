import pandas as pd
import sqlalchemy as sa
import urllib.request
import zipfile

# Import the data
url = 'https://gtfs.rhoenenergie-bus.de/GTFS.zip'
with urllib.request.urlopen(url) as response:
    with zipfile.ZipFile(io.BytesIO(response.read())) as zip_ref:
        with zip_ref.open('stops.txt') as file:
            df = pd.read_csv(file, sep=',', encoding='UTF-8', header=0, usecols=[0,2,4,5,6],names=["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"], dtype={"stop_id": int, "stop_name": str, "stop_lat": float, "stop_lon":float, "zone_id": int})

# Filter the data
df = df[df['zone_id'] != 2001]

# Validate the data
invalid_lats = df[df['stop_lat'] < -90]
invalid_lons = df[df['stop_lon'] < -90]
invalid_rows = invalid_lats.append(invalid_lons)
df = df.drop(invalid_rows.index)

# Drop NaN values
df = df.dropna()

# Save the data to a SQL database
engine = sa.create_engine('sqlite:///./gtfs.sqlite')
df.to_sql('stops', con=engine, index=False)
