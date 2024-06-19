import pandas as pd

# Load the CSV file into a DataFrame
file_path = r"C:\Users\shivansh\Downloads\grocery_items.csv"
df = pd.read_csv(file_path)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Filter items where the quantity is greater than 5
filtered_df = df[df['Quantity'] > 5]
print("\nFiltered DataFrame (Quantity > 5):")
print(filtered_df)

# Fill missing values with a specific value, e.g., 0
df_filled = df.fillna(0)
print("\nDataFrame with Filled Missing Values:")
print(df_filled)

# Drop rows with any missing values
df_dropped = df.dropna()
print("\nDataFrame with Dropped Rows (No Missing Values):")
print(df_dropped)

# Calculate summary statistics
summary_statistics = df.describe()
print("\nSummary Statistics:")
print(summary_statistics)
