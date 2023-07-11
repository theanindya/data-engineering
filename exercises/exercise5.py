import os
import urllib.request
import zipfile
import pandas as pd
import sqlite3

# Set the file paths
db_path = "gtfs.sqlite"
zip_file_path = "GTFS.zip"
csv_file_path = "stops.txt"

# Step 1: Download the ZIP file
download_zip_file("https://gtfs.rhoenenergie-bus.de/GTFS.zip", zip_file_path)

# Step 2: Unzip the file and get the CSV file path
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(".")

# Step 3: Read the CSV file and create a Pandas DataFrame
df = pd.read_csv(csv_file_path, sep=',', encoding='UTF-8', header=0, usecols=[0, 2, 4, 5, 6],dtype={"stop_id": int, "stop_name": str, "stop_lat": float, "stop_lon":float, "zone_id": int})

# Step 4: Filter the data to only keep stops from zone 2001
df = df[df['zone_id'] == 2001]

# Step 5: Validate the data
invalid_lats = df[df['stop_lat'] < -90]
invalid_lons = df[df['stop_lon'] < -90]
invalid_rows = invalid_lats.append(invalid_lons)
df = df.drop(invalid_rows.index)

# Step 6: Write the data to the SQLite database
conn = sqlite3.connect(db_path)
df.to_sql('stops', conn, if_exists="replace", index=False)
conn.commit()
conn.close()

# Print a message to indicate that the data pipeline has run successfully
print("Data pipeline runs successfully.")
