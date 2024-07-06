from __future__ import annotations
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
from src.main.org.apache.commons.codec.binary.Base32 import *
from src.main.org.apache.commons.codec.binary.Base32OutputStream import *
from src.test.org.apache.commons.codec.binary.Base32Test import *
from src.test.org.apache.commons.codec.binary.Base32TestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.BaseNCodecOutputStream import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base32OutputStreamTest(unittest.TestCase):

    __LF: typing.List[int] = [10]
    __CR_LF: typing.List[int] = [13, 10]

    def testStrictDecoding(self) -> None:
        for s in Base32Test.BASE32_IMPOSSIBLE_CASES:
            encoded = StringUtils.getBytesUtf8(s)
            bout = io.BytesIO()
            out = Base32OutputStream.Base32OutputStream1(bout, False)
            self.assertFalse(out.isStrictDecoding())
            out.write(encoded)
            out.close()
            self.assertTrue(bout.getbuffer().nbytes > 0)

            bout = io.BytesIO()
            out = Base32OutputStream(bout, False, 0, None, CodecPolicy.STRICT)
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
        with Base32OutputStream.Base32OutputStream0(bout) as out:
            try:
                out.write0(buf, -1, 1)
                self.fail(
                    "Expected Base32OutputStream.write(buf, -1, 1) to throw a IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                out.write0(buf, 1, -1)
                self.fail(
                    "Expected Base32OutputStream.write(buf, 1, -1) to throw a IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                out.write0(buf, len(buf) + 1, 0)
                self.fail(
                    "Expected Base32OutputStream.write(buf, buf.length + 1, 0) to throw a IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                out.write0(buf, len(buf) - 1, 2)
                self.fail(
                    "Expected Base32OutputStream.write(buf, buf.length - 1, 2) to throw a IndexOutOfBoundsException"
                )
            except IndexError:
                pass

    def testBase32OutputStreamByteByByte(self) -> None:
        encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE)
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        codec = Base32.Base320()
        for i in range(0, 150 + 1):
            randomData = BaseNTestData.randomData(codec, i)
            encoded = randomData[1]
            decoded = randomData[0]
            self.__testByteByByte(encoded, decoded, 0, self.__LF)

    def testBase32OutputStreamByChunk(self) -> None:
        encoded: typing.List[int] = StringUtils.getBytesUtf8(
            Base32TestData.BASE32_FIXTURE
        )
        decoded: typing.List[int] = StringUtils.getBytesUtf8(
            Base32TestData.STRING_FIXTURE
        )
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        codec: Base32 = Base32.Base320()
        for i in range(0, 150 + 1):
            randomData: typing.List[typing.List[int]] = BaseNTestData.randomData(
                codec, i
            )
            encoded = randomData[1]
            decoded = randomData[0]
            self.__testByChunk(encoded, decoded, 0, self.__LF)

    def testBase32EmptyOutputStreamPemChunkSize(self) -> None:
        self.__testBase32EmptyOutputStream(BaseNCodec.PEM_CHUNK_SIZE)

    def testBase32EmptyOutputStreamMimeChunkSize(self) -> None:
        self.__testBase32EmptyOutputStream(BaseNCodec.MIME_CHUNK_SIZE)

    def __testByteByByte(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:
        byteOut = io.BytesIO()
        out = Base32OutputStream.Base32OutputStream2(
            byteOut, True, chunkSize, separator
        )
        for element in decoded:
            out.write(element)
        out.close()
        output = byteOut.toByteArray()
        assertArrayEquals("Streaming byte-by-byte Base32 encode", encoded, output)

        byteOut = io.BytesIO()
        out = Base32OutputStream.Base32OutputStream1(byteOut, False)
        for element in encoded:
            out.write(element)
        out.close()
        output = byteOut.toByteArray()
        assertArrayEquals("Streaming byte-by-byte Base32 decode", decoded, output)

        byteOut = io.BytesIO()
        out = Base32OutputStream.Base32OutputStream1(byteOut, False)
        for element in encoded:
            out.write(element)
            out.flush()
        out.close()
        output = byteOut.toByteArray()
        assertArrayEquals(
            "Streaming byte-by-byte flush() Base32 decode", decoded, output
        )

        byteOut = io.BytesIO()
        out = byteOut
        for i in range(10):
            out = Base32OutputStream.Base32OutputStream1(out, False)
            out = Base32OutputStream.Base32OutputStream2(
                out, True, chunkSize, separator
            )
        for element in decoded:
            out.write(element)
        out.close()
        output = byteOut.toByteArray()

        assertArrayEquals(
            "Streaming byte-by-byte Base32 wrap-wrap-wrap!", decoded, output
        )

    def __testByChunk(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:
        byteOut = io.BytesIO()
        out = Base32OutputStream.Base32OutputStream2(
            byteOut, True, chunkSize, separator
        )
        out.write(decoded)
        out.close()
        output = byteOut.toByteArray()
        assertArrayEquals("Streaming chunked Base32 encode", encoded, output)

        byteOut = io.BytesIO()
        out = Base32OutputStream.Base32OutputStream1(byteOut, False)
        out.write(encoded)
        out.close()
        output = byteOut.toByteArray()
        assertArrayEquals("Streaming chunked Base32 decode", decoded, output)

        byteOut = io.BytesIO()
        out = byteOut
        for i in range(0, 10):
            out = Base32OutputStream.Base32OutputStream1(out, False)
            out = Base32OutputStream.Base32OutputStream2(
                out, True, chunkSize, separator
            )
        out.write(decoded)
        out.close()
        output = byteOut.toByteArray()

        assertArrayEquals("Streaming chunked Base32 wrap-wrap-wrap!", decoded, output)

    def __testBase32EmptyOutputStream(self, chunkSize: int) -> None:
        emptyEncoded: typing.List[int] = []
        emptyDecoded: typing.List[int] = []
        self.__testByteByByte(emptyEncoded, emptyDecoded, chunkSize, self.__CR_LF)
        self.__testByChunk(emptyEncoded, emptyDecoded, chunkSize, self.__CR_LF)
