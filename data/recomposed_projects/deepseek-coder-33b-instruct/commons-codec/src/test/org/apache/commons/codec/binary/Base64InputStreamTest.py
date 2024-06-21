from __future__ import annotations
import re
import sys
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.binary.Base64InputStream import *
from src.test.org.apache.commons.codec.binary.Base64TestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.test.org.apache.commons.codec.binary.Codec105ErrorInputStream import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base64InputStreamTest(unittest.TestCase):

    __STRING_FIXTURE: str = "Hello World"

    __LF: typing.List[int] = [10]

    __CRLF: typing.List[int] = [13, 10]

    __ENCODED_B64: str = "AAAA////"

    def testSkipWrongArgument(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            b64stream.skip(-10)

    def testSkipToEnd(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            assert b64stream.skip(6) == 6
            assert b64stream.read0() == -1
            assert b64stream.read0() == -1

    def testSkipPastEnd(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            assert b64stream.skip(10) == 6
            assert b64stream.read0() == -1
            assert b64stream.read0() == -1

    def testSkipNone(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            actualBytes = bytearray(6)
            assert b64stream.skip(0) == 0
            b64stream.read1(actualBytes, 0, len(actualBytes))
            assert actualBytes == bytearray([0, 0, 0, 255, 255, 255])
            assert b64stream.read0() == -1

    def testSkipBig(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            assert b64stream.skip(sys.maxsize) == 6
            assert b64stream.read0() == -1
            assert b64stream.read0() == -1

    def testReadOutOfBounds(self) -> None:

        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        buf = bytearray(1024)
        bin = io.BytesIO(decoded)

        with Base64InputStream.Base64InputStream2(
            bin, True, 4, bytearray([0, 0, 0])
        ) as inp:

            try:
                inp.read1(buf, -1, 0)
                assert (
                    False
                ), "Expected Base64InputStream.read(buf, -1, 0) to throw IndexOutOfBoundsException"
            except IndexError:
                pass

            try:
                inp.read1(buf, 0, -1)
                assert (
                    False
                ), "Expected Base64InputStream.read(buf, 0, -1) to throw IndexOutOfBoundsException"
            except IndexError:
                pass

            try:
                inp.read1(buf, len(buf) + 1, 0)
                assert (
                    False
                ), "Expected Base64InputStream.read(buf, len(buf) + 1, 0) to throw IndexOutOfBoundsException"
            except IndexError:
                pass

            try:
                inp.read1(buf, len(buf) - 1, 2)
                assert (
                    False
                ), "Expected Base64InputStream.read(buf, len(buf) - 1, 2) to throw IndexOutOfBoundsException"
            except IndexError:
                pass

    def testReadNull(self) -> None:

        decoded: bytes = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        bin: io.BytesIO = io.BytesIO(decoded)
        try:
            with Base64InputStream.Base64InputStream2(
                bin, True, 4, bytes([0, 0, 0])
            ) as in_stream:
                in_stream.read1(None, 0, 0)
            self.fail(
                "Base64InputStream.read(None, 0, 0) to throw a NullPointerException"
            )
        except NullPointerException:
            pass

    def testRead0(self) -> None:

        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        buf = bytearray(1024)
        bytesRead = 0
        bin = io.BytesIO(decoded)
        try:
            in_stream = Base64InputStream.Base64InputStream2(
                bin, True, 4, bytearray([0, 0, 0])
            )
            bytesRead = in_stream.read1(buf, 0, 0)
            assert bytesRead == 0, "Base64InputStream.read(buf, 0, 0) returns 0"
        finally:
            in_stream.close()

    def testMarkSupported(self) -> None:

        decoded: bytes = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        bin: io.BytesIO = io.BytesIO(decoded)

        with Base64InputStream.Base64InputStream2(
            bin, True, 4, bytes([0, 0, 0])
        ) as in_stream:
            assert (
                not in_stream.markSupported()
            ), "Base64InputStream.markSupported() is false"

    def testBase64EmptyInputStreamPemChuckSize(self) -> None:

        self.__testBase64EmptyInputStream(BaseNCodec.PEM_CHUNK_SIZE)

    def testBase64EmptyInputStreamMimeChuckSize(self) -> None:

        self.__testBase64EmptyInputStream(BaseNCodec.MIME_CHUNK_SIZE)

    def testAvailable(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            assert b64stream.available() == 1
            assert b64stream.skip(10) == 6
            assert b64stream.available() == 0
            assert b64stream.read0() == -1
            assert b64stream.read0() == -1
            assert b64stream.available() == 0

    def testInputStreamReader(self) -> None:

        codec101 = StringUtils.getBytesUtf8(
            Base64TestData.CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3
        )
        bais = io.BytesIO(codec101)
        in_stream = Base64InputStream.Base64InputStream0(bais)
        isr = io.TextIOWrapper(io.BufferedReader(in_stream))

        line = isr.readline()
        assert line is not None, "Codec101:  InputStreamReader works!"

    def testCodec101(self) -> None:

        codec101 = StringUtils.getBytesUtf8(
            Base64TestData.CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3
        )
        bais = io.BytesIO(codec101)
        with Base64InputStream.Base64InputStream0(bais) as in_stream:
            result = bytearray(8192)
            c = in_stream.readinto(result)
            assert c > 0, "Codec101: First read successful [c=" + str(c) + "]"

            c = in_stream.readinto(result)
            assert c == -1, (
                "Codec101: Second read should report end-of-stream [c=" + str(c) + "]"
            )

    def testCodec105(self) -> None:

        try:
            in_ = Base64InputStream.Base64InputStream2(
                Codec105ErrorInputStream(), True, 0, None
            )
            for i in range(5):
                in_.read0()
        finally:
            in_.close()

    def __testByteByByte(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:

        in_stream = Base64InputStream.Base64InputStream2(
            io.BytesIO(bytes(decoded)), True, chunkSize, bytes(separator)
        )
        output = list(in_stream.read())

        assert -1 == in_stream.read(), "EOF"
        assert -1 == in_stream.read(), "Still EOF"
        assert encoded == output, "Streaming base64 encode"

        in_stream.close()

        in_stream = Base64InputStream.Base64InputStream0(io.BytesIO(bytes(encoded)))
        output = list(in_stream.read())

        assert -1 == in_stream.read(), "EOF"
        assert -1 == in_stream.read(), "Still EOF"
        assert decoded == output, "Streaming base64 decode"

        in_stream.close()

        in_stream = io.BytesIO(bytes(decoded))
        for i in range(10):
            in_stream = Base64InputStream.Base64InputStream2(
                in_stream, True, chunkSize, bytes(separator)
            )
            in_stream = Base64InputStream.Base64InputStream1(in_stream, False)

        output = list(in_stream.read())

        assert -1 == in_stream.read(), "EOF"
        assert -1 == in_stream.read(), "Still EOF"
        assert decoded == output, "Streaming base64 wrap-wrap-wrap!"

        in_stream.close()

    def __testByChunk(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:

        in_stream = Base64InputStream.Base64InputStream2(
            io.BytesIO(bytes(decoded)), True, chunkSize, bytes(separator)
        )
        output = BaseNTestData.streamToBytes0(in_stream)

        assert in_stream.read() == -1
        assert in_stream.read() == -1
        assert output == encoded

        in_stream.close()

        in_stream = Base64InputStream.Base64InputStream0(io.BytesIO(bytes(encoded)))
        output = BaseNTestData.streamToBytes0(in_stream)

        assert in_stream.read() == -1
        assert in_stream.read() == -1
        assert output == decoded

        in_stream = io.BytesIO(bytes(decoded))
        for i in range(10):
            in_stream = Base64InputStream.Base64InputStream2(
                in_stream, True, chunkSize, bytes(separator)
            )
            in_stream = Base64InputStream.Base64InputStream1(in_stream, False)

        output = BaseNTestData.streamToBytes0(in_stream)

        assert in_stream.read() == -1
        assert in_stream.read() == -1
        assert output == decoded

        in_stream.close()

    def __testBase64EmptyInputStream(self, chuckSize: int) -> None:

        emptyEncoded = b""
        emptyDecoded = b""
        self.__testByteByByte(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)
        self.__testByChunk(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)
