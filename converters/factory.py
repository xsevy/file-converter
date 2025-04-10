import enum
from pathlib import Path

from converters.base import BaseConverter
from converters.txt import UTF8Converter


class ConverterType(enum.StrEnum):
    UTF8 = enum.auto()


def create_converter(converter_type: ConverterType, input_path: Path, output_path: Path) -> BaseConverter:
    match converter_type:
        case ConverterType.UTF8:
            return UTF8Converter(input_path, output_path)
        case _:
            raise NotImplementedError
