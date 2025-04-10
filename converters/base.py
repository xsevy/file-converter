import abc
from pathlib import Path


class BaseConverter(abc.ABC):
    def __init__(self, input_path: Path, output_path: Path) -> None:
        self.input_path = input_path
        self.output_path = output_path
