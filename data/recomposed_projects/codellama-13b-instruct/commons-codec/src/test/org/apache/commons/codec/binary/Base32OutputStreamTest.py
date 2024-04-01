# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodecOutputStream import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.Base32TestData import *
from src.main.org.apache.commons.codec.binary.Base32Test import *
from src.main.org.apache.commons.codec.binary.Base32OutputStream import *
from src.main.org.apache.commons.codec.binary.Base32 import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class Base32OutputStreamTest(unittest.TestCase):

    # Class Fields Begin
    __CR_LF: typing.List[int] = ""  # LLM could not translate field
    __LF: typing.List[int] = ""  # LLM could not translate field
    # Class Fields End

    # Class Methods Begin
    def testStrictDecoding(self) -> None:

        for s in Base32Test.BASE32_IMPOSSIBLE_CASES:
            encoded = StringUtils.getBytesUtf8(s)
            bout = io.BytesIO()
            out = Base32OutputStream.Base32OutputStream1(bout, False)
            assert not out.isStrictDecoding()
            out.write(encoded)
            out.close()
            assert bout.getbuffer().nbytes > 0
            bout = io.BytesIO()
            out = Base32OutputStream(bout, False, 0, None, CodecPolicy.STRICT)
            assert out.isStrictDecoding()
            try:
                out.write(encoded)
                out.close()
                self.fail()
            except IllegalArgumentException:
                pass

    def testWriteToNullCoverage(self) -> None:

        bout = io.BytesIO()
        with BaseNCodecOutputStream(bout) as out:
            try:
                out.write0(None, 0, 0)
                self.fail(
                    "Expected Base32OutputStream.write(None) to raise a NullPointerException"
                )
            except NullPointerException:
                pass

    def testWriteOutOfBounds(self) -> None:

        buf = bytearray(1024)
        bout = io.BytesIO()
        with BaseNCodecOutputStream(bout) as out:
            try:
                out.write0(buf, -1, 1)
                self.fail(
                    "Expected Base32OutputStream.write(buf, -1, 1) to throw a"
                    + " IndexOutOfBoundsException"
                )
            except IndexError as e:
                pass
            try:
                out.write0(buf, 1, -1)
                self.fail(
                    "Expected Base32OutputStream.write(buf, 1, -1) to throw a"
                    + " IndexOutOfBoundsException"
                )
            except IndexError as e:
                pass
            try:
                out.write0(buf, len(buf) + 1, 0)
                self.fail(
                    "Expected Base32OutputStream.write(buf, buf.length + 1, 0) to throw a"
                    + " IndexOutOfBoundsException"
                )
            except IndexError as e:
                pass
            try:
                out.write0(buf, len(buf) - 1, 2)
                self.fail(
                    "Expected Base32OutputStream.write(buf, buf.length - 1, 2) to throw a"
                    + " IndexOutOfBoundsException"
                )
            except IndexError as e:
                pass

    def testBase32OutputStreamByteByByte(self) -> None:

        encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE)
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        self.__testByteByByte(encoded, decoded, 76, CR_LF)
        codec = Base32.Base320()
        for i in range(0, 150):
            random_data = BaseNTestData.randomData(codec, i)
            encoded = random_data[1]
            decoded = random_data[0]
            self.__testByteByByte(encoded, decoded, 0, LF)

    def testBase32OutputStreamByChunk(self) -> None:

        encoded = StringUtils.getBytesUtf8(Base32TestData.BASE32_FIXTURE)
        decoded = StringUtils.getBytesUtf8(Base32TestData.STRING_FIXTURE)
        self.__testByChunk(encoded, decoded, BaseNCodec.MIME_CHUNK_SIZE, CR_LF)
        codec = Base32.Base320()
        for i in range(0, 150):
            random_data = BaseNTestData.randomData(codec, i)
            encoded = random_data[1]
            decoded = random_data[0]
            self.__testByChunk(encoded, decoded, 0, LF)

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

        pass  # LLM could not translate method body

    def __testByChunk(
        self,
        encoded: typing.List[int],
        decoded: typing.List[int],
        chunkSize: int,
        separator: typing.List[int],
    ) -> None:

        pass  # LLM could not translate method body

    def __testBase32EmptyOutputStream(self, chunkSize: int) -> None:

        emptyEncoded = b""
        emptyDecoded = b""
        self.__testByteByByte(emptyEncoded, emptyDecoded, chunkSize, self.__CR_LF)
        self.__testByChunk(emptyEncoded, emptyDecoded, chunkSize, self.__CR_LF)

    # Class Methods End
