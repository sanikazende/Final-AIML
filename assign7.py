import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.naive_bayes import GaussianNB
import requests

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
response = requests.get(url)

# Save downloaded dataset as 'IRIS.csv'
with open("IRIS.csv", "wb") as f:
    f.write(response.content)
    
# Load the dataset
df = pd.read_csv('IRIS.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

# Encode the target variable
le = LabelEncoder()
df['species'] = le.fit_transform(df['species'])

# Separate features and target variable
X = df.iloc[:, :4]
y = df['species']

# Standardize features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
X_validate, X_test, y_validate, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Train the Gaussian Naive Bayes model
bayes = GaussianNB()
bayes.fit(X_train, y_train)

# Validate the model
validation_score = bayes.score(X_validate, y_validate)
test_score = bayes.score(X_test, y_test)

print("Validation Score:", validation_score)
print("Test Score:", test_score)
