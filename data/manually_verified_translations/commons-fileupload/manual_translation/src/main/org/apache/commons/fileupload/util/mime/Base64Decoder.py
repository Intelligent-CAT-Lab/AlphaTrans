from __future__ import annotations
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *


class Base64Decoder:

    __DECODING_TABLE: typing.List[int] = [0] * (2**8)
    __PADDING: int = ord("=")
    __ENCODING_TABLE: typing.List[int] = [
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
        97,
        98,
        99,
        100,
        101,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        109,
        110,
        111,
        112,
        113,
        114,
        115,
        116,
        117,
        118,
        119,
        120,
        121,
        122,
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
        43,
        47,
    ]
    __INPUT_BYTES_PER_CHUNK: int = 4
    __MASK_BYTE_UNSIGNED: int = 0xFF
    __PAD_BYTE: int = -2
    __INVALID_BYTE: int = -1

    def run_static_init():
        for i in range(len(Base64Decoder.__DECODING_TABLE)):
            Base64Decoder.__DECODING_TABLE[i] = Base64Decoder.__INVALID_BYTE
        for i in range(len(Base64Decoder.__ENCODING_TABLE)):
            Base64Decoder.__DECODING_TABLE[Base64Decoder.__ENCODING_TABLE[i]] = int(i)
        Base64Decoder.__DECODING_TABLE[Base64Decoder.__PADDING] = Base64Decoder.__PAD_BYTE

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
                out.write(bytes([(b1 << 2) | (b2 >> 4)]))
                outLen += 1
                if b3 != Base64Decoder.__PAD_BYTE:
                    out.write(bytes([((b2 & 0xF) << 4) | (b3 >> 2)]))
                    outLen += 1
                    if b4 != Base64Decoder.__PAD_BYTE:
                        out.write(bytes([((b3 & 0x3) << 6) | b4]))
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
        pass


Base64Decoder.run_static_init()
