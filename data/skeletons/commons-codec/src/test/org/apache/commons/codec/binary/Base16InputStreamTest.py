from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.Base16InputStream import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class Base16InputStreamTest(unittest.TestCase):

    # Class Fields Begin
    __ENCODED_B16: str = None
    __STRING_FIXTURE: str = None
    # Class Fields End

    # Class Methods Begin
    def testSkipWrongArgument_test1_decomposed(self) -> None:
        pass

    def testSkipWrongArgument_test0_decomposed(self) -> None:
        pass

    def testSkipToEnd_test1_decomposed(self) -> None:
        pass

    def testSkipToEnd_test0_decomposed(self) -> None:
        pass

    def testSkipPastEnd_test1_decomposed(self) -> None:
        pass

    def testSkipPastEnd_test0_decomposed(self) -> None:
        pass

    def testSkipNone_test1_decomposed(self) -> None:
        pass

    def testSkipNone_test0_decomposed(self) -> None:
        pass

    def testSkipBig_test1_decomposed(self) -> None:
        pass

    def testSkipBig_test0_decomposed(self) -> None:
        pass

    def testReadOutOfBounds_test1_decomposed(self) -> None:
        pass

    def testReadOutOfBounds_test0_decomposed(self) -> None:
        pass

    def testReadNull_test1_decomposed(self) -> None:
        pass

    def testReadNull_test0_decomposed(self) -> None:
        pass

    def testRead0_test1_decomposed(self) -> None:
        pass

    def testRead0_test0_decomposed(self) -> None:
        pass

    def testMarkSupported_test1_decomposed(self) -> None:
        pass

    def testMarkSupported_test0_decomposed(self) -> None:
        pass

    def testBase16EmptyInputStream_test1_decomposed(self) -> None:
        pass

    def testBase16EmptyInputStream_test0_decomposed(self) -> None:
        pass

    def testAvailable_test1_decomposed(self) -> None:
        pass

    def testAvailable_test0_decomposed(self) -> None:
        pass

    def __testByteByByte1(
        self, encoded: typing.List[int], decoded: typing.List[int], lowerCase: bool
    ) -> None:
        pass

    def __testByteByByte0(
        self, encoded: typing.List[int], decoded: typing.List[int]
    ) -> None:
        pass

    def __testByChunk1(
        self, encoded: typing.List[int], decoded: typing.List[int], lowerCase: bool
    ) -> None:
        pass

    def __testByChunk0(
        self, encoded: typing.List[int], decoded: typing.List[int]
    ) -> None:
        pass

    # Class Methods End
