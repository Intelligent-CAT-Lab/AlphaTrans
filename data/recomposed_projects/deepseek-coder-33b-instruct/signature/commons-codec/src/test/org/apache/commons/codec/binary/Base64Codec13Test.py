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

    __STRINGS: List[str] = [""] * 181
    __BYTES: typing.List[typing.List[int]] = [[] for _ in range(len(__STRINGS))]
    __CHUNKED_STRINGS: typing.List[str] = ["" for _ in range(len(__STRINGS))]

    @staticmethod
    def run_static_init():
        Base64Codec13Test.__initSTRINGS()
        Base64Codec13Test.__initCHUNKED_STRINGS()
        Base64Codec13Test.__initBYTES()

    def testStaticDecodeChunked(self) -> None:

        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64Chunked = self.__utf8(self.__CHUNKED_STRINGS[i])
                binary = self.__BYTES[i]
                b = binary == Base64.decodeBase640(base64Chunked)
                self.assertTrue(f"static Base64.decodeBase64Chunked() test-{i}", b)

    def testStaticEncodeChunked(self) -> None:

        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64Chunked = self.__utf8(self.__CHUNKED_STRINGS[i])
                binary = self.__BYTES[i]
                b = base64Chunked == Base64.encodeBase64Chunked(binary)
                self.assertTrue(f"static Base64.encodeBase64Chunked() test-{i}", b)

    def testStaticDecode(self) -> None:

        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] != "":
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = binary == Base64.decodeBase640(base64)
                self.assertTrue(f"static Base64.decodeBase64() test-{i}", b)

    def testStaticEncode(self) -> None:

        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] != "":
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = base64 == Base64.encodeBase640(binary)
                self.assertTrue(f"static Base64.encodeBase64() test-{i}", b)

    def testBinaryDecoder(self) -> None:

        dec = Base64.Base645()
        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] != "":
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = binary == dec.decode(base64)
                self.assertTrue(f"BinaryDecoder test-{i}", b)

    def testBinaryEncoder(self) -> None:

        enc = Base64.Base645()
        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = base64 == enc.encode(binary)
                self.assertTrue(f"BinaryEncoder test-{i}", b)

    def testDecoder(self) -> None:

        dec = Base64.Base645()
        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = binary == dec.decode(base64)
                self.assertTrue(f"Decoder test-{i}", b)

    def testEncoder(self) -> None:

        enc = Base64.Base645()
        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = list(binary) == list(enc.encode(binary))
                self.assertTrue(f"Encoder test-{i}", b)

    @staticmethod
    def __utf8(s: str) -> typing.List[int]:
        return list(s.encode("utf-8")) if s is not None else None

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
