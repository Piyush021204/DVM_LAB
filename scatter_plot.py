import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# --- Create clustered data with positive correlation ---
x_cluster = np.random.normal(50, 10, 100)
y_cluster = x_cluster + np.random.normal(0, 5, 100)  # positive correlation

# --- Add another cluster ---
x_cluster2 = np.random.normal(20, 5, 50)
y_cluster2 = x_cluster2 + np.random.normal(0, 3, 50)

# --- Add outliers ---
x_outliers = np.array([100, 110, 120])
y_outliers = np.array([10, 5, 0])

# --- Combine all data ---
x = np.concatenate([x_cluster, x_cluster2, x_outliers])
y = np.concatenate([y_cluster, y_cluster2, y_outliers])

# --- Plot scatter ---
plt.scatter(x, y, color='blue')

# Highlight outliers in red
plt.scatter(x_outliers, y_outliers, color='red', label='Outliers')

# Labels and title
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot with Cluster, Correlation, and Outliers")
plt.legend()

plt.show()