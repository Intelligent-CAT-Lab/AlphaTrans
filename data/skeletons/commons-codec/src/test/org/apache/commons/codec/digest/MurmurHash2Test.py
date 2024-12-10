from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.digest.MurmurHash2 import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class MurmurHash2Test(unittest.TestCase):

    # Class Fields Begin
    results32_standard: typing.List[int] = None
    results32_seed: typing.List[int] = None
    results64_standard: typing.List[int] = None
    results64_seed: typing.List[int] = None
    text: str = None
    input: typing.List[typing.List[int]] = None
    # Class Fields End

    # Class Methods Begin
    def testHash64StringIntInt_test2_decomposed(self) -> None:
        pass

    def testHash64StringIntInt_test1_decomposed(self) -> None:
        pass

    def testHash64StringIntInt_test0_decomposed(self) -> None:
        pass

    def testHash64String_test1_decomposed(self) -> None:
        pass

    def testHash64String_test0_decomposed(self) -> None:
        pass

    def testHash64ByteArrayInt_test0_decomposed(self) -> None:
        pass

    def testHash64ByteArrayIntInt_test0_decomposed(self) -> None:
        pass

    def testHash32StringIntInt_test2_decomposed(self) -> None:
        pass

    def testHash32StringIntInt_test1_decomposed(self) -> None:
        pass

    def testHash32StringIntInt_test0_decomposed(self) -> None:
        pass

    def testHash32String_test1_decomposed(self) -> None:
        pass

    def testHash32String_test0_decomposed(self) -> None:
        pass

    def testHash32ByteArrayInt_test0_decomposed(self) -> None:
        pass

    def testHash32ByteArrayIntInt_test0_decomposed(self) -> None:
        pass

    # Class Methods End
