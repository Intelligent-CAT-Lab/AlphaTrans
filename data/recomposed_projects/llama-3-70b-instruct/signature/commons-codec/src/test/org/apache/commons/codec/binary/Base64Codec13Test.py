from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.BinaryDecoder import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.Decoder import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.Encoder import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.binary.Base64 import *


class Base64Codec13Test(unittest.TestCase):

    __BYTES: typing.List[typing.List[int]] = [None] * STRINGS.length
    CHUNKED_STRINGS: typing.List[str] = None
    __STRINGS: typing.List[str] = [None] * 181

    @staticmethod
    def run_static_init():
        Base64Codec13Test.__initSTRINGS()
        Base64Codec13Test.__initCHUNKED_STRINGS()
        Base64Codec13Test.__initBYTES()

    def testStaticDecodeChunked(self) -> None:
        for i in range(0, len(STRINGS)):
            if STRINGS[i] is not None:
                base64Chunked = self.__utf8(CHUNKED_STRINGS[i])
                binary = BYTES[i]
                b = Arrays.equals(binary, Base64.decodeBase640(base64Chunked))
                assertTrue("static Base64.decodeBase64Chunked() test-" + i, b)

    def testStaticEncodeChunked(self) -> None:
        for i in range(0, len(STRINGS)):
            if STRINGS[i] != None:
                base64Chunked = self.__utf8(CHUNKED_STRINGS[i])
                binary = BYTES[i]
                b = Arrays.equals(base64Chunked, Base64.encodeBase64Chunked(binary))
                assertTrue("static Base64.encodeBase64Chunked() test-" + i, b)

    def testStaticDecode(self) -> None:
        for i in range(0, len(self.__STRINGS)):
            if self.__STRINGS[i] != None:
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = Arrays.equals(binary, Base64.decodeBase640(base64))
                assertTrue("static Base64.decodeBase64() test-" + i, b)

    def testStaticEncode(self) -> None:
        for i in range(0, len(STRINGS)):
            if STRINGS[i] != None:
                base64 = self.__utf8(STRINGS[i])
                binary = BYTES[i]
                b = Arrays.equals(base64, Base64.encodeBase640(binary))
                assertTrue("static Base64.encodeBase64() test-" + i, b)

    def testBinaryDecoder(self) -> None:
        dec: BinaryDecoder = Base64.Base645()
        for i in range(0, STRINGS.length):
            if STRINGS[i] != None:
                base64: typing.List[int] = self.__utf8(STRINGS[i])
                binary: typing.List[int] = self.__BYTES[i]
                b: bool = Arrays.equals(binary, dec.decode(base64))
                assertTrue("BinaryDecoder test-" + i, b)

    def testBinaryEncoder(self) -> None:
        enc: BinaryEncoder = Base64.Base645()
        for i in range(0, STRINGS.length):
            if STRINGS[i] != None:
                base64: typing.List[int] = self.__utf8(STRINGS[i])
                binary: typing.List[int] = self.__BYTES[i]
                b: bool = Arrays.equals(base64, enc.encode(binary))
                assertTrue("BinaryEncoder test-" + i, b)

    def testDecoder(self) -> None:
        dec: Decoder = Base64.Base645()
        for i in range(0, STRINGS.length):
            if STRINGS[i] != None:
                base64: typing.List[int] = self.__utf8(STRINGS[i])
                binary: typing.List[int] = self.__BYTES[i]
                b: bool = Arrays.equals(binary, dec.decode(base64))
                assertTrue("Decoder test-" + i, b)

    def testEncoder(self) -> None:
        enc: Encoder = Base64.Base645()
        for i in range(0, STRINGS.length):
            if STRINGS[i] != None:
                base64: typing.List[int] = self.__utf8(STRINGS[i])
                binary: typing.List[int] = self.__BYTES[i]
                b: bool = Arrays.equals(base64, enc.encode(binary))
                assertTrue("Encoder test-" + i, b)

    @staticmethod
    def __utf8(s: str) -> typing.List[int]:
        return s.encode("utf-8") if s is not None else None

    @staticmethod
    def __initBYTES() -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __initCHUNKED_STRINGS() -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __initSTRINGS() -> None:

        pass  # LLM could not translate this method


Base64Codec13Test.run_static_init()
