import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_data():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "main_data.csv")

    df = pd.read_csv(file_path)

    season_map = {
        1: "Musim Semi",
        2: "Musim Panas",
        3: "Musim Gugur",
        4: "Musim Dingin"
    }

    weather_map = {
        1: "Cerah",
        2: "Berawan",
        3: "Hujan Kecil",
        4: "Hujan Besar/Salju"
    }

    if "season" in df.columns:
        df["season"] = df["season"].map(season_map)

    if "weathersit" in df.columns:
        df["weathersit"] = df["weathersit"].map(weather_map)

    return df