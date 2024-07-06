from __future__ import annotations
import re
import random
from io import BytesIO
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.binary.Base16 import *
from src.main.org.apache.commons.codec.binary.Base16OutputStream import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base16OutputStreamTest(unittest.TestCase):

    __STRING_FIXTURE: str = "Hello World"

    def testWriteToNullCoverage(self) -> None:
        with self.assertRaises(NullPointerException):
            bout = io.BytesIO()
            with Base16OutputStream.Base16OutputStream3(bout) as out:
                out.write0(None, 0, 0)

    def testWriteOutOfBounds(self) -> None:
        buf = [0] * 1024
        bout = io.BytesIO()
        with Base16OutputStream.Base16OutputStream3(bout) as out:
            try:
                out.write0(buf, -1, 1)
                self.fail(
                    "Expected Base16OutputStream.write(buf, -1, 1) to throw a IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                out.write0(buf, 1, -1)
                self.fail(
                    "Expected Base16OutputStream.write(buf, 1, -1) to throw a IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                out.write0(buf, len(buf) + 1, 0)
                self.fail(
                    "Expected Base16OutputStream.write(buf, buf.length + 1, 0) to throw a IndexOutOfBoundsException"
                )
            except IndexError:
                pass

            try:
                out.write0(buf, len(buf) - 1, 2)
                self.fail(
                    "Expected Base16OutputStream.write(buf, buf.length - 1, 2) to throw a IndexOutOfBoundsException"
                )
            except IndexError:
                pass

    def testBase16OutputStreamByteByByte(self) -> None:
        encoded = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.__testByteByByte0(encoded, decoded)

        encoded = StringUtils.getBytesUtf8("41")
        decoded = [0x41]
        self.__testByteByByte0(encoded, decoded)

        codec = Base16.Base161(True)
        for i in range(0, 151):
            randomData = BaseNTestData.randomData(codec, i)
            encoded = randomData[1]
            decoded = randomData[0]
            self.__testByteByByte1(encoded, decoded, True)

    def testBase16OutputStreamByChunk(self) -> None:
        encoded = StringUtils.getBytesUtf8("48656C6C6F20576F726C64")
        decoded = StringUtils.getBytesUtf8(STRING_FIXTURE)
        self.__testByChunk0(encoded, decoded)

        encoded = StringUtils.getBytesUtf8("41")
        decoded = [0x41]
        self.__testByChunk0(encoded, decoded)

        codec = Base16.Base161(True)
        for i in range(0, 150):
            randomData = BaseNTestData.randomData(codec, i)
            encoded = randomData[1]
            decoded = randomData[0]
            self.__testByChunk1(encoded, decoded, True)

    def testBase16EmptyOutputStream(self) -> None:
        emptyEncoded: typing.List[int] = []
        emptyDecoded: typing.List[int] = []
        self.__testByteByByte0(emptyEncoded, emptyDecoded)
        self.__testByChunk0(emptyEncoded, emptyDecoded)

    def __testByteByByte1(
        self, encoded: typing.List[int], decoded: typing.List[int], lowerCase: bool
    ) -> None:
        with io.BytesIO() as byteOut:
            with Base16OutputStream.Base16OutputStream1(
                byteOut, True, lowerCase
            ) as out:
                for element in decoded:
                    out.write(element)
                output = byteOut.getvalue()
                self.assertListEqual(
                    "Streaming byte-by-byte base16 encode", encoded, output
                )

            with Base16OutputStream.Base16OutputStream1(
                byteOut, False, lowerCase
            ) as out:
                for element in encoded:
                    out.write(element)
                output = byteOut.getvalue()
                self.assertListEqual(
                    "Streaming byte-by-byte base16 decode", decoded, output
                )

            with Base16OutputStream.Base16OutputStream1(
                byteOut, False, lowerCase
            ) as out:
                for element in encoded:
                    out.write(element)
                    out.flush()
                output = byteOut.getvalue()
                self.assertListEqual(
                    "Streaming byte-by-byte flush() base16 decode", decoded, output
                )

            with Base16OutputStream.Base16OutputStream1(
                byteOut, False, lowerCase
            ) as decoderOut:
                with Base16OutputStream.Base16OutputStream1(
                    decoderOut, True, lowerCase
                ) as encoderOut:
                    for element in decoded:
                        encoderOut.write(element)
                    output = byteOut.getvalue()
                    self.assertListEqual(
                        "Streaming byte-by-byte base16 wrap-wrap!", decoded, output
                    )

    def __testByteByByte0(
        self, encoded: typing.List[int], decoded: typing.List[int]
    ) -> None:
        self.__testByteByByte1(encoded, decoded, False)

    def __testByChunk1(
        self, encoded: typing.List[int], decoded: typing.List[int], lowerCase: bool
    ) -> None:
        with io.BytesIO() as byteOut:
            with Base16OutputStream.Base16OutputStream1(
                byteOut, True, lowerCase
            ) as out:
                out.write(decoded)
                output = byteOut.toByteArray()
                self.assertArrayEquals(
                    "Streaming chunked base16 encode", encoded, output
                )

            with Base16OutputStream.Base16OutputStream1(
                byteOut, False, lowerCase
            ) as out:
                out.write(encoded)
                output = byteOut.toByteArray()
                self.assertArrayEquals(
                    "Streaming chunked base16 decode", decoded, output
                )

            with io.BytesIO() as byteOut:
                decoderOut = Base16OutputStream.Base16OutputStream1(
                    byteOut, False, lowerCase
                )
                encoderOut = Base16OutputStream.Base16OutputStream1(
                    decoderOut, True, lowerCase
                )

                encoderOut.write(decoded)
                output = byteOut.toByteArray()

                self.assertArrayEquals(
                    "Streaming chunked base16 wrap-wrap!", decoded, output
                )

    def __testByChunk0(
        self, encoded: typing.List[int], decoded: typing.List[int]
    ) -> None:
        self.__testByChunk1(encoded, decoded, False)
