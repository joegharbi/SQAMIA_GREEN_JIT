from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results"
RAW_RESULTS_DIR = RESULTS_DIR / "raw"
SUMMARY_RESULTS_DIR = RESULTS_DIR / "summary"
DERIVED_RESULTS_DIR = RESULTS_DIR / "derived"
ARCHIVE_DIR = BASE_DIR / "archive"
GENERATED_DIR = BASE_DIR / "generated"

for directory in (RAW_RESULTS_DIR, SUMMARY_RESULTS_DIR, DERIVED_RESULTS_DIR, ARCHIVE_DIR, GENERATED_DIR):
    directory.mkdir(parents=True, exist_ok=True)


def resolve_input_path(filename: str, *search_dirs: Path) -> Path:
    path = Path(filename)
    if path.is_absolute() or path.parent != Path('.'):
        return path
    for directory in search_dirs:
        candidate = directory / filename
        if candidate.exists():
            return candidate
    return search_dirs[0] / filename


def resolve_output_path(filename: str, default_dir: Path) -> Path:
    path = Path(filename)
    if path.is_absolute() or path.parent != Path('.'):
        path.parent.mkdir(parents=True, exist_ok=True)
        return path
    default_dir.mkdir(parents=True, exist_ok=True)
    return default_dir / filename
