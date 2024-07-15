from __future__ import annotations
import copy
import re
import random
import os
from io import BytesIO
import unittest
import pytest
import io
import typing
from typing import *
import unittest
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
    __CR_LF: typing.List[int] = [13, 10]

    def testStrictDecoding(self) -> None:
        for s in Base64Test.BASE64_IMPOSSIBLE_CASES:
            encoded = StringUtils.getBytesUtf8(s)
            bout = io.BytesIO()
            out = Base64OutputStream.Base64OutputStream1(bout, False)
            self.assertFalse(out.isStrictDecoding())
            out.write(encoded)
            out.close()
            self.assertTrue(bout.getbuffer().nbytes > 0)

            bout = io.BytesIO()
            out = Base64OutputStream(bout, False, 0, None, CodecPolicy.STRICT)
            self.assertTrue(out.isStrictDecoding())
            try:
                out.write(encoded)
                out.close()
                self.fail()
            except ValueError:
                pass

    def testWriteToNullCoverage(self) -> None:

        pass  # LLM could not translate this method

    def testWriteOutOfBounds(self) -> None:
        buf = [0] * 1024
        bout = io.BytesIO()
        with Base64OutputStream.Base64OutputStream0(bout) as out:
            try:
                out.write0(buf, -1, 1)
                self.fail(
                    "Expected Base64OutputStream.write(buf, -1, 1) to throw a IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                out.write0(buf, 1, -1)
                self.fail(
                    "Expected Base64OutputStream.write(buf, 1, -1) to throw a IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                out.write0(buf, len(buf) + 1, 0)
                self.fail(
                    "Expected Base64OutputStream.write(buf, buf.length + 1, 0) to throw a IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                out.write0(buf, len(buf) - 1, 2)
                self.fail(
                    "Expected Base64OutputStream.write(buf, buf.length - 1, 2) to throw a IndexOutOfBoundsException"
                )
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

        singleLine = Base64TestData.ENCODED_64_CHARS_PER_LINE.replace("\n", "")
        encoded = StringUtils.getBytesUtf8(singleLine)
        decoded = BaseNTestData.DECODED
        self.__testByteByByte(encoded, decoded, 0, self.__LF)

        codec = Base64.Base641(0, None, False)
        for i in range(0, 151):
            randomData = BaseNTestData.randomData(codec, i)
            encoded = randomData[1]
            decoded = randomData[0]
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
        for i in range(0, 150 + 1):
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
        codec98_1024 = [0] * 1024
        System.arraycopy(codec98, 0, codec98_1024, 0, codec98.length)
        data = io.BytesIO()
        with BaseNCodecOutputStream(
            Base64OutputStream.Base64OutputStream1(data, False)
        ) as stream:
            stream.write0(codec98_1024, 0, 1024)

        decodedBytes = data.toByteArray()
        decoded = StringUtils.newStringUtf8(decodedBytes)
        self.assertEqual(
            "codec-98 NPE Base64OutputStream",
            Base64TestData.CODEC_98_NPE_DECODED,
            decoded,
        )

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
        output = byteOut.toByteArray()
        assertArrayEquals("Streaming byte-by-byte base64 encode", encoded, output)

        byteOut = io.BytesIO()
        out = Base64OutputStream.Base64OutputStream1(byteOut, False)
        for element in encoded:
            out.write(element)
        out.close()
        output = byteOut.toByteArray()
        assertArrayEquals("Streaming byte-by-byte base64 decode", decoded, output)

        byteOut = io.BytesIO()
        out = Base64OutputStream.Base64OutputStream1(byteOut, False)
        for element in encoded:
            out.write(element)
            out.flush()
        out.close()
        output = byteOut.toByteArray()
        assertArrayEquals(
            "Streaming byte-by-byte flush() base64 decode", decoded, output
        )

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
        output = byteOut.toByteArray()

        assertArrayEquals(
            "Streaming byte-by-byte base64 wrap-wrap-wrap!", decoded, output
        )

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
        output = byteOut.toByteArray()
        assertArrayEquals("Streaming chunked base64 encode", encoded, output)

        byteOut = io.BytesIO()
        out = Base64OutputStream.Base64OutputStream1(byteOut, False)
        out.write(encoded)
        out.close()
        output = byteOut.toByteArray()
        assertArrayEquals("Streaming chunked base64 decode", decoded, output)

        byteOut = io.BytesIO()
        out = byteOut
        for i in range(0, 10):
            out = Base64OutputStream.Base64OutputStream1(out, False)
            out = Base64OutputStream.Base64OutputStream2(
                out, True, chunkSize, separator
            )
        out.write(decoded)
        out.close()
        output = byteOut.toByteArray()

        assertArrayEquals("Streaming chunked base64 wrap-wrap-wrap!", decoded, output)

    def __testBase64EmptyOutputStream(self, chunkSize: int) -> None:
        emptyEncoded: typing.List[int] = []
        emptyDecoded: typing.List[int] = []
        self.__testByteByByte(emptyEncoded, emptyDecoded, chunkSize, self.__CR_LF)
        self.__testByChunk(emptyEncoded, emptyDecoded, chunkSize, self.__CR_LF)
