import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# CONFIG
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")


# LOAD DATA
@st.cache_data
def load_data():
    base_path = os.path.dirname(__file__)

    # beberapa kemungkinan path (biar anti error)
    possible_paths = [
        os.path.join(base_path, "main_data.csv"),      # dashboard/
        os.path.join(base_path, "../main_data.csv"),   # submission/
        "main_data.csv"                                # fallback lokal
    ]

    for path in possible_paths:
        if os.path.exists(path):
            df = pd.read_csv(path)

            # Mapping Season
            season_map = {
                1: "Musim Semi",
                2: "Musim Panas",
                3: "Musim Gugur",
                4: "Musim Dingin"
            }

            # Mapping Weather
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

    st.error("❌ main_data.csv tidak ditemukan. Pastikan file ada di folder dashboard/")
    st.stop()


df = load_data()


# TITLE
st.title("Bike Sharing Dashboard")
st.markdown("Analisis penyewaan sepeda berdasarkan waktu, musim, dan kondisi cuaca")


# SIDEBAR FILTER
st.sidebar.header("Filter Data")

if "season" in df.columns:
    season = st.sidebar.multiselect(
        "Pilih Musim",
        df["season"].dropna().unique(),
        default=df["season"].dropna().unique()
    )
    df = df[df["season"].isin(season)]

if "weathersit" in df.columns:
    weather = st.sidebar.multiselect(
        "Pilih Cuaca",
        df["weathersit"].dropna().unique(),
        default=df["weathersit"].dropna().unique()
    )
    df = df[df["weathersit"].isin(weather)]


# KPI
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Penyewaan", int(df["cnt"].sum()))
col2.metric("Rata-rata Penyewaan", round(df["cnt"].mean(), 2))
col3.metric("Penyewaan Tertinggi", int(df["cnt"].max()))


# GRAFIK JAM
if "hr" in df.columns:
    st.subheader("Pola Penyewaan per Jam")

    fig, ax = plt.subplots()
    df.groupby("hr")["cnt"].mean().plot(kind="line", ax=ax)

    ax.set_xlabel("Jam")
    ax.set_ylabel("Rata-rata Penyewaan")

    st.pyplot(fig)


# GRAFIK CUACA
if "weathersit" in df.columns:
    st.subheader("Pengaruh Cuaca")

    fig2, ax2 = plt.subplots()
    sns.barplot(x="weathersit", y="cnt", data=df, ax=ax2)

    ax2.set_xlabel("Kondisi Cuaca")
    ax2.set_ylabel("Jumlah Penyewaan")

    st.pyplot(fig2)


# GRAFIK MUSIM
if "season" in df.columns:
    st.subheader("Penyewaan Berdasarkan Musim")

    fig3, ax3 = plt.subplots()
    sns.barplot(x="season", y="cnt", data=df, ax=ax3)

    ax3.set_xlabel("Musim")
    ax3.set_ylabel("Jumlah Penyewaan")

    st.pyplot(fig3)


# DATA
st.subheader("Preview Data")
st.dataframe(df.head())