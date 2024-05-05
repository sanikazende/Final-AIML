import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_wine

# Load Wine dataset
wine = load_wine()
wine_df = pd.DataFrame(data=np.c_[wine['data'], wine['target']], columns=wine['feature_names'] + ['target'])

# Standardize the Wine dataset
wine_features = wine_df.drop('target', axis=1)
wine_features_scaled = StandardScaler().fit_transform(wine_features)

# K-means clustering for Wine dataset
kmeans_wine = KMeans(n_clusters=3, random_state=42)
wine_cluster_labels = kmeans_wine.fit_predict(wine_features_scaled)

# Add cluster labels to the dataset
wine_df['cluster'] = wine_cluster_labels

# Load Cars dataset
cars_df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data",
                      names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class'])

# Convert categorical variables to numerical
cars_df = pd.get_dummies(cars_df, columns=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety'])

# Standardize the Cars dataset
cars_features_scaled = StandardScaler().fit_transform(cars_df.drop('class', axis=1))

# K-means clustering for Cars dataset
kmeans_cars = KMeans(n_clusters=4, random_state=42)
cars_cluster_labels = kmeans_cars.fit_predict(cars_features_scaled)

# Add cluster labels to the dataset
cars_df['cluster'] = cars_cluster_labels

# Print cluster centers for both datasets
print("Wine dataset cluster centers:")
print(kmeans_wine.cluster_centers_)
print("\nCars dataset cluster centers:")
print(kmeans_cars.cluster_centers_)
