from __future__ import annotations
import re
from io import BytesIO
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.binary.Base16InputStream import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base16InputStreamTest(unittest.TestCase):

    __STRING_FIXTURE: str = "Hello World"
    __ENCODED_B16: str = "CAFEBABEFFFF"

    def testSkipWrongArgument(self) -> None:

        ins = io.BytesIO(bytes(StringUtils.getBytesIso8859_1(self.__ENCODED_B16)))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            with pytest.raises(ValueError):
                b16Stream.skip(-10)

    def testSkipToEnd(self) -> None:

        ins = io.BytesIO(bytes(StringUtils.getBytesIso8859_1(self.__ENCODED_B16)))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            self.assertEqual(6, b16Stream.skip(6))
            self.assertEqual(-1, b16Stream.read0())
            self.assertEqual(-1, b16Stream.read0())

    def testSkipPastEnd(self) -> None:

        ins = io.BytesIO(bytes(StringUtils.getBytesIso8859_1(self.__ENCODED_B16)))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            self.assertEqual(6, b16Stream.skip(10))
            self.assertEqual(-1, b16Stream.read0())
            self.assertEqual(-1, b16Stream.read0())

    def testSkipNone(self) -> None:

        ins = io.BytesIO(bytes(StringUtils.getBytesIso8859_1(self.__ENCODED_B16)))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            actualBytes = bytearray(6)
            self.assertEqual(0, b16Stream.skip(0))
            b16Stream.read1(actualBytes, 0, len(actualBytes))
            self.assertEqual(actualBytes, bytearray([202, 254, 186, 190, 255, 255]))
            self.assertEqual(-1, b16Stream.read0())

    def testSkipBig(self) -> None:

        ins = io.BytesIO(bytes(StringUtils.getBytesIso8859_1(self.__ENCODED_B16)))
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
                self.fail(
                    "Expected Base16InputStream.read(buf, -1, 0) to throw"
                    + " IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                in_.read1(buf, 0, -1)
                self.fail(
                    "Expected Base16InputStream.read(buf, 0, -1) to throw"
                    + " IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                in_.read1(buf, len(buf) + 1, 0)
                self.fail(
                    "Base16InputStream.read(buf, len(buf) + 1, 0) throws"
                    + " IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                in_.read1(buf, len(buf) - 1, 2)
                self.fail(
                    "Base16InputStream.read(buf, len(buf) - 1, 2) throws"
                    + " IndexOutOfBoundsException"
                )
            except IndexError:
                pass

    def testReadNull(self) -> None:

        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        bin = io.BytesIO(decoded)
        with Base16InputStream.Base16InputStream2(bin, True) as in_:
            try:
                in_.read1(None, 0, 0)
                self.fail("Base16InputStream.read(null, 0, 0) to throw a RuntimeError")
            except Exception as e:
                pass

    def testRead0(self) -> None:

        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        buf = bytearray(1024)
        bytesRead = 0
        bin = io.BytesIO(decoded)
        with Base16InputStream.Base16InputStream2(bin, True) as in_:
            bytesRead = in_.read1(buf, 0, 0)
            self.assertEqual(
                bytesRead, 0, "Base16InputStream.read(buf, 0, 0) returns 0"
            )

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

        ins = io.BytesIO(bytes(StringUtils.getBytesIso8859_1(self.__ENCODED_B16)))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            self.assertEqual(1, b16Stream.available())
            self.assertEqual(6, b16Stream.skip(10))
            self.assertEqual(0, b16Stream.available())
            self.assertEqual(-1, b16Stream.read0())
            self.assertEqual(-1, b16Stream.read0())
            self.assertEqual(0, b16Stream.available())

    def __testByteByByte1(
        self, encoded: typing.List[int], decoded: typing.List[int], lowerCase: bool
    ) -> None:

        # Encoding test
        with Base16InputStream.Base16InputStream1(
            io.BytesIO(bytes(decoded)), True, lowerCase
        ) as in_:
            output = [in_.read(1)[0] for _ in range(len(encoded))]
            self.assertEqual(-1, in_.read(1)[0])
            self.assertEqual(-1, in_.read(1)[0])
            self.assertEqual(encoded, output)

        # Decoding test
        with Base16InputStream.Base16InputStream1(
            io.BytesIO(bytes(encoded)), False, lowerCase
        ) as in_:
            output = [in_.read(1)[0] for _ in range(len(decoded))]
            self.assertEqual(-1, in_.read(1)[0])
            self.assertEqual(-1, in_.read(1)[0])
            self.assertEqual(decoded, output)

        # Wrap-wrap test
        with io.BytesIO(bytes(decoded)) as in_, Base16InputStream.Base16InputStream1(
            in_, True, lowerCase
        ) as inEncode, Base16InputStream.Base16InputStream1(
            inEncode, False, lowerCase
        ) as inDecode:

            output = [inDecode.read(1)[0] for _ in range(len(decoded))]
            self.assertEqual(-1, inDecode.read(1)[0])
            self.assertEqual(-1, inDecode.read(1)[0])
            self.assertEqual(decoded, output)

    def __testByteByByte0(
        self, encoded: typing.List[int], decoded: typing.List[int]
    ) -> None:
        self.__testByteByByte1(encoded, decoded, False)

    def __testByChunk1(
        self, encoded: typing.List[int], decoded: typing.List[int], lowerCase: bool
    ) -> None:

        # Encoding test
        with Base16InputStream.Base16InputStream1(
            io.BytesIO(decoded), True, lowerCase
        ) as in_:
            output = BaseNTestData.streamToBytes0(in_)
            self.assertEqual(-1, in_.read())
            self.assertEqual(-1, in_.read())
            self.assertListEqual(encoded, output)

        # Decoding test
        with Base16InputStream.Base16InputStream1(
            io.BytesIO(encoded), False, lowerCase
        ) as in_:
            output = BaseNTestData.streamToBytes0(in_)
            self.assertEqual(-1, in_.read())
            self.assertEqual(-1, in_.read())
            self.assertListEqual(decoded, output)

        # Wrap-wrap test
        with io.BytesIO(decoded) as in_, Base16InputStream.Base16InputStream1(
            in_, True, lowerCase
        ) as inEncode, Base16InputStream.Base16InputStream1(
            inEncode, False, lowerCase
        ) as inDecode:

            output = BaseNTestData.streamToBytes0(inDecode)
            self.assertEqual(-1, inDecode.read())
            self.assertEqual(-1, inDecode.read())
            self.assertListEqual(decoded, output)

    def __testByChunk0(
        self, encoded: typing.List[int], decoded: typing.List[int]
    ) -> None:
        self.__testByChunk1(encoded, decoded, False)
