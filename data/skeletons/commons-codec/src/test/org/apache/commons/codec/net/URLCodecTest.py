from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.net.URLCodec import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CharEncoding import *
import unittest
import typing
from typing import *
import io

# Imports End


class URLCodecTest(unittest.TestCase):

    # Class Fields Begin
    SWISS_GERMAN_STUFF_UNICODE: typing.List[int] = None
    RUSSIAN_STUFF_UNICODE: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def testDefaultEncoding(self) -> None:
        pass

    def testDecodeObjects(self) -> None:
        pass

    def testInvalidEncoding(self) -> None:
        pass

    def testEncodeObjects(self) -> None:
        pass

    def testDecodeStringWithNull(self) -> None:
        pass

    def testEncodeStringWithNull(self) -> None:
        pass

    def testDecodeWithNullArray(self) -> None:
        pass

    def testEncodeUrlWithNullBitSet(self) -> None:
        pass

    def testEncodeNull(self) -> None:
        pass

    def testDecodeInvalidContent(self) -> None:
        pass

    def testDecodeInvalid(self) -> None:
        pass

    def testEncodeDecodeNull(self) -> None:
        pass

    def testUnsafeEncodeDecode(self) -> None:
        pass

    def testSafeCharEncodeDecode(self) -> None:
        pass

    def testBasicEncodeDecode(self) -> None:
        pass

    def testUTF8RoundTrip(self) -> None:
        pass

    def __constructString(self, unicodeChars: typing.List[int]) -> str:
        pass

    def __validateState(self, urlCodec: URLCodec) -> None:
        pass

    # Class Methods End
