from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.digest.Blake3 import *
from src.main.org.apache.commons.codec.binary.Hex import *
from src.main.org.apache.commons.codec.DecoderException import *
import unittest
import typing
from typing import *
import io

# Imports End


class Blake3TestVectorsTest(unittest.TestCase):

    # Class Fields Begin
    __hasher: Blake3 = None
    __keyedHasher: Blake3 = None
    __kdfHasher: Blake3 = None
    __input: typing.List[int] = None
    __hash: typing.List[int] = None
    __keyedHash: typing.List[int] = None
    __deriveKey: typing.List[int] = None
    __KEY: typing.List[int] = None
    __CTX: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def keyDerivation(self) -> None:
        pass

    def keyedHashTruncatedOutput(self) -> None:
        pass

    def keyedHashArbitraryOutputLength(self) -> None:
        pass

    def hashTruncatedOutput(self) -> None:
        pass

    def hashArbitraryOutputLength(self) -> None:
        pass

    @staticmethod
    def testCases() -> typing.List[typing.List[typing.Any]]:
        pass

    def __init__(
        self, inputLength: int, hash_: str, keyedHash: str, deriveKey: str
    ) -> None:
        pass

    # Class Methods End
