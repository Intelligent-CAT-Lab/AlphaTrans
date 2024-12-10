from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodecOutputStream import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.test.org.apache.commons.codec.binary.Base64TestData import *
from src.test.org.apache.commons.codec.binary.Base64Test import *
from src.main.org.apache.commons.codec.binary.Base64OutputStream import *
from src.main.org.apache.commons.codec.binary.Base64 import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class Base64OutputStreamTest(unittest.TestCase):

    # Class Fields Begin
    __CR_LF: typing.List[int] = None
    __LF: typing.List[int] = None
    __STRING_FIXTURE: str = None
    # Class Fields End

    # Class Methods Begin
    def testStrictDecoding_test0_decomposed(self) -> None:
        pass

    def testWriteToNullCoverage_test0_decomposed(self) -> None:
        pass

    def testWriteOutOfBounds_test0_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByteByByte_test9_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByteByByte_test8_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByteByByte_test7_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByteByByte_test6_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByteByByte_test5_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByteByByte_test4_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByteByByte_test3_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByteByByte_test2_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByteByByte_test1_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByteByByte_test0_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByChunk_test9_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByChunk_test8_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByChunk_test7_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByChunk_test6_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByChunk_test5_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByChunk_test4_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByChunk_test3_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByChunk_test2_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByChunk_test1_decomposed(self) -> None:
        pass

    def testBase64OutputStreamByChunk_test0_decomposed(self) -> None:
        pass

    def testBase64EmptyOutputStreamPemChunkSize_test0_decomposed(self) -> None:
        pass

    def testBase64EmptyOutputStreamMimeChunkSize_test0_decomposed(self) -> None:
        pass

    def testCodec98NPE_test4_decomposed(self) -> None:
        pass

    def testCodec98NPE_test3_decomposed(self) -> None:
        pass

    def testCodec98NPE_test2_decomposed(self) -> None:
        pass

    def testCodec98NPE_test1_decomposed(self) -> None:
        pass

    def testCodec98NPE_test0_decomposed(self) -> None:
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

    def __testBase64EmptyOutputStream(self, chunkSize: int) -> None:
        pass

    # Class Methods End
