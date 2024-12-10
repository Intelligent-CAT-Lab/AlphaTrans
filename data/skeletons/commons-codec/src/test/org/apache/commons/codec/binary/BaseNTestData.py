from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class BaseNTestData:

    # Class Fields Begin
    __SIZE_KEY: int = None
    __LAST_READ_KEY: int = None
    DECODED: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def bytesContain(bytes_: typing.List[int], c: int) -> bool:
        pass

    @staticmethod
    def randomData(codec: BaseNCodec, size: int) -> typing.List[typing.List[int]]:
        pass

    @staticmethod
    def streamToBytes1(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        buf: typing.List[int],
    ) -> typing.List[int]:
        pass

    @staticmethod
    def streamToBytes0(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> typing.List[int]:
        pass

    @staticmethod
    def __resizeArray(bytes_: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def __fill(
        buf: typing.List[int],
        offset: int,
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
    ) -> typing.List[int]:
        pass

    # Class Methods End
