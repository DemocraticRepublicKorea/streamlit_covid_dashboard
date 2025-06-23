import pandas as pd
from sqlalchemy import create_engine

# CSV-Datei laden
df = pd.read_csv("data/covid_data.csv", parse_dates=["date"])

# SQLite-Datenbank speichern
engine = create_engine("sqlite:///data/covid_data.sqlite")
df.to_sql("covid_cases", con=engine, if_exists="replace", index=False)

print("Datenbank wurde erfolgreich erstellt!")
