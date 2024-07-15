from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.net.RFC1522Codec import *
from src.main.org.apache.commons.codec.net.QuotedPrintableCodec import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.StringDecoder import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
import typing
from typing import *
import io

# Imports End


class QCodec(StringDecoder, StringEncoder, RFC1522Codec):

    # Class Fields Begin
    __UNDERSCORE: int = None
    __encodeBlanks: bool = None
    __charset: str = None
    __PRINTABLE_CHARS: typing.List[bool] = None
    __SPACE: int = None
    # Class Fields End

    # Class Methods Begin
    def decode(self, obj: typing.Any) -> typing.Any:
        pass

    def encode(self, obj: typing.Any) -> typing.Any:
        pass

    def decode(self, str_: str) -> str:
        pass

    def encode(self, sourceStr: str) -> str:
        pass

    def _doDecoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def _doEncoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def _getEncoding(self) -> str:
        pass

    def setEncodeBlanks(self, b: bool) -> None:
        pass

    def isEncodeBlanks(self) -> bool:
        pass

    def getDefaultCharset(self) -> str:
        pass

    def getCharset(self) -> str:
        pass

    def decode1(self, obj: typing.Any) -> typing.Any:
        pass

    def encode3(self, obj: typing.Any) -> typing.Any:
        pass

    def decode0(self, str_: str) -> str:
        pass

    def encode2(self, sourceStr: str) -> str:
        pass

    def encode1(self, sourceStr: str, sourceCharset: str) -> str:
        pass

    def encode0(self, sourceStr: str, sourceCharset: str) -> str:
        pass

    @staticmethod
    def QCodec2() -> QCodec:
        pass

    @staticmethod
    def QCodec0(charsetName: str) -> QCodec:
        pass

    def __init__(self, constructorId: int, charsetName: str, charset: str) -> None:
        pass

    # Class Methods End
