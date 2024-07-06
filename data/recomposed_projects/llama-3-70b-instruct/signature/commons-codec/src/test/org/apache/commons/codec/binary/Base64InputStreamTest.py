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
            self.assertEqual(6, b64stream.skip(6))
            self.assertEqual(-1, b64stream.read0())
            self.assertEqual(-1, b64stream.read0())

    def testSkipPastEnd(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            self.assertEqual(6, b64stream.skip(10))
            self.assertEqual(-1, b64stream.read0())
            self.assertEqual(-1, b64stream.read0())

    def testSkipNone(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            actualBytes = [0] * 6
            self.assertEqual(0, b64stream.skip(0))
            b64stream.read1(actualBytes, 0, len(actualBytes))
            self.assertListEqual(actualBytes, [0, 0, 0, 255, 255, 255])
            self.assertEqual(-1, b64stream.read0())

    def testSkipBig(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            self.assertEqual(6, b64stream.skip(Integer.MAX_VALUE))
            self.assertEqual(-1, b64stream.read0())
            self.assertEqual(-1, b64stream.read0())

    def testReadOutOfBounds(self) -> None:
        decoded: typing.List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        buf: typing.List[int] = [0] * 1024
        bin: io.BytesIO = io.BytesIO(bytes(decoded))
        with Base64InputStream.Base64InputStream2(bin, True, 4, [0, 0, 0]) as in_:
            try:
                in_.read1(buf, -1, 0)
                self.fail(
                    "Expected Base64InputStream.read(buf, -1, 0) to throw IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                in_.read1(buf, 0, -1)
                self.fail(
                    "Expected Base64InputStream.read(buf, 0, -1) to throw IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                in_.read1(buf, len(buf) + 1, 0)
                self.fail(
                    "Base64InputStream.read(buf, buf.length + 1, 0) throws IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                in_.read1(buf, len(buf) - 1, 2)
                self.fail(
                    "Base64InputStream.read(buf, buf.length - 1, 2) throws IndexOutOfBoundsException"
                )
            except IndexError:
                pass

    def testReadNull(self) -> None:

        pass  # LLM could not translate this method

    def testRead0(self) -> None:
        decoded: typing.List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        buf: typing.List[int] = [0] * 1024
        bytesRead: int = 0
        bin: io.BytesIO = io.BytesIO(bytes(decoded))
        with Base64InputStream.Base64InputStream2(bin, True, 4, [0, 0, 0]) as in_:
            bytesRead = in_.read1(buf, 0, 0)
            self.assertEqual(
                "Base64InputStream.read(buf, 0, 0) returns 0", 0, bytesRead
            )

    def testMarkSupported(self) -> None:
        decoded: typing.List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        bin: io.BytesIO = io.BytesIO(decoded)
        with BaseNCodecInputStream(
            Base64InputStream.Base64InputStream2(bin, True, 4, [0, 0, 0])
        ) as in_:
            self.assertFalse(
                "Base64InputStream.markSupported() is false", in_.markSupported()
            )

    def testBase64EmptyInputStreamPemChuckSize(self) -> None:
        self.__testBase64EmptyInputStream(BaseNCodec.PEM_CHUNK_SIZE)

    def testBase64EmptyInputStreamMimeChuckSize(self) -> None:
        self.__testBase64EmptyInputStream(BaseNCodec.MIME_CHUNK_SIZE)

    def testAvailable(self) -> None:
        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            self.assertEqual(1, b64stream.available())
            self.assertEqual(6, b64stream.skip(10))
            self.assertEqual(0, b64stream.available())
            self.assertEqual(-1, b64stream.read0())
            self.assertEqual(-1, b64stream.read0())
            self.assertEqual(0, b64stream.available())

    def testInputStreamReader(self) -> None:
        codec101 = StringUtils.getBytesUtf8(
            Base64TestData.CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3
        )
        bais = io.BytesIO(codec101)
        in_ = Base64InputStream.Base64InputStream0(bais)
        isr = io.BufferedReader(in_)
        with io.BufferedReader(isr) as br:
            line = br.readLine()
            self.assertIsNotNone(line, "Codec101:  InputStreamReader works!")

    def testCodec101(self) -> None:
        codec101 = StringUtils.getBytesUtf8(
            Base64TestData.CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3
        )
        bais = io.BytesIO(codec101)
        with Base64InputStream.Base64InputStream0(bais) as in_:
            result = [0] * 8192
            c = in_.read(result)
            self.assertTrue("Codec101: First read successful [c=" + str(c) + "]", c > 0)

            c = in_.read(result)
            self.assertTrue(
                "Codec101: Second read should report end-of-stream [c=" + str(c) + "]",
                c < 0,
            )

    def testCodec105(self) -> None:
        with BaseNCodecInputStream(
            Base64InputStream.Base64InputStream2(
                Codec105ErrorInputStream(), True, 0, None
            )
        ) as in_:
            for i in range(5):
                in_.read0()

    def __testByteByByte(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = (
            Base64InputStream.Base64InputStream2(
                io.BytesIO(decoded), True, chunkSize, separator
            )
        )
        output: typing.List[int] = [0] * len(encoded)
        for i in range(len(output)):
            output[i] = in_.read(1)[0]
        self.assertEqual(-1, in_.read(1)[0])
        self.assertEqual(-1, in_.read(1)[0])
        self.assertListEqual(encoded, output)
        in_.close()
        in_ = Base64InputStream.Base64InputStream0(io.BytesIO(encoded))
        output = [0] * len(decoded)
        for i in range(len(output)):
            output[i] = in_.read(1)[0]
        self.assertEqual(-1, in_.read(1)[0])
        self.assertEqual(-1, in_.read(1)[0])
        self.assertListEqual(decoded, output)
        in_.close()
        in_ = io.BytesIO(decoded)
        for i in range(10):
            in_ = Base64InputStream.Base64InputStream2(in_, True, chunkSize, separator)
            in_ = Base64InputStream.Base64InputStream1(in_, False)
        output = [0] * len(decoded)
        for i in range(len(output)):
            output[i] = in_.read(1)[0]
        self.assertEqual(-1, in_.read(1)[0])
        self.assertEqual(-1, in_.read(1)[0])
        self.assertListEqual(decoded, output)
        in_.close()

    def __testByChunk(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader] = None
        in_ = Base64InputStream.Base64InputStream2(
            io.BytesIO(decoded), True, chunkSize, separator
        )
        output: typing.List[int] = BaseNTestData.streamToBytes0(in_)

        self.assertEqual(-1, in_.read(), "EOF")
        self.assertEqual(-1, in_.read(), "Still EOF")
        self.assertArrayEquals(encoded, output, "Streaming base64 encode")

        in_.close()

        in_ = Base64InputStream.Base64InputStream0(io.BytesIO(encoded))
        output = BaseNTestData.streamToBytes0(in_)

        self.assertEqual(-1, in_.read(), "EOF")
        self.assertEqual(-1, in_.read(), "Still EOF")
        self.assertArrayEquals(decoded, output, "Streaming base64 decode")

        in_ = io.BytesIO(decoded)
        for i in range(10):
            in_ = Base64InputStream.Base64InputStream2(in_, True, chunkSize, separator)
            in_ = Base64InputStream.Base64InputStream1(in_, False)
        output = BaseNTestData.streamToBytes0(in_)

        self.assertEqual(-1, in_.read(), "EOF")
        self.assertEqual(-1, in_.read(), "Still EOF")
        self.assertArrayEquals(decoded, output, "Streaming base64 wrap-wrap-wrap!")
        in_.close()

    def __testBase64EmptyInputStream(self, chuckSize: int) -> None:
        emptyEncoded: typing.List[int] = []
        emptyDecoded: typing.List[int] = []
        self.__testByteByByte(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)
        self.__testByChunk(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)
