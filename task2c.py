import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Alice'],
    'Age': [25, 30, 35, 25, 30, 25],
    'Score': [80, 90, 85, 88, 92, 82]
}

# Create DataFrame
df = pd.DataFrame(data)

# Filtering data
filtered_data = df[df['Age'] > 25]

# Sorting data
sorted_data = df.sort_values(by='Score', ascending=False)

# Grouping data
grouped_data = df.groupby('Name').agg({'Age': 'mean', 'Score': 'max'})

print("Filtered Data:")
print(filtered_data)

print("\nSorted Data:")
print(sorted_data)

print("\nGrouped Data:")
print(grouped_data)
