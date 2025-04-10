from collections.abc import Sequence
from pathlib import Path
from typing import Callable

ValidatorType = Callable[[Path, Path], None]


def make_extension_validator(allowed_extensions: Sequence[str]) -> ValidatorType:
    def validator(input_path: Path, output_path: Path) -> None:
        if input_path.suffix not in allowed_extensions or output_path.suffix not in allowed_extensions:
            raise ValueError(f"Invalid file extension for one of the paths: {input_path=}, {output_path=}")

    return validator


def file_exists_validator(input_path: Path, _: Path) -> None:
    if not input_path.exists():
        raise ValueError(f"File {input_path} does not exist")
