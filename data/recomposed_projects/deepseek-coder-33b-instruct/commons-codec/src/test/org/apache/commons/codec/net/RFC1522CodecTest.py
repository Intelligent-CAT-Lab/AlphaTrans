from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
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

        def assertExpectedDecoderException(s: str) -> None:
            try:
                RFC1522Codec.decode(s)
                assert False, "Expected DecoderException"
            except DecoderException:
                pass

        assertExpectedDecoderException("whatever")
        assertExpectedDecoderException("=?")
        assertExpectedDecoderException("?=")
        assertExpectedDecoderException("==")
        assertExpectedDecoderException("=??=")
        assertExpectedDecoderException("=?stuff?=")
        assertExpectedDecoderException("=?UTF-8??=")
        assertExpectedDecoderException("=?UTF-8?stuff?=")
        assertExpectedDecoderException("=?UTF-8?T?stuff")
        assertExpectedDecoderException("=??T?stuff?=")
        assertExpectedDecoderException("=?UTF-8??stuff?=")
        assertExpectedDecoderException("=?UTF-8?W?stuff?=")

    def testNullInput(self) -> None:

        testcodec = RFC1522Codec()
        assert testcodec.decodeText(None) is None
        assert testcodec.encodeText1(None, CharEncoding.UTF_8) is None

    def __assertExpectedDecoderException(self, s: str) -> None:

        testcodec = RFC1522TestCodec()
        try:
            testcodec.decodeText(s)
            self.fail("DecoderException should have been thrown")
        except DecoderException:
            pass
