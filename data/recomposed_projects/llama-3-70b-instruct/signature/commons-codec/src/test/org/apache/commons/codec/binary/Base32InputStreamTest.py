from __future__ import annotations
import re
import os
from io import BytesIO
from io import StringIO
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.binary.Base32InputStream import *
from src.test.org.apache.commons.codec.binary.Base32TestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.test.org.apache.commons.codec.binary.Codec105ErrorInputStream import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base32InputStreamTest(unittest.TestCase):

    __STRING_FIXTURE: str = "Hello World"
    __LF: typing.List[int] = [10]
    __CRLF: typing.List[int] = [13, 10]
    __ENCODED_FOO: str = "MZXW6==="

    def testSkipWrongArgument(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))
        with Base32InputStream.Base32InputStream0(ins) as b32stream:
            b32stream.skip(-10)

    def testSkipToEnd(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))
        with Base32InputStream.Base32InputStream0(ins) as b32stream:
            self.assertEqual(3, b32stream.skip(3))
            self.assertEqual(-1, b32stream.read0())
            self.assertEqual(-1, b32stream.read0())

    def testSkipPastEnd(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))
        with Base32InputStream.Base32InputStream0(ins) as b32stream:
            self.assertEqual(3, b32stream.skip(10))
            self.assertEqual(-1, b32stream.read0())
            self.assertEqual(-1, b32stream.read0())

    def testSkipBig(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))
        with Base32InputStream.Base32InputStream0(ins) as b32stream:
            self.assertEqual(3, b32stream.skip(1024))
            self.assertEqual(-1, b32stream.read0())
            self.assertEqual(-1, b32stream.read0())

    def testSkipNone(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))
        with Base32InputStream.Base32InputStream0(ins) as b32stream:
            actualBytes = [0] * 6
            self.assertEqual(0, b32stream.skip(0))
            b32stream.read1(actualBytes, 0, len(actualBytes))
            self.assertEqual(actualBytes, [102, 111, 111, 0, 0, 0])
            self.assertEqual(-1, b32stream.read0())

    def testReadOutOfBounds(self) -> None:
        decoded: typing.List[int] = StringUtils.getBytesUtf8(
            Base32TestData.STRING_FIXTURE
        )
        buf: typing.List[int] = [0] * 1024
        bin: io.BytesIO = io.BytesIO(bytes(decoded))
        with Base32InputStream.Base32InputStream2(bin, True, 4, [0, 0, 0]) as in_:
            try:
                in_.read1(buf, -1, 0)
                self.fail(
                    "Expected Base32InputStream.read(buf, -1, 0) to throw IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                in_.read1(buf, 0, -1)
                self.fail(
                    "Expected Base32InputStream.read(buf, 0, -1) to throw IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                in_.read1(buf, len(buf) + 1, 0)
                self.fail(
                    "Base32InputStream.read(buf, buf.length + 1, 0) throws IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                in_.read1(buf, len(buf) - 1, 2)
                self.fail(
                    "Base32InputStream.read(buf, buf.length - 1, 2) throws IndexOutOfBoundsException"
                )
            except IndexError:
                pass

    def testReadNull(self) -> None:

        pass  # LLM could not translate this method

    def testRead0(self) -> None:

        pass  # LLM could not translate this method

    def testMarkSupported(self) -> None:
        decoded: typing.List[int] = StringUtils.getBytesUtf8(
            Base32TestData.STRING_FIXTURE
        )
        bin: io.BytesIO = io.BytesIO(decoded)
        with Base32InputStream.Base32InputStream2(bin, True, 4, [0, 0, 0]) as in_:
            self.assertFalse(
                in_.markSupported(), "Base32InputStream.markSupported() is false"
            )

    def testBase32EmptyInputStreamPemChuckSize(self) -> None:
        self.__testBase32EmptyInputStream(BaseNCodec.PEM_CHUNK_SIZE)

    def testBase32EmptyInputStreamMimeChuckSize(self) -> None:
        self.__testBase32EmptyInputStream(BaseNCodec.MIME_CHUNK_SIZE)

    def testAvailable(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))
        with Base32InputStream.Base32InputStream0(ins) as b32stream:
            self.assertEqual(1, b32stream.available())
            self.assertEqual(3, b32stream.skip(10))
            self.assertEqual(0, b32stream.available())
            self.assertEqual(-1, b32stream.read0())
            self.assertEqual(-1, b32stream.read0())
            self.assertEqual(0, b32stream.available())

    def testCodec105(self) -> None:

        pass  # LLM could not translate this method

    def __testByteByByte(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:

        pass  # LLM could not translate this method

    def __testByChunk(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None

        in_ = Base32InputStream.Base32InputStream2(
            io.BytesIO(decoded), True, chunkSize, separator
        )
        output: typing.List[int] = BaseNTestData.streamToBytes0(in_)

        self.assertEqual(-1, in_.read(), "EOF")
        self.assertEqual(-1, in_.read(), "Still EOF")
        self.assertArrayEquals("Streaming base32 encode", encoded, output)

        in_ = Base32InputStream.Base32InputStream0(io.BytesIO(encoded))
        output = BaseNTestData.streamToBytes0(in_)

        self.assertEqual(-1, in_.read(), "EOF")
        self.assertEqual(-1, in_.read(), "Still EOF")
        self.assertArrayEquals("Streaming base32 decode", decoded, output)

        in_ = io.BytesIO(decoded)
        for i in range(10):
            in_ = Base32InputStream.Base32InputStream2(in_, True, chunkSize, separator)
            in_ = Base32InputStream.Base32InputStream1(in_, False)
        output = BaseNTestData.streamToBytes0(in_)

        self.assertEqual(-1, in_.read(), "EOF")
        self.assertEqual(-1, in_.read(), "Still EOF")
        self.assertArrayEquals("Streaming base32 wrap-wrap-wrap!", decoded, output)
        in_.close()

    def __testBase32EmptyInputStream(self, chuckSize: int) -> None:
        emptyEncoded: typing.List[int] = []
        emptyDecoded: typing.List[int] = []
        self.__testByteByByte(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)
        self.__testByChunk(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)
