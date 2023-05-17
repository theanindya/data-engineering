import sqlite3
import pandas as pd
import os

#1st data source

d1 = pd.read_excel("F:/Anindya/FAU/AMSE/Zaehlstelle_Hammer_Strasse_Tagesauswertung_2019(2).xlsx", engine="openpyxl") # data collected from https://opendata.stadt-muenster.de/dataset/verkehrsz%C3%A4hlung-fahrradverkehr-daten-der-z%C3%A4hlstellen-m%C3%BCnster-josefsviertel/resource/dbd8be87

#2nd data source

d2 = pd.read_excel("F:/Anindya/FAU/AMSE/MRN_OSM_shop_bycicle_repair_4326_Point.csv") # data collected from  https://geoserver.digitale-mrn.de/geoserver/metropolatlas/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=metropolatlas%3AMRN_OSM_shop_bycicle_repair_4326_Point&outputFormat=csv


conn = sqlite3.connect("data/dbanindya.sqlite")

# Write the DataFrame to a SQL table

d1.to_sql("bikedata", conn, if_exists="replace")
d2.to_sql("bicycle workshops", conn, if_exists="replace")


