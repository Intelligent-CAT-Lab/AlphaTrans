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
    def testStrictDecoding(self) -> None:
        pass

    def testWriteToNullCoverage(self) -> None:
        pass

    def testWriteOutOfBounds(self) -> None:
        pass

    def testBase64OutputStreamByteByByte(self) -> None:
        pass

    def testBase64OutputStreamByChunk(self) -> None:
        pass

    def testBase64EmptyOutputStreamPemChunkSize(self) -> None:
        pass

    def testBase64EmptyOutputStreamMimeChunkSize(self) -> None:
        pass

    def testCodec98NPE(self) -> None:
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
