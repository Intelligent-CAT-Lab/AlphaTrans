from __future__ import annotations
import re
import random
import unittest
import pytest
import io
import typing
from typing import *
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

    __CR_LF: typing.List[int] = [0x0D, 0x0A]

    def testStrictDecoding(self) -> None:

        for s in Base32Test.BASE32_IMPOSSIBLE_CASES:
            encoded = StringUtils.getBytesUtf8(s)
            bout = io.BytesIO()
            out = Base32OutputStream.Base32OutputStream1(bout, False)
            assert not out.isStrictDecoding()
            out.write(encoded)
            out.close()
            assert bout.tell() > 0

            bout = io.BytesIO()
            out = Base32OutputStream(bout, False, 0, None, CodecPolicy.STRICT)
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
            out = Base32OutputStream.Base32OutputStream0(bout)
            out.write0(None, 0, 0)
            assert (
                False
            ), "Expcted Base32OutputStream.write(null) to throw a NullPointerException"
        except Exception as e:
            assert isinstance(e, NullPointerException), "Expected NullPointerException"

    def testWriteOutOfBounds(self) -> None:

        buf = bytearray(1024)
        bout = io.BytesIO()
        try:
            out = Base32OutputStream.Base32OutputStream0(bout)

            try:
                out.write0(buf, -1, 1)
                assert (
                    False
                ), "Expected Base32OutputStream.write(buf, -1, 1) to throw a IndexOutOfBoundsException"
            except IndexError:
                pass

            try:
                out.write0(buf, 1, -1)
                assert (
                    False
                ), "Expected Base32OutputStream.write(buf, 1, -1) to throw a IndexOutOfBoundsException"
            except IndexError:
                pass

            try:
                out.write0(buf, len(buf) + 1, 0)
                assert (
                    False
                ), "Expected Base32OutputStream.write(buf, len(buf) + 1, 0) to throw a IndexOutOfBoundsException"
            except IndexError:
                pass

            try:
                out.write0(buf, len(buf) - 1, 2)
                assert (
                    False
                ), "Expected Base32OutputStream.write(buf, len(buf) - 1, 2) to throw a IndexOutOfBoundsException"
            except IndexError:
                pass
        finally:
            out.close()

    def testBase32OutputStreamByteByByte(self) -> None:

        encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE)
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, self.__CR_LF)

        codec = Base32.Base320()
        for i in range(151):
            randomData = BaseNTestData.randomData(codec, i)
            encoded = randomData[1]
            decoded = randomData[0]
            self.__testByteByByte(encoded, decoded, 0, self.__LF)

    def testBase32OutputStreamByChunk(self) -> None:

        encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE)
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, self.__CR_LF)

        codec = Base32.Base320()
        for i in range(151):
            randomData = BaseNTestData.randomData(codec, i)
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
        output = byteOut.getvalue()
        assert output == encoded, "Streaming byte-by-byte Base32 encode"

        byteOut = io.BytesIO()
        out = Base32OutputStream.Base32OutputStream1(byteOut, False)
        for element in encoded:
            out.write(element)
        out.close()
        output = byteOut.getvalue()
        assert output == decoded, "Streaming byte-by-byte Base32 decode"

        byteOut = io.BytesIO()
        out = Base32OutputStream.Base32OutputStream1(byteOut, False)
        for element in encoded:
            out.write(element)
            out.flush()
        out.close()
        output = byteOut.getvalue()
        assert output == decoded, "Streaming byte-by-byte flush() Base32 decode"

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
        output = byteOut.getvalue()

        assert output == decoded, "Streaming byte-by-byte Base32 wrap-wrap-wrap!"

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
        out.write(bytes(decoded))
        out.close()
        output = byteOut.getvalue()
        assert output == bytes(encoded), "Streaming chunked Base32 encode"

        byteOut = io.BytesIO()
        out = Base32OutputStream.Base32OutputStream1(byteOut, False)
        out.write(bytes(encoded))
        out.close()
        output = byteOut.getvalue()
        assert output == bytes(decoded), "Streaming chunked Base32 decode"

        byteOut = io.BytesIO()
        out = byteOut
        for i in range(10):
            out = Base32OutputStream.Base32OutputStream1(out, False)
            out = Base32OutputStream.Base32OutputStream2(
                out, True, chunkSize, separator
            )
        out.write(bytes(decoded))
        out.close()
        output = byteOut.getvalue()

        assert output == bytes(decoded), "Streaming chunked Base32 wrap-wrap-wrap!"

    def __testBase32EmptyOutputStream(self, chunkSize: int) -> None:

        emptyEncoded = b""
        emptyDecoded = b""

        self.__testByteByByte(emptyEncoded, emptyDecoded, chunkSize, self.__CR_LF)
        self.__testByChunk(emptyEncoded, emptyDecoded, chunkSize, self.__CR_LF)
