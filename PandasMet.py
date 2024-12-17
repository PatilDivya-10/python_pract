import pandas as pd
import numpy as np

# 1. DATA CREATION AND INITIALIZATION
# Creating DataFrames and Series
data_dict = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
             'Age': [25, 30, 35, 40],
             'City': ['NY', 'LA', 'Chicago', 'Houston']}
df = pd.DataFrame(data_dict)
print("Initial DataFrame:\n", df)

# Creating Series
series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("Series:\n", series)

# Creating DataFrame with Random Data
random_df = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
print("Random DataFrame:\n", random_df)

# 2. VIEWING AND INSPECTING DATA
print("\nHead of DataFrame:\n", df.head(2))
print("Tail of DataFrame:\n", df.tail(2))
print("Info of DataFrame:\n", df.info())
print("Describe DataFrame:\n", df.describe())

# Column and Index Names
print("Columns:", df.columns)
print("Index:", df.index)

# 3. DATA MANIPULATION
# Adding a New Column
df['Salary'] = [5000, 6000, 7000, 8000]
print("\nDataFrame After Adding New Column:\n", df)

# Modifying Existing Column
df['Age'] = df['Age'] + 5
print("DataFrame After Modifying 'Age':\n", df)

# Dropping Columns and Rows
df_dropped = df.drop(['City'], axis=1)
print("DataFrame After Dropping Column 'City':\n", df_dropped)

df_dropped_row = df.drop(1, axis=0)
print("DataFrame After Dropping Row 1:\n", df_dropped_row)

# Renaming Columns
df_renamed = df.rename(columns={'Salary': 'Income'})
print("Renamed DataFrame:\n", df_renamed)

# Sorting
df_sorted = df.sort_values(by='Income', ascending=False)
print("Sorted DataFrame by 'Income':\n", df_sorted)

# 4. HANDLING MISSING DATA
df_with_nan = df.copy()
df_with_nan.loc[1, 'Age'] = np.nan
print("\nDataFrame with Missing Data:\n", df_with_nan)

# Detecting NaN
print("Check for NaN:\n", df_with_nan.isnull())

# Filling Missing Values
filled_df = df_with_nan.fillna(30)
print("DataFrame After Filling Missing Values:\n", filled_df)

# Dropping Missing Values
dropped_df = df_with_nan.dropna()
print("DataFrame After Dropping Rows with NaN:\n", dropped_df)

# 5. STATISTICAL OPERATIONS
print("\nMean of 'Age':", df['Age'].mean())
print("Median of 'Age':", df['Age'].median())
print("Sum of 'Income':", df['Salary'].sum())

# Min and Max
print("Min Age:", df['Age'].min())
print("Max Salary:", df['Salary'].max())

# Value Counts
print("Value Counts of Cities:\n", df['City'].value_counts())

# 6. GROUPING AND AGGREGATION
# Grouping by City
grouped = df.groupby('City').mean()
print("Grouped Data (Mean by City):\n", grouped)

# Aggregate Functions
agg_result = df.groupby('City')['Salary'].agg(['sum', 'mean'])
print("Aggregated Results:\n", agg_result)

# 7. MERGING, JOINING, AND CONCATENATION
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [25, 30, 35]})

# Merge
merged_df = pd.merge(df1, df2, on='ID', how='inner')
print("\nMerged DataFrame:\n", merged_df)

# Join
df_left = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['X', 'Y'])
df_right = pd.DataFrame({'C': [5, 6]}, index=['X', 'Y'])
joined_df = df_left.join(df_right)
print("Joined DataFrame:\n", joined_df)

# Concatenation
concat_df = pd.concat([df1, df2], axis=0, ignore_index=True)
print("Concatenated DataFrame:\n", concat_df)

# 8. INDEXING AND SLICING
print("\nSelecting Single Column:\n", df['Name'])
print("Selecting Rows by Index:\n", df.iloc[0:2])

# Conditional Selection
filtered_df = df[df['Age'] > 30]
print("Filtered DataFrame (Age > 30):\n", filtered_df)

# Setting Index
df_indexed = df.set_index('Name')
print("DataFrame with 'Name' as Index:\n", df_indexed)

# 9. DATA TRANSFORMATION
# Apply Function
df['Age_Squared'] = df['Age'].apply(lambda x: x ** 2)
print("\nDataFrame After Applying Lambda Function:\n", df)

# Map Function
df['Bonus'] = df['Salary'].map(lambda x: x * 0.1)
print("DataFrame After Mapping Function:\n", df)

# Replace Values
df_replaced = df.replace({'City': {'NY': 'New York'}})
print("Replaced 'City' Values:\n", df_replaced)

# 10. INPUT/OUTPUT OPERATIONS
# Saving to CSV
df.to_csv('output.csv', index=False)
print("\nDataFrame Saved to 'output.csv'")

# Reading CSV
loaded_df = pd.read_csv('output.csv')
print("Loaded DataFrame from CSV:\n", loaded_df)
