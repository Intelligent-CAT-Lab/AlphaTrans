from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import os
import typing
from typing import *
import io

# Imports End


class Base64(BaseNCodec):

    # Class Fields Begin
    __DECODE_TABLE: typing.List[int] = None
    __MASK_6BITS: int = None
    __MASK_4BITS: int = None
    __MASK_2BITS: int = None
    __encodeTable: typing.List[int] = None
    __decodeTable: typing.List[int] = None
    __lineSeparator: typing.List[int] = None
    __decodeSize: int = None
    __encodeSize: int = None
    __BITS_PER_ENCODED_BYTE: int = None
    __BYTES_PER_UNENCODED_BLOCK: int = None
    __BYTES_PER_ENCODED_BLOCK: int = None
    __STANDARD_ENCODE_TABLE: typing.List[int] = None
    __URL_SAFE_ENCODE_TABLE: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def _isInAlphabet0(self, octet: int) -> bool:
        pass

    @staticmethod
    def isArrayByteBase64(arrayOctet: typing.List[int]) -> bool:
        pass

    def isUrlSafe(self) -> bool:
        pass

    @staticmethod
    def Base645() -> Base64:
        pass

    @staticmethod
    def Base644(urlSafe: bool) -> Base64:
        pass

    @staticmethod
    def Base643(lineLength: int) -> Base64:
        pass

    @staticmethod
    def Base642(lineLength: int, lineSeparator: typing.List[int]) -> Base64:
        pass

    @staticmethod
    def Base641(
        lineLength: int, lineSeparator: typing.List[int], urlSafe: bool
    ) -> Base64:
        pass

    def __init__(
        self,
        lineLength: int,
        lineSeparator: typing.List[int],
        urlSafe: bool,
        decodingPolicy: CodecPolicy,
    ) -> None:
        pass

    @staticmethod
    def toIntegerBytes(bigInt: int) -> typing.List[int]:
        pass

    @staticmethod
    def isBase642(base64: str) -> bool:
        pass

    @staticmethod
    def isBase641(arrayOctet: typing.List[int]) -> bool:
        pass

    @staticmethod
    def isBase640(octet: int) -> bool:
        pass

    @staticmethod
    def encodeInteger(bigInteger: int) -> typing.List[int]:
        pass

    @staticmethod
    def encodeBase64URLSafeString(binaryData: typing.List[int]) -> str:
        pass

    @staticmethod
    def encodeBase64URLSafe(binaryData: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def encodeBase64String(binaryData: typing.List[int]) -> str:
        pass

    @staticmethod
    def encodeBase64Chunked(binaryData: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def encodeBase643(
        binaryData: typing.List[int], isChunked: bool, urlSafe: bool, maxResultSize: int
    ) -> typing.List[int]:
        pass

    @staticmethod
    def encodeBase642(
        binaryData: typing.List[int], isChunked: bool, urlSafe: bool
    ) -> typing.List[int]:
        pass

    @staticmethod
    def encodeBase641(
        binaryData: typing.List[int], isChunked: bool
    ) -> typing.List[int]:
        pass

    @staticmethod
    def encodeBase640(binaryData: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def decodeInteger(pArray: typing.List[int]) -> int:
        pass

    @staticmethod
    def decodeBase641(base64String: str) -> typing.List[int]:
        pass

    @staticmethod
    def decodeBase640(base64Data: typing.List[int]) -> typing.List[int]:
        pass

    def __validateTrailingCharacter(self) -> None:
        pass

    def __validateCharacter(self, emptyBitsMask: int, context: Context) -> None:
        pass

    def encode2(
        self, in_: typing.List[int], inPos: int, inAvail: int, context: Context
    ) -> None:
        pass

    def decode1(
        self, in_: typing.List[int], inPos: int, inAvail: int, context: Context
    ) -> None:
        pass

    # Class Methods End
