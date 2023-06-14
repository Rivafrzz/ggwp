import numpy as np
from sklearn.cluster import KMeans

# Contoh dataset baru
X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

# Membangun model K-Means dengan 2 klaster
kmeans = KMeans(n_clusters=2)

# Melatih model
kmeans.fit(X)

# Mendapatkan label klaster untuk setiap sampel dalam dataset
labels = kmeans.predict(X)

# Menampilkan label klaster
print(labels)
