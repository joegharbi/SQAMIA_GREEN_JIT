import pandas as pd

# Read the CSV file
df = pd.read_csv('data.csv', sep=';', header=None)

# Convert the third column from microjoules to joules
df[2] = df[2] / 1e6

df[3] = df[3] * 1000

# Add a new column which is the result of the division of the 3rd column by the 4th column
df['new_column'] = df[2] / df[3]


df[2] = df[2].round(3)
df[3] = df[3].round(3)

# Round the values to three decimal places
df['new_column'] = df['new_column'].round(3)

# Save the updated DataFrame back to a CSV file
df.to_csv('ration1.csv', sep=';', header=False, index=False)
