from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.net.BCodec import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.CharEncoding import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class BCodecTest(unittest.TestCase):

    # Class Fields Begin
    __BASE64_IMPOSSIBLE_CASES: typing.List[typing.List[str]] = None
    SWISS_GERMAN_STUFF_UNICODE: typing.List[int] = None
    RUSSIAN_STUFF_UNICODE: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def testBase64ImpossibleSamplesStrict_test2_decomposed(self) -> None:
        pass

    def testBase64ImpossibleSamplesStrict_test1_decomposed(self) -> None:
        pass

    def testBase64ImpossibleSamplesStrict_test0_decomposed(self) -> None:
        pass

    def testBase64ImpossibleSamplesLenient_test2_decomposed(self) -> None:
        pass

    def testBase64ImpossibleSamplesLenient_test1_decomposed(self) -> None:
        pass

    def testBase64ImpossibleSamplesLenient_test0_decomposed(self) -> None:
        pass

    def testBase64ImpossibleSamplesDefault_test2_decomposed(self) -> None:
        pass

    def testBase64ImpossibleSamplesDefault_test1_decomposed(self) -> None:
        pass

    def testBase64ImpossibleSamplesDefault_test0_decomposed(self) -> None:
        pass

    def testDecodeObjects_test3_decomposed(self) -> None:
        pass

    def testDecodeObjects_test2_decomposed(self) -> None:
        pass

    def testDecodeObjects_test1_decomposed(self) -> None:
        pass

    def testDecodeObjects_test0_decomposed(self) -> None:
        pass

    def testInvalidEncoding_test0_decomposed(self) -> None:
        pass

    def testEncodeObjects_test3_decomposed(self) -> None:
        pass

    def testEncodeObjects_test2_decomposed(self) -> None:
        pass

    def testEncodeObjects_test1_decomposed(self) -> None:
        pass

    def testEncodeObjects_test0_decomposed(self) -> None:
        pass

    def testDecodeStringWithNull_test2_decomposed(self) -> None:
        pass

    def testDecodeStringWithNull_test1_decomposed(self) -> None:
        pass

    def testDecodeStringWithNull_test0_decomposed(self) -> None:
        pass

    def testEncodeStringWithNull_test2_decomposed(self) -> None:
        pass

    def testEncodeStringWithNull_test1_decomposed(self) -> None:
        pass

    def testEncodeStringWithNull_test0_decomposed(self) -> None:
        pass

    def testEncodeDecodeNull_test2_decomposed(self) -> None:
        pass

    def testEncodeDecodeNull_test1_decomposed(self) -> None:
        pass

    def testEncodeDecodeNull_test0_decomposed(self) -> None:
        pass

    def testBasicEncodeDecode_test2_decomposed(self) -> None:
        pass

    def testBasicEncodeDecode_test1_decomposed(self) -> None:
        pass

    def testBasicEncodeDecode_test0_decomposed(self) -> None:
        pass

    def testUTF8RoundTrip_test5_decomposed(self) -> None:
        pass

    def testUTF8RoundTrip_test4_decomposed(self) -> None:
        pass

    def testUTF8RoundTrip_test3_decomposed(self) -> None:
        pass

    def testUTF8RoundTrip_test2_decomposed(self) -> None:
        pass

    def testUTF8RoundTrip_test1_decomposed(self) -> None:
        pass

    def testUTF8RoundTrip_test0_decomposed(self) -> None:
        pass

    def testNullInput_test2_decomposed(self) -> None:
        pass

    def testNullInput_test1_decomposed(self) -> None:
        pass

    def testNullInput_test0_decomposed(self) -> None:
        pass

    def __constructString(self, unicodeChars: typing.List[int]) -> str:
        pass

    # Class Methods End
