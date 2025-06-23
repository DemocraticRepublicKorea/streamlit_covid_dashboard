# import_data.py
import pandas as pd
from sqlalchemy import create_engine

# Beispiel-URL (Our World in Data)
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

# Lade die CSV-Datei
df = pd.read_csv(url, parse_dates=["date"])

# Wähle nur Spalten, die dich interessieren
df = df[["iso_code", "location", "date", "total_cases", "new_cases"]]

# Erstelle SQLite-Datenbank
engine = create_engine("sqlite:///covid_data.db")
df.to_sql("covid_cases", engine, if_exists="replace", index=False)

print("CSV wurde in Datenbank gespeichert.")
