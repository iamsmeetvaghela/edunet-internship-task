import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


# 1. Load the Dataset

# We select the climate change impact dataset for its relevance to sustainability
file_path = 'climate_change_impact_on_agriculture_2024.csv'
df = pd.read_csv(file_path)


# 2. Data Cleaning & Feature Selection

# Selecting columns relevant to environmental sustainability and impact
features = ['CO2_Emissions_MT', 'Crop_Yield_MT_per_HA', 'Economic_Impact_Million_USD']
clustering_data = df[features].copy()

# Drop any potential missing values to ensure the distance algorithm runs smoothly
clustering_data = clustering_data.dropna()

 
# 3. Exploratory Data Analysis (EDA)

# Visualizing the relationships between our selected metrics using seaborn
plt.figure(figsize=(10, 6))
sns.pairplot(clustering_data, diag_kind='kde', corner=True)
plt.suptitle('Pairplot of Sustainability Features', y=1.02)
plt.show()


# 4. Data Preprocessing

# K-Means is a distance-based algorithm. Features with larger numeric ranges 
# (like Economic Impact) will dominate features with smaller ranges (like Crop Yield).
# We scale features to have a mean of 0 and a variance of 1.
scaler = StandardScaler()
scaled_data = scaler.fit_transform(clustering_data)


# 5. Finding Optimal Clusters (Elbow Method)

inertia = []
cluster_range = range(2, 11)

for k in cluster_range:
    kmeans_temp = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans_temp.fit(scaled_data)
    inertia.append(kmeans_temp.inertia_)

# Plotting the Elbow Curve to visually identify the best 'k'
plt.figure(figsize=(8, 5))
plt.plot(cluster_range, inertia, marker='o', linestyle='--')
plt.title('Elbow Method For Optimal k')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia (Within-Cluster Sum of Squares)')
plt.grid(True)
plt.show()

# 6. Apply K-Means Clustering Algorithm

# Based on general dataset variance, we will use k=3 (adjust based on your visual elbow plot)
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)

# Fit the model and assign the cluster labels back to our dataframe
clustering_data['Cluster'] = kmeans.fit_predict(scaled_data)

# Visualizing the final clusters (Comparing CO2 Emissions vs Economic Impact)
plt.figure(figsize=(8, 6))
sns.scatterplot(
    x=clustering_data['CO2_Emissions_MT'], 
    y=clustering_data['Economic_Impact_Million_USD'], 
    hue=clustering_data['Cluster'], 
    palette='viridis',
    alpha=0.7
)
plt.title(f'K-Means Clustering (k={optimal_k})')
plt.show()


# 7. Model Evaluation

# The Silhouette Score evaluates how well-defined the clusters are.
# It ranges from -1 to 1. Scores closer to 1 indicate dense, well-separated clusters.
sil_score = silhouette_score(scaled_data, clustering_data['Cluster'])
print(f"Model Evaluation - Silhouette Score (k={optimal_k}): {sil_score:.4f}")


# in out put -: Model Evaluation - Silhouette Score (k=3): 0.3209