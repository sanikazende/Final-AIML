import pandas as pd
from sklearn.datasets import load_breast_cancer

# Load Breast Cancer dataset
data = load_breast_cancer()

# Create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Display the first few rows of the DataFrame
print("First few rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check for duplicated rows
print("\nDuplicated rows:")
print(df.duplicated().sum())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Check the distribution of the target variable
print("\nDistribution of the target variable:")
print(df['target'].value_counts())

# Split the dataset into features and target variable
X = df.drop('target', axis=1)
y = df['target']

# Perform feature scaling if necessary
# Example:
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# Perform other preprocessing steps as required (e.g., encoding categorical variables, feature selection, etc.)

# Split the dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Your preprocessing steps may vary depending on the dataset and the machine learning task you are working on.