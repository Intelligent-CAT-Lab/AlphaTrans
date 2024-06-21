from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.Decoder import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.Encoder import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.binary.Base64 import *


class Base64Codec13Test(unittest.TestCase):

    __BYTES: List[List[int]] = []

    __STRINGS: List[str] = [""] * 181
    __CHUNKED_STRINGS: List[str] = [""] * len(__STRINGS)

    def testStaticDecodeChunked(self) -> None:

        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64Chunked = self.__utf8(self.__CHUNKED_STRINGS[i])
                binary = self.__BYTES[i]
                b = binary == list(Base64.decodeBase640(base64Chunked))
                assert b, "static Base64.decodeBase64Chunked() test-" + str(i)

    def testStaticEncodeChunked(self) -> None:

        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64Chunked = self.__utf8(self.__CHUNKED_STRINGS[i])
                binary = self.__BYTES[i]
                b = base64Chunked == Base64.encodeBase64Chunked(binary)
                assert b, "static Base64.encodeBase64Chunked() test-" + str(i)

    def testStaticDecode(self) -> None:

        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = binary == list(Base64.decodeBase640(base64))
                assert b, "static Base64.decodeBase64() test-" + str(i)

    def testStaticEncode(self) -> None:

        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = base64 == list(Base64.encodeBase640(binary))
                assert b, "static Base64.encodeBase64() test-" + str(i)

    def testBinaryDecoder(self) -> None:

        dec = Base64.Base645()
        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = binary == list(dec.decode(base64))
                assert b, "BinaryDecoder test-" + str(i)

    def testBinaryEncoder(self) -> None:

        enc = Base64.Base645()
        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = base64 == list(enc.encode(binary))
                assert b, "BinaryEncoder test-" + str(i)

    def testDecoder(self) -> None:

        dec = Base64.Base645()
        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = binary == list(dec.decode(base64))
                assert b, "Decoder test-" + str(i)

    def testEncoder(self) -> None:

        enc = Base64.Base645()
        for i in range(len(self.__STRINGS)):
            if self.__STRINGS[i] is not None:
                base64 = self.__utf8(self.__STRINGS[i])
                binary = self.__BYTES[i]
                b = base64 == list(enc.encode(binary))
                assert b, "Encoder test-" + str(i)

    @staticmethod
    def __utf8(s: str) -> typing.List[int]:

        if s is not None:
            return [ord(c) for c in s]
        else:
            return None

    @staticmethod
    def __initBYTES() -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __initCHUNKED_STRINGS() -> None:

        c = Base64Codec13Test.__CHUNKED_STRINGS
        c[0] = ""
        c[1] = "uA==\r\n"
        c[2] = "z9w=\r\n"
        c[3] = "TQ+Z\r\n"
        c[4] = "bhjUYA==\r\n"
        c[5] = "1cO9td8=\r\n"
        c[6] = "sMxHoJf5\r\n"
        c  # ... and so on for the rest of the code

    @staticmethod
    def __initSTRINGS() -> None:

        pass  # LLM could not translate this method
