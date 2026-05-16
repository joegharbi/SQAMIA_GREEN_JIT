import os
import subprocess
import sys
from pathlib import Path

from paths import BASE_DIR

ACTION = 'compile'
SKIP_DIRS = {'archive', 'results', '__pycache__', '.git'}


def file_exists(file_path: Path) -> bool:
    return file_path.is_file()


def main() -> None:
    for root, dirs, _ in os.walk(BASE_DIR):
        dirs[:] = [directory for directory in dirs if directory not in SKIP_DIRS]
        root_path = Path(root)
        print(f'Checking {root_path.relative_to(BASE_DIR)}')
        makefile = root_path / 'Makefile'

        if file_exists(makefile):
            completed = subprocess.run(
                ['make', ACTION],
                cwd=root_path,
                capture_output=True,
                text=True,
            )

            if ACTION in {'compile', 'run', 'clean'}:
                if completed.returncode != 0:
                    print(f'[E] Error on {root_path}:')
                    print(completed.stderr.strip())
                else:
                    print('[OK]')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        candidate_action = sys.argv[1]
        if candidate_action in {'compile', 'run', 'clean'}:
            print(f'Performing "{candidate_action}" action...')
            ACTION = candidate_action
        else:
            print(f'Error: Unrecognized action "{candidate_action}"')
            sys.exit(1)
    else:
        print('Performing "compile" action...')

    main()
