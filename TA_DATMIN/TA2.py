import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Persiapan Data (contoh data sederhana)
data = {
    'ID Pelanggan': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Jumlah Pembelian': [5, 10, 2, 8, 4, 9, 6, 3, 1, 7]
}
df = pd.DataFrame(data)

# Analisis Klastering menggunakan K-means
jumlah_klaster = 3
kmeans = KMeans(n_clusters=jumlah_klaster)
df['Klaster'] = kmeans.fit_predict(df[['Jumlah Pembelian']])

# Visualisasi hasil klastering
plt.scatter(df['ID Pelanggan'], df['Jumlah Pembelian'], c=df['Klaster'], cmap='rainbow')
plt.xlabel('ID Pelanggan')
plt.ylabel('Jumlah Pembelian')
plt.title('Klaster Data Penjualan Produk')
plt.show()
