from __future__ import annotations

# Imports Begin
import os
import typing
from typing import *
from io import BytesIO
import io
import pathlib

# Imports End


class DiskFileItemSerializeTest:

    # Class Fields Begin
    __REPO: pathlib.Path = None
    __textContentType: str = None
    __threshold: int = None
    # Class Fields End

    # Class Methods Begin
    def __deserialize(self, baos: typing.Union[io.BytesIO, bytearray]) -> typing.Any:
        pass

    def __serialize(self, target: typing.Any) -> typing.Union[io.BytesIO, bytearray]:
        pass

    def __createContentBytes(self, size: int) -> typing.List[int]:
        pass

    def __compareBytes(
        self, text: str, origBytes: typing.List[int], newBytes: typing.List[int]
    ) -> None:
        pass

    # Class Methods End
