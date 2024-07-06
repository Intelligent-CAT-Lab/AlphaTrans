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

    __DECODE_TABLE: typing.List[int] = None  # LLM could not translate this field

    __ENCODE_TABLE: typing.List[int] = [
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        50,
        51,
        52,
        53,
        54,
        55,
    ]
    __BYTES_PER_UNENCODED_BLOCK: int = 5
    __BYTES_PER_ENCODED_BLOCK: int = 8
    __BITS_PER_ENCODED_BYTE: int = 5
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
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
    ]

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
            Base32.__BYTES_PER_UNENCODED_BLOCK,
            Base32.__BYTES_PER_ENCODED_BLOCK,
            lineLength,
            0 if lineSeparator is None else len(lineSeparator),
            padding,
            decodingPolicy,
        )
        if useHex:
            self.__encodeTable = Base32.__HEX_ENCODE_TABLE
            self.__decodeTable = Base32.__HEX_DECODE_TABLE
        else:
            self.__encodeTable = Base32.__ENCODE_TABLE
            self.__decodeTable = Base32.__DECODE_TABLE
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
            self.__encodeSize = Base32.__BYTES_PER_ENCODED_BLOCK + len(lineSeparator)
            self.__lineSeparator = lineSeparator.copy()
        else:
            self.__encodeSize = Base32.__BYTES_PER_ENCODED_BLOCK
            self.__lineSeparator = None
        self.__decodeSize = self.__encodeSize - 1
        if self.isInAlphabet0(padding) or BaseNCodec._isWhiteSpace(padding):
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
        return Base327(lineLength, lineSeparator, useHex, PAD_DEFAULT)

    @staticmethod
    def Base325(lineLength: int, lineSeparator: typing.List[int]) -> Base32:
        return Base327(lineLength, lineSeparator, False, PAD_DEFAULT)

    @staticmethod
    def Base324(lineLength: int) -> Base32:
        return Base325(lineLength, CHUNK_SEPARATOR)

    @staticmethod
    def Base323(pad: int) -> Base32:
        return Base322(False, pad)

    @staticmethod
    def Base322(useHex: bool, padding: int) -> Base32:
        return Base327(0, None, useHex, padding)

    @staticmethod
    def Base321(useHex: bool) -> Base32:
        return Base327(0, None, useHex, PAD_DEFAULT)

    @staticmethod
    def Base320() -> Base32:
        return Base32.Base321(False)

    def __validateTrailingCharacters(self) -> None:
        if self.isStrictDecoding():
            raise ValueError(
                "Strict decoding: Last encoded character(s) (before the paddings if any) are"
                + " valid base 32 alphabet but not a possible encoding. Decoding requires"
                + " either 2, 4, 5, or 7 trailing 5-bit characters to create bytes."
            )

    def __validateCharacter(self, emptyBitsMask: int, context: Context) -> None:
        if self.isStrictDecoding() and (context.lbitWorkArea & emptyBitsMask) != 0:
            raise ValueError(
                "Strict decoding: Last encoded character (before the paddings if any) is a"
                + " valid base 32 alphabet but not a possible encoding. Expected the"
                + " discarded bits from the character to be zero."
            )

    def encode2(
        self, input: typing.List[int], inPos: int, inAvail: int, context: Context
    ) -> None:
        if context.eof:
            return
        if inAvail < 0:
            context.eof = True
            if 0 == context.modulus and self._lineLength == 0:
                return  # no leftovers to process and not using chunking
            buffer = self._ensureBufferSize(self.__encodeSize, context)
            savedPos = context.pos
            match context.modulus:  # % 5
                case 0:
                    pass
                case 1:  # Only 1 octet; take top 5 bits then remainder
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 3) & self.__MASK_5BITS
                    ]  # 8-1*5 = 3
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea << 2) & self.__MASK_5BITS
                    ]  # 5-3=2
                    context.pos += 1
                    buffer[context.pos] = self._pad
                    context.pos += 1
                    buffer[context.pos] = self._pad
                    context.pos += 1
                    buffer[context.pos] = self._pad
                    context.pos += 1
                    buffer[context.pos] = self._pad
                    context.pos += 1
                    buffer[context.pos] = self._pad
                    context.pos += 1
                    buffer[context.pos] = self._pad
                    context.pos += 1
                case 2:  # 2 octets = 16 bits to use
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 11) & self.__MASK_5BITS
                    ]  # 16-1*5 = 11
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 6) & self.__MASK_5BITS
                    ]  # 16-2*5 = 6
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 1) & self.__MASK_5BITS
                    ]  # 16-3*5 = 1
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea << 4) & self.__MASK_5BITS
                    ]  # 5-1 = 4
                    context.pos += 1
                    buffer[context.pos] = self._pad
                    context.pos += 1
                    buffer[context.pos] = self._pad
                    context.pos += 1
                    buffer[context.pos] = self._pad
                    context.pos += 1
                    buffer[context.pos] = self._pad
                    context.pos += 1
                case 3:  # 3 octets = 24 bits to use
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 19) & self.__MASK_5BITS
                    ]  # 24-1*5 = 19
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 14) & self.__MASK_5BITS
                    ]  # 24-2*5 = 14
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 9) & self.__MASK_5BITS
                    ]  # 24-3*5 = 9
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 4) & self.__MASK_5BITS
                    ]  # 24-4*5 = 4
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea << 1) & self.__MASK_5BITS
                    ]  # 5-4 = 1
                    context.pos += 1
                    buffer[context.pos] = self._pad
                    context.pos += 1
                    buffer[context.pos] = self._pad
                    context.pos += 1
                    buffer[context.pos] = self._pad
                    context.pos += 1
                case 4:  # 4 octets = 32 bits to use
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 27) & self.__MASK_5BITS
                    ]  # 32-1*5 = 27
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 22) & self.__MASK_5BITS
                    ]  # 32-2*5 = 22
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 17) & self.__MASK_5BITS
                    ]  # 32-3*5 = 17
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 12) & self.__MASK_5BITS
                    ]  # 32-4*5 = 12
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 7) & self.__MASK_5BITS
                    ]  # 32-5*5 =  7
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 2) & self.__MASK_5BITS
                    ]  # 32-6*5 =  2
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea << 3) & self.__MASK_5BITS
                    ]  # 5-2 = 3
                    context.pos += 1
                    buffer[context.pos] = self._pad
                    context.pos += 1
                case _:
                    raise RuntimeError("Impossible modulus " + context.modulus)
            context.currentLinePos += (
                context.pos - savedPos
            )  # keep track of current line position
            if (
                self._lineLength > 0 and context.currentLinePos > 0
            ):  # add chunk separator if required
                self.__lineSeparator.copy(
                    buffer, context.pos, 0, self.__lineSeparator.length
                )
                context.pos += self.__lineSeparator.length
        else:
            for i in range(inAvail):
                buffer = self._ensureBufferSize(self.__encodeSize, context)
                context.modulus = (
                    context.modulus + 1
                ) % self.__BYTES_PER_UNENCODED_BLOCK
                b = input[inPos]
                inPos += 1
                if b < 0:
                    b += 256
                context.lbitWorkArea = (context.lbitWorkArea << 8) + b  # BITS_PER_BYTE
                if 0 == context.modulus:  # we have enough bytes to create our output
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 35) & self.__MASK_5BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 30) & self.__MASK_5BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 25) & self.__MASK_5BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 20) & self.__MASK_5BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 15) & self.__MASK_5BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 10) & self.__MASK_5BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.lbitWorkArea >> 5) & self.__MASK_5BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        context.lbitWorkArea & self.__MASK_5BITS
                    ]
                    context.pos += 1
                    context.currentLinePos += self.__BYTES_PER_ENCODED_BLOCK
                    if (
                        self._lineLength > 0
                        and self._lineLength <= context.currentLinePos
                    ):
                        self.__lineSeparator.copy(
                            buffer, context.pos, 0, self.__lineSeparator.length
                        )
                        context.pos += self.__lineSeparator.length
                        context.currentLinePos = 0

    def decode1(
        self, input: typing.List[int], inPos: int, inAvail: int, context: Context
    ) -> None:
        if context.eof:
            return
        if inAvail < 0:
            context.eof = True
        for i in range(inAvail):
            b = input[inPos]
            inPos += 1
            if b == self._pad:
                context.eof = True
                break
            buffer = self._ensureBufferSize(self.__decodeSize, context)
            if b >= 0 and b < len(self.__decodeTable):
                result = self.__decodeTable[b]
                if result >= 0:
                    context.modulus = (
                        context.modulus + 1
                    ) % self.__BYTES_PER_ENCODED_BLOCK
                    context.lbitWorkArea = (
                        context.lbitWorkArea << self.__BITS_PER_ENCODED_BYTE
                    ) + result
                    if context.modulus == 0:
                        buffer[context.pos] = (
                            context.lbitWorkArea >> 32
                        ) & self._MASK_8BITS
                        context.pos += 1
                        buffer[context.pos] = (
                            context.lbitWorkArea >> 24
                        ) & self._MASK_8BITS
                        context.pos += 1
                        buffer[context.pos] = (
                            context.lbitWorkArea >> 16
                        ) & self._MASK_8BITS
                        context.pos += 1
                        buffer[context.pos] = (
                            context.lbitWorkArea >> 8
                        ) & self._MASK_8BITS
                        context.pos += 1
                        buffer[context.pos] = context.lbitWorkArea & self._MASK_8BITS
                        context.pos += 1
        if context.eof and context.modulus > 0:
            buffer = self._ensureBufferSize(self.__decodeSize, context)
            if context.modulus == 1:
                self.__validateTrailingCharacters()
            elif context.modulus == 2:
                self.__validateCharacter(self.__MASK_2BITS, context)
                buffer[context.pos] = (context.lbitWorkArea >> 2) & self._MASK_8BITS
                context.pos += 1
            elif context.modulus == 3:
                self.__validateTrailingCharacters()
                buffer[context.pos] = (context.lbitWorkArea >> 7) & self._MASK_8BITS
                context.pos += 1
            elif context.modulus == 4:
                self.__validateCharacter(self.__MASK_4BITS, context)
                context.lbitWorkArea = context.lbitWorkArea >> 4
                buffer[context.pos] = (context.lbitWorkArea >> 8) & self._MASK_8BITS
                context.pos += 1
                buffer[context.pos] = context.lbitWorkArea & self._MASK_8BITS
                context.pos += 1
            elif context.modulus == 5:
                self.__validateCharacter(self.__MASK_1BITS, context)
                context.lbitWorkArea = context.lbitWorkArea >> 1
                buffer[context.pos] = (context.lbitWorkArea >> 16) & self._MASK_8BITS
                context.pos += 1
                buffer[context.pos] = (context.lbitWorkArea >> 8) & self._MASK_8BITS
                context.pos += 1
                buffer[context.pos] = context.lbitWorkArea & self._MASK_8BITS
                context.pos += 1
            elif context.modulus == 6:
                self.__validateTrailingCharacters()
                context.lbitWorkArea = context.lbitWorkArea >> 6
                buffer[context.pos] = (context.lbitWorkArea >> 16) & self._MASK_8BITS
                context.pos += 1
                buffer[context.pos] = (context.lbitWorkArea >> 8) & self._MASK_8BITS
                context.pos += 1
                buffer[context.pos] = context.lbitWorkArea & self._MASK_8BITS
                context.pos += 1
            elif context.modulus == 7:
                self.__validateCharacter(self.__MASK_3BITS, context)
                context.lbitWorkArea = context.lbitWorkArea >> 3
                buffer[context.pos] = (context.lbitWorkArea >> 24) & self._MASK_8BITS
                context.pos += 1
                buffer[context.pos] = (context.lbitWorkArea >> 16) & self._MASK_8BITS
                context.pos += 1
                buffer[context.pos] = (context.lbitWorkArea >> 8) & self._MASK_8BITS
                context.pos += 1
                buffer[context.pos] = context.lbitWorkArea & self._MASK_8BITS
                context.pos += 1
            else:
                raise RuntimeError("Impossible modulus " + context.modulus)
