from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.binary.Hex import *
from src.main.org.apache.commons.codec.digest.Blake3 import *


class Blake3TestVectorsTest(unittest.TestCase):

    __deriveKey: typing.List[int] = None

    __keyedHash: typing.List[int] = None

    __hash: typing.List[int] = None

    __input: typing.List[int] = None

    __kdfHasher: Blake3 = Blake3.initKeyDerivationFunction(CTX)
    __keyedHasher: Blake3 = Blake3.initKeyedHash(KEY)
    __hasher: Blake3 = Blake3.initHash()
    __CTX: typing.List[int] = [
        66,
        76,
        65,
        75,
        69,
        51,
        32,
        50,
        48,
        49,
        57,
        45,
        49,
        50,
        45,
        50,
        55,
        32,
        49,
        54,
        58,
        50,
        57,
        58,
        53,
        50,
        32,
        116,
        101,
        115,
        116,
        32,
        118,
        101,
        99,
        116,
        111,
        114,
        115,
        32,
        99,
        111,
        110,
        116,
        101,
        120,
        116,
    ]
    __KEY: typing.List[int] = [
        119,
        104,
        97,
        116,
        115,
        32,
        116,
        104,
        101,
        32,
        69,
        108,
        118,
        105,
        115,
        104,
        32,
        119,
        111,
        114,
        100,
        32,
        102,
        114,
        105,
        101,
        110,
        100,
    ]

    def testkeyDerivation(self) -> None:

        self.__kdfHasher.update0(self.__input)
        actual = self.__kdfHasher.doFinalize2(len(self.__deriveKey))
        assert actual == self.__deriveKey
        self.__kdfHasher.reset()
        self.__kdfHasher.update0(self.__input)
        truncated = self.__kdfHasher.doFinalize2(32)
        assert truncated == self.__deriveKey[:32]

    def testkeyedHashTruncatedOutput(self) -> None:

        actual = Blake3.keyedHash(self.__KEY, self.__input)
        self.assertEqual(actual[:32], self.__keyedHash[:32])

    def testkeyedHashArbitraryOutputLength(self) -> None:

        self.__keyedHasher.update0(self.__input)
        actual = self.__keyedHasher.doFinalize2(len(self.__keyedHash))
        self.assertEqual(self.__keyedHash, actual)

    def testhashTruncatedOutput(self) -> None:

        actual = Blake3.hash(self.__input)
        self.assertEqual(actual[:32], self.__hash[:32])

    def testhashArbitraryOutputLength(self) -> None:

        if self.__input is None:
            raise ValueError("Input cannot be None")

        self.__hasher.update0(self.__input)
        actual = self.__hasher.doFinalize2(len(self.__hash))
        assert actual == self.__hash, f"Expected: {self.__hash}, Actual: {actual}"

    @staticmethod
    def testCases() -> typing.List[typing.List[typing.Any]]:

        pass  # LLM could not translate this method

    def __init__(
        self, inputLength: int, hash: str, keyedHash: str, deriveKey: str
    ) -> None:

        self.__input = [(i % 251) for i in range(inputLength)]
        self.__hash = Hex.decodeHex2(hash)
        self.__keyedHash = Hex.decodeHex2(keyedHash)
        self.__deriveKey = Hex.decodeHex2(deriveKey)
        self.__kdfHasher = Blake3.initKeyDerivationFunction(self.__CTX)
        self.__keyedHasher = Blake3.initKeyedHash(self.__KEY)
        self.__hasher = Blake3.initHash()
