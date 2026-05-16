import csv
import json
import os
import subprocess
import sys
import time
import timeit
from pathlib import Path

from paths import BASE_DIR, RAW_RESULTS_DIR

ACTION = 'compile'
SKIP_DIRS = {'archive', 'results', 'generated', '__pycache__'}


def main() -> None:
    for root, dirs, _ in os.walk(BASE_DIR):
        dirs[:] = [directory for directory in dirs if directory not in SKIP_DIRS]
        root_path = Path(root)
        print(f'Checking {root_path.relative_to(BASE_DIR)}')
        makefile = root_path / 'Makefile'

        if makefile.is_file():
            start_time = timeit.default_timer()
            completed = subprocess.run(
                ['make', ACTION],
                cwd=root_path,
                capture_output=True,
                text=True,
            )
            end_time = timeit.default_timer()
            runtime = end_time - start_time - 10

            if ACTION in {'compile', 'run', 'clean'}:
                if completed.returncode != 0:
                    print(f'[E] Error on {root_path}:')
                    print(completed.stderr.strip())
                else:
                    print('[OK]')
            elif ACTION == 'measure' and root_path != BASE_DIR:
                json_files = sorted(root_path.glob('*.json'))
                if not json_files:
                    continue

                with json_files[0].open('r') as file:
                    data = json.load(file)

                total_server_consumption = 0.0
                number_samples = 0
                for entry in data:
                    consumers = entry.get('consumers', [])
                    for consumer in consumers:
                        exe = consumer.get('exe', '')
                        consumption = consumer.get('consumption', 0.0)
                        if 'beam.smp' in exe.lower() and consumption != 0.0:
                            total_server_consumption += consumption
                            number_samples += 1

                total_consumption = total_server_consumption / number_samples if number_samples else 0
                final_consumption = total_consumption * runtime
                output_file = RAW_RESULTS_DIR / 'output.csv'
                with output_file.open('a', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file, delimiter=';')
                    csv_writer.writerow([root_path.name, final_consumption, runtime])
                time.sleep(5)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        candidate_action = sys.argv[1]
        if candidate_action in {'compile', 'run', 'clean', 'measure'}:
            print(f'Performing "{candidate_action}" action...')
            ACTION = candidate_action
        else:
            print(f'Error: Unrecognized action "{candidate_action}"')
            sys.exit(1)
    else:
        print('Performing "compile" action...')

    main()
