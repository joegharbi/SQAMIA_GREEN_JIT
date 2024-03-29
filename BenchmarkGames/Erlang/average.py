import pandas as pd
import sys
import os

def process_csv(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file, sep=';', header=None, names=['col1', 'col2', 'col3', 'col4'])

    # Convert the 3rd column from microjoules to joules and round to 2 decimal places
    df['col3'] = df['col3'].apply(lambda x: round(x / 10**6, 2))

    # Round the 4th column to 2 decimal places
    df['col4'] = df['col4'].round(2)

    # Create a new column which is the ratio of the 3rd column to the 4th column
    df['new_col'] = df['col3'] / df['col4']

    # Round the 4th column to 2 decimal places
    df = df.round(2)

    # Check if the file exists and if it's empty
    file_exists = os.path.isfile(output_file)
    file_is_empty = file_exists and os.stat(output_file).st_size == 0

    # Open the file in append mode
    with open(output_file, 'a') as f:
        # If the file is empty, write the header
        if file_is_empty:
            f.write(';'.join(df.columns) + '\n')

        # Write the data
        for _, row in df.iterrows():
            f.write(';'.join(row.astype(str).values) + '\n')

# Get the input and output file names from the command-line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Process the CSV file
process_csv(input_file, output_file)
