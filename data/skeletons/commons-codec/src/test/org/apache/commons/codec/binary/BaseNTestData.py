# Imports Begin
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
import typing
import io

# Imports End


class BaseNTestData:

    # Class Fields Begin
    __SIZE_KEY: int = None
    __LAST_READ_KEY: int = None
    DECODED: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def bytesContain(bytes: typing.List[int], c: int) -> bool:
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
    def __resizeArray(bytes: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def __fill(
        buf: typing.List[int],
        offset: int,
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
    ) -> typing.List[int]:
        pass

    # Class Methods End
