# app.py
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Verbinde dich mit der SQLite-Datenbank
engine = create_engine("sqlite:///covid_data.db")

@st.cache_data
def load_data():
    return pd.read_sql("SELECT * FROM covid_cases", engine, parse_dates=["date"])

df = load_data()

# Sidebar-Filter
country = st.sidebar.selectbox("Land wählen", sorted(df["location"].unique()))
start_date, end_date = st.sidebar.date_input(
    "Zeitraum wählen",
    [df["date"].min(), df["date"].max()]
)

# Filter anwenden
df_filtered = df[(df["location"] == country) &
                 (df["date"] >= pd.to_datetime(start_date)) &
                 (df["date"] <= pd.to_datetime(end_date))]

# Titel
st.title(f"COVID-19 Dashboard für {country}")

# Diagramm
fig = px.line(df_filtered, x="date", y="new_cases", title="Neue Fälle pro Tag")
st.plotly_chart(fig)
