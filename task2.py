import pandas as pd 
import numpy as np 

# Creating a sample DataFrame with missing values 
data = { 
	'School ID': [101, 102, 103, np.nan, 105, 106, 107, 108], 
	'Name': ['Alice', 'Bob', 'Charlie', 'David', np.nan, 'Frank', 'Grace', 'Henry'], 
	'Address': ['123 Main Street',np.nan, '789 Pine Ln', '155 anji', np.nan, '222 Maple Rd', '444 Cedar Blvd', '555 Birch Dr'], 
	'City': ['Los Angeles', 'New York', 'Houston', 'Los Angeles', 'Miami', np.nan, 'Houston', 'New York'], 
	'Subject': ['Math', 'English', 'Science', 'Math', 'History', 'Math', 'Science', 'English'], 
	'Marks': [85, 92, 78, 85, np.nan, 92, 80, 88], 
	'Rank': [2, 1, 4, 3, 8, 1, 5, 3], 
	'Grade': ['B', 'A', 'C', 'B', 'D', 'A', 'C', 'B'] 
} 
df = pd.DataFrame(data) 
print("Sample DataFrame:") 
print(df)

df_cleaned = df.dropna() 
# Displaying the DataFrame after removing missing values 
print("\nDataFrame after removing rows with missing values:") 
print(df_cleaned)
mean_imputation = df['Marks'].fillna(df['Marks'].mean()) 
median_imputation = df['Marks'].fillna(df['Marks'].median()) 
mode_imputation = df['Marks'].fillna(df['Marks'].mode().iloc[0]) 
  
print("\nImputation using Mean:") 
print(mean_imputation) 
  
print("\nImputation using Median:") 
print(median_imputation) 
  
print("\nImputation using Mode:") 
print(mode_imputation)
dups = df.duplicated(['Marks'])
df[dups]