# Import library yang dibutuhkan
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Membuat dataset
X = np.array([[2.0, 3.0], [5.0, 4.0], [3.0, 7.0], [8.0, 1.0], [7.0, 2.0], [1.0, 5.0]])
y = np.array(['A', 'B', 'B', 'A', 'B', 'A'])

# Membagi dataset menjadi data training dan data testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inisialisasi objek KNN dengan nilai k = 3
knn = KNeighborsClassifier(n_neighbors=3)

# Melatih model KNN dengan data training
knn.fit(X_train, y_train)

# Memprediksi label dari data testing
y_pred = knn.predict(X_test)

# Menghitung akurasi dari model KNN
accuracy = accuracy_score(y_test, y_pred)
print("Akurasi model KNN:", accuracy)
