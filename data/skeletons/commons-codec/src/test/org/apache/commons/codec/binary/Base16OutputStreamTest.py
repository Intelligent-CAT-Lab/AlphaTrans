from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.Base16OutputStream import *
from src.main.org.apache.commons.codec.binary.Base16 import *
import typing
from typing import *
import io

# Imports End


class Base16OutputStreamTest:

    # Class Fields Begin
    __STRING_FIXTURE: str = None
    # Class Fields End

    # Class Methods Begin
    def testWriteToNullCoverage(self) -> None:
        pass

    def testWriteOutOfBounds(self) -> None:
        pass

    def testBase16OutputStreamByteByByte(self) -> None:
        pass

    def testBase16OutputStreamByChunk(self) -> None:
        pass

    def testBase16EmptyOutputStream(self) -> None:
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
