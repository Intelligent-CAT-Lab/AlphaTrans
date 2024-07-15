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
from src.main.org.apache.commons.codec.binary.Base64InputStream import *
from src.test.org.apache.commons.codec.binary.Base64TestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.test.org.apache.commons.codec.binary.Codec105ErrorInputStream import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base64InputStreamTest(unittest.TestCase):

    __STRING_FIXTURE: str = "Hello World"
    __LF: typing.List[int] = [ord("\n")]
    __CRLF: typing.List[int] = [ord("\r"), ord("\n")]
    __ENCODED_B64: str = "AAAA////"

    def testSkipWrongArgument(self) -> None:

        ins = io.BytesIO(StringUtils.getBytesIso8859_1(self.__ENCODED_B64))
        with Base64InputStream.Base64InputStream0(ins) as b64stream:
            with pytest.raises(ValueError):
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
            self.assertEqual(6, b64stream.skip(2**31 - 1))
            self.assertEqual(-1, b64stream.read0())
            self.assertEqual(-1, b64stream.read0())

    def testReadOutOfBounds(self) -> None:

        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        buf = [0] * 1024
        bin = io.BytesIO(bytes(decoded))

        with Base64InputStream.Base64InputStream2(bin, True, 4, [0, 0, 0]) as in_:

            try:
                in_.read1(buf, -1, 0)
                self.fail(
                    "Expected Base64InputStream.read(buf, -1, 0) to throw"
                    + " IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                in_.read1(buf, 0, -1)
                self.fail(
                    "Expected Base64InputStream.read(buf, 0, -1) to throw"
                    + " IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                in_.read1(buf, len(buf) + 1, 0)
                self.fail(
                    "Base64InputStream.read(buf, len(buf) + 1, 0) throws"
                    + " IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                in_.read1(buf, len(buf) - 1, 2)
                self.fail(
                    "Base64InputStream.read(buf, len(buf) - 1, 2) throws"
                    + " IndexOutOfBoundsException"
                )
            except IndexError:
                pass

    def testReadNull(self) -> None:

        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        bin = io.BytesIO(bytes(decoded))

        with Base64InputStream.Base64InputStream2(bin, True, 4, [0, 0, 0]) as in_:
            try:
                in_.read1(None, 0, 0)
                self.fail("Base64InputStream.read(None, 0, 0) to throw a RuntimeError")
            except Exception as e:
                pass

    def testRead0(self) -> None:

        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        buf = [0] * 1024
        bytesRead = 0
        bin = io.BytesIO(bytes(decoded))

        with Base64InputStream.Base64InputStream2(bin, True, 4, [0, 0, 0]) as in_:
            bytesRead = in_.read1(buf, 0, 0)
            self.assertEqual(
                bytesRead, 0, "Base64InputStream.read(buf, 0, 0) returns 0"
            )

    def testMarkSupported(self) -> None:

        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        bin = io.BytesIO(bytes(decoded))

        with Base64InputStream.Base64InputStream2(bin, True, 4, [0, 0, 0]) as in_:
            self.assertFalse(
                in_.markSupported(), "Base64InputStream.markSupported() is false"
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
        bais = io.BytesIO(bytes(codec101))
        in_ = Base64InputStream.Base64InputStream0(bais)
        isr = io.TextIOWrapper(io.BufferedReader(in_))
        br = io.BufferedReader(isr)
        line = br.readline()
        self.assertIsNotNone(line, "Codec101:  InputStreamReader works1")

    def testCodec101(self) -> None:

        codec101 = StringUtils.getBytesUtf8(
            Base64TestData.CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3
        )
        bais = io.BytesIO(codec101)
        with Base64InputStream.Base64InputStream0(bais) as in_:
            result = bytearray(8192)
            c = in_.readinto(result)
            self.assertTrue("Codec101: First read successful [c=" + str(c) + "]", c > 0)

            c = in_.readinto(result)
            self.assertTrue(
                "Codec101: Second read should report end-of-stream [c=" + str(c) + "]",
                c < 0,
            )

    def testCodec105(self) -> None:

        with Base64InputStream.Base64InputStream2(
            Codec105ErrorInputStream(), True, 0, None
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

        in_ = Base64InputStream.Base64InputStream2(
            io.BytesIO(bytes(decoded)), True, chunkSize, separator
        )
        output = bytearray(encoded.length)
        for i in range(len(output)):
            output[i] = in_.read(1)[0]

        self.assertEqual("EOF", -1, in_.read(1)[0])
        self.assertEqual("Still EOF", -1, in_.read(1)[0])
        self.assertListEqual("Streaming base64 encode", list(encoded), list(output))

        in_.close()
        in_ = Base64InputStream.Base64InputStream0(io.BytesIO(bytes(encoded)))
        output = bytearray(decoded.length)
        for i in range(len(output)):
            output[i] = in_.read(1)[0]

        self.assertEqual("EOF", -1, in_.read(1)[0])
        self.assertEqual("Still EOF", -1, in_.read(1)[0])
        self.assertListEqual("Streaming base64 decode", list(decoded), list(output))

        in_.close()

        in_ = io.BytesIO(bytes(decoded))
        for i in range(10):
            in_ = Base64InputStream.Base64InputStream2(in_, True, chunkSize, separator)
            in_ = Base64InputStream.Base64InputStream1(in_, False)
        output = bytearray(decoded.length)
        for i in range(len(output)):
            output[i] = in_.read(1)[0]

        self.assertEqual("EOF", -1, in_.read(1)[0])
        self.assertEqual("Still EOF", -1, in_.read(1)[0])
        self.assertListEqual(
            "Streaming base64 wrap-wrap-wrap", list(decoded), list(output)
        )
        in_.close()

    def __testByChunk(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:

        in_ = Base64InputStream.Base64InputStream2(
            io.BytesIO(decoded), True, chunkSize, separator
        )
        output = BaseNTestData.streamToBytes0(in_)

        self.assertEqual("EOF", -1, in_.read())
        self.assertEqual("Still EOF", -1, in_.read())
        self.assertListEqual("Streaming base64 encode", list(encoded), list(output))

        in_.close()

        in_ = Base64InputStream.Base64InputStream0(io.BytesIO(encoded))
        output = BaseNTestData.streamToBytes0(in_)

        self.assertEqual("EOF", -1, in_.read())
        self.assertEqual("Still EOF", -1, in_.read())
        self.assertListEqual("Streaming base64 decode", list(decoded), list(output))

        in_ = io.BytesIO(decoded)
        for i in range(10):
            in_ = Base64InputStream.Base64InputStream2(in_, True, chunkSize, separator)
            in_ = Base64InputStream.Base64InputStream1(in_, False)

        output = BaseNTestData.streamToBytes0(in_)

        self.assertEqual("EOF", -1, in_.read())
        self.assertEqual("Still EOF", -1, in_.read())
        self.assertListEqual(
            "Streaming base64 wrap-wrap-wrap", list(decoded), list(output)
        )
        in_.close()

    def __testBase64EmptyInputStream(self, chuckSize: int) -> None:

        emptyEncoded = []
        emptyDecoded = []
        self.__testByteByByte(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)
        self.__testByChunk(emptyEncoded, emptyDecoded, chuckSize, self.__CRLF)
