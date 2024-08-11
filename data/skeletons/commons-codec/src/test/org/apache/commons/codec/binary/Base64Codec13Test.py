from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.Base64 import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.Encoder import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.Decoder import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class Base64Codec13Test(unittest.TestCase):

    # Class Fields Begin
    __STRINGS: typing.List[typing.List[str]] = None
    __CHUNKED_STRINGS: typing.List[typing.List[str]] = None
    __BYTES: typing.List[typing.List[int]] = None
    # Class Fields End

    # Class Methods Begin
    def testStaticDecodeChunked_test0_decomposed(self) -> None:
        pass

    def testStaticEncodeChunked_test0_decomposed(self) -> None:
        pass

    def testStaticDecode_test0_decomposed(self) -> None:
        pass

    def testStaticEncode_test0_decomposed(self) -> None:
        pass

    def testBinaryDecoder_test1_decomposed(self) -> None:
        pass

    def testBinaryDecoder_test0_decomposed(self) -> None:
        pass

    def testBinaryEncoder_test1_decomposed(self) -> None:
        pass

    def testBinaryEncoder_test0_decomposed(self) -> None:
        pass

    def testDecoder_test1_decomposed(self) -> None:
        pass

    def testDecoder_test0_decomposed(self) -> None:
        pass

    def testEncoder_test1_decomposed(self) -> None:
        pass

    def testEncoder_test0_decomposed(self) -> None:
        pass

    @staticmethod
    def __utf8(s: str) -> typing.List[int]:
        pass

    @staticmethod
    def __initBYTES() -> None:
        pass

    @staticmethod
    def __initCHUNKED_STRINGS() -> None:
        pass

    @staticmethod
    def __initSTRINGS() -> None:
        pass

    # Class Methods End
