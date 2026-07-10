import pandas as pd

print("--- Loading Data ---")
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
print("Data loaded successfully!\n")

# 1. head() - Show the first 5 rows
print("1. METHOD: head()")
print(df.head())
print("-" * 50 + "\n")

# 2. info() - Get a summary of columns and data types
print("2. METHOD: info()")
df.info()  # info() prints to the console automatically
print("-" * 50 + "\n")

# 3. describe() - Get statistical summary of numerical columns (Age, Fare, etc.)
print("3. METHOD: describe()")
print(df.describe())
print("-" * 50 + "\n")

# 4. shape - Get the number of rows and columns (Rows, Columns)
print("4. ATTRIBUTE: shape")
print(f"Dataset shape: {df.shape}")
print("-" * 50 + "\n")

# 5. columns - List all column names
print("5. ATTRIBUTE: columns")
print(df.columns)
print("-" * 50 + "\n")

# 6. sort_values() - Sort the data by passenger Fare (highest to lowest)
print("6. METHOD: sort_values() (Sorting by Fare descending)")
sorted_df = df.sort_values(by='Fare', ascending=False)
print(sorted_df[['Name', 'Fare']].head())
print("-" * 50 + "\n")

# 7. isnull().sum() - Count missing values in each column
print("7. METHOD: isnull().sum()")
print(df.isnull().sum())
print("-" * 50 + "\n")

# 8. value_counts() - Count how many males vs females were on board
print("8. METHOD: value_counts() (Count by Sex)")
print(df['Sex'].value_counts())
print("-" * 50 + "\n")

# 9. groupby() and mean() - Find the average survival rate for each gender
print("9. METHOD: groupby() with mean() (Survival rate by Sex)")
print(df.groupby('Sex')['Survived'].mean())
print("-" * 50 + "\n")

# 10. to_excel() - Save this dataframe into an Excel file on your computer
print("10. METHOD: to_excel()")

try:
    df.to_excel('titanic_output.xlsx', index=False)
    print("Success! Created 'titanic_output.xlsx' in your current folder.")
except ImportError:
    print("Could not save to Excel because 'openpyxl' is not installed.")
    print("Run: pip install openpyxl")
print("-" * 50 + "\n")


# OR


import numpy as np

print("--- Creating a Multidimensional Array ---")
# Creating a 3x4 array (3 rows, 4 columns)
matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
print("Original 3x4 Matrix:")
print(matrix)
print("-" * 50 + "\n")

print("---Indexing and Mathematical Operations ---")
# Accessing specific values using [row, column] index (0-based indexing)
val1 = matrix[0, 1]  # Row 0, Column 1 (Value: 20)
val2 = matrix[2, 3]  # Row 2, Column 3 (Value: 120)

print(f"Accessed Value 1 (Row 0, Col 1): {val1}")
print(f"Accessed Value 2 (Row 2, Col 3): {val2}")

addition = val1 + val2
multiplication = val1 * 5

print(f"Math Operation (Addition): {val1} + {val2} = {addition}")
print(f"Math Operation (Multiplication): {val1} * 5 = {multiplication}")
print("-" * 50 + "\n")

print("---Applying 15 NumPy Methods ---")

# 1. np.ndim() - Get the number of dimensions
print(f"1. ndim (Dimensions): {np.ndim(matrix)}")

# 2. np.shape() - Get rows and columns
print(f"2. shape (Rows, Columns): {np.shape(matrix)}")

# 3. np.size() - Get total number of elements
print(f"3. size (Total elements): {np.size(matrix)}")

# 4. np.sum() - Get the sum of all elements
print(f"4. sum: {np.sum(matrix)}")

# 5. np.mean() - Get the average value of the array
print(f"5. mean (Average): {np.mean(matrix)}")

# 6. np.max() - Find the highest value
print(f"6. max (Highest value): {np.max(matrix)}")

# 7. np.min() - Find the lowest value
print(f"7. min (Lowest value): {np.min(matrix)}")

# 8. np.std() - Calculate the standard deviation
print(f"8. std (Standard Deviation): {np.std(matrix):.2f}")

# 9. np.reshape() - Change the shape of the array (converting 3x4 to 2x6)
reshaped_matrix = np.reshape(matrix, (2, 6))
print("9. reshape (Converted to 2x6):")
print(reshaped_matrix)

# 10. np.transpose() - Flip rows and columns (T)
transposed_matrix = np.transpose(matrix)
print("10. transpose (Rows become columns):")
print(transposed_matrix)

# 11. np.flatten() - Collapse multidimensional array into 1D
flat_array = matrix.flatten()
print(f"11. flatten (Converted to 1D): {flat_array}")

# 12. np.sqrt() - Calculate the square root of each element
# Using flat_array to keep the output readable
print(f"12. sqrt (Square roots of first 3 elements): {np.sqrt(flat_array[:3])}")

# 13. np.square() - Square each element
small_arr = np.array([2, 3, 4])
print(f"13. square (Squaring [2, 3, 4]): {np.square(small_arr)}")

# 14. np.sort() - Sort an un-ordered array
unsorted_arr = np.array([45, 12, 89, 5])
print(f"14. sort (Sorting [45, 12, 89, 5]): {np.sort(unsorted_arr)}")

# 15. np.where() - Return indexes where a condition is met
# Finding elements in flat_array that are greater than 80
indices = np.where(flat_array > 80)
print(f"15. where (Indices where value > 80): {indices[0]}")

print("-" * 50 + "\n")
print("All tasks completed successfully!")