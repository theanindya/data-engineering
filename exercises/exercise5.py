import os
import urllib.request
import zipfile
import pandas as pd
import sqlite3

# Step 1: Download function to download the GTFS ZIP file
def download_zip_file(url, file_path):
    urllib.request.urlretrieve(url, file_path)

# Step 2: Unzip function to extract stops.txt from the downloaded ZIP file
def unzip_file(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extract('stops.txt', path=extract_path)

# Step 3: Data processing function to reshape and transform the data
def data_transformation():
    # Read the stops.txt file
    df = pd.read_csv("stops.txt")

    # Select only the required columns
    df = df[['stop_id', 'stop_name', 'stop_lat', 'stop_lon', 'zone_id']]

    # Filter data for zone_id 2001
    df = df[df['zone_id'] == 2001]

    # Validate stop_name with German umlauts
    df['stop_name'] = df['stop_name'].str.replace('ae', 'ä').replace('oe', 'ö').replace('ue', 'ü').replace('ss', 'ß')

    # Validate stop_lat/stop_lon as geographic coordinates
    df = df[df['stop_lat'].between(-90, 90)]
    df = df[df['stop_lon'].between(-90, 90)]

    return df

# Step 4: Data validation function
def data_validations(df):
    # Drop rows containing invalid data
    df.dropna(inplace=True)

    return df

# Step 5: Function to write the data to the SQLite database
def load_data(df, db_path, table_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Define the table name and schema
    table_name = table_name
    table_schema = [
        ("stop_id", "BIGINT"),
        ("stop_name", "TEXT"),
        ("stop_lat", "FLOAT"),
        ("stop_lon", "FLOAT"),
        ("zone_id", "BIGINT")
    ]

    # Create the table
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
    for column, data_type in table_schema:
        create_table_query += f"{column} {data_type}, "
    create_table_query = create_table_query.rstrip(", ") + ")"

    cursor.execute(create_table_query)

    # Commit the changes and close the connection
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()

# Step 6: Main function
def main():
    # Set the file paths
    db_path = "gtfs.sqlite"
    zip_file_path = "GTFS.zip"

    # Step 1: Download the GTFS ZIP file
    download_zip_file("https://gtfs.rhoenenergie-bus.de/GTFS.zip", zip_file_path)
    print("Downloaded GTFS data successfully.")

    # Step 2: Unzip the file and get the stops.txt file path
    unzip_file(zip_file_path, ".")
    stops_file_path = os.path.join(".", "stops.txt")
    print("Unzipped GTFS data successfully.")

    # Step 3: Data transformation
    df = data_transformation()
    print("Data transformation completed.")

    # Step 4: Data validation
    df = data_validations(df)
    print("Data validation completed.")

    # Step 5: Load data
    load_data(df, db_path, "stops")
    print("Data loaded into SQLite database successfully.")

    print("Data pipeline run completed.")

# Main execution
if __name__ == "__main__":
    main()
