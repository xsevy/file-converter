from collections.abc import Sequence
from pathlib import Path
from typing import Callable


def make_extension_validator(allowed_extensions: Sequence[str]) -> Callable[[Path, Path], None]:
    def validator(input_path: Path, _: Path) -> None:
        if input_path.suffix not in allowed_extensions:
            raise ValueError(f"Invalid file extension: {input_path.suffix}")

    return validator
