# Imports Begin
from src.main.org.apache.commons.codec.net.RFC1522Codec import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CharEncoding import *
import unittest
import typing
from typing import *

# Imports End


class RFC1522TestCodec(unittest.TestCase, RFC1522Codec):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _getEncoding(self) -> str:

        return "T"

    def _doEncoding(self, bytes: typing.List[int]) -> typing.List[int]:

        return bytes

    def _doDecoding(self, bytes: typing.List[int]) -> typing.List[int]:

        return bytes

    # Class Methods End


class RFC1522CodecTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testDecodeInvalid(self) -> None:

        self.__assertExpectedDecoderException("whatever")
        self.__assertExpectedDecoderException("=?")
        self.__assertExpectedDecoderException("?=")
        self.__assertExpectedDecoderException("==")
        self.__assertExpectedDecoderException("=??=")
        self.__assertExpectedDecoderException("=?stuff?=")
        self.__assertExpectedDecoderException("=?UTF-8??=")
        self.__assertExpectedDecoderException("=?UTF-8?stuff?=")
        self.__assertExpectedDecoderException("=?UTF-8?T?stuff")
        self.__assertExpectedDecoderException("=??T?stuff?=")
        self.__assertExpectedDecoderException("=?UTF-8??stuff?=")
        self.__assertExpectedDecoderException("=?UTF-8?W?stuff?=")

    def testNullInput(self) -> None:

        testcodec = RFC1522TestCodec()
        assertNull(testcodec.decodeText(None))
        assertNull(testcodec.encodeText1(None, "UTF-8"))

    def __assertExpectedDecoderException(self, s: str) -> None:

        testcodec = RFC1522TestCodec()
        try:
            testcodec.decodeText(s)
            fail("DecoderException should have been thrown")
        except DecoderException:
            pass

    # Class Methods End
