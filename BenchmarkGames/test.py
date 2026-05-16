import csv
import os
import subprocess
import timeit
from pathlib import Path

from paths import BASE_DIR

SKIP_DIRS = {'archive', 'results', 'generated', '__pycache__', '.git'}


def measure_runtime(lang_path: Path, function_folder: str, measurement_count: int = 10) -> float:
    runtimes = []

    for _ in range(measurement_count):
        start_time = timeit.default_timer()
        subprocess.run(['make', 'measure'], cwd=lang_path / function_folder, check=False)
        end_time = timeit.default_timer()
        runtimes.append(end_time - start_time)

    return sum(runtimes) / measurement_count


def main() -> None:
    for entry in sorted(BASE_DIR.iterdir()):
        if not entry.is_dir() or entry.name in SKIP_DIRS:
            continue

        makefile = entry / 'Makefile'
        if not makefile.is_file():
            continue

        results_dir = entry / 'results' / 'summary'
        results_dir.mkdir(parents=True, exist_ok=True)
        csv_file_path = results_dir / f'{entry.name}.csv'

        with csv_file_path.open('w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Function', 'Average Runtime'])

            for function_folder in sorted(os.listdir(entry)):
                function_path = entry / function_folder
                if function_path.is_dir() and function_folder not in SKIP_DIRS:
                    avg_runtime = measure_runtime(entry, function_folder)
                    csv_writer.writerow([function_folder, avg_runtime])

        print(f'Results for {entry.name} saved to {csv_file_path}')


if __name__ == '__main__':
    main()
