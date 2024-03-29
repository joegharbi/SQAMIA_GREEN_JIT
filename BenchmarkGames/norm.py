import pandas as pd

# Specify the column names
column_names = ["Language", "Function", "Energy consumption in microjoules", "Runtime in seconds"]

# Read the CSV file
df = pd.read_csv('data.csv', names=column_names, sep=';')

# Select only the numeric columns
numeric_columns = ["Energy consumption in microjoules", "Runtime in seconds"]

# Group by the language and calculate the mean of the numeric columns
mean_df = df.groupby("Language")[numeric_columns].mean()

# Get the values for 'C'
c_values = mean_df.loc['c']

# Normalize the data compared to 'C'
normalized_df = mean_df / c_values

# Save the normalized DataFrame to a CSV file
normalized_df.to_csv('normalized_file2.csv')
