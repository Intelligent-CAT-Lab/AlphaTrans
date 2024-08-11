from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.net.QuotedPrintableCodec import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CharEncoding import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class QuotedPrintableCodecTest(unittest.TestCase):

    # Class Fields Begin
    SWISS_GERMAN_STUFF_UNICODE: typing.List[int] = None
    RUSSIAN_STUFF_UNICODE: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def testFinalBytes_test1_decomposed(self) -> None:
        pass

    def testFinalBytes_test0_decomposed(self) -> None:
        pass

    def testUltimateSoftBreak_test4_decomposed(self) -> None:
        pass

    def testUltimateSoftBreak_test3_decomposed(self) -> None:
        pass

    def testUltimateSoftBreak_test2_decomposed(self) -> None:
        pass

    def testUltimateSoftBreak_test1_decomposed(self) -> None:
        pass

    def testUltimateSoftBreak_test0_decomposed(self) -> None:
        pass

    def testTrailingSpecial_test2_decomposed(self) -> None:
        pass

    def testTrailingSpecial_test1_decomposed(self) -> None:
        pass

    def testTrailingSpecial_test0_decomposed(self) -> None:
        pass

    def testSkipNotEncodedCRLF_test3_decomposed(self) -> None:
        pass

    def testSkipNotEncodedCRLF_test2_decomposed(self) -> None:
        pass

    def testSkipNotEncodedCRLF_test1_decomposed(self) -> None:
        pass

    def testSkipNotEncodedCRLF_test0_decomposed(self) -> None:
        pass

    def testSoftLineBreakEncode_test3_decomposed(self) -> None:
        pass

    def testSoftLineBreakEncode_test2_decomposed(self) -> None:
        pass

    def testSoftLineBreakEncode_test1_decomposed(self) -> None:
        pass

    def testSoftLineBreakEncode_test0_decomposed(self) -> None:
        pass

    def testSoftLineBreakDecode_test3_decomposed(self) -> None:
        pass

    def testSoftLineBreakDecode_test2_decomposed(self) -> None:
        pass

    def testSoftLineBreakDecode_test1_decomposed(self) -> None:
        pass

    def testSoftLineBreakDecode_test0_decomposed(self) -> None:
        pass

    def testDefaultEncoding_test4_decomposed(self) -> None:
        pass

    def testDefaultEncoding_test3_decomposed(self) -> None:
        pass

    def testDefaultEncoding_test2_decomposed(self) -> None:
        pass

    def testDefaultEncoding_test1_decomposed(self) -> None:
        pass

    def testDefaultEncoding_test0_decomposed(self) -> None:
        pass

    def testDecodeObjects_test6_decomposed(self) -> None:
        pass

    def testDecodeObjects_test5_decomposed(self) -> None:
        pass

    def testDecodeObjects_test4_decomposed(self) -> None:
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

    def testEncodeObjects_test6_decomposed(self) -> None:
        pass

    def testEncodeObjects_test5_decomposed(self) -> None:
        pass

    def testEncodeObjects_test4_decomposed(self) -> None:
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

    def testDecodeWithNullArray_test1_decomposed(self) -> None:
        pass

    def testDecodeWithNullArray_test0_decomposed(self) -> None:
        pass

    def testEncodeUrlWithNullBitSet_test3_decomposed(self) -> None:
        pass

    def testEncodeUrlWithNullBitSet_test2_decomposed(self) -> None:
        pass

    def testEncodeUrlWithNullBitSet_test1_decomposed(self) -> None:
        pass

    def testEncodeUrlWithNullBitSet_test0_decomposed(self) -> None:
        pass

    def testEncodeNull_test2_decomposed(self) -> None:
        pass

    def testEncodeNull_test1_decomposed(self) -> None:
        pass

    def testEncodeNull_test0_decomposed(self) -> None:
        pass

    def testDecodeInvalid_test1_decomposed(self) -> None:
        pass

    def testDecodeInvalid_test0_decomposed(self) -> None:
        pass

    def testEncodeDecodeNull_test2_decomposed(self) -> None:
        pass

    def testEncodeDecodeNull_test1_decomposed(self) -> None:
        pass

    def testEncodeDecodeNull_test0_decomposed(self) -> None:
        pass

    def testUnsafeEncodeDecode_test2_decomposed(self) -> None:
        pass

    def testUnsafeEncodeDecode_test1_decomposed(self) -> None:
        pass

    def testUnsafeEncodeDecode_test0_decomposed(self) -> None:
        pass

    def testSafeCharEncodeDecode_test2_decomposed(self) -> None:
        pass

    def testSafeCharEncodeDecode_test1_decomposed(self) -> None:
        pass

    def testSafeCharEncodeDecode_test0_decomposed(self) -> None:
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

    def __constructString(self, unicodeChars: typing.List[int]) -> str:
        pass

    # Class Methods End
