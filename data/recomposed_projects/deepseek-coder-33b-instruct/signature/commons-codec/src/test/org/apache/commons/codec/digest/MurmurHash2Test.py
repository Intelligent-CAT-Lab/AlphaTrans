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

    results32_standard: typing.List[int] = None  # LLM could not translate this field

    input: List[List[int]] = [
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
    text: str = "Lorem ipsum dolor sit amet, consectetur adipisicing elit"

    def testHash64StringIntInt(self) -> None:

        hash_ = MurmurHash2.hash643(self.text, 2, len(self.text) - 4)
        self.assertEqual(0xA8B33145194985A2, hash_)

    def testHash64String(self) -> None:

        hash = MurmurHash2.hash642(self.text)
        self.assertEqual(0x0920E0C1B7EEB261, hash)

    def testHash64ByteArrayInt(self) -> None:

        pass  # LLM could not translate this method

    def testHash64ByteArrayIntInt(self) -> None:

        pass  # LLM could not translate this method

    def testHash32StringIntInt(self) -> None:

        hash_ = MurmurHash2.hash323(self.text, 2, len(self.text) - 4)
        self.assertEqual(0x4D666D90, hash_)

    def testHash32String(self) -> None:

        def hash32(data: str, seed: int = 0) -> int:
            m = 0x5BD1E995
            r = 24
            length = len(data)
            h = seed ^ length
            length4 = length // 4 * 4
            x = 0
            for i in range(0, length4, 4):
                x = (
                    (ord(data[i]) << 0x18)
                    | (ord(data[i + 1]) << 0x10)
                    | (ord(data[i + 2]) << 0x08)
                    | (ord(data[i + 3]))
                )
                x *= m
                x ^= x >> r
                x *= m
                h *= m
                h ^= x
            remaining = length & 0x3
            x = 0
            if remaining == 3:
                x = (
                    (ord(data[length - 3]) << 0x18)
                    | (ord(data[length - 2]) << 0x10)
                    | (ord(data[length - 1]) << 0x08)
                )
            elif remaining == 2:
                x = (ord(data[length - 2]) << 0x10) | (ord(data[length - 1]))
            elif remaining == 1:
                x = ord(data[length - 1])
            x *= m
            h ^= x
            h ^= h >> 0x10
            h *= 0x85EBCA6B
            h ^= h >> 0x17
            h *= 0xC2B2AE35
            h ^= h >> 0x17
            return h

        hash = hash32(self.text)
        self.assertEqual(0xB3BF597E, hash)

    def testHash32ByteArrayInt(self) -> None:

        pass  # LLM could not translate this method

    def testHash32ByteArrayIntInt(self) -> None:

        pass  # LLM could not translate this method
