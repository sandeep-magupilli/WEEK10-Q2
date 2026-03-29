# Import pandas
import pandas as pd

# Create sample data (you can also read from CSV)
data = {
    'Name': ['Ram', 'Sita', 'John', 'Asha', 'David'],
    'Age': [23, 21, 25, 22, 24],
    'Marks': [85, 90, 78, 88, 82]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# -------------------------------
# Sorting Operations
# -------------------------------

# Sort by Age (ascending)
print("\nSorted by Age (Ascending):")
print(df.sort_values(by='Age'))

# Sort by Marks (descending)
print("\nSorted by Marks (Descending):")
print(df.sort_values(by='Marks', ascending=False))

# Sort by multiple columns
print("\nSorted by Age and Marks:")
print(df.sort_values(by=['Age', 'Marks']))

# -------------------------------
# Slicing Operations
# -------------------------------

# Slice first 3 rows
print("\nFirst 3 rows:")
print(df[0:3])

# Slice rows using iloc (index-based)
print("\nRows 1 to 3 using iloc:")
print(df.iloc[1:4])

# Slice specific columns
print("\nSelecting Name and Marks columns:")
print(df[['Name', 'Marks']])

# Slice rows and columns together
print("\nRows 0 to 2 and columns Name, Age:")
print(df.loc[0:2, ['Name', 'Age']])