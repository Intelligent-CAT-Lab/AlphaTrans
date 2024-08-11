from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.Base16OutputStream import *
from src.main.org.apache.commons.codec.binary.Base16 import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class Base16OutputStreamTest(unittest.TestCase):

    # Class Fields Begin
    __STRING_FIXTURE: str = None
    # Class Fields End

    # Class Methods Begin
    def testWriteToNullCoverage_test0_decomposed(self) -> None:
        pass

    def testWriteOutOfBounds_test0_decomposed(self) -> None:
        pass

    def testBase16OutputStreamByteByByte_test5_decomposed(self) -> None:
        pass

    def testBase16OutputStreamByteByByte_test4_decomposed(self) -> None:
        pass

    def testBase16OutputStreamByteByByte_test3_decomposed(self) -> None:
        pass

    def testBase16OutputStreamByteByByte_test2_decomposed(self) -> None:
        pass

    def testBase16OutputStreamByteByByte_test1_decomposed(self) -> None:
        pass

    def testBase16OutputStreamByteByByte_test0_decomposed(self) -> None:
        pass

    def testBase16OutputStreamByChunk_test5_decomposed(self) -> None:
        pass

    def testBase16OutputStreamByChunk_test4_decomposed(self) -> None:
        pass

    def testBase16OutputStreamByChunk_test3_decomposed(self) -> None:
        pass

    def testBase16OutputStreamByChunk_test2_decomposed(self) -> None:
        pass

    def testBase16OutputStreamByChunk_test1_decomposed(self) -> None:
        pass

    def testBase16OutputStreamByChunk_test0_decomposed(self) -> None:
        pass

    def testBase16EmptyOutputStream_test1_decomposed(self) -> None:
        pass

    def testBase16EmptyOutputStream_test0_decomposed(self) -> None:
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
