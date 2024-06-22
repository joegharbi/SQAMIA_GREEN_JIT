import pandas as pd

# Read the CSV file
df = pd.read_csv('list16_both.csv', sep=';', header=None)

# Convert the third column from microjoules to joules
df[4] = df[4] / 1e6

# Add a new column which is the result of the division of the 3rd column by the 4th column
df['new_column'] = df[4] / df[5]

df[4] = df[4].round(2)
df[5] = df[5].round(2)

# Round the values to three decimal places
df['new_column'] = df['new_column'].round(2)

# Save the updated DataFrame back to a CSV file
df.to_csv('ratio_list16_both.csv', sep=';', header=False, index=False)