import pandas as pd

from paths import DERIVED_RESULTS_DIR, SUMMARY_RESULTS_DIR

column_names = ["Language", "Function", "Energy consumption in microjoules", "Runtime in seconds"]
input_file = SUMMARY_RESULTS_DIR / 'data.csv'
output_file = DERIVED_RESULTS_DIR / 'normalized_mean.csv'

df = pd.read_csv(input_file, names=column_names, sep=';')
numeric_columns = ["Energy consumption in microjoules", "Runtime in seconds"]
mean_df = df.groupby("Language")[numeric_columns].mean()
c_values = mean_df.loc['c']
normalized_df = mean_df / c_values
normalized_df.to_csv(output_file)
