from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.net.RFC1522Codec import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.Base64 import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.StringDecoder import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import typing
from typing import *
import io

# Imports End


class BCodec(StringDecoder, StringEncoder, RFC1522Codec):

    # Class Fields Begin
    __DECODING_POLICY_DEFAULT: CodecPolicy = None
    __charset: str = None
    __decodingPolicy: CodecPolicy = None
    # Class Fields End

    # Class Methods Begin
    def decode(self, value: typing.Any) -> typing.Any:
        pass

    def encode(self, value: typing.Any) -> typing.Any:
        pass

    def decode(self, value: str) -> str:
        pass

    def encode(self, strSource: str) -> str:
        pass

    def _doDecoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def _doEncoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def _getEncoding(self) -> str:
        pass

    def getDefaultCharset(self) -> str:
        pass

    def getCharset(self) -> str:
        pass

    def decode1(self, value: typing.Any) -> typing.Any:
        pass

    def encode3(self, value: typing.Any) -> typing.Any:
        pass

    def decode0(self, value: str) -> str:
        pass

    def encode2(self, strSource: str) -> str:
        pass

    def encode1(self, strSource: str, sourceCharset: str) -> str:
        pass

    def encode0(self, strSource: str, sourceCharset: str) -> str:
        pass

    def encode(self, strSource: str, sourceCharset: str) -> str:
        pass

    def isStrictDecoding(self) -> bool:
        pass

    @staticmethod
    def BCodec2(charsetName: str) -> BCodec:
        pass

    def __init__(self, charset: str, decodingPolicy: CodecPolicy) -> None:
        pass

    @staticmethod
    def BCodec1(charset: str) -> BCodec:
        pass

    @staticmethod
    def BCodec0() -> BCodec:
        pass

    # Class Methods End
