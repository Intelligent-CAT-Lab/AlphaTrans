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

    __hasher: Blake3 = Blake3.initHash()
    __CTX: typing.List[int] = "BLAKE3 2019-12-27 16:29:52 test vectors context".encode('utf-8')
    __KEY: typing.List[int] = "whats the Elvish word for friend".encode('utf-8')

    __kdfHasher: Blake3 = Blake3.initKeyDerivationFunction(__CTX)
    __keyedHasher: Blake3 = Blake3.initKeyedHash(__KEY)

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

    # def __init__(
    #     self, inputLength: int, hash: str, keyedHash: str, deriveKey: str
    # ) -> None:
    #
    #     self.__input = [(i % 251) for i in range(inputLength)]
    #     self.__hash = Hex.decodeHex2(hash)
    #     self.__keyedHash = Hex.decodeHex2(keyedHash)
    #     self.__deriveKey = Hex.decodeHex2(deriveKey)
    #     self.__kdfHasher = Blake3.initKeyDerivationFunction(self.__CTX)
    #     self.__keyedHasher = Blake3.initKeyedHash(self.__KEY)
    #     self.__hasher = Blake3.initHash()
