import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [2, 3, 5, 7, 11]
}

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Dataset:")
print(df)

# Plot the data using matplotlib
plt.plot(df['x'], df['y'], marker='o')
plt.title('Sample Data')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
