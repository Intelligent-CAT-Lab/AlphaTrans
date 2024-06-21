from __future__ import annotations
import re
from dataclasses import field
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *


class Base16(BaseNCodec):

    __encodeTable: typing.List[int] = None
    __decodeTable: typing.List[int] = None

    __MASK_4BITS: int = 0x0F

    __LOWER_CASE_ENCODE_TABLE: typing.List[int] = [
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
        ord("a"),
        ord("b"),
        ord("c"),
        ord("d"),
        ord("e"),
        ord("f"),
    ]
    __LOWER_CASE_DECODE_TABLE: typing.List[int] = (
        None  # LLM could not translate this field
    )

    __UPPER_CASE_ENCODE_TABLE: typing.List[int] = [
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
    ]

    __UPPER_CASE_DECODE_TABLE: List[int] = (
        [-1] * 16
        + [-1] * 6
        + [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1, -1, -1, -1]
        + [-1, 10, 11, 12, 13, 14, 15]
    )

    __BYTES_PER_UNENCODED_BLOCK: int = 1

    __BYTES_PER_ENCODED_BLOCK: int = 2

    __BITS_PER_ENCODED_BYTE: int = 4

    def isInAlphabet0(self, octet: int) -> bool:

        return (octet & 0xFF) < len(self.__decodeTable) and self.__decodeTable[
            octet
        ] != -1

    @staticmethod
    def Base162() -> Base16:

        return Base16.Base161(False)

    @staticmethod
    def Base161(lowerCase: bool) -> Base16:

        return Base16(lowerCase, DECODING_POLICY_DEFAULT)

    def __init__(self, lowerCase: bool, decodingPolicy: CodecPolicy) -> None:

        super().__init__(
            2,
            self.__BYTES_PER_UNENCODED_BLOCK,
            self.__BYTES_PER_ENCODED_BLOCK,
            0,
            0,
            self.PAD_DEFAULT,
            decodingPolicy,
        )

        if lowerCase:
            self.__encodeTable = self.__LOWER_CASE_ENCODE_TABLE
            self.__decodeTable = self.__LOWER_CASE_DECODE_TABLE
        else:
            self.__encodeTable = self.__UPPER_CASE_ENCODE_TABLE
            self.__decodeTable = self.__UPPER_CASE_DECODE_TABLE

    def __validateTrailingCharacter(self) -> None:

        if self.isStrictDecoding():
            raise ValueError(
                "Strict decoding: Last encoded character is a valid base 16 alphabet"
                + "character but not a possible encoding. "
                + "Decoding requires at least two characters to create one byte."
            )

    def __decodeOctet(self, octet: int) -> int:

        decoded = -1
        if (octet & 0xFF) < len(self.__decodeTable):
            decoded = self.__decodeTable[octet]

        if decoded == -1:
            raise ValueError("Invalid octet in encoded value: " + str(octet))

        return decoded

    def encode2(
        self, data: typing.List[int], offset: int, length: int, context: Context
    ) -> None:

        if context.eof:
            return

        if length < 0:
            context.eof = True
            return

        size = length * self.__BYTES_PER_ENCODED_BLOCK
        if size < 0:
            raise ValueError(
                "Input length exceeds maximum size for encoded data: " + str(length)
            )

        buffer = self.ensureBufferSize(size, context)

        end = offset + length
        for i in range(offset, end):
            value = data[i]
            high = (value >> self.__BITS_PER_ENCODED_BYTE) & self.__MASK_4BITS
            low = value & self.__MASK_4BITS
            buffer[context.pos] = self.__encodeTable[high]
            context.pos += 1
            buffer[context.pos] = self.__encodeTable[low]
            context.pos += 1

    def decode1(
        self, data: typing.List[int], offset: int, length: int, context: Context
    ) -> None:

        pass  # LLM could not translate this method
