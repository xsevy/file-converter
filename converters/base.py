import abc
from collections.abc import Sequence
from pathlib import Path
from typing import Callable


class BaseConverter(abc.ABC):
    def __init__(
        self,
        input_path: Path,
        output_path: Path,
        validators: Sequence[Callable[[Path, Path], None]] = (),
    ) -> None:
        self._input_path = input_path
        self._output_path = output_path
        self._validators = validators

    def _validate(self) -> None:
        for validator in self._validators:
            validator(self._input_path, self._output_path)

    @abc.abstractmethod
    def _convert(self) -> None:
        raise NotImplementedError

    def convert(self) -> None:
        self._validate()
        self._convert()
