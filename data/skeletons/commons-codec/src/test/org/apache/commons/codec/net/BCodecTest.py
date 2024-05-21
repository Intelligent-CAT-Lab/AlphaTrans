from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.net.BCodec import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.CharEncoding import *
import os
import typing
from typing import *
import io

# Imports End


class BCodecTest:

    # Class Fields Begin
    __BASE64_IMPOSSIBLE_CASES: typing.List[str] = None
    SWISS_GERMAN_STUFF_UNICODE: typing.List[int] = None
    RUSSIAN_STUFF_UNICODE: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def testBase64ImpossibleSamplesStrict(self) -> None:
        pass

    def testBase64ImpossibleSamplesLenient(self) -> None:
        pass

    def testBase64ImpossibleSamplesDefault(self) -> None:
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

    def testEncodeDecodeNull(self) -> None:
        pass

    def testBasicEncodeDecode(self) -> None:
        pass

    def testUTF8RoundTrip(self) -> None:
        pass

    def testNullInput(self) -> None:
        pass

    def __constructString(self, unicodeChars: typing.List[int]) -> str:
        pass

    # Class Methods End
