from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.binary.Hex import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.test.org.apache.commons.codec.binary.BaseNCodecTest import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.test.org.apache.commons.codec.binary.Base64TestData import *
from src.main.org.apache.commons.codec.binary.Base64 import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class Base64Test(unittest.TestCase):

    # Class Fields Begin
    __CHARSET_UTF8: str = None
    BASE64_IMPOSSIBLE_CASES: typing.List[typing.List[str]] = None
    __STANDARD_ENCODE_TABLE: typing.List[int] = None
    __random: random.Random = None
    # Class Fields End

    # Class Methods Begin
    def testCodec265_test2_decomposed(self) -> None:
        pass

    def testCodec265_test1_decomposed(self) -> None:
        pass

    def testCodec265_test0_decomposed(self) -> None:
        pass

    def testBase64DecodingOfTrailing18Bits_test0_decomposed(self) -> None:
        pass

    def testBase64DecodingOfTrailing12Bits_test0_decomposed(self) -> None:
        pass

    def testBase64DecodingOfTrailing6Bits_test0_decomposed(self) -> None:
        pass

    def testBase64ImpossibleSamples_test1_decomposed(self) -> None:
        pass

    def testBase64ImpossibleSamples_test0_decomposed(self) -> None:
        pass

    def testHugeLineSeparator_test4_decomposed(self) -> None:
        pass

    def testHugeLineSeparator_test3_decomposed(self) -> None:
        pass

    def testHugeLineSeparator_test2_decomposed(self) -> None:
        pass

    def testHugeLineSeparator_test1_decomposed(self) -> None:
        pass

    def testHugeLineSeparator_test0_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test17_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test16_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test15_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test14_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test13_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test12_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test11_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test10_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test9_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test8_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test7_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test6_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test5_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test4_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test3_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test2_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test1_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test0_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test11_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test10_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test9_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test8_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test7_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test6_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test5_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test4_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test3_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test2_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test1_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test0_decomposed(self) -> None:
        pass

    def testUUID_test10_decomposed(self) -> None:
        pass

    def testUUID_test9_decomposed(self) -> None:
        pass

    def testUUID_test8_decomposed(self) -> None:
        pass

    def testUUID_test7_decomposed(self) -> None:
        pass

    def testUUID_test6_decomposed(self) -> None:
        pass

    def testUUID_test5_decomposed(self) -> None:
        pass

    def testUUID_test4_decomposed(self) -> None:
        pass

    def testUUID_test3_decomposed(self) -> None:
        pass

    def testUUID_test2_decomposed(self) -> None:
        pass

    def testUUID_test1_decomposed(self) -> None:
        pass

    def testUUID_test0_decomposed(self) -> None:
        pass

    def testUrlSafe_test1_decomposed(self) -> None:
        pass

    def testUrlSafe_test0_decomposed(self) -> None:
        pass

    def testTripletsChunked_test0_decomposed(self) -> None:
        pass

    def testTriplets_test0_decomposed(self) -> None:
        pass

    def testSingletonsChunked_test0_decomposed(self) -> None:
        pass

    def testSingletons_test1_decomposed(self) -> None:
        pass

    def testSingletons_test0_decomposed(self) -> None:
        pass

    def testRfc4648Section10EncodeDecode_test0_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeEncode_test0_decomposed(self) -> None:
        pass

    def testRfc4648Section10Encode_test13_decomposed(self) -> None:
        pass

    def testRfc4648Section10Encode_test12_decomposed(self) -> None:
        pass

    def testRfc4648Section10Encode_test11_decomposed(self) -> None:
        pass

    def testRfc4648Section10Encode_test10_decomposed(self) -> None:
        pass

    def testRfc4648Section10Encode_test9_decomposed(self) -> None:
        pass

    def testRfc4648Section10Encode_test8_decomposed(self) -> None:
        pass

    def testRfc4648Section10Encode_test7_decomposed(self) -> None:
        pass

    def testRfc4648Section10Encode_test6_decomposed(self) -> None:
        pass

    def testRfc4648Section10Encode_test5_decomposed(self) -> None:
        pass

    def testRfc4648Section10Encode_test4_decomposed(self) -> None:
        pass

    def testRfc4648Section10Encode_test3_decomposed(self) -> None:
        pass

    def testRfc4648Section10Encode_test2_decomposed(self) -> None:
        pass

    def testRfc4648Section10Encode_test1_decomposed(self) -> None:
        pass

    def testRfc4648Section10Encode_test0_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf_test14_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf_test13_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf_test12_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf_test11_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf_test10_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf_test9_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf_test8_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf_test7_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf_test6_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf_test5_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf_test4_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf_test3_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf_test2_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf_test1_decomposed(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf_test0_decomposed(self) -> None:
        pass

    def testRfc4648Section10Decode_test13_decomposed(self) -> None:
        pass

    def testRfc4648Section10Decode_test12_decomposed(self) -> None:
        pass

    def testRfc4648Section10Decode_test11_decomposed(self) -> None:
        pass

    def testRfc4648Section10Decode_test10_decomposed(self) -> None:
        pass

    def testRfc4648Section10Decode_test9_decomposed(self) -> None:
        pass

    def testRfc4648Section10Decode_test8_decomposed(self) -> None:
        pass

    def testRfc4648Section10Decode_test7_decomposed(self) -> None:
        pass

    def testRfc4648Section10Decode_test6_decomposed(self) -> None:
        pass

    def testRfc4648Section10Decode_test5_decomposed(self) -> None:
        pass

    def testRfc4648Section10Decode_test4_decomposed(self) -> None:
        pass

    def testRfc4648Section10Decode_test3_decomposed(self) -> None:
        pass

    def testRfc4648Section10Decode_test2_decomposed(self) -> None:
        pass

    def testRfc4648Section10Decode_test1_decomposed(self) -> None:
        pass

    def testRfc4648Section10Decode_test0_decomposed(self) -> None:
        pass

    def testRfc1421Section6Dot8ChunkSizeDefinition_test0_decomposed(self) -> None:
        pass

    def testRfc2045Section6Dot8ChunkSizeDefinition_test0_decomposed(self) -> None:
        pass

    def testRfc2045Section2Dot1CrLfDefinition_test0_decomposed(self) -> None:
        pass

    def testPairs_test1_decomposed(self) -> None:
        pass

    def testPairs_test0_decomposed(self) -> None:
        pass

    def testObjectEncode_test2_decomposed(self) -> None:
        pass

    def testObjectEncode_test1_decomposed(self) -> None:
        pass

    def testObjectEncode_test0_decomposed(self) -> None:
        pass

    def testObjectEncodeWithValidParameter_test4_decomposed(self) -> None:
        pass

    def testObjectEncodeWithValidParameter_test3_decomposed(self) -> None:
        pass

    def testObjectEncodeWithValidParameter_test2_decomposed(self) -> None:
        pass

    def testObjectEncodeWithValidParameter_test1_decomposed(self) -> None:
        pass

    def testObjectEncodeWithValidParameter_test0_decomposed(self) -> None:
        pass

    def testObjectEncodeWithInvalidParameter_test1_decomposed(self) -> None:
        pass

    def testObjectEncodeWithInvalidParameter_test0_decomposed(self) -> None:
        pass

    def testObjectDecodeWithValidParameter_test4_decomposed(self) -> None:
        pass

    def testObjectDecodeWithValidParameter_test3_decomposed(self) -> None:
        pass

    def testObjectDecodeWithValidParameter_test2_decomposed(self) -> None:
        pass

    def testObjectDecodeWithValidParameter_test1_decomposed(self) -> None:
        pass

    def testObjectDecodeWithValidParameter_test0_decomposed(self) -> None:
        pass

    def testObjectDecodeWithInvalidParameter_test1_decomposed(self) -> None:
        pass

    def testObjectDecodeWithInvalidParameter_test0_decomposed(self) -> None:
        pass

    def testNonBase64Test_test1_decomposed(self) -> None:
        pass

    def testNonBase64Test_test0_decomposed(self) -> None:
        pass

    def testKnownEncodings_test13_decomposed(self) -> None:
        pass

    def testKnownEncodings_test12_decomposed(self) -> None:
        pass

    def testKnownEncodings_test11_decomposed(self) -> None:
        pass

    def testKnownEncodings_test10_decomposed(self) -> None:
        pass

    def testKnownEncodings_test9_decomposed(self) -> None:
        pass

    def testKnownEncodings_test8_decomposed(self) -> None:
        pass

    def testKnownEncodings_test7_decomposed(self) -> None:
        pass

    def testKnownEncodings_test6_decomposed(self) -> None:
        pass

    def testKnownEncodings_test5_decomposed(self) -> None:
        pass

    def testKnownEncodings_test4_decomposed(self) -> None:
        pass

    def testKnownEncodings_test3_decomposed(self) -> None:
        pass

    def testKnownEncodings_test2_decomposed(self) -> None:
        pass

    def testKnownEncodings_test1_decomposed(self) -> None:
        pass

    def testKnownEncodings_test0_decomposed(self) -> None:
        pass

    def testKnownDecodings_test11_decomposed(self) -> None:
        pass

    def testKnownDecodings_test10_decomposed(self) -> None:
        pass

    def testKnownDecodings_test9_decomposed(self) -> None:
        pass

    def testKnownDecodings_test8_decomposed(self) -> None:
        pass

    def testKnownDecodings_test7_decomposed(self) -> None:
        pass

    def testKnownDecodings_test6_decomposed(self) -> None:
        pass

    def testKnownDecodings_test5_decomposed(self) -> None:
        pass

    def testKnownDecodings_test4_decomposed(self) -> None:
        pass

    def testKnownDecodings_test3_decomposed(self) -> None:
        pass

    def testKnownDecodings_test2_decomposed(self) -> None:
        pass

    def testKnownDecodings_test1_decomposed(self) -> None:
        pass

    def testKnownDecodings_test0_decomposed(self) -> None:
        pass

    def testIsUrlSafe_test2_decomposed(self) -> None:
        pass

    def testIsUrlSafe_test1_decomposed(self) -> None:
        pass

    def testIsUrlSafe_test0_decomposed(self) -> None:
        pass

    def testIsArrayByteBase64_test0_decomposed(self) -> None:
        pass

    def testIgnoringNonBase64InDecode_test1_decomposed(self) -> None:
        pass

    def testIgnoringNonBase64InDecode_test0_decomposed(self) -> None:
        pass

    def testCodec112_test1_decomposed(self) -> None:
        pass

    def testCodec112_test0_decomposed(self) -> None:
        pass

    def testEncodeOverMaxSize0_test0_decomposed(self) -> None:
        pass

    def testEncodeDecodeSmall_test0_decomposed(self) -> None:
        pass

    def testEncodeDecodeRandom_test0_decomposed(self) -> None:
        pass

    def testEmptyBase64_test7_decomposed(self) -> None:
        pass

    def testEmptyBase64_test6_decomposed(self) -> None:
        pass

    def testEmptyBase64_test5_decomposed(self) -> None:
        pass

    def testEmptyBase64_test4_decomposed(self) -> None:
        pass

    def testEmptyBase64_test3_decomposed(self) -> None:
        pass

    def testEmptyBase64_test2_decomposed(self) -> None:
        pass

    def testEmptyBase64_test1_decomposed(self) -> None:
        pass

    def testEmptyBase64_test0_decomposed(self) -> None:
        pass

    def testDecodeWithWhitespace_test5_decomposed(self) -> None:
        pass

    def testDecodeWithWhitespace_test4_decomposed(self) -> None:
        pass

    def testDecodeWithWhitespace_test3_decomposed(self) -> None:
        pass

    def testDecodeWithWhitespace_test2_decomposed(self) -> None:
        pass

    def testDecodeWithWhitespace_test1_decomposed(self) -> None:
        pass

    def testDecodeWithWhitespace_test0_decomposed(self) -> None:
        pass

    def testDecodePadOnlyChunked_test11_decomposed(self) -> None:
        pass

    def testDecodePadOnlyChunked_test10_decomposed(self) -> None:
        pass

    def testDecodePadOnlyChunked_test9_decomposed(self) -> None:
        pass

    def testDecodePadOnlyChunked_test8_decomposed(self) -> None:
        pass

    def testDecodePadOnlyChunked_test7_decomposed(self) -> None:
        pass

    def testDecodePadOnlyChunked_test6_decomposed(self) -> None:
        pass

    def testDecodePadOnlyChunked_test5_decomposed(self) -> None:
        pass

    def testDecodePadOnlyChunked_test4_decomposed(self) -> None:
        pass

    def testDecodePadOnlyChunked_test3_decomposed(self) -> None:
        pass

    def testDecodePadOnlyChunked_test2_decomposed(self) -> None:
        pass

    def testDecodePadOnlyChunked_test1_decomposed(self) -> None:
        pass

    def testDecodePadOnlyChunked_test0_decomposed(self) -> None:
        pass

    def testDecodePadOnly_test11_decomposed(self) -> None:
        pass

    def testDecodePadOnly_test10_decomposed(self) -> None:
        pass

    def testDecodePadOnly_test9_decomposed(self) -> None:
        pass

    def testDecodePadOnly_test8_decomposed(self) -> None:
        pass

    def testDecodePadOnly_test7_decomposed(self) -> None:
        pass

    def testDecodePadOnly_test6_decomposed(self) -> None:
        pass

    def testDecodePadOnly_test5_decomposed(self) -> None:
        pass

    def testDecodePadOnly_test4_decomposed(self) -> None:
        pass

    def testDecodePadOnly_test3_decomposed(self) -> None:
        pass

    def testDecodePadOnly_test2_decomposed(self) -> None:
        pass

    def testDecodePadOnly_test1_decomposed(self) -> None:
        pass

    def testDecodePadOnly_test0_decomposed(self) -> None:
        pass

    def testDecodePadMarkerIndex3_test3_decomposed(self) -> None:
        pass

    def testDecodePadMarkerIndex3_test2_decomposed(self) -> None:
        pass

    def testDecodePadMarkerIndex3_test1_decomposed(self) -> None:
        pass

    def testDecodePadMarkerIndex3_test0_decomposed(self) -> None:
        pass

    def testDecodePadMarkerIndex2_test1_decomposed(self) -> None:
        pass

    def testDecodePadMarkerIndex2_test0_decomposed(self) -> None:
        pass

    def testConstructor_Int_ByteArray_Boolean_UrlSafe_test3_decomposed(self) -> None:
        pass

    def testConstructor_Int_ByteArray_Boolean_UrlSafe_test2_decomposed(self) -> None:
        pass

    def testConstructor_Int_ByteArray_Boolean_UrlSafe_test1_decomposed(self) -> None:
        pass

    def testConstructor_Int_ByteArray_Boolean_UrlSafe_test0_decomposed(self) -> None:
        pass

    def testConstructor_Int_ByteArray_Boolean_test3_decomposed(self) -> None:
        pass

    def testConstructor_Int_ByteArray_Boolean_test2_decomposed(self) -> None:
        pass

    def testConstructor_Int_ByteArray_Boolean_test1_decomposed(self) -> None:
        pass

    def testConstructor_Int_ByteArray_Boolean_test0_decomposed(self) -> None:
        pass

    def testConstructors_test3_decomposed(self) -> None:
        pass

    def testConstructors_test2_decomposed(self) -> None:
        pass

    def testConstructors_test1_decomposed(self) -> None:
        pass

    def testConstructors_test0_decomposed(self) -> None:
        pass

    def testCodeIntegerNull_test0_decomposed(self) -> None:
        pass

    def testCodeInteger4_test2_decomposed(self) -> None:
        pass

    def testCodeInteger4_test1_decomposed(self) -> None:
        pass

    def testCodeInteger4_test0_decomposed(self) -> None:
        pass

    def testCodeInteger3_test2_decomposed(self) -> None:
        pass

    def testCodeInteger3_test1_decomposed(self) -> None:
        pass

    def testCodeInteger3_test0_decomposed(self) -> None:
        pass

    def testCodeInteger2_test2_decomposed(self) -> None:
        pass

    def testCodeInteger2_test1_decomposed(self) -> None:
        pass

    def testCodeInteger2_test0_decomposed(self) -> None:
        pass

    def testCodeInteger1_test2_decomposed(self) -> None:
        pass

    def testCodeInteger1_test1_decomposed(self) -> None:
        pass

    def testCodeInteger1_test0_decomposed(self) -> None:
        pass

    def testCodec68_test0_decomposed(self) -> None:
        pass

    def testChunkedEncodeMultipleOf76_test2_decomposed(self) -> None:
        pass

    def testChunkedEncodeMultipleOf76_test1_decomposed(self) -> None:
        pass

    def testChunkedEncodeMultipleOf76_test0_decomposed(self) -> None:
        pass

    def testDecodeWithInnerPad_test2_decomposed(self) -> None:
        pass

    def testDecodeWithInnerPad_test1_decomposed(self) -> None:
        pass

    def testDecodeWithInnerPad_test0_decomposed(self) -> None:
        pass

    def testBase64_test13_decomposed(self) -> None:
        pass

    def testBase64_test12_decomposed(self) -> None:
        pass

    def testBase64_test11_decomposed(self) -> None:
        pass

    def testBase64_test10_decomposed(self) -> None:
        pass

    def testBase64_test9_decomposed(self) -> None:
        pass

    def testBase64_test8_decomposed(self) -> None:
        pass

    def testBase64_test7_decomposed(self) -> None:
        pass

    def testBase64_test6_decomposed(self) -> None:
        pass

    def testBase64_test5_decomposed(self) -> None:
        pass

    def testBase64_test4_decomposed(self) -> None:
        pass

    def testBase64_test3_decomposed(self) -> None:
        pass

    def testBase64_test2_decomposed(self) -> None:
        pass

    def testBase64_test1_decomposed(self) -> None:
        pass

    def testBase64_test0_decomposed(self) -> None:
        pass

    def testIsStringBase64_test1_decomposed(self) -> None:
        pass

    def testIsStringBase64_test0_decomposed(self) -> None:
        pass

    def getRandom(self) -> random.Random:
        pass

    @staticmethod
    def __assertBase64DecodingOfTrailingBits(nbits: int) -> None:
        pass

    def __toString(self, data: typing.List[int]) -> str:
        pass

    def __testEncodeDecode(self, plainText: str) -> None:
        pass

    def __testDecodeEncode(self, encodedText: str) -> None:
        pass

    def __testEncodeOverMaxSize1(self, maxSize: int) -> None:
        pass

    # Class Methods End
