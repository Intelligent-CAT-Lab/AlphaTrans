from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.binary.Base16InputStream import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base16InputStreamTest(unittest.TestCase):

    __STRING_FIXTURE: str = "Hello World"

    __ENCODED_B16: str = "CAFEBABEFFFF"

    def testSkipWrongArgument(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            b16Stream.skip(-10)

    def testSkipToEnd(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            self.assertEqual(6, b16Stream.skip(6))
            self.assertEqual(-1, b16Stream.read0())
            self.assertEqual(-1, b16Stream.read0())

    def testSkipPastEnd(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            self.assertEqual(6, b16Stream.skip(10))
            self.assertEqual(-1, b16Stream.read0())
            self.assertEqual(-1, b16Stream.read0())

    def testSkipNone(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            actualBytes = bytearray(6)
            assert 0 == b16Stream.skip(0)
            b16Stream.read1(actualBytes, 0, len(actualBytes))
            assert actualBytes == bytearray([202, 254, 186, 190, 255, 255])
            assert -1 == b16Stream.read0()

    def testSkipBig(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            self.assertEqual(6, b16Stream.skip(2**31 - 1))
            self.assertEqual(-1, b16Stream.read0())
            self.assertEqual(-1, b16Stream.read0())

    def testReadOutOfBounds(self) -> None:

        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        buf = bytearray(1024)
        bin = io.BytesIO(decoded)

        with Base16InputStream.Base16InputStream2(bin, True) as in_:

            try:
                in_.read1(buf, -1, 0)
                assert (
                    False
                ), "Expected Base16InputStream.read(buf, -1, 0) to throw IndexOutOfBoundsException"
            except IndexError:
                pass

            try:
                in_.read1(buf, 0, -1)
                assert (
                    False
                ), "Expected Base16InputStream.read(buf, 0, -1) to throw IndexOutOfBoundsException"
            except IndexError:
                pass

            try:
                in_.read1(buf, len(buf) + 1, 0)
                assert (
                    False
                ), "Expected Base16InputStream.read(buf, len(buf) + 1, 0) to throw IndexOutOfBoundsException"
            except IndexError:
                pass

            try:
                in_.read1(buf, len(buf) - 1, 2)
                assert (
                    False
                ), "Expected Base16InputStream.read(buf, len(buf) - 1, 2) to throw IndexOutOfBoundsException"
            except IndexError:
                pass

    def testReadNull(self) -> None:

        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        bin = io.BytesIO(decoded)
        try:
            in_stream = Base16InputStream.Base16InputStream2(bin, True)
            in_stream.read1(None, 0, 0)
            self.fail(
                "Base16InputStream.read(None, 0, 0) to throw a NullPointerException"
            )
        except NullPointerException:
            pass

    def testRead0(self) -> None:

        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        buf = bytearray(1024)
        bytesRead = 0
        bin = io.BytesIO(decoded)
        with Base16InputStream.Base16InputStream2(bin, True) as in_:
            bytesRead = in_.read1(buf, 0, 0)
            assert bytesRead == 0, "Base16InputStream.read(buf, 0, 0) returns 0"

    def testMarkSupported(self) -> None:

        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        bin = io.BytesIO(decoded)
        with Base16InputStream.Base16InputStream2(bin, True) as in_:
            assert not in_.markSupported(), "Base16InputStream.markSupported() is false"

    def testBase16EmptyInputStream(self) -> None:

        emptyEncoded = []
        emptyDecoded = []
        self.__testByteByByte0(emptyEncoded, emptyDecoded)
        self.__testByChunk0(emptyEncoded, emptyDecoded)

    def testAvailable(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            assert b16Stream.available() == 1
            assert b16Stream.skip(10) == 6
            assert b16Stream.available() == 0
            assert b16Stream.read0() == -1
            assert b16Stream.read0() == -1
            assert b16Stream.available() == 0

    def __testByteByByte1(
        self, encoded: typing.List[int], decoded: typing.List[int], lowerCase: bool
    ) -> None:

        # test encoding
        with Base16InputStream.Base16InputStream1(
            io.BytesIO(bytes(decoded)), True, lowerCase
        ) as in_:
            output = [in_.read(1)[0] for _ in range(len(encoded))]
            assert in_.read(1) == b"", "EOF"
            assert in_.read(1) == b"", "Still EOF"
            assert output == encoded, "Streaming Base16 encode"

        # test decoding
        with Base16InputStream.Base16InputStream1(
            io.BytesIO(bytes(encoded)), False, lowerCase
        ) as in_:
            output = [in_.read(1)[0] for _ in range(len(decoded))]
            assert in_.read(1) == b"", "EOF"
            assert in_.read(1) == b"", "Still EOF"
            assert output == decoded, "Streaming Base16 decode"

        # test wrapping
        with io.BytesIO(bytes(decoded)) as in_, Base16InputStream.Base16InputStream1(
            in_, True, lowerCase
        ) as inEncode, Base16InputStream.Base16InputStream1(
            inEncode, False, lowerCase
        ) as inDecode:

            output = [inDecode.read(1)[0] for _ in range(len(decoded))]
            assert inDecode.read(1) == b"", "EOF"
            assert inDecode.read(1) == b"", "Still EOF"
            assert output == decoded, "Streaming Base16 wrap-wrap!"

    def __testByteByByte0(
        self, encoded: typing.List[int], decoded: typing.List[int]
    ) -> None:

        self.__testByteByByte1(encoded, decoded, False)

    def __testByChunk1(
        self, encoded: typing.List[int], decoded: typing.List[int], lowerCase: bool
    ) -> None:

        with Base16InputStream.Base16InputStream1(
            io.BytesIO(decoded), True, lowerCase
        ) as in_:
            output = BaseNTestData.streamToBytes0(in_)

            assert in_.read() == -1, "EOF"
            assert in_.read() == -1, "Still EOF"
            assert output == encoded, "Streaming Base16 encode"

        with Base16InputStream.Base16InputStream1(
            io.BytesIO(encoded), False, lowerCase
        ) as in_:
            output = BaseNTestData.streamToBytes0(in_)

            assert in_.read() == -1, "EOF"
            assert in_.read() == -1, "Still EOF"
            assert output == decoded, "Streaming Base16 decode"

        with io.BytesIO(decoded) as in_, Base16InputStream.Base16InputStream1(
            in_, True, lowerCase
        ) as inEncode, Base16InputStream.Base16InputStream1(
            inEncode, False, lowerCase
        ) as inDecode:

            output = BaseNTestData.streamToBytes0(inDecode)

            assert inDecode.read() == -1, "EOF"
            assert inDecode.read() == -1, "Still EOF"
            assert output == decoded, "Streaming Base16 wrap-wrap!"

    def __testByChunk0(
        self, encoded: typing.List[int], decoded: typing.List[int]
    ) -> None:

        self.__testByChunk1(encoded, decoded, False)
