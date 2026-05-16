import pandas as pd

from paths import DERIVED_RESULTS_DIR, RAW_RESULTS_DIR

input_file = RAW_RESULTS_DIR / 'nqueens27.csv'
output_file = DERIVED_RESULTS_DIR / 'ratio_n_linux_queens27.csv'

df = pd.read_csv(input_file, sep=';', header=None)
df[4] = df[4] / 1e6
df['new_column'] = df[4] / df[5]
df[4] = df[4].round(2)
df[5] = df[5].round(2)
df['new_column'] = df['new_column'].round(2)
df.to_csv(output_file, sep=';', header=False, index=False)
