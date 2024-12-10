from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.net.Utils import *
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.StringDecoder import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
import typing
from typing import *
from io import BytesIO
import io

# Imports End


class QuotedPrintableCodec:

    # Class Fields Begin
    __charset: str = None
    __strict: bool = None
    __PRINTABLE_CHARS: typing.List[bool] = None
    __ESCAPE_CHAR: int = None
    __TAB: int = None
    __SPACE: int = None
    __CR: int = None
    __LF: int = None
    __SAFE_LENGTH: int = None
    # Class Fields End

    # Class Methods Begin
    def decode(self, obj: typing.Any) -> typing.Any:
        pass

    def encode(self, obj: typing.Any) -> typing.Any:
        pass

    def decode(self, sourceStr: str) -> str:
        pass

    def encode(self, sourceStr: str) -> str:
        pass

    def decode(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def encode(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def encode4(self, sourceStr: str, sourceCharset: str) -> str:
        pass

    def encode3(self, sourceStr: str, sourceCharset: str) -> str:
        pass

    def getDefaultCharset(self) -> str:
        pass

    def getCharset(self) -> str:
        pass

    def decode4(self, obj: typing.Any) -> typing.Any:
        pass

    def encode2(self, obj: typing.Any) -> typing.Any:
        pass

    def decode3(self, sourceStr: str) -> str:
        pass

    def decode2(self, sourceStr: str, sourceCharset: str) -> str:
        pass

    def decode1(self, sourceStr: str, sourceCharset: str) -> str:
        pass

    def encode1(self, sourceStr: str) -> str:
        pass

    def decode0(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def encode0(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def decodeQuotedPrintable(bytes_: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def encodeQuotedPrintable2(
        printable: typing.List[bool], bytes_: typing.List[int], strict: bool
    ) -> typing.List[int]:
        pass

    @staticmethod
    def encodeQuotedPrintable1(
        printable: typing.List[bool], bytes_: typing.List[int]
    ) -> typing.List[int]:
        pass

    @staticmethod
    def QuotedPrintableCodec4() -> QuotedPrintableCodec:
        pass

    @staticmethod
    def QuotedPrintableCodec3(strict: bool) -> QuotedPrintableCodec:
        pass

    @staticmethod
    def QuotedPrintableCodec2(charset: str) -> QuotedPrintableCodec:
        pass

    @staticmethod
    def QuotedPrintableCodec0(charsetName: str) -> QuotedPrintableCodec:
        pass

    def __init__(
        self, constructorId: int, charsetName: str, charset: str, strict: bool
    ) -> None:
        pass

    @staticmethod
    def __isWhitespace(b: int) -> bool:
        pass

    @staticmethod
    def __encodeByte(
        b: int, encode: bool, buffer: typing.Union[io.BytesIO, bytearray]
    ) -> int:
        pass

    @staticmethod
    def __getUnsignedOctet(index: int, bytes_: typing.List[int]) -> int:
        pass

    @staticmethod
    def __encodeQuotedPrintable0(
        b: int, buffer: typing.Union[io.BytesIO, bytearray]
    ) -> int:
        pass

    # Class Methods End
