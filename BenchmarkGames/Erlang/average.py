import os
import sys

import pandas as pd

from paths import DERIVED_RESULTS_DIR, RAW_RESULTS_DIR, SUMMARY_RESULTS_DIR, resolve_input_path, resolve_output_path


def process_csv(input_file: str, output_file: str) -> None:
    input_path = resolve_input_path(input_file, RAW_RESULTS_DIR, SUMMARY_RESULTS_DIR, DERIVED_RESULTS_DIR)
    output_path = resolve_output_path(output_file, DERIVED_RESULTS_DIR)

    df = pd.read_csv(input_path, sep=';', header=None, names=['col1', 'col2', 'col3', 'col4'])
    df['col3'] = df['col3'].apply(lambda x: round(x / 10**6, 2))
    df['col4'] = df['col4'].round(2)
    df['new_col'] = df['col3'] / df['col4']
    df = df.round(2)

    file_exists = os.path.isfile(output_path)
    file_is_empty = file_exists and os.stat(output_path).st_size == 0

    with output_path.open('a') as file_handle:
        if file_is_empty:
            file_handle.write(';'.join(df.columns) + '\n')
        for _, row in df.iterrows():
            file_handle.write(';'.join(map(str, row.tolist())) + '\n')


input_file = sys.argv[1]
output_file = sys.argv[2]
process_csv(input_file, output_file)
