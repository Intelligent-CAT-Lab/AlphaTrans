from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.test.org.apache.commons.codec.binary.Codec105ErrorInputStream import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.test.org.apache.commons.codec.binary.Base64TestData import *
from src.main.org.apache.commons.codec.binary.Base64InputStream import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class Base64InputStreamTest(unittest.TestCase):

    # Class Fields Begin
    __ENCODED_B64: str = None
    __CRLF: typing.List[int] = None
    __LF: typing.List[int] = None
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

    def testBase64EmptyInputStreamPemChuckSize_test0_decomposed(self) -> None:
        pass

    def testBase64EmptyInputStreamMimeChuckSize_test0_decomposed(self) -> None:
        pass

    def testAvailable_test1_decomposed(self) -> None:
        pass

    def testAvailable_test0_decomposed(self) -> None:
        pass

    def testInputStreamReader_test2_decomposed(self) -> None:
        pass

    def testInputStreamReader_test1_decomposed(self) -> None:
        pass

    def testInputStreamReader_test0_decomposed(self) -> None:
        pass

    def testCodec101_test1_decomposed(self) -> None:
        pass

    def testCodec101_test0_decomposed(self) -> None:
        pass

    def testCodec105_test0_decomposed(self) -> None:
        pass

    def __testByteByByte(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:
        pass

    def __testByChunk(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:
        pass

    def __testBase64EmptyInputStream(self, chuckSize: int) -> None:
        pass

    # Class Methods End
