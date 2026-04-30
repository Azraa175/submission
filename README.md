# Bike Sharing Data Analysis Dashboard

## Deskripsi Proyek

Proyek ini merupakan analisis data end-to-end menggunakan **Bike Sharing Dataset** dengan tujuan memahami pola penyewaan sepeda berdasarkan waktu dan kondisi cuaca. Analisis dilakukan melalui tahapan data wrangling, exploratory data analysis (EDA), serta visualisasi data.

Hasil analisis kemudian disajikan dalam bentuk **dashboard interaktif menggunakan Streamlit** untuk memudahkan eksplorasi data dan penyampaian insight.

---

## Menentukan Pertanyaan Bisnis

Analisis ini difokuskan untuk menjawab beberapa pertanyaan berikut:

1. Bagaimana tren dan perbandingan performa penyewaan sepeda pada setiap bulan antara tahun 2011 dan 2012?
2. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda harian, dan kondisi cuaca mana yang menghasilkan penyewaan tertinggi?

---

## Proses Analisis Data

### 1. Data Wrangling

* **Gathering Data**: Mengambil dataset dari sumber yang tersedia (Bike Sharing Dataset)
* **Assessing Data**: Mengidentifikasi permasalahan seperti missing values, duplicate data, dan outlier
* **Cleaning Data**: Melakukan pembersihan data untuk memastikan kualitas data yang digunakan

### 2. Exploratory Data Analysis (EDA)

* Menganalisis pola penyewaan sepeda berdasarkan waktu (bulanan)
* Menganalisis pengaruh kondisi cuaca terhadap jumlah penyewaan

### 3. Visualization & Explanatory Analysis

* Visualisasi tren penyewaan sepeda per bulan
* Visualisasi pengaruh kondisi cuaca terhadap jumlah penyewaan

---

## Insight Utama

* Terjadi peningkatan jumlah penyewaan sepeda dari tahun 2011 ke 2012
* Pola penyewaan menunjukkan tren musiman dengan puncak pada bulan tertentu
* Kondisi cuaca cerah (Clear) menghasilkan jumlah penyewaan tertinggi
* Cuaca buruk seperti hujan lebat menurunkan jumlah penyewaan secara signifikan

---

## Rekomendasi

* Meningkatkan jumlah sepeda dan kesiapan operasional pada bulan dengan permintaan tinggi
* Mengoptimalkan layanan saat kondisi cuaca cerah
* Mengantisipasi penurunan permintaan saat cuaca buruk dengan strategi alternatif (misalnya promosi)

---

## Teknologi yang Digunakan

* Python
* Pandas
* Matplotlib
* Seaborn
* Streamlit

---

## Struktur Direktori

```
submission/
├── dashboard/
│   ├── main_data.csv
│   └── dashboard.py
├── data/
│   ├── day.csv
│   └── hour.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

## Cara Menjalankan Dashboard

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Jalankan dashboard:

```
cd dashboard
streamlit run dashboard.py
```

3. Buka browser di:

```
http://localhost:8501
```

---

## Akses Dashboard (Opsional)

Tambahkan link berikut jika dashboard sudah di-deploy:

```
https://your-dashboard-link.streamlit.app
```

---

## Dataset

Dataset yang digunakan adalah **Bike Sharing Dataset**, yang berisi informasi penyewaan sepeda berdasarkan waktu, musim, dan kondisi cuaca.

---

## Fitur Dashboard

* Filter interaktif berdasarkan musim dan kondisi cuaca
* Visualisasi tren penyewaan per bulan
* Analisis pengaruh cuaca terhadap penyewaan
* Penyajian metrik utama (KPI)

---
