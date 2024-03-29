import pandas as pd

# Specify the column names
column_names = ["Language", "Function", "Energy consumption in microjoules", "Runtime in seconds"]

# Read the CSV file
df = pd.read_csv('data.csv', names=column_names, sep=';')

# Group by the language and function, then calculate the mean of the numeric columns
mean_df = df.groupby(["Language", "Function"]).mean()

# Get the values for 'C'
c_values = mean_df.loc['c']

# Normalize the data compared to 'C' for each function
normalized_df = mean_df / c_values

# Reset the index to make 'Language' and 'Function' regular columns again
normalized_df.reset_index(inplace=True)

# Save the normalized DataFrame to a CSV file
normalized_df.to_csv('normalized_file3.csv', index=False)
