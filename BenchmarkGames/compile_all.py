import os
import subprocess
import sys
from pathlib import Path

from paths import BASE_DIR

SKIP_DIRS = {'archive', 'results', 'generated', '__pycache__', '.git'}
VALID_ACTIONS = {'compile', 'run', 'clean'}


def main(action: str) -> None:
    for root, dirs, _ in os.walk(BASE_DIR):
        dirs[:] = [directory for directory in dirs if directory not in SKIP_DIRS]
        root_path = Path(root)
        print(f'Checking {root_path.relative_to(BASE_DIR)}')
        makefile = root_path / 'Makefile'

        if makefile.is_file():
            completed = subprocess.run(
                ['make', action],
                cwd=root_path,
                capture_output=True,
                text=True,
            )

            if action in VALID_ACTIONS:
                if completed.returncode != 0:
                    print(f'[E] Error on {root_path}:')
                    print(completed.stderr.strip())
                else:
                    print('[OK]')


if __name__ == '__main__':
    action = 'compile'
    if len(sys.argv) == 2:
        candidate_action = sys.argv[1]
        if candidate_action in VALID_ACTIONS:
            print(f'Performing "{candidate_action}" action...')
            action = candidate_action
        else:
            print(f'Error: Unrecognized action "{candidate_action}"')
            sys.exit(1)
    else:
        print('Performing "compile" action...')

    main(action)
