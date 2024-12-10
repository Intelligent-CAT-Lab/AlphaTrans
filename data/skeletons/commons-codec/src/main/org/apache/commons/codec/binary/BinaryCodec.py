from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
import typing
from typing import *
import io

# Imports End


class BinaryCodec(BinaryDecoder, BinaryEncoder):

    # Class Fields Begin
    __EMPTY_CHAR_ARRAY: typing.List[str] = None
    __EMPTY_BYTE_ARRAY: typing.List[int] = None
    __BIT_0: int = None
    __BIT_1: int = None
    __BIT_2: int = None
    __BIT_3: int = None
    __BIT_4: int = None
    __BIT_5: int = None
    __BIT_6: int = None
    __BIT_7: int = None
    __BITS: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def encode(self, raw: typing.Any) -> typing.Any:
        pass

    def encode(self, raw: typing.List[int]) -> typing.List[int]:
        pass

    def decode(self, ascii_: typing.Any) -> typing.Any:
        pass

    def decode(self, ascii_: typing.List[int]) -> typing.List[int]:
        pass

    def toByteArray(self, ascii_: str) -> typing.List[int]:
        pass

    def encode1(self, raw: typing.Any) -> typing.Any:
        pass

    def encode0(self, raw: typing.List[int]) -> typing.List[int]:
        pass

    def decode1(self, ascii_: typing.Any) -> typing.Any:
        pass

    def decode0(self, ascii_: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def toAsciiString(raw: typing.List[int]) -> str:
        pass

    @staticmethod
    def toAsciiChars(raw: typing.List[int]) -> typing.List[str]:
        pass

    @staticmethod
    def toAsciiBytes(raw: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def fromAscii1(ascii_: typing.List[str]) -> typing.List[int]:
        pass

    @staticmethod
    def fromAscii0(ascii_: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def __isEmpty(array: typing.List[int]) -> bool:
        pass

    # Class Methods End
