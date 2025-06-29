import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dan persiapan data
df = pd.read_csv("dashboard/main_data.csv")
df['date'] = pd.to_datetime(df['date'])

# Filter data jika perlu (sementara ini ambil semua)
filtered_day_df = df.copy()

# Judul dashboard
st.title("🚲 Bike Rental Dashboard")
st.markdown("#### Analysis of bike rental data from 2011–2012")

# Menghitung metrik utama
total_bike_sharing = filtered_day_df['casual'].sum() + filtered_day_df['registered'].sum()
total_casual_users = filtered_day_df['casual'].sum()
total_registered_users = filtered_day_df['registered'].sum()

# Menampilkan metrik utama
col1, col2, col3 = st.columns(3)
col1.metric("Total Bike Rentals", f"{total_bike_sharing:,}")
col2.metric("Total Casual Users", f"{total_casual_users:,}")
col3.metric("Total Registered Users", f"{total_registered_users:,}")

st.markdown("---")

# 1. Tren Penyewaan Sepeda Bulanan
st.subheader("📈 1. Tren Penyewaan Sepeda Bulanan (2011–2012)")
trends_data = filtered_day_df.groupby(['year', 'month'], observed=False)['count'].sum().reset_index()
trends_data['year_month'] = trends_data['year'].astype(str) + '-' + trends_data['month'].astype(str).str.zfill(2)

plt.figure(figsize=(12, 6))
plt.plot(trends_data['year_month'], trends_data['count'], marker='o', color='teal', linewidth=2)
plt.title('Tren Penyewaan Sepeda (2011–2012)', fontsize=16, fontweight='bold')
plt.xlabel('Bulan dan Tahun', fontsize=12)
plt.ylabel('Jumlah Penyewaan', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.grid(visible=True, linestyle='--', alpha=0.5)
plt.tight_layout()
st.pyplot(plt)

st.markdown("---")

# 2. Rata-rata Penyewaan Berdasarkan Musim
st.subheader("🍁 2. Rata-rata Penyewaan Berdasarkan Musim")
plt.figure(figsize=(10, 6))
sns.barplot(
    data=filtered_day_df,
    x='season',
    y='count',
    hue='season',
    estimator='mean',
    palette='viridis',
    edgecolor='black',
    legend=False
)
plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Musim', fontsize=16, fontweight='bold')
plt.xlabel('Musim', fontsize=12)
plt.ylabel('Rata-rata Jumlah Penyewa', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
st.pyplot(plt)

st.markdown("---")

# 3. Rata-rata Penyewaan Berdasarkan Kondisi Cuaca
st.subheader("⛅ 3. Rata-rata Penyewaan Berdasarkan Kondisi Cuaca")
plt.figure(figsize=(10, 6))
sns.barplot(
    data=filtered_day_df,
    x='weather',
    y='count',
    hue='weather',
    estimator='mean',
    palette='cubehelix',
    edgecolor='black',
    legend=False
)
plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca', fontsize=16, fontweight='bold')
plt.xlabel('Kondisi Cuaca', fontsize=12)
plt.ylabel('Rata-rata Jumlah Penyewa', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
st.pyplot(plt)

st.markdown("")