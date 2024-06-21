from __future__ import annotations
import re
from dataclasses import field
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.digest.MurmurHash2 import *


class MurmurHash2Test(unittest.TestCase):

    text: str = "Lorem ipsum dolor sit amet, consectetur adipisicing elit"
    results64_seed: typing.List[int] = None  # LLM could not translate this field
    results64_standard: typing.List[int] = None  # LLM could not translate this field
    results32_seed: typing.List[int] = None  # LLM could not translate this field
    results32_standard: typing.List[int] = None  # LLM could not translate this field

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
        [0x23, 0xA8, 0xB1, 0x87, 0x55, 0xF7, 0x8A, 0x4B],
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

        hash = MurmurHash2.hash643(self.text, 2, len(self.text) - 4)
        assert hash == 0xA8B33145194985A2

    def testHash64String(self) -> None:

        hash = MurmurHash2.hash642(self.text)
        assert 0x0920E0C1B7EEB261 == hash

    def testHash64ByteArrayInt(self) -> None:

        for i in range(len(self.input)):
            hash = MurmurHash2.hash641(self.input[i], len(self.input[i]))
            if hash != self.results64_standard[i]:
                raise AssertionError(
                    f"Unexpected hash64 result for example {i}: 0x{hash:016x} instead of 0x{self.results64_standard[i]:016x}"
                )

    def testHash64ByteArrayIntInt(self) -> None:

        for i in range(len(self.input)):
            hash = MurmurHash2.hash640(self.input[i], len(self.input[i]), 0x344D1F5C)
            if hash != self.results64_seed[i]:
                raise AssertionError(
                    f"Unexpected hash64 result for example {i}: 0x{hash:016x} instead of 0x{self.results64_seed[i]:016x}"
                )

    def testHash32StringIntInt(self) -> None:

        hash = MurmurHash2.hash323(self.text, 2, len(self.text) - 4)
        assert 0x4D666D90 == hash

    def testHash32String(self) -> None:

        hash = MurmurHash2.hash322(self.text)
        assert 0xB3BF597E == hash

    def testHash32ByteArrayInt(self) -> None:

        for i in range(len(self.input)):
            hash = MurmurHash2.hash321(self.input[i], len(self.input[i]))
            if hash != self.results32_standard[i]:
                raise AssertionError(
                    f"Unexpected hash32 result for example {i}: 0x{hash:08x} instead of 0x{self.results32_standard[i]:08x}"
                )

    def testHash32ByteArrayIntInt(self) -> None:

        for i in range(len(self.input)):
            hash = MurmurHash2.hash320(self.input[i], len(self.input[i]), 0x71B4954D)
            if hash != self.results32_seed[i]:
                raise AssertionError(
                    f"Unexpected hash32 result for example {i}: 0x{hash:08x} instead of 0x{self.results32_seed[i]:08x}"
                )
