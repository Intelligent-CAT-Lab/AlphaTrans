from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.net.RFC1522Codec import *


class RFC1522TestCodec(RFC1522Codec):

    def _getEncoding(self) -> str:
        return "T"

    def _doEncoding(self, bytes: typing.List[int]) -> typing.List[int]:
        return bytes

    def _doDecoding(self, bytes: typing.List[int]) -> typing.List[int]:
        return bytes


class RFC1522CodecTest(unittest.TestCase):

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
        self.assertIsNone(testcodec.decodeText(None))
        self.assertIsNone(testcodec.encodeText1(None, CharEncoding.UTF_8))

    def __assertExpectedDecoderException(self, s: str) -> None:

        testcodec = RFC1522TestCodec()
        try:
            testcodec.decodeText(s)
            self.fail("DecoderException should have been thrown")
        except DecoderException:
            pass
