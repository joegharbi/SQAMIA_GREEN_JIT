import os
import sys

import pandas as pd

from paths import RAW_RESULTS_DIR, SUMMARY_RESULTS_DIR, resolve_input_path, resolve_output_path

input_file = sys.argv[1]
output_file = sys.argv[2]
input_path = resolve_input_path(input_file, RAW_RESULTS_DIR, SUMMARY_RESULTS_DIR, DERIVED_RESULTS_DIR)
output_path = resolve_output_path(output_file, SUMMARY_RESULTS_DIR)

df = pd.read_csv(input_path, delimiter=';')
df.iloc[:, 4] = df.iloc[:, 4] / 1e6
df['new_column'] = df.iloc[:, 3] / df.iloc[:, 4]
df = df.drop(df.columns[3], axis=1)
grouped_df = df.groupby(df.columns.tolist()[:3]).mean().reset_index()
grouped_df = grouped_df.round(2)

file_exists = os.path.isfile(output_path)
file_is_empty = file_exists and os.stat(output_path).st_size == 0

with output_path.open('a') as file_handle:
    if file_is_empty:
        file_handle.write(';'.join(grouped_df.columns) + '\n')
    for _, row in grouped_df.iterrows():
        file_handle.write(';'.join(map(str, row.tolist())) + '\n')
