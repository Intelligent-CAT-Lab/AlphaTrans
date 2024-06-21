from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
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

    __CRLF: typing.List[int] = [ord("\r"), ord("\n")]

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
        try:
            b32stream = Base32InputStream.Base32InputStream0(ins)
            self.assertEqual(3, b32stream.skip(1024))
            self.assertEqual(-1, b32stream.read0())
            self.assertEqual(-1, b32stream.read0())
        finally:
            b32stream.close()

    def testSkipNone(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))
        with Base32InputStream.Base32InputStream0(ins) as b32stream:
            actualBytes = bytearray(6)
            assert b32stream.skip(0) == 0
            b32stream.read1(actualBytes, 0, len(actualBytes))
            assert actualBytes == bytearray([102, 111, 111, 0, 0, 0])
            assert b32stream.read0() == -1

    def testReadOutOfBounds(self) -> None:

        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        buf = bytearray(1024)
        bin = io.BytesIO(decoded)

        with Base32InputStream.Base32InputStream2(
            bin, True, 4, bytearray([0, 0, 0])
        ) as inp:

            try:
                inp.read1(buf, -1, 0)
                assert (
                    False
                ), "Expected Base32InputStream.read(buf, -1, 0) to throw IndexOutOfBoundsException"
            except IndexError:
                pass

            try:
                inp.read1(buf, 0, -1)
                assert (
                    False
                ), "Expected Base32InputStream.read(buf, 0, -1) to throw IndexOutOfBoundsException"
            except IndexError:
                pass

            try:
                inp.read1(buf, len(buf) + 1, 0)
                assert (
                    False
                ), "Expected Base32InputStream.read(buf, len(buf) + 1, 0) to throw IndexOutOfBoundsException"
            except IndexError:
                pass

            try:
                inp.read1(buf, len(buf) - 1, 2)
                assert (
                    False
                ), "Expected Base32InputStream.read(buf, len(buf) - 1, 2) to throw IndexOutOfBoundsException"
            except IndexError:
                pass

    def testReadNull(self) -> None:

        decoded: bytes = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        bin: ByteArrayInputStream = ByteArrayInputStream(decoded)
        try:
            in_stream: BaseNCodecInputStream = Base32InputStream.Base32InputStream2(
                bin, True, 4, bytes([0, 0, 0])
            )
            in_stream.read1(None, 0, 0)
            self.fail(
                "Base32InputStream.read(None, 0, 0) to throw a NullPointerException"
            )
        except NullPointerException:
            pass

    def testRead0(self) -> None:

        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        buf = bytearray(1024)
        bytesRead = 0
        bin = io.BytesIO(decoded)
        with Base32InputStream.Base32InputStream2(
            bin, True, 4, bytearray([0, 0, 0])
        ) as inp:
            bytesRead = inp.read1(buf, 0, 0)
            assert bytesRead == 0, "Base32InputStream.read(buf, 0, 0) returns 0"

    def testMarkSupported(self) -> None:

        decoded: bytes = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        bin: ByteArrayInputStream = ByteArrayInputStream(decoded)
        try:
            in_: BaseNCodecInputStream = Base32InputStream.Base32InputStream2(
                bin, True, 4, bytes([0, 0, 0])
            )
            assert not in_.markSupported(), "Base32InputStream.markSupported() is false"
        finally:
            in_.close()

    def testBase32EmptyInputStreamPemChuckSize(self) -> None:

        self.__testBase32EmptyInputStream(BaseNCodec.PEM_CHUNK_SIZE)

    def testBase32EmptyInputStreamMimeChuckSize(self) -> None:

        self.__testBase32EmptyInputStream(BaseNCodec.MIME_CHUNK_SIZE)

    def testAvailable(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_FOO))
        b32stream = Base32InputStream.Base32InputStream0(ins)

        try:
            self.assertEqual(1, b32stream.available())
            self.assertEqual(3, b32stream.skip(10))
            self.assertEqual(0, b32stream.available())
            self.assertEqual(-1, b32stream.read0())
            self.assertEqual(-1, b32stream.read0())
            self.assertEqual(0, b32stream.available())
        finally:
            b32stream.close()

    def testCodec105(self) -> None:

        try:
            with Base32InputStream.Base32InputStream2(
                Codec105ErrorInputStream(), True, 0, None
            ) as in_:
                for i in range(5):
                    in_.read0()
        except Exception as e:
            print(f"An error occurred: {e}")

    def __testByteByByte(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:

        in_stream = Base32InputStream.Base32InputStream2(
            io.BytesIO(bytes(decoded)), True, chunkSize, bytes(separator)
        )
        output = list(in_stream.read())

        assert -1 == in_stream.read(), "EOF"
        assert -1 == in_stream.read(), "Still EOF"
        assert encoded == output, "Streaming base32 encode"

        in_stream.close()

        in_stream = Base32InputStream.Base32InputStream0(io.BytesIO(bytes(encoded)))
        output = list(in_stream.read())

        assert -1 == in_stream.read(), "EOF"
        assert -1 == in_stream.read(), "Still EOF"
        assert decoded == output, "Streaming base32 decode"

        in_stream.close()

        in_stream = io.BytesIO(bytes(decoded))
        for i in range(10):
            in_stream = Base32InputStream.Base32InputStream2(
                in_stream, True, chunkSize, bytes(separator)
            )
            in_stream = Base32InputStream.Base32InputStream1(in_stream, False)

        output = list(in_stream.read())

        assert -1 == in_stream.read(), "EOF"
        assert -1 == in_stream.read(), "Still EOF"
        assert decoded == output, "Streaming base32 wrap-wrap-wrap!"

    def __testByChunk(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:

        in_stream = Base32InputStream.Base32InputStream2(
            io.BytesIO(bytes(decoded)), True, chunkSize, bytes(separator)
        )
        output = BaseNTestData.streamToBytes0(in_stream)

        assert in_stream.read() == -1
        assert in_stream.read() == -1
        assert output == encoded

        in_stream = Base32InputStream.Base32InputStream0(io.BytesIO(bytes(encoded)))
        output = BaseNTestData.streamToBytes0(in_stream)

        assert in_stream.read() == -1
        assert in_stream.read() == -1
        assert output == decoded

        in_stream = io.BytesIO(bytes(decoded))
        for i in range(10):
            in_stream = Base32InputStream.Base32InputStream2(
                in_stream, True, chunkSize, bytes(separator)
            )
            in_stream = Base32InputStream.Base32InputStream1(in_stream, False)

        output = BaseNTestData.streamToBytes0(in_stream)

        assert in_stream.read() == -1
        assert in_stream.read() == -1
        assert output == decoded
        in_stream.close()

    def __testBase32EmptyInputStream(self, chuckSize: int) -> None:

        emptyEncoded = b""
        emptyDecoded = b""
        self.__testByteByByte(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)
        self.__testByChunk(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)
