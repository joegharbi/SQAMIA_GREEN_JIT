import os
import subprocess
import csv
import timeit

def file_exists(file_path):
    return os.path.isfile(file_path) if file_path else False

def measure_runtime(lang_path, function_folder, measurement_count=10):
    runtimes = []

    for _ in range(measurement_count):
        start_time = timeit.default_timer()
        subprocess.run(['make', 'measure'], cwd=os.path.join(lang_path, function_folder))
        end_time = timeit.default_timer()
        runtimes.append(end_time - start_time)

    avg_runtime = sum(runtimes) / measurement_count
    return avg_runtime

def main():
    path = '.'  # Current directory as the root path

    for root, dirs, files in os.walk(path):
        for lang_folder in dirs:
            lang_path = os.path.join(root, lang_folder)
            # print(lang_path)
            makefile = os.path.join(lang_path, "Makefile")
            # print (makefile)

            if file_exists(makefile):
                print ("makefile" + makefile)
                csv_file_path = os.path.join(f'{lang_folder}.csv')
                print(csv_file_path)

                with open(csv_file_path, 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(['Function', 'Average Runtime'])

                    for function_folder in os.listdir(os.path.join(lang_path)):
                        if os.path.isdir(os.path.join(lang_path, function_folder)):
                            avg_runtime = measure_runtime(lang_path, function_folder)

                            # Write the results to CSV
                            csv_writer.writerow([function_folder, avg_runtime])

                    print(f'Results for {lang_folder} saved to {csv_file_path}')

if __name__ == '__main__':
    main()
