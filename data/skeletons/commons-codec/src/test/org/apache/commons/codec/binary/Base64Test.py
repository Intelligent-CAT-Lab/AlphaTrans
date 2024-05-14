# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.binary.Hex import *
from src.main.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodecTest import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.Base64TestData import *
from src.main.org.apache.commons.codec.binary.Base64 import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import typing

# Imports End


class Base64Test:

    # Class Fields Begin
    __CHARSET_UTF8: str = None
    BASE64_IMPOSSIBLE_CASES: typing.List[str] = None
    __STANDARD_ENCODE_TABLE: typing.List[int] = None
    __random: random.Random = None
    # Class Fields End

    # Class Methods Begin
    def testCodec265(self) -> None:
        pass

    def testBase64DecodingOfTrailing18Bits(self) -> None:
        pass

    def testBase64DecodingOfTrailing12Bits(self) -> None:
        pass

    def testBase64DecodingOfTrailing6Bits(self) -> None:
        pass

    def testBase64ImpossibleSamples(self) -> None:
        pass

    def testHugeLineSeparator(self) -> None:
        pass

    def testStringToByteVariations(self) -> None:
        pass

    def testByteToStringVariations(self) -> None:
        pass

    def testUUID(self) -> None:
        pass

    def testUrlSafe(self) -> None:
        pass

    def testTripletsChunked(self) -> None:
        pass

    def testTriplets(self) -> None:
        pass

    def testSingletonsChunked(self) -> None:
        pass

    def testSingletons(self) -> None:
        pass

    def testRfc4648Section10EncodeDecode(self) -> None:
        pass

    def testRfc4648Section10DecodeEncode(self) -> None:
        pass

    def testRfc4648Section10Encode(self) -> None:
        pass

    def testRfc4648Section10DecodeWithCrLf(self) -> None:
        pass

    def testRfc4648Section10Decode(self) -> None:
        pass

    def testRfc1421Section6Dot8ChunkSizeDefinition(self) -> None:
        pass

    def testRfc2045Section6Dot8ChunkSizeDefinition(self) -> None:
        pass

    def testRfc2045Section2Dot1CrLfDefinition(self) -> None:
        pass

    def testPairs(self) -> None:
        pass

    def testObjectEncode(self) -> None:
        pass

    def testObjectEncodeWithValidParameter(self) -> None:
        pass

    def testObjectEncodeWithInvalidParameter(self) -> None:
        pass

    def testObjectDecodeWithValidParameter(self) -> None:
        pass

    def testObjectDecodeWithInvalidParameter(self) -> None:
        pass

    def testNonBase64Test(self) -> None:
        pass

    def testKnownEncodings(self) -> None:
        pass

    def testKnownDecodings(self) -> None:
        pass

    def testIsUrlSafe(self) -> None:
        pass

    def testIsArrayByteBase64(self) -> None:
        pass

    def testIgnoringNonBase64InDecode(self) -> None:
        pass

    def testCodec112(self) -> None:
        pass

    def testEncodeOverMaxSize0(self) -> None:
        pass

    def testEncodeDecodeSmall(self) -> None:
        pass

    def testEncodeDecodeRandom(self) -> None:
        pass

    def testEmptyBase64(self) -> None:
        pass

    def testDecodeWithWhitespace(self) -> None:
        pass

    def testDecodePadOnlyChunked(self) -> None:
        pass

    def testDecodePadOnly(self) -> None:
        pass

    def testDecodePadMarkerIndex3(self) -> None:
        pass

    def testDecodePadMarkerIndex2(self) -> None:
        pass

    def testConstructor_Int_ByteArray_Boolean_UrlSafe(self) -> None:
        pass

    def testConstructor_Int_ByteArray_Boolean(self) -> None:
        pass

    def testConstructors(self) -> None:
        pass

    def testCodeIntegerNull(self) -> None:
        pass

    def testCodeIntegerEdgeCases(self) -> None:
        pass

    def testCodeInteger4(self) -> None:
        pass

    def testCodeInteger3(self) -> None:
        pass

    def testCodeInteger2(self) -> None:
        pass

    def testCodeInteger1(self) -> None:
        pass

    def testCodec68(self) -> None:
        pass

    def testChunkedEncodeMultipleOf76(self) -> None:
        pass

    def testDecodeWithInnerPad(self) -> None:
        pass

    def testBase64(self) -> None:
        pass

    def testIsStringBase64(self) -> None:
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
