import argparse
import csv
import json
import subprocess
import sys
import time
import timeit

from paths import GENERATED_DIR, RAW_RESULTS_DIR, resolve_output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Measure process-level energy with Scaphandre on Linux.',
        epilog='GitHub repository: https://github.com/joegharbi/rosetta',
    )
    parser.add_argument('module', metavar='module', type=str, help='Provide the module.')
    parser.add_argument('function', metavar='function', type=str, help='Provide the function.')
    parser.add_argument('parameters', nargs='+', metavar='parameters', type=str, help='Provide one or more arguments.')
    parser.add_argument('-c', '--cmd', metavar='command', default='', type=str, help='Provide the command to run the program executable.')
    parser.add_argument('-e', '--exe', metavar='executable', default='beam.smp', type=str, help='Provide the process name without extension.')
    parser.add_argument('-r', '--rep', metavar='repetition', default=1, type=int, help='Provide the number of repetitions.')
    parser.add_argument('-f', '--file', metavar='file', default='', type=str, help='Provide the CSV file name.')
    args = parser.parse_args()

    module = args.module
    function = args.function
    parameters = args.parameters
    repetitions = args.rep
    result_file = args.file
    prog_lang = args.exe
    measure_cmd = args.cmd
    exe_prog_lang = f"{prog_lang}"

    for parameter in parameters:
        for _ in range(repetitions):
            file_name = f"{module}_{function}_{parameter}"
            json_file_path = GENERATED_DIR / f"{file_name}.json"
            command = f'scaphandre json -n 100000 -m 100 -f "{json_file_path}"'
            subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
            time.sleep(5)

            if measure_cmd == '':
                subprocess.Popen(f"erlc {module}.erl", shell=True)
                erl_command = f"erl -noshell -run {module} {function} {parameter} -s init stop"
            else:
                erl_command = measure_cmd

            print(erl_command)
            process = subprocess.Popen(erl_command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
            start_time = timeit.default_timer()
            process.wait()
            end_time = timeit.default_timer()
            runtime = end_time - start_time

            subprocess.run('pkill -f scaphandre', shell=True)
            subprocess.run('pkill -f erl', shell=True)

            with json_file_path.open('r') as file_handle:
                data = json.load(file_handle)

            total_server_consumption = 0.0
            number_samples = 0
            average_energy = 0
            for entry in data:
                consumers = entry.get('consumers', [])
                for consumer in consumers:
                    exe = consumer.get('exe', '')
                    consumption = consumer.get('consumption', 0.0)
                    if exe_prog_lang in exe.lower():
                        total_server_consumption += consumption
                        number_samples += 1

            if number_samples != 0:
                average_energy = total_server_consumption / number_samples

            final_consumption = average_energy * runtime
            if result_file == '':
                result_file = f"{prog_lang}_{module}"
            output_file = resolve_output_path(f"linux_{result_file}.csv", RAW_RESULTS_DIR)
            with output_file.open('a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=';')
                csv_writer.writerow([module, function, parameter, number_samples, final_consumption, runtime])

    sys.exit()
