from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.digest.MurmurHash2 import *


class MurmurHash2Test(unittest.TestCase):

    text: str = "Lorem ipsum dolor sit amet, consectetur adipisicing elit"
    results64_seed: typing.List[int] = [
        0x0822B1481A92E97B,
        0xF8A9223FEF0822DD,
        0x4B49E56AFFAE3A89,
        0xC970296E32E1D1C1,
        0xE2F9F88789F1B08F,
        0x2B0459D9B4C10C61,
        0x377E97EA9197EE89,
        0xD2CCAD460751E0E7,
        0xFF162CA8D6DA8C47,
        0xF12E051405769857,
        0xDABBA41293D5B035,
        0xACF326B0BB690D0E,
        0x0617F431BC1A8E04,
        0x15B81F28D576E1B2,
        0x28C1FE59E4F8E5BA,
        0x694DD315C9354CA9,
        0xA97052A8F088AE6C,
    ]
    results64_standard: typing.List[int] = [
        0x4987CB15118A83D9,
        0x28E2A79E3F0394D9,
        0x8F4600D786FC5C05,
        0xA09B27FEA4B54AF3,
        0x25F34447525BFD1E,
        0x32FAD4C21379C7BF,
        0x4B30B99A9D931921,
        0x4E5DAB004F936CDB,
        0x06825C27BC96CF40,
        0xFF4BF2F8A4823905,
        0x7F7E950C064E6367,
        0x821ADE90CAAA5889,
        0x6D28C915D791686A,
        0x9C32649372163BA2,
        0xD66AE956C14D5212,
        0x38ED30EE5161200F,
        0x9BFAE0A4E613FC3C,
    ]
    results32_seed: typing.List[int] = [
        0xD92E493E,
        0x8B50903B,
        0xC3372A7B,
        0x48F07E9E,
        0x8A5E4A6E,
        0x57916DF4,
        0xA346171F,
        0x1E319C86,
        0x9E1A03CD,
        0x9F973E6C,
        0x2D8C77F5,
        0xABED8751,
        0x296708B6,
        0x24F8078B,
        0x111B1553,
        0xA7DA1996,
        0xFE776C70,
    ]
    results32_standard: typing.List[int] = [
        0x96814FB3,
        0x485DCABA,
        0x331DC4AE,
        0xC6A7BF2F,
        0xCDF35DE0,
        0xD9DEC7CC,
        0x63A7318A,
        0xD0D3C2DE,
        0x90923AEF,
        0xAF35C1E2,
        0x735377B2,
        0x366C98F3,
        0x9C48EE29,
        0x0B615790,
        0xB4308AC1,
        0xEC98125A,
        0x106E08D9,
    ]
    input: typing.List[typing.List[int]] = [
        [
            0xED,
            0x53,
            0xC4,
            0xA5,
            0x3B,
            0x1B,
            0xBD,
            0xC2,
            0x52,
            0x7D,
            0xC3,
            0xEF,
            0x53,
            0x5F,
            0xAE,
            0x3B,
        ],
        [
            0x21,
            0x65,
            0x59,
            0x4E,
            0xD8,
            0x12,
            0xF9,
            0x05,
            0x80,
            0xE9,
            0x1E,
            0xED,
            0xE4,
            0x56,
            0xBB,
        ],
        [
            0x2B,
            0x02,
            0xB1,
            0xD0,
            0x3D,
            0xCE,
            0x31,
            0x3D,
            0x97,
            0xC4,
            0x91,
            0x0D,
            0xF7,
            0x17,
        ],
        [0x8E, 0xA7, 0x9A, 0x02, 0xE8, 0xB9, 0x6A, 0xDA, 0x92, 0xAD, 0xE9, 0x2D, 0x21],
        [0xA9, 0x6D, 0xEA, 0x77, 0x06, 0xCE, 0x1B, 0x85, 0x48, 0x27, 0x4C, 0xFE],
        [0xEC, 0x93, 0xA0, 0x12, 0x60, 0xEE, 0xC8, 0x0A, 0xC5, 0x90, 0x62],
        [0x55, 0x6D, 0x93, 0x66, 0x14, 0x6D, 0xDF, 0x00, 0x58, 0x99],
        [0x3C, 0x72, 0x20, 0x1F, 0xD2, 0x59, 0x19, 0xDB, 0xA1],
        [
            0x23,
            0xA8,
            0xB1,
            0x87,
            0x55,
            0xF7,
            0x8A,
            0x4B,
        ],
        [0xE2, 0x42, 0x1C, 0x2D, 0xC1, 0xE4, 0x3E],
        [0x66, 0xA6, 0xB5, 0x5A, 0x74, 0xD9],
        [0xE8, 0x76, 0xA8, 0x90, 0x76],
        [0xEB, 0x25, 0x3F, 0x87],
        [0x37, 0xA0, 0xA9],
        [0x5B, 0x5D],
        [0x7E],
        [],
    ]

    def testHash64StringIntInt(self) -> None:

        pass  # LLM could not translate this method

    def testHash64String(self) -> None:

        pass  # LLM could not translate this method

    def testHash64ByteArrayInt(self) -> None:
        for i in range(len(self.input)):
            hash: int = MurmurHash2.hash641(self.input[i], len(self.input[i]))
            if hash != self.results64_standard[i]:
                self.fail(
                    f"Unexpected hash64 result for example {i}: 0x{hash:016x} instead of"
                    f" 0x{self.results64_standard[i]:016x}"
                )

    def testHash64ByteArrayIntInt(self) -> None:
        for i in range(len(self.input)):
            hash: int = MurmurHash2.hash640(
                self.input[i], len(self.input[i]), 0x344D1F5C
            )
            if hash != self.results64_seed[i]:
                self.fail(
                    f"Unexpected hash64 result for example {i}: 0x{hash:016x} instead of"
                    f" 0x{self.results64_seed[i]:016x}"
                )

    def testHash32StringIntInt(self) -> None:

        pass  # LLM could not translate this method

    def testHash32String(self) -> None:

        pass  # LLM could not translate this method

    def testHash32ByteArrayInt(self) -> None:
        for i in range(len(self.input)):
            hash = MurmurHash2.hash321(self.input[i], len(self.input[i]))
            if hash != self.results32_standard[i]:
                self.fail(
                    f"Unexpected hash32 result for example {i}: 0x{hash:08x} instead of 0x{self.results32_standard[i]:08x}"
                )

    def testHash32ByteArrayIntInt(self) -> None:
        for i in range(len(self.input)):
            hash: int = MurmurHash2.hash320(
                self.input[i], len(self.input[i]), 0x71B4954D
            )
            if hash != self.results32_seed[i]:
                self.fail(
                    f"Unexpected hash32 result for example {i}: 0x{hash:08x} instead of 0x{self.results32_seed[i]:08x}"
                )
