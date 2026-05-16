import csv

from paths import DERIVED_RESULTS_DIR, SUMMARY_RESULTS_DIR

input_file = SUMMARY_RESULTS_DIR / 'data.csv'
output_file = DERIVED_RESULTS_DIR / 'normalized_data.csv'

with input_file.open('r') as file_handle:
    reader = csv.reader(file_handle, delimiter=';')
    data = list(reader)

c_values = {}
for row in data:
    if row[0] == 'c':
        condition = (row[1], int(row[2]))
        c_values[condition] = (float(row[3]), float(row[4]))

for row in data:
    condition = (row[1], int(row[2]))
    if condition in c_values:
        c_energy, c_runtime = c_values[condition]
        row[3] = str(float(row[3]) / c_energy if c_energy else 'NA')
        row[4] = str(float(row[4]) / c_runtime if c_runtime else 'NA')

with output_file.open('w', newline='') as file_handle:
    writer = csv.writer(file_handle, delimiter=';')
    writer.writerows(data)
