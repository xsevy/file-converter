import abc
from collections.abc import Sequence
from pathlib import Path

from validators import ValidatorType, file_exists_validator


class BaseConverter(abc.ABC):
    def __init__(
        self,
        input_path: Path,
        output_path: Path,
        validators: Sequence[ValidatorType] = (),
    ) -> None:
        self._input_path = input_path
        self._output_path = output_path
        self._validators = validators
        self._default_validators: Sequence[ValidatorType] = (file_exists_validator,)

    def __validate(self) -> None:
        for validator in [*self._default_validators, *self._validators]:
            validator(self._input_path, self._output_path)

    @abc.abstractmethod
    def _convert(self) -> None:
        raise NotImplementedError

    def _create_output_path(self) -> None:
        self._output_path.parent.mkdir(parents=True, exist_ok=True)

    def convert(self) -> None:
        self.__validate()
        self._convert()
