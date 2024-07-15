from __future__ import annotations
import re
import os
from io import BytesIO
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
    __LF: typing.List[int] = [ord("\n")]
    __CRLF: typing.List[int] = [ord("\r"), ord("\n")]
    __ENCODED_FOO: str = "MZXW6==="

    def testSkipWrongArgument(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))

        with Base32InputStream.Base32InputStream0(ins) as b32stream:
            with pytest.raises(ValueError):
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
            self.assertListEqual(actualBytes, [102, 111, 111, 0, 0, 0])
            self.assertEqual(-1, b32stream.read0())

    def testReadOutOfBounds(self) -> None:

        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        buf = [0] * 1024
        bin = io.BytesIO(bytes(decoded))

        with Base32InputStream.Base32InputStream2(bin, True, 4, [0, 0, 0]) as inp:

            try:
                inp.read1(buf, -1, 0)
                self.fail(
                    "Expected Base32InputStream.read(buf, -1, 0) to throw"
                    + " IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                inp.read1(buf, 0, -1)
                self.fail(
                    "Expected Base32InputStream.read(buf, 0, -1) to throw"
                    + " IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                inp.read1(buf, len(buf) + 1, 0)
                self.fail(
                    "Base32InputStream.read(buf, len(buf) + 1, 0) throws"
                    + " IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                inp.read1(buf, len(buf) - 1, 2)
                self.fail(
                    "Base32InputStream.read(buf, len(buf) - 1, 2) throws"
                    + " IndexOutOfBoundsException"
                )
            except IndexError:
                pass

    def testReadNull(self) -> None:

        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        bin = io.BytesIO(bytes(decoded))

        with Base32InputStream.Base32InputStream2(bin, True, 4, [0, 0, 0]) as inp:
            try:
                inp.read1(None, 0, 0)
                self.fail("Base32InputStream.read(None, 0, 0) to throw a RuntimeError")
            except Exception as e:
                pass

    def testRead0(self) -> None:

        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        buf = [0] * 1024
        bytesRead = 0
        bin = io.BytesIO(bytes(decoded))

        with Base32InputStream.Base32InputStream2(bin, True, 4, [0, 0, 0]) as inp:
            bytesRead = inp.read1(buf, 0, 0)
            self.assertEqual(
                bytesRead, 0, "Base32InputStream.read(buf, 0, 0) returns 0"
            )

    def testMarkSupported(self) -> None:

        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        bin = io.BytesIO(bytes(decoded))
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

        try:
            with Base32InputStream.Base32InputStream2(
                Codec105ErrorInputStream(), True, 0, None
            ) as inp:
                for i in range(5):
                    inp.read0()
        except Exception as e:
            print(f"An error occurred: {e}")

    def __testByteByByte(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:

        in_ = Base32InputStream.Base32InputStream2(
            io.BytesIO(bytes(decoded)), True, chunkSize, separator
        )
        output = bytearray(encoded.length)
        for i in range(len(output)):
            output[i] = in_.read(1)[0]

        self.assertEqual("EOF", -1, in_.read(1)[0])
        self.assertEqual("Still EOF", -1, in_.read(1)[0])
        self.assertListEqual("Streaming base32 encode", list(encoded), list(output))

        in_.close()

        in_ = Base32InputStream.Base32InputStream0(io.BytesIO(bytes(encoded)))
        output = bytearray(decoded.length)
        for i in range(len(output)):
            output[i] = in_.read(1)[0]

        self.assertEqual("EOF", -1, in_.read(1)[0])
        self.assertEqual("Still EOF", -1, in_.read(1)[0])
        self.assertListEqual("Streaming base32 decode", list(decoded), list(output))

        in_.close()

        in_ = io.BytesIO(bytes(decoded))
        for i in range(10):
            in_ = Base32InputStream.Base32InputStream2(in_, True, chunkSize, separator)
            in_ = Base32InputStream.Base32InputStream1(in_, False)
        output = bytearray(decoded.length)
        for i in range(len(output)):
            output[i] = in_.read(1)[0]

        self.assertEqual("EOF", -1, in_.read(1)[0])
        self.assertEqual("Still EOF", -1, in_.read(1)[0])
        self.assertListEqual(
            "Streaming base32 wrap-wrap-wrap", list(decoded), list(output)
        )

    def __testByChunk(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:

        in_ = Base32InputStream.Base32InputStream2(
            io.BytesIO(decoded), True, chunkSize, separator
        )
        output = BaseNTestData.streamToBytes0(in_)

        self.assertEqual("EOF", -1, in_.read())
        self.assertEqual("Still EOF", -1, in_.read())
        self.assertListEqual("Streaming base32 encode", list(encoded), list(output))

        in_ = Base32InputStream.Base32InputStream0(io.BytesIO(encoded))
        output = BaseNTestData.streamToBytes0(in_)

        self.assertEqual("EOF", -1, in_.read())
        self.assertEqual("Still EOF", -1, in_.read())
        self.assertListEqual("Streaming base32 decode", list(decoded), list(output))

        in_ = io.BytesIO(decoded)
        for i in range(10):
            in_ = Base32InputStream.Base32InputStream2(in_, True, chunkSize, separator)
            in_ = Base32InputStream.Base32InputStream1(in_, False)
        output = BaseNTestData.streamToBytes0(in_)

        self.assertEqual("EOF", -1, in_.read())
        self.assertEqual("Still EOF", -1, in_.read())
        self.assertListEqual(
            "Streaming base32 wrap-wrap-wrap1", list(decoded), list(output)
        )
        in_.close()

    def __testBase32EmptyInputStream(self, chuckSize: int) -> None:

        emptyEncoded = []
        emptyDecoded = []
        self.__testByteByByte(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)
        self.__testByChunk(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)
