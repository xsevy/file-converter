from converters.base import BaseConverter


class UTF8Converter(BaseConverter):
    def _convert(self) -> None:
        print("converting file...")  # noqa: T201
