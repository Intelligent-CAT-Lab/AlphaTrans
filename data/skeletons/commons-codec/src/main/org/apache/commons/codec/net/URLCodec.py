from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.net.Utils import *
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.StringDecoder import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
import typing
from typing import *
import io

# Imports End


class URLCodec(BinaryDecoder, BinaryEncoder, StringDecoder, StringEncoder):

    # Class Fields Begin
    _charset: str = None
    _ESCAPE_CHAR: int = None
    _WWW_FORM_URL: typing.List[bool] = None
    __WWW_FORM_URL_SAFE: typing.List[bool] = None
    # Class Fields End

    # Class Methods Begin
    def getEncoding(self) -> str:
        pass

    def decode(self, obj: typing.Any) -> typing.Any:
        pass

    def encode(self, obj: typing.Any) -> typing.Any:
        pass

    def decode(self, str_: str) -> str:
        pass

    def encode(self, str_: str) -> str:
        pass

    def decode(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def encode(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def getDefaultCharset(self) -> str:
        pass

    def decode3(self, obj: typing.Any) -> typing.Any:
        pass

    def encode3(self, obj: typing.Any) -> typing.Any:
        pass

    def decode2(self, str_: str) -> str:
        pass

    def decode1(self, str_: str, charsetName: str) -> str:
        pass

    def decode(self, str_: str, charsetName: str) -> str:
        pass

    def encode2(self, str_: str) -> str:
        pass

    def encode1(self, str_: str, charsetName: str) -> str:
        pass

    def encode(self, str_: str, charsetName: str) -> str:
        pass

    def decode0(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def encode0(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def decodeUrl(bytes_: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def encodeUrl(
        urlsafe: typing.List[bool], bytes_: typing.List[int]
    ) -> typing.List[int]:
        pass

    @staticmethod
    def URLCodec1() -> URLCodec:
        pass

    def __init__(self, charset: str) -> None:
        pass

    # Class Methods End
