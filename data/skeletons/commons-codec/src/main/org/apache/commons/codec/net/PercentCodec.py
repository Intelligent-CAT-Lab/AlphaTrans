from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.net.Utils import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
import typing
from typing import *
import io

# Imports End


class PercentCodec(BinaryDecoder, BinaryEncoder):

    # Class Fields Begin
    __ESCAPE_CHAR: int = None
    __alwaysEncodeChars: typing.List[bool] = None
    __plusForSpace: bool = None
    __alwaysEncodeCharsMax: int = None
    __alwaysEncodeCharsMin: int = None
    # Class Fields End

    # Class Methods Begin
    def decode(self, obj: typing.Any) -> typing.Any:
        pass

    def encode(self, obj: typing.Any) -> typing.Any:
        pass

    def decode(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def encode(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def decode1(self, obj: typing.Any) -> typing.Any:
        pass

    def encode1(self, obj: typing.Any) -> typing.Any:
        pass

    def decode0(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def encode0(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def __init__(
        self,
        constructorId: int,
        plusForSpace: bool,
        alwaysEncodeChars: typing.List[int],
    ) -> None:
        pass

    def __expectedDecodingBytes(self, bytes_: typing.List[int]) -> int:
        pass

    def __isAsciiChar(self, c: int) -> bool:
        pass

    def __inAlwaysEncodeCharsRange(self, c: int) -> bool:
        pass

    def __canEncode(self, c: int) -> bool:
        pass

    def __containsSpace(self, bytes_: typing.List[int]) -> bool:
        pass

    def __expectedEncodingBytes(self, bytes_: typing.List[int]) -> int:
        pass

    def __doEncode(
        self, bytes_: typing.List[int], expectedLength: int, willEncode: bool
    ) -> typing.List[int]:
        pass

    def __insertAlwaysEncodeChar(self, b: int) -> None:
        pass

    def __insertAlwaysEncodeChars(
        self, alwaysEncodeCharsArray: typing.List[int]
    ) -> None:
        pass

    # Class Methods End
