from __future__ import annotations
import re
import random
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.Base64 import *
from src.main.org.apache.commons.codec.binary.Base64OutputStream import *
from src.test.org.apache.commons.codec.binary.Base64Test import *
from src.test.org.apache.commons.codec.binary.Base64TestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.BaseNCodecOutputStream import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base64OutputStreamTest(unittest.TestCase):

    __STRING_FIXTURE: str = "Hello World"

    __LF: typing.List[int] = [10]

    __CR_LF: typing.List[int] = [ord("\r"), ord("\n")]

    def testStrictDecoding(self) -> None:

        for s in Base64Test.BASE64_IMPOSSIBLE_CASES:
            encoded = StringUtils.getBytesUtf8(s)
            bout = io.BytesIO()
            out = Base64OutputStream.Base64OutputStream1(bout, False)
            assert not out.isStrictDecoding()
            out.write(encoded)
            out.close()
            assert bout.tell() > 0

            bout = io.BytesIO()
            out = Base64OutputStream(bout, False, 0, None, CodecPolicy.STRICT)
            assert out.isStrictDecoding()
            try:
                out.write(encoded)
                out.close()
                assert False
            except ValueError:
                pass

    def testWriteToNullCoverage(self) -> None:

        bout = io.BytesIO()
        try:
            out = Base64OutputStream.Base64OutputStream0(bout)
            out.write0(None, 0, 0)
            assert (
                False
            ), "Expcted Base64OutputStream.write(null) to throw a NullPointerException"
        except Exception as e:
            assert isinstance(
                e, NullPointerException
            ), "Expected NullPointerException, but got {}".format(type(e))

    def testWriteOutOfBounds(self) -> None:

        buf = bytearray(1024)
        bout = io.BytesIO()
        with Base64OutputStream.Base64OutputStream0(bout) as out:

            try:
                out.write0(buf, -1, 1)
                assert (
                    False
                ), "Expected Base64OutputStream.write(buf, -1, 1) to throw a IndexOutOfBoundsException"
            except IndexError:
                pass

            try:
                out.write0(buf, 1, -1)
                assert (
                    False
                ), "Expected Base64OutputStream.write(buf, 1, -1) to throw a IndexOutOfBoundsException"
            except IndexError:
                pass

            try:
                out.write0(buf, len(buf) + 1, 0)
                assert (
                    False
                ), "Expected Base64OutputStream.write(buf, len(buf) + 1, 0) to throw a IndexOutOfBoundsException"
            except IndexError:
                pass

            try:
                out.write0(buf, len(buf) - 1, 2)
                assert (
                    False
                ), "Expected Base64OutputStream.write(buf, len(buf) - 1, 2) to throw a IndexOutOfBoundsException"
            except IndexError:
                pass

    def testBase64OutputStreamByteByByte(self) -> None:

        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE)
        decoded = BaseNTestData.DECODED
        self.__testByteByByte(encoded, decoded, 64, self.__LF)

        single_line = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "")
        encoded = StringUtils.getBytesUtf8(single_line)
        decoded = BaseNTestData.DECODED
        self.__testByteByByte(encoded, decoded, 0, self.__LF)

        codec = Base64.Base641(0, None, False)
        for i in range(151):
            random_data = BaseNTestData.randomData(codec, i)
            encoded = random_data[1]
            decoded = random_data[0]
            self.__testByteByByte(encoded, decoded, 0, self.__LF)

    def testBase64OutputStreamByChunk(self) -> None:

        encoded = StringUtils.getBytesUtf8("SGVsbG8gV29ybGQ=\r\n")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8("AA==\r\n")
        decoded = [0]
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        encoded = StringUtils.getBytesUtf8(Base64TestData.ENCODED_64_CHARS_PER_LINE)
        decoded = BaseNTestData.DECODED
        self.__testByChunk(encoded, decoded, BaseNCodec.PEM_CHUNK_SIZE, self.__LF)

        singleLine = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "")
        encoded = StringUtils.getBytesUtf8(singleLine)
        decoded = BaseNTestData.DECODED
        self.__testByChunk(encoded, decoded, 0, self.__LF)

        codec = Base64.Base641(0, None, False)
        for i in range(151):
            randomData = BaseNTestData.randomData(codec, i)
            encoded = randomData[1]
            decoded = randomData[0]
            self.__testByChunk(encoded, decoded, 0, self.__LF)

    def testBase64EmptyOutputStreamPemChunkSize(self) -> None:

        self.__testBase64EmptyOutputStream(BaseNCodec.PEM_CHUNK_SIZE)

    def testBase64EmptyOutputStreamMimeChunkSize(self) -> None:

        self.__testBase64EmptyOutputStream(BaseNCodec.MIME_CHUNK_SIZE)

    def testCodec98NPE(self) -> None:

        codec98 = StringUtils.getBytesUtf8(Base64TestData.CODEC_98_NPE)
        codec98_1024 = bytearray(1024)
        codec98_1024[: len(codec98)] = codec98
        data = io.BytesIO()
        try:
            stream = Base64OutputStream.Base64OutputStream1(data, False)
            stream.write0(codec98_1024, 0, 1024)
        finally:
            stream.close()

        decodedBytes = data.getvalue()
        decoded = StringUtils.newStringUtf8(decodedBytes)
        assert (
            decoded == Base64TestData.CODEC_98_NPE_DECODED
        ), "codec-98 NPE Base64OutputStream"

    def __testByteByByte(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:

        byteOut = io.BytesIO()
        out = Base64OutputStream.Base64OutputStream2(
            byteOut, True, chunkSize, separator
        )
        for element in decoded:
            out.write(element)
        out.close()
        output = byteOut.getvalue()
        assert output == encoded, "Streaming byte-by-byte base64 encode"

        byteOut = io.BytesIO()
        out = Base64OutputStream.Base64OutputStream1(byteOut, False)
        for element in encoded:
            out.write(element)
        out.close()
        output = byteOut.getvalue()
        assert output == decoded, "Streaming byte-by-byte base64 decode"

        byteOut = io.BytesIO()
        out = Base64OutputStream.Base64OutputStream1(byteOut, False)
        for element in encoded:
            out.write(element)
            out.flush()
        out.close()
        output = byteOut.getvalue()
        assert output == decoded, "Streaming byte-by-byte flush() base64 decode"

        byteOut = io.BytesIO()
        out = byteOut
        for i in range(10):
            out = Base64OutputStream.Base64OutputStream1(out, False)
            out = Base64OutputStream.Base64OutputStream2(
                out, True, chunkSize, separator
            )
        for element in decoded:
            out.write(element)
        out.close()
        output = byteOut.getvalue()

        assert output == decoded, "Streaming byte-by-byte base64 wrap-wrap-wrap!"

    def __testByChunk(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:

        byteOut = io.BytesIO()
        out = Base64OutputStream.Base64OutputStream2(
            byteOut, True, chunkSize, separator
        )
        out.write(decoded)
        out.close()
        output = byteOut.getvalue()
        assert output == encoded, "Streaming chunked base64 encode"

        byteOut = io.BytesIO()
        out = Base64OutputStream.Base64OutputStream1(byteOut, False)
        out.write(encoded)
        out.close()
        output = byteOut.getvalue()
        assert output == decoded, "Streaming chunked base64 decode"

        byteOut = io.BytesIO()
        out = byteOut
        for i in range(10):
            out = Base64OutputStream.Base64OutputStream1(out, False)
            out = Base64OutputStream.Base64OutputStream2(
                out, True, chunkSize, separator
            )
        out.write(decoded)
        out.close()
        output = byteOut.getvalue()

        assert output == decoded, "Streaming chunked base64 wrap-wrap-wrap!"

    def __testBase64EmptyOutputStream(self, chunkSize: int) -> None:

        emptyEncoded = b""
        emptyDecoded = b""
        self.__testByteByByte(emptyEncoded, emptyDecoded, chunkSize, self.__CR_LF)
        self.__testByChunk(emptyEncoded, emptyDecoded, chunkSize, self.__CR_LF)
