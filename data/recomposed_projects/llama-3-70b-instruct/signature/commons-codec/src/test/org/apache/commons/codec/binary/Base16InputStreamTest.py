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
        with pytest.raises(ValueError):
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
            actualBytes = [0] * 6
            self.assertEqual(0, b16Stream.skip(0))
            b16Stream.read1(actualBytes, 0, len(actualBytes))
            self.assertListEqual(actualBytes, [202, 254, 186, 190, 255, 255])
            self.assertEqual(-1, b16Stream.read0())

    def testSkipBig(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))
        with Base16InputStream.Base16InputStream3(ins) as b16Stream:
            self.assertEqual(6, b16Stream.skip(Integer.MAX_VALUE))
            self.assertEqual(-1, b16Stream.read0())
            self.assertEqual(-1, b16Stream.read0())

    def testReadOutOfBounds(self) -> None:
        decoded: typing.List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        buf: typing.List[int] = [0] * 1024
        bin: io.BytesIO = io.BytesIO(bytes(decoded))
        with Base16InputStream.Base16InputStream2(bin, True) as in_:
            try:
                in_.read1(buf, -1, 0)
                self.fail(
                    "Expected Base16InputStream.read(buf, -1, 0) to throw IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                in_.read1(buf, 0, -1)
                self.fail(
                    "Expected Base16InputStream.read(buf, 0, -1) to throw IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                in_.read1(buf, len(buf) + 1, 0)
                self.fail(
                    "Base16InputStream.read(buf, buf.length + 1, 0) throws IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                in_.read1(buf, len(buf) - 1, 2)
                self.fail(
                    "Base16InputStream.read(buf, buf.length - 1, 2) throws IndexOutOfBoundsException"
                )
            except IndexError:
                pass

    def testReadNull(self) -> None:

        pass  # LLM could not translate this method

    def testRead0(self) -> None:
        decoded: typing.List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        buf: typing.List[int] = [0] * 1024
        bytesRead: int = 0
        bin: io.BytesIO = io.BytesIO(decoded)
        with Base16InputStream.Base16InputStream2(bin, True) as in_:
            bytesRead = in_.read1(buf, 0, 0)
            self.assertEqual(
                "Base16InputStream.read(buf, 0, 0) returns 0", 0, bytesRead
            )

    def testMarkSupported(self) -> None:
        decoded: typing.List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        bin: io.BytesIO = io.BytesIO(decoded)
        with Base16InputStream.Base16InputStream2(bin, True) as in_:
            self.assertFalse(
                "Base16InputStream.markSupported() is false", in_.markSupported()
            )

    def testBase16EmptyInputStream(self) -> None:
        emptyEncoded: typing.List[int] = []
        emptyDecoded: typing.List[int] = []
        self.__testByteByByte0(emptyEncoded, emptyDecoded)
        self.__testByChunk0(emptyEncoded, emptyDecoded)

    def testAvailable(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B16))
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
        with Base16InputStream.Base16InputStream1(
            io.BytesIO(decoded), True, lowerCase
        ) as in_:
            output = [0] * len(encoded)
            for i in range(len(output)):
                output[i] = in_.read()
            self.assertEqual(-1, in_.read())
            self.assertEqual(-1, in_.read())
            self.assertListEqual(encoded, output)
        with Base16InputStream.Base16InputStream1(
            io.BytesIO(encoded), False, lowerCase
        ) as in_:
            output = [0] * len(decoded)
            for i in range(len(output)):
                output[i] = in_.read()
            self.assertEqual(-1, in_.read())
            self.assertEqual(-1, in_.read())
            self.assertListEqual(decoded, output)
        with io.BytesIO(decoded) as in_, Base16InputStream.Base16InputStream1(
            in_, True, lowerCase
        ) as inEncode, Base16InputStream.Base16InputStream1(
            inEncode, False, lowerCase
        ) as inDecode:
            output = [0] * len(decoded)
            for i in range(len(output)):
                output[i] = inDecode.read()
            self.assertEqual(-1, inDecode.read())
            self.assertEqual(-1, inDecode.read())
            self.assertListEqual(decoded, output)

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
            output: typing.List[int] = BaseNTestData.streamToBytes0(in_)

            self.assertEqual(-1, in_.read(), "EOF")
            self.assertEqual(-1, in_.read(), "Still EOF")
            self.assertArrayEquals("Streaming Base16 encode", encoded, output)

        with Base16InputStream.Base16InputStream1(
            io.BytesIO(encoded), False, lowerCase
        ) as in_:
            output: typing.List[int] = BaseNTestData.streamToBytes0(in_)

            self.assertEqual(-1, in_.read(), "EOF")
            self.assertEqual(-1, in_.read(), "Still EOF")
            self.assertArrayEquals("Streaming Base16 decode", decoded, output)

        with io.BytesIO(decoded) as in_, Base16InputStream.Base16InputStream1(
            in_, True, lowerCase
        ) as inEncode, Base16InputStream.Base16InputStream1(
            inEncode, False, lowerCase
        ) as inDecode:

            output: typing.List[int] = BaseNTestData.streamToBytes0(inDecode)

            self.assertEqual(-1, inDecode.read(), "EOF")
            self.assertEqual(-1, inDecode.read(), "Still EOF")
            self.assertArrayEquals("Streaming Base16 wrap-wrap!", decoded, output)

    def __testByChunk0(
        self, encoded: typing.List[int], decoded: typing.List[int]
    ) -> None:
        self.__testByChunk1(encoded, decoded, False)
