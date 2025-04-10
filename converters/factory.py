import enum
from pathlib import Path

from converters.base import BaseConverter
from converters.txt import TXTConverter


class ConverterType(enum.StrEnum):
    TXT = enum.auto()


def create_converter(converter_type: ConverterType, input_path: Path, output_path: Path) -> BaseConverter:
    match converter_type:
        case ConverterType.TXT:
            return TXTConverter(input_path, output_path)
        case _:
            raise NotImplementedError
