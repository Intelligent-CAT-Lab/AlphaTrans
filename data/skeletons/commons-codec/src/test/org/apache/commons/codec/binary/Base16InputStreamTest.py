# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.Base16InputStream import *
import typing

# Imports End


class Base16InputStreamTest:

    # Class Fields Begin
    __ENCODED_B16: str = None
    __STRING_FIXTURE: str = None
    # Class Fields End

    # Class Methods Begin
    def testSkipWrongArgument(self) -> None:
        pass

    def testSkipToEnd(self) -> None:
        pass

    def testSkipPastEnd(self) -> None:
        pass

    def testSkipNone(self) -> None:
        pass

    def testSkipBig(self) -> None:
        pass

    def testReadOutOfBounds(self) -> None:
        pass

    def testReadNull(self) -> None:
        pass

    def testRead0(self) -> None:
        pass

    def testMarkSupported(self) -> None:
        pass

    def testBase16EmptyInputStream(self) -> None:
        pass

    def testAvailable(self) -> None:
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
