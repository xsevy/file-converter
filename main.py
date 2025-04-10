from pathlib import Path
from typing import Annotated

import typer


def main(input_path: Annotated[Path, typer.Option()], output_path: Annotated[Path, typer.Option()]) -> None:
    pass


if __name__ == "__main__":
    typer.run(main)
