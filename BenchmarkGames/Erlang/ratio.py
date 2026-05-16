import pandas as pd

from paths import DERIVED_RESULTS_DIR, RAW_RESULTS_DIR

input_file = RAW_RESULTS_DIR / 'benchmark27.csv'
output_file = DERIVED_RESULTS_DIR / 'ratio_linux27.csv'

df = pd.read_csv(input_file, sep=';', header=None)
df[1] = df[1] / 1e6
df['new_column'] = df[1] / df[2]
df[1] = df[1].round(3)
df[2] = df[2].round(3)
df['new_column'] = df['new_column'].round(5)
df.to_csv(output_file, sep=';', header=False, index=False)
