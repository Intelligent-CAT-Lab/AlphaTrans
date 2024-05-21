from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.test.org.apache.commons.codec.binary.Codec105ErrorInputStream import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.test.org.apache.commons.codec.binary.Base32TestData import *
from src.main.org.apache.commons.codec.binary.Base32InputStream import *
import typing
from typing import *
import io

# Imports End


class Base32InputStreamTest:

    # Class Fields Begin
    __ENCODED_FOO: str = None
    __CRLF: typing.List[int] = None
    __LF: typing.List[int] = None
    __STRING_FIXTURE: str = None
    # Class Fields End

    # Class Methods Begin
    def testSkipWrongArgument(self) -> None:
        pass

    def testSkipToEnd(self) -> None:
        pass

    def testSkipPastEnd(self) -> None:
        pass

    def testSkipBig(self) -> None:
        pass

    def testSkipNone(self) -> None:
        pass

    def testReadOutOfBounds(self) -> None:
        pass

    def testReadNull(self) -> None:
        pass

    def testRead0(self) -> None:
        pass

    def testMarkSupported(self) -> None:
        pass

    def testBase32EmptyInputStreamPemChuckSize(self) -> None:
        pass

    def testBase32EmptyInputStreamMimeChuckSize(self) -> None:
        pass

    def testAvailable(self) -> None:
        pass

    def testCodec105(self) -> None:
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

    def __testBase32EmptyInputStream(self, chuckSize: int) -> None:
        pass

    # Class Methods End
