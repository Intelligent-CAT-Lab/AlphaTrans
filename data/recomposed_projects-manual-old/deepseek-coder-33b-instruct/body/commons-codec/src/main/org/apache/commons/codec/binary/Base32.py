from __future__ import annotations
import copy
import re
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base32(BaseNCodec):

    __lineSeparator: typing.List[int] = None

    __encodeTable: typing.List[int] = None

    __encodeSize: int = 0

    __decodeTable: typing.List[int] = None

    __decodeSize: int = 0

    __MASK_1BITS: int = 0x01
    __MASK_2BITS: int = 0x03
    __MASK_3BITS: int = 0x07
    __MASK_4BITS: int = 0x0F
    __MASK_5BITS: int = 0x1F
    __HEX_ENCODE_TABLE: typing.List[int] = [
        ord("0"),
        ord("1"),
        ord("2"),
        ord("3"),
        ord("4"),
        ord("5"),
        ord("6"),
        ord("7"),
        ord("8"),
        ord("9"),
        ord("A"),
        ord("B"),
        ord("C"),
        ord("D"),
        ord("E"),
        ord("F"),
        ord("G"),
        ord("H"),
        ord("I"),
        ord("J"),
        ord("K"),
        ord("L"),
        ord("M"),
        ord("N"),
        ord("O"),
        ord("P"),
        ord("Q"),
        ord("R"),
        ord("S"),
        ord("T"),
        ord("U"),
        ord("V"),
    ]
    __HEX_DECODE_TABLE: typing.List[int] = [
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # 00-0f
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # 10-1f
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # 20-2f
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # 30-3f 0-9
        -1,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,  # 40-4f A-O
        25,
        26,
        27,
        28,
        29,
        30,
        31,  # 50-56 P-V
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # 57-5f
        -1,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,  # 60-6f a-o
        25,
        26,
        27,
        28,
        29,
        30,
        31,  # 70-76 p-v
    ]
    __ENCODE_TABLE: typing.List[int] = [
        ord("A"),
        ord("B"),
        ord("C"),
        ord("D"),
        ord("E"),
        ord("F"),
        ord("G"),
        ord("H"),
        ord("I"),
        ord("J"),
        ord("K"),
        ord("L"),
        ord("M"),
        ord("N"),
        ord("O"),
        ord("P"),
        ord("Q"),
        ord("R"),
        ord("S"),
        ord("T"),
        ord("U"),
        ord("V"),
        ord("W"),
        ord("X"),
        ord("Y"),
        ord("Z"),
        ord("2"),
        ord("3"),
        ord("4"),
        ord("5"),
        ord("6"),
        ord("7"),
    ]
    __DECODE_TABLE: typing.List[int] = [
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # 00-0f
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # 10-1f
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # 20-2f
        -1,
        -1,
        26,
        27,
        28,
        29,
        30,
        31,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,
        -1,  # 30-3f 2-7
        -1,
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,  # 40-4f A-O
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,  # 50-5a P-Z
        -1,
        -1,
        -1,
        -1,
        -1,  # 5b-5f
        -1,
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,  # 60-6f a-o
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,  # 70-7a p-z
    ]
    __BYTES_PER_UNENCODED_BLOCK: int = 5
    __BYTES_PER_ENCODED_BLOCK: int = 8
    __BITS_PER_ENCODED_BYTE: int = 5

    def isInAlphabet0(self, octet: int) -> bool:
        return (
            octet >= 0
            and octet < len(self.__decodeTable)
            and self.__decodeTable[octet] != -1
        )

    def __init__(
        self,
        lineLength: int,
        lineSeparator: typing.List[int],
        useHex: bool,
        padding: int,
        decodingPolicy: CodecPolicy,
    ) -> None:

        super().__init__(
            2,
            self.__BYTES_PER_UNENCODED_BLOCK,
            self.__BYTES_PER_ENCODED_BLOCK,
            lineLength,
            lineSeparator.length if lineSeparator is not None else 0,
            padding,
            decodingPolicy,
        )

        if useHex:
            self.__encodeTable = self.__HEX_ENCODE_TABLE
            self.__decodeTable = self.__HEX_DECODE_TABLE
        else:
            self.__encodeTable = self.__ENCODE_TABLE
            self.__decodeTable = self.__DECODE_TABLE

        if lineLength > 0:
            if lineSeparator is None:
                raise ValueError(
                    "lineLength " + str(lineLength) + " > 0, but lineSeparator is null"
                )
            if self._containsAlphabetOrPad(lineSeparator):
                sep = StringUtils.newStringUtf8(lineSeparator)
                raise ValueError(
                    "lineSeparator must not contain Base32 characters: [" + sep + "]"
                )
            self.__encodeSize = self.__BYTES_PER_ENCODED_BLOCK + len(lineSeparator)
            self.__lineSeparator = lineSeparator.copy()
        else:
            self.__encodeSize = self.__BYTES_PER_ENCODED_BLOCK
            self.__lineSeparator = None

        self.__decodeSize = self.__encodeSize - 1

        if self.isInAlphabet0(padding) or StringUtils._isWhiteSpace(padding):
            raise ValueError("pad must not be in alphabet or whitespace")

    @staticmethod
    def Base327(
        lineLength: int, lineSeparator: typing.List[int], useHex: bool, padding: int
    ) -> Base32:

        return Base32(
            lineLength, lineSeparator, useHex, padding, DECODING_POLICY_DEFAULT
        )

    @staticmethod
    def Base326(
        lineLength: int, lineSeparator: typing.List[int], useHex: bool
    ) -> Base32:

        return Base32.Base327(lineLength, lineSeparator, useHex, Base32.PAD_DEFAULT)

    @staticmethod
    def Base325(lineLength: int, lineSeparator: typing.List[int]) -> Base32:

        return Base32.Base327(lineLength, lineSeparator, False, PAD_DEFAULT)

    @staticmethod
    def Base324(lineLength: int) -> Base32:

        return Base32.Base325(lineLength, CHUNK_SEPARATOR)

    @staticmethod
    def Base323(pad: int) -> Base32:

        return Base32.Base322(False, pad)

    @staticmethod
    def Base322(useHex: bool, padding: int) -> Base32:

        return Base32.Base327(0, None, useHex, padding)

    @staticmethod
    def Base321(useHex: bool) -> Base32:

        return Base32.Base327(0, None, useHex, Base32.PAD_DEFAULT)

    @staticmethod
    def Base320() -> Base32:

        return Base32.Base321(False)

    def __validateTrailingCharacters(self) -> None:
        if self.isStrictDecoding():
            raise ValueError(
                "Strict decoding: Last encoded character(s) (before the paddings if any) are"
                " valid base 32 alphabet but not a possible encoding. Decoding requires"
                " either 2, 4, 5, or 7 trailing 5-bit characters to create bytes."
            )

    def __validateCharacter(self, emptyBitsMask: int, context: Context) -> None:
        if self.isStrictDecoding() and (context.lbitWorkArea & emptyBitsMask) != 0:
            raise ValueError(
                "Strict decoding: Last encoded character (before the paddings if any) is a"
                " valid base 32 alphabet but not a possible encoding. Expected the"
                " discarded bits from the character to be zero."
            )

    def encode2(
        self, input: typing.List[int], inPos: int, inAvail: int, context: Context
    ) -> None:

        pass  # LLM could not translate this method

    def decode1(
        self, input: typing.List[int], inPos: int, inAvail: int, context: Context
    ) -> None:

        pass  # LLM could not translate this method
