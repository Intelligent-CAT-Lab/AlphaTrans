from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodecOutputStream import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.test.org.apache.commons.codec.binary.Base32TestData import *
from src.test.org.apache.commons.codec.binary.Base32Test import *
from src.main.org.apache.commons.codec.binary.Base32OutputStream import *
from src.main.org.apache.commons.codec.binary.Base32 import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class Base32OutputStreamTest(unittest.TestCase):

    # Class Fields Begin
    __CR_LF: typing.List[int] = None
    __LF: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def testStrictDecoding_test0_decomposed(self) -> None:
        pass

    def testWriteToNullCoverage_test0_decomposed(self) -> None:
        pass

    def testWriteOutOfBounds_test0_decomposed(self) -> None:
        pass

    def testBase32OutputStreamByteByByte_test3_decomposed(self) -> None:
        pass

    def testBase32OutputStreamByteByByte_test2_decomposed(self) -> None:
        pass

    def testBase32OutputStreamByteByByte_test1_decomposed(self) -> None:
        pass

    def testBase32OutputStreamByteByByte_test0_decomposed(self) -> None:
        pass

    def testBase32OutputStreamByChunk_test3_decomposed(self) -> None:
        pass

    def testBase32OutputStreamByChunk_test2_decomposed(self) -> None:
        pass

    def testBase32OutputStreamByChunk_test1_decomposed(self) -> None:
        pass

    def testBase32OutputStreamByChunk_test0_decomposed(self) -> None:
        pass

    def testBase32EmptyOutputStreamPemChunkSize_test0_decomposed(self) -> None:
        pass

    def testBase32EmptyOutputStreamMimeChunkSize_test0_decomposed(self) -> None:
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

    def __testBase32EmptyOutputStream(self, chunkSize: int) -> None:
        pass

    # Class Methods End
