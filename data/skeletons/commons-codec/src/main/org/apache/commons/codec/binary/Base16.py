from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import typing
from typing import *
import io

# Imports End


class Base16(BaseNCodec):

    # Class Fields Begin
    __UPPER_CASE_ENCODE_TABLE: typing.List[int] = None
    __LOWER_CASE_DECODE_TABLE: typing.List[int] = None
    __LOWER_CASE_ENCODE_TABLE: typing.List[int] = None
    __MASK_4BITS: int = None
    __decodeTable: typing.List[int] = None
    __encodeTable: typing.List[int] = None
    __BITS_PER_ENCODED_BYTE: int = None
    __BYTES_PER_ENCODED_BLOCK: int = None
    __BYTES_PER_UNENCODED_BLOCK: int = None
    __UPPER_CASE_DECODE_TABLE: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def isInAlphabet0(self, octet: int) -> bool:
        pass

    @staticmethod
    def Base162() -> Base16:
        pass

    @staticmethod
    def Base161(lowerCase: bool) -> Base16:
        pass

    def __init__(self, lowerCase: bool, decodingPolicy: CodecPolicy) -> None:
        pass

    def __validateTrailingCharacter(self) -> None:
        pass

    def __decodeOctet(self, octet: int) -> int:
        pass

    def encode2(
        self, data: typing.List[int], offset: int, length: int, context: Context
    ) -> None:
        pass

    def decode1(
        self, data: typing.List[int], offset: int, length: int, context: Context
    ) -> None:
        pass

    # Class Methods End
