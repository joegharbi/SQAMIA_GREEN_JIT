import pandas as pd

from paths import DERIVED_RESULTS_DIR, SUMMARY_RESULTS_DIR

input_file = SUMMARY_RESULTS_DIR / 'data.csv'
output_file = DERIVED_RESULTS_DIR / 'ration1.csv'

df = pd.read_csv(input_file, sep=';', header=None)
df[2] = df[2] / 1e6
df[3] = df[3] * 1000
df['new_column'] = df[2] / df[3]
df[2] = df[2].round(3)
df[3] = df[3].round(3)
df['new_column'] = df['new_column'].round(3)
df.to_csv(output_file, sep=';', header=False, index=False)
