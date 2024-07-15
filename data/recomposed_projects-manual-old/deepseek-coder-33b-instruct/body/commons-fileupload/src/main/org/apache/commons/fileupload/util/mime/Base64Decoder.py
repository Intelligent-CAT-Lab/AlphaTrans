from __future__ import annotations
import re
from abc import ABC
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *


class Base64Decoder:

    __DECODING_TABLE: typing.List[int] = [0] * (2**8)
    __PADDING: int = ord("=")
    __ENCODING_TABLE: typing.List[int] = [
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
        ord("a"),
        ord("b"),
        ord("c"),
        ord("d"),
        ord("e"),
        ord("f"),
        ord("g"),
        ord("h"),
        ord("i"),
        ord("j"),
        ord("k"),
        ord("l"),
        ord("m"),
        ord("n"),
        ord("o"),
        ord("p"),
        ord("q"),
        ord("r"),
        ord("s"),
        ord("t"),
        ord("u"),
        ord("v"),
        ord("w"),
        ord("x"),
        ord("y"),
        ord("z"),
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
        ord("+"),
        ord("/"),
    ]
    __INPUT_BYTES_PER_CHUNK: int = 4
    __MASK_BYTE_UNSIGNED: int = 0xFF
    __PAD_BYTE: int = -2  # must be outside range 0-63
    __INVALID_BYTE: int = -1  # must be outside range 0-63

    @staticmethod
    def run_static_init():

        Base64Decoder.__DECODING_TABLE = [Base64Decoder.__INVALID_BYTE] * (
            max(Base64Decoder.__ENCODING_TABLE) + 1
        )
        for i in range(len(Base64Decoder.__ENCODING_TABLE)):
            Base64Decoder.__DECODING_TABLE[Base64Decoder.__ENCODING_TABLE[i]] = i

        Base64Decoder.__DECODING_TABLE[Base64Decoder.__PADDING] = (
            Base64Decoder.__PAD_BYTE
        )

    @staticmethod
    def decode(
        data: typing.List[int],
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
    ) -> int:

        outLen = 0
        cache = [0] * Base64Decoder.__INPUT_BYTES_PER_CHUNK
        cachedBytes = 0

        for b in data:
            d = Base64Decoder.__DECODING_TABLE[Base64Decoder.__MASK_BYTE_UNSIGNED & b]
            if d == Base64Decoder.__INVALID_BYTE:
                continue
            cache[cachedBytes] = d
            cachedBytes += 1
            if cachedBytes == Base64Decoder.__INPUT_BYTES_PER_CHUNK:
                b1 = cache[0]
                b2 = cache[1]
                b3 = cache[2]
                b4 = cache[3]
                if b1 == Base64Decoder.__PAD_BYTE or b2 == Base64Decoder.__PAD_BYTE:
                    raise IOError(
                        "Invalid Base64 input: incorrect padding, first two bytes cannot be"
                        + " padding"
                    )
                out.write((b1 << 2) | (b2 >> 4))
                outLen += 1
                if b3 != Base64Decoder.__PAD_BYTE:
                    out.write((b2 << 4) | (b3 >> 2))
                    outLen += 1
                    if b4 != Base64Decoder.__PAD_BYTE:
                        out.write((b3 << 6) | b4)
                        outLen += 1
                else:
                    if b4 != Base64Decoder.__PAD_BYTE:
                        raise IOError(
                            "Invalid Base64 input: incorrect padding, 4th byte must be padding if"
                            + " 3rd byte is"
                        )
                cachedBytes = 0

        if cachedBytes != 0:
            raise IOError("Invalid Base64 input: truncated")

        return outLen

    def __init__(self) -> None:

        self.__DECODING_TABLE = [self.__INVALID_BYTE] * (max(self.__ENCODING_TABLE) + 1)
        for i in range(len(self.__ENCODING_TABLE)):
            self.__DECODING_TABLE[self.__ENCODING_TABLE[i]] = i

        self.__PADDING = ord("=")
        self.__ENCODING_TABLE = [
            ord(c)
            for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        ]

        self.__INPUT_BYTES_PER_CHUNK = 4
        self.__MASK_BYTE_UNSIGNED = 0xFF
        self.__PAD_BYTE = -2
        self.__INVALID_BYTE = -1


Base64Decoder.run_static_init()
