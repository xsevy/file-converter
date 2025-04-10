import chardet

from converters.base import BaseConverter


class UTF8Converter(BaseConverter):
    def __detect_encoding(self, raw_data: bytes | bytearray) -> str | None:
        result = chardet.detect(raw_data)
        return result["encoding"]

    def _convert(self) -> None:
        with self._input_path.open("rb") as f:
            raw_data = f.read()

        if (encoding := self.__detect_encoding(raw_data)) is None:
            raise ValueError(f"Unable to detect encoding for {self._input_path}")

        self._create_output_path()

        with self._output_path.open("w", encoding="utf-8") as dest_file:
            dest_file.write(raw_data.decode(encoding))
