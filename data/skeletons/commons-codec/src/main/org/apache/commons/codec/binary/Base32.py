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


class Base32(BaseNCodec):

    # Class Fields Begin
    __HEX_ENCODE_TABLE: typing.List[int] = None
    __MASK_5BITS: int = None
    __MASK_4BITS: int = None
    __MASK_3BITS: int = None
    __MASK_2BITS: int = None
    __MASK_1BITS: int = None
    __decodeSize: int = None
    __decodeTable: typing.List[int] = None
    __encodeSize: int = None
    __encodeTable: typing.List[int] = None
    __lineSeparator: typing.List[int] = None
    __BITS_PER_ENCODED_BYTE: int = None
    __BYTES_PER_ENCODED_BLOCK: int = None
    __BYTES_PER_UNENCODED_BLOCK: int = None
    __DECODE_TABLE: typing.List[int] = None
    __ENCODE_TABLE: typing.List[int] = None
    __HEX_DECODE_TABLE: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def isInAlphabet0(self, octet: int) -> bool:
        pass

    def __init__(
        self,
        lineLength: int,
        lineSeparator: typing.List[int],
        useHex: bool,
        padding: int,
        decodingPolicy: CodecPolicy,
    ) -> None:
        pass

    @staticmethod
    def Base327(
        lineLength: int, lineSeparator: typing.List[int], useHex: bool, padding: int
    ) -> Base32:
        pass

    @staticmethod
    def Base326(
        lineLength: int, lineSeparator: typing.List[int], useHex: bool
    ) -> Base32:
        pass

    @staticmethod
    def Base325(lineLength: int, lineSeparator: typing.List[int]) -> Base32:
        pass

    @staticmethod
    def Base324(lineLength: int) -> Base32:
        pass

    @staticmethod
    def Base323(pad: int) -> Base32:
        pass

    @staticmethod
    def Base322(useHex: bool, padding: int) -> Base32:
        pass

    @staticmethod
    def Base321(useHex: bool) -> Base32:
        pass

    @staticmethod
    def Base320() -> Base32:
        pass

    def __validateTrailingCharacters(self) -> None:
        pass

    def __validateCharacter(self, emptyBitsMask: int, context: Context) -> None:
        pass

    def encode2(
        self, input_: typing.List[int], inPos: int, inAvail: int, context: Context
    ) -> None:
        pass

    def decode1(
        self, input_: typing.List[int], inPos: int, inAvail: int, context: Context
    ) -> None:
        pass

    # Class Methods End
