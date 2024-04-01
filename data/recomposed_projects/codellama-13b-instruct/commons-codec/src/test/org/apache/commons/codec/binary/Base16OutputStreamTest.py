# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.Base16OutputStream import *
from src.main.org.apache.commons.codec.binary.Base16 import *
import unittest
import typing
from typing import *
import io

# Imports End


class Base16OutputStreamTest(unittest.TestCase):

    # Class Fields Begin
    __STRING_FIXTURE: str = "Hello World"
    # Class Fields End

    # Class Methods Begin
    def testWriteToNullCoverage(self) -> None:

        bout = io.BytesIO()
        with Base16OutputStream(bout) as out:
            try:
                out.write0(None, 0, 0)
                self.fail(
                    "Expected Base16OutputStream.write(None) to raise a NullPointerException"
                )
            except NullPointerException:
                pass

    def testWriteOutOfBounds(self) -> None:

        buf = bytearray(1024)
        bout = io.BytesIO()
        with Base16OutputStream(bout) as out:
            try:
                out.write0(buf, -1, 1)
                self.fail(
                    "Expected Base16OutputStream.write(buf, -1, 1) to throw a"
                    + " IndexOutOfBoundsException"
                )
            except IndexError as e:
                pass
            try:
                out.write0(buf, 1, -1)
                self.fail(
                    "Expected Base16OutputStream.write(buf, 1, -1) to throw a"
                    + " IndexOutOfBoundsException"
                )
            except IndexError as e:
                pass
            try:
                out.write0(buf, len(buf) + 1, 0)
                self.fail(
                    "Expected Base16OutputStream.write(buf, len(buf) + 1, 0) to throw a"
                    + " IndexOutOfBoundsException"
                )
            except IndexError as e:
                pass
            try:
                out.write0(buf, len(buf) - 1, 2)
                self.fail(
                    "Expected Base16OutputStream.write(buf, len(buf) - 1, 2) to throw a"
                    + " IndexOutOfBoundsException"
                )
            except IndexError as e:
                pass

    def testBase16OutputStreamByteByByte(self) -> None:

        encoded = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded = StringUtils.getBytesUtf8(STRING_FIXTURE)
        self.__testByteByByte0(encoded, decoded)
        encoded = StringUtils.getBytesUtf8("41")
        decoded = [0x41]
        self.__testByteByByte0(encoded, decoded)
        codec = Base16.Base161(True)
        for i in range(151):
            random_data = BaseNTestData.randomData(codec, i)
            encoded = random_data[1]
            decoded = random_data[0]
            self.__testByteByByte1(encoded, decoded, True)

    def testBase16OutputStreamByChunk(self) -> None:

        encoded = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded = StringUtils.getBytesUtf8(STRING_FIXTURE)
        self.__testByChunk0(encoded, decoded)
        encoded = StringUtils.getBytesUtf8("41")
        decoded = [0x41]
        self.__testByChunk0(encoded, decoded)
        codec = Base16.Base161(True)
        for i in range(0, 150):
            random_data = BaseNTestData.randomData(codec, i)
            encoded = random_data[1]
            decoded = random_data[0]
            self.__testByChunk1(encoded, decoded, True)

    def testBase16EmptyOutputStream(self) -> None:

        empty_encoded = b""
        empty_decoded = b""
        self.__testByteByByte0(empty_encoded, empty_decoded)
        self.__testByChunk0(empty_encoded, empty_decoded)

    def __testByteByByte1(
        self, encoded: typing.List[int], decoded: typing.List[int], lowerCase: bool
    ) -> None:

        pass  # LLM could not translate method body

    def __testByteByByte0(
        self, encoded: typing.List[int], decoded: typing.List[int]
    ) -> None:

        self.__testByteByByte1(encoded, decoded, False)

    def __testByChunk1(
        self, encoded: typing.List[int], decoded: typing.List[int], lowerCase: bool
    ) -> None:

        pass  # LLM could not translate method body

    def __testByChunk0(
        self, encoded: typing.List[int], decoded: typing.List[int]
    ) -> None:

        self.__testByChunk1(encoded, decoded, False)

    # Class Methods End
