from pathlib import Path
from typing import Annotated

import typer

from converters import ConverterType, create_converter


def main(
    input_path: Annotated[Path, typer.Option()],
    output_path: Annotated[Path, typer.Option()],
    converter_type: Annotated[ConverterType, typer.Option()] = ConverterType.UTF8,
) -> None:
    converter = create_converter(converter_type=converter_type, input_path=input_path, output_path=output_path)
    converter.convert()


if __name__ == "__main__":
    typer.run(main)
