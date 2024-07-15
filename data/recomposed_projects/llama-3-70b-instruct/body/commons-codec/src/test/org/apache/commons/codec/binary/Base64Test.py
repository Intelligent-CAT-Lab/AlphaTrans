from __future__ import annotations
import re
import random
import uuid
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.binary.Base64 import *
from src.test.org.apache.commons.codec.binary.Base64TestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.test.org.apache.commons.codec.binary.BaseNCodecTest import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.Hex import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base64Test(unittest.TestCase):

    BASE64_IMPOSSIBLE_CASES: typing.List[str] = [
        "ZE==",
        "ZmC=",
        "Zm9vYE==",
        "Zm9vYmC=",
        "AB",
    ]
    __random: random.Random = random.Random()
    __STANDARD_ENCODE_TABLE: typing.List[int] = [
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        97,
        98,
        99,
        100,
        101,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        109,
        110,
        111,
        112,
        113,
        114,
        115,
        116,
        117,
        118,
        119,
        120,
        121,
        122,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        43,
        47,
    ]
    __CHARSET_UTF8: str = "UTF-8"

    def testCodec265(self) -> None:

        pass  # LLM could not translate this method

    def testBase64DecodingOfTrailing18Bits(self) -> None:
        self.__assertBase64DecodingOfTrailingBits(18)

    def testBase64DecodingOfTrailing12Bits(self) -> None:
        self.__assertBase64DecodingOfTrailingBits(12)

    def testBase64DecodingOfTrailing6Bits(self) -> None:
        self.__assertBase64DecodingOfTrailingBits(6)

    def testBase64ImpossibleSamples(self) -> None:
        codec = Base64(0, None, False, CodecPolicy.STRICT)
        for s in self.BASE64_IMPOSSIBLE_CASES:
            try:
                codec.decode3(s)
                self.fail()
            except ValueError:
                pass

    def testHugeLineSeparator(self) -> None:
        BaseNCodec_DEFAULT_BUFFER_SIZE = 8192
        Base64_BYTES_PER_ENCODED_BLOCK = 4
        baLineSeparator = [0] * (BaseNCodec_DEFAULT_BUFFER_SIZE * 4 - 3)
        b64 = Base64.Base642(Base64_BYTES_PER_ENCODED_BLOCK, baLineSeparator)
        strOriginal = "Hello World"
        strDecoded = str(
            b64.decode0(b64.encode0(StringUtils.getBytesUtf8(strOriginal)))
        )
        self.assertEqual("testDEFAULT_BUFFER_SIZE", strOriginal, strDecoded)

    def testStringToByteVariations(self) -> None:

        pass  # LLM could not translate this method

    def testByteToStringVariations(self) -> None:
        base64 = Base64.Base643(0)
        b1 = StringUtils.getBytesUtf8("Hello World")
        b2 = []
        b3 = None
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")  # for

        self.assertEqual(
            "byteToString Hello World", "SGVsbG8gV29ybGQ=", base64.encodeToString(b1)
        )
        self.assertEqual(
            "byteToString static Hello World",
            "SGVsbG8gV29ybGQ=",
            Base64.encodeBase64String(b1),
        )
        self.assertEqual('byteToString ""', "", base64.encodeToString(b2))
        self.assertEqual('byteToString static ""', "", Base64.encodeBase64String(b2))
        self.assertIsNone("byteToString null", base64.encodeToString(b3))
        self.assertIsNone("byteToString static null", Base64.encodeBase64String(b3))
        self.assertEqual(
            "byteToString UUID", "K/fMJwH+Q5e0nr7tWsxwkA==", base64.encodeToString(b4)
        )
        self.assertEqual(
            "byteToString static UUID",
            "K/fMJwH+Q5e0nr7tWsxwkA==",
            Base64.encodeBase64String(b4),
        )
        self.assertEqual(
            "byteToString static-url-safe UUID",
            "K_fMJwH-Q5e0nr7tWsxwkA",
            Base64.encodeBase64URLSafeString(b4),
        )

    def testUUID(self) -> None:
        ids: typing.List[typing.List[int]] = [None] * 4
        ids[0] = Hex.decodeHex2("94ed8d0319e4493399560fb67404d370")
        ids[1] = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")
        ids[2] = Hex.decodeHex2("64be154b6ffa40258d1a01288e7c31ca")
        ids[3] = Hex.decodeHex2("ff7f8fc01cdb471a8c8b5a9306183fe8")
        standard: typing.List[typing.List[int]] = [None] * 4
        standard[0] = StringUtils.getBytesUtf8("lO2NAxnkSTOZVg+2dATTcA==")
        standard[1] = StringUtils.getBytesUtf8("K/fMJwH+Q5e0nr7tWsxwkA==")
        standard[2] = StringUtils.getBytesUtf8("ZL4VS2/6QCWNGgEojnwxyg==")
        standard[3] = StringUtils.getBytesUtf8("/3+PwBzbRxqMi1qTBhg/6A==")
        urlSafe1: typing.List[typing.List[int]] = [None] * 4
        urlSafe1[0] = StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA==")
        urlSafe1[1] = StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA==")
        urlSafe1[2] = StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg==")
        urlSafe1[3] = StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A==")
        urlSafe2: typing.List[typing.List[int]] = [None] * 4
        urlSafe2[0] = StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA=")
        urlSafe2[1] = StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA=")
        urlSafe2[2] = StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg=")
        urlSafe2[3] = StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A=")
        urlSafe3: typing.List[typing.List[int]] = [None] * 4
        urlSafe3[0] = StringUtils.getBytesUtf8("lO2NAxnkSTOZVg-2dATTcA")
        urlSafe3[1] = StringUtils.getBytesUtf8("K_fMJwH-Q5e0nr7tWsxwkA")
        urlSafe3[2] = StringUtils.getBytesUtf8("ZL4VS2_6QCWNGgEojnwxyg")
        urlSafe3[3] = StringUtils.getBytesUtf8("_3-PwBzbRxqMi1qTBhg_6A")
        for i in range(4):
            encodedStandard: typing.List[int] = Base64.encodeBase640(ids[i])
            encodedUrlSafe: typing.List[int] = Base64.encodeBase64URLSafe(ids[i])
            decodedStandard: typing.List[int] = Base64.decodeBase640(standard[i])
            decodedUrlSafe1: typing.List[int] = Base64.decodeBase640(urlSafe1[i])
            decodedUrlSafe2: typing.List[int] = Base64.decodeBase640(urlSafe2[i])
            decodedUrlSafe3: typing.List[int] = Base64.decodeBase640(urlSafe3[i])
            self.assertArrayEquals("standard encode uuid", encodedStandard, standard[i])
            self.assertArrayEquals("url-safe encode uuid", encodedUrlSafe, urlSafe3[i])
            self.assertArrayEquals("standard decode uuid", decodedStandard, ids[i])
            self.assertArrayEquals("url-safe1 decode uuid", decodedUrlSafe1, ids[i])
            self.assertArrayEquals("url-safe2 decode uuid", decodedUrlSafe2, ids[i])
            self.assertArrayEquals("url-safe3 decode uuid", decodedUrlSafe3, ids[i])

    def testUrlSafe(self) -> None:
        codec = Base64.Base644(True)
        for i in range(0, 151):
            randomData = BaseNTestData.randomData(codec, i)
            encoded = randomData[1]
            decoded = randomData[0]
            result = Base64.decodeBase640(encoded)
            assertArrayEquals("url-safe i=" + str(i), decoded, result)
            assertFalse(
                "url-safe i=" + str(i) + " no '='",
                BaseNTestData.bytesContain(encoded, 61),
            )
            assertFalse(
                "url-safe i=" + str(i) + " no '\\'",
                BaseNTestData.bytesContain(encoded, 92),
            )
            assertFalse(
                "url-safe i=" + str(i) + " no '+'",
                BaseNTestData.bytesContain(encoded, 43),
            )

    def testTripletsChunked(self) -> None:

        pass  # LLM could not translate this method

    def testTriplets(self) -> None:
        self.assertEqual(
            "AAAA", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 0]))
        )
        self.assertEqual(
            "AAAB", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 1]))
        )
        self.assertEqual(
            "AAAC", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 2]))
        )
        self.assertEqual(
            "AAAD", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 3]))
        )
        self.assertEqual(
            "AAAE", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 4]))
        )
        self.assertEqual(
            "AAAF", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 5]))
        )
        self.assertEqual(
            "AAAG", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 6]))
        )
        self.assertEqual(
            "AAAH", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 7]))
        )
        self.assertEqual(
            "AAAI", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 8]))
        )
        self.assertEqual(
            "AAAJ", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 9]))
        )
        self.assertEqual(
            "AAAK", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 10]))
        )
        self.assertEqual(
            "AAAL", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 11]))
        )
        self.assertEqual(
            "AAAM", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 12]))
        )
        self.assertEqual(
            "AAAN", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 13]))
        )
        self.assertEqual(
            "AAAO", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 14]))
        )
        self.assertEqual(
            "AAAP", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 15]))
        )
        self.assertEqual(
            "AAAQ", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 16]))
        )
        self.assertEqual(
            "AAAR", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 17]))
        )
        self.assertEqual(
            "AAAS", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 18]))
        )
        self.assertEqual(
            "AAAT", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 19]))
        )
        self.assertEqual(
            "AAAU", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 20]))
        )
        self.assertEqual(
            "AAAV", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 21]))
        )
        self.assertEqual(
            "AAAW", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 22]))
        )
        self.assertEqual(
            "AAAX", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 23]))
        )
        self.assertEqual(
            "AAAY", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 24]))
        )
        self.assertEqual(
            "AAAZ", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 25]))
        )
        self.assertEqual(
            "AAAa", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 26]))
        )
        self.assertEqual(
            "AAAb", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 27]))
        )
        self.assertEqual(
            "AAAc", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 28]))
        )
        self.assertEqual(
            "AAAd", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 29]))
        )
        self.assertEqual(
            "AAAe", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 30]))
        )
        self.assertEqual(
            "AAAf", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 31]))
        )
        self.assertEqual(
            "AAAg", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 32]))
        )
        self.assertEqual(
            "AAAh", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 33]))
        )
        self.assertEqual(
            "AAAi", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 34]))
        )
        self.assertEqual(
            "AAAj", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 35]))
        )
        self.assertEqual(
            "AAAk", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 36]))
        )
        self.assertEqual(
            "AAAl", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 37]))
        )
        self.assertEqual(
            "AAAm", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 38]))
        )
        self.assertEqual(
            "AAAn", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 39]))
        )
        self.assertEqual(
            "AAAo", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 40]))
        )
        self.assertEqual(
            "AAAp", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 41]))
        )
        self.assertEqual(
            "AAAq", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 42]))
        )
        self.assertEqual(
            "AAAr", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 43]))
        )
        self.assertEqual(
            "AAAs", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 44]))
        )
        self.assertEqual(
            "AAAt", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 45]))
        )
        self.assertEqual(
            "AAAu", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 46]))
        )
        self.assertEqual(
            "AAAv", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 47]))
        )
        self.assertEqual(
            "AAAw", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 48]))
        )
        self.assertEqual(
            "AAAx", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 49]))
        )
        self.assertEqual(
            "AAAy", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 50]))
        )
        self.assertEqual(
            "AAAz", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 51]))
        )
        self.assertEqual(
            "AAA0", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 52]))
        )
        self.assertEqual(
            "AAA1", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 53]))
        )
        self.assertEqual(
            "AAA2", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 54]))
        )
        self.assertEqual(
            "AAA3", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 55]))
        )
        self.assertEqual(
            "AAA4", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 56]))
        )
        self.assertEqual(
            "AAA5", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 57]))
        )
        self.assertEqual(
            "AAA6", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 58]))
        )
        self.assertEqual(
            "AAA7", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 59]))
        )
        self.assertEqual(
            "AAA8", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 60]))
        )
        self.assertEqual(
            "AAA9", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 61]))
        )
        self.assertEqual(
            "AAA+", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 62]))
        )
        self.assertEqual(
            "AAA/", "".join(chr(x) for x in Base64.encodeBase640([0, 0, 63]))
        )

    def testSingletonsChunked(self) -> None:

        pass  # LLM could not translate this method

    def testSingletons(self) -> None:

        pass  # LLM could not translate this method

    def testRfc4648Section10EncodeDecode(self) -> None:

        pass  # LLM could not translate this method

    def testRfc4648Section10DecodeEncode(self) -> None:

        pass  # LLM could not translate this method

    def testRfc4648Section10Encode(self) -> None:
        self.assertEqual("", Base64.encodeBase64String(StringUtils.getBytesUtf8("")))
        self.assertEqual(
            "Zg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("f"))
        )
        self.assertEqual(
            "Zm8=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fo"))
        )
        self.assertEqual(
            "Zm9v", Base64.encodeBase64String(StringUtils.getBytesUtf8("foo"))
        )
        self.assertEqual(
            "Zm9vYg==", Base64.encodeBase64String(StringUtils.getBytesUtf8("foob"))
        )
        self.assertEqual(
            "Zm9vYmE=", Base64.encodeBase64String(StringUtils.getBytesUtf8("fooba"))
        )
        self.assertEqual(
            "Zm9vYmFy", Base64.encodeBase64String(StringUtils.getBytesUtf8("foobar"))
        )

    def testRfc4648Section10DecodeWithCrLf(self) -> None:
        CRLF: str = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)
        self.assertEqual(
            "", StringUtils.newStringUsAscii(Base64.decodeBase641("" + CRLF))
        )
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==" + CRLF))
        )
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8=" + CRLF))
        )
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v" + CRLF))
        )
        self.assertEqual(
            "foob",
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg==" + CRLF)),
        )
        self.assertEqual(
            "fooba",
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmE=" + CRLF)),
        )
        self.assertEqual(
            "foobar",
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmFy" + CRLF)),
        )

    def testRfc4648Section10Decode(self) -> None:
        self.assertEqual("", StringUtils.newStringUsAscii(Base64.decodeBase641("")))
        self.assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg=="))
        )
        self.assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8="))
        )
        self.assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v"))
        )
        self.assertEqual(
            "foob", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg=="))
        )
        self.assertEqual(
            "fooba", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmE="))
        )
        self.assertEqual(
            "foobar", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmFy"))
        )

    def testRfc1421Section6Dot8ChunkSizeDefinition(self) -> None:
        self.assertEqual(64, BaseNCodec.PEM_CHUNK_SIZE)

    def testRfc2045Section6Dot8ChunkSizeDefinition(self) -> None:
        self.assertEqual(76, BaseNCodec.MIME_CHUNK_SIZE)

    def testRfc2045Section2Dot1CrLfDefinition(self) -> None:
        self.assertEqual(Base64.CHUNK_SEPARATOR, b"\r\n")

    def testPairs(self) -> None:
        self.assertEqual("AAA=", str(Base64.encodeBase640([0, 0])))
        for i in range(-128, 128):
            test = [i, i]
            self.assertListEqual(test, Base64.decodeBase640(Base64.encodeBase640(test)))

    def testObjectEncode(self) -> None:
        b64: Base64 = Base64.Base645()
        self.assertEqual(
            "SGVsbG8gV29ybGQ=", b64.encode0("Hello World".encode(self.__CHARSET_UTF8))
        )

    def testObjectEncodeWithValidParameter(self) -> None:
        original: str = "Hello World!"
        origObj: typing.List[int] = original.encode(self.__CHARSET_UTF8)
        b64: Base64 = Base64.Base645()
        oEncoded: typing.List[int] = b64.encode3(origObj)
        bArray: typing.List[int] = Base64.decodeBase640(oEncoded)
        dest: str = bArray.decode(self.__CHARSET_UTF8)
        self.assertEqual("dest string does not equal original", original, dest)

    def testObjectEncodeWithInvalidParameter(self) -> None:
        b64 = Base64.Base645()
        with self.assertRaises(EncoderException):
            b64.encode3("Yadayadayada")

    def testObjectDecodeWithValidParameter(self) -> None:
        original: str = "Hello World!"
        o: typing.Any = Base64.encodeBase640(original.encode(self.__CHARSET_UTF8))
        b64: Base64 = Base64.Base645()
        oDecoded: typing.Any = b64.decode2(o)
        baDecoded: typing.List[int] = typing.cast(typing.List[int], oDecoded)
        dest: str = str(baDecoded, self.__CHARSET_UTF8)
        self.assertEqual("dest string does not equal original", original, dest)

    def testObjectDecodeWithInvalidParameter(self) -> None:
        b64: Base64 = Base64.Base645()

        try:
            b64.decode2(Integer.valueOf(5))
            self.fail(
                "decode(Object) didn't throw an exception when passed an Integer object"
            )
        except DecoderException as e:
            pass

    def testNonBase64Test(self) -> None:
        bArray = [37]
        self.assertFalse(
            "Invalid Base64 array was incorrectly validated as "
            + "an array of Base64 encoded data",
            Base64.isBase641(bArray),
        )
        try:
            b64 = Base64.Base645()
            result = b64.decode0(bArray)
            self.assertEqual(
                "The result should be empty as the test encoded content did "
                + "not contain any valid base 64 characters",
                0,
                len(result),
            )
        except Exception as e:
            self.fail(
                "Exception was thrown when trying to decode "
                + "invalid base64 encoded data - RFC 2045 requires that all "
                + "non base64 character be discarded, an exception should not"
                + " have been thrown"
            )

    def testKnownEncodings(self) -> None:

        pass  # LLM could not translate this method

    def testKnownDecodings(self) -> None:

        pass  # LLM could not translate this method

    def testIsUrlSafe(self) -> None:
        base64Standard: Base64 = Base64.Base644(False)
        base64URLSafe: Base64 = Base64.Base644(True)

        self.assertFalse("Base64.isUrlSafe=false", base64Standard.isUrlSafe())
        self.assertTrue("Base64.isUrlSafe=true", base64URLSafe.isUrlSafe())

        whiteSpace: typing.List[int] = [32, 10, 13, 9]
        self.assertTrue(
            "Base64.isBase641(whiteSpace)=true", Base64.isBase641(whiteSpace)
        )

    def testIsArrayByteBase64(self) -> None:
        self.assertFalse(Base64.isBase641([-128]))
        self.assertFalse(Base64.isBase641([-125]))
        self.assertFalse(Base64.isBase641([-10]))
        self.assertFalse(Base64.isBase641([0]))
        self.assertFalse(Base64.isBase641([64, 127]))
        self.assertFalse(Base64.isBase641([127]))
        self.assertTrue(Base64.isBase641(["A"]))
        self.assertFalse(Base64.isBase641(["A", -128]))
        self.assertTrue(Base64.isBase641(["A", "Z", "a"]))
        self.assertTrue(Base64.isBase641(["/"]))
        self.assertFalse(Base64.isBase641(["$"]))

    def testIgnoringNonBase64InDecode(self) -> None:
        self.assertEqual(
            "The quick brown fox jumped over the lazy dogs.",
            str(
                Base64.decodeBase640(
                    "VGhlIH@$#$@%F1aWN@#@#@@rIGJyb3duIGZve\n\r\t%#%#%#%CBqd##$#$W1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==".encode(
                        self.__CHARSET_UTF8
                    )
                )
            ),
        )

    def testCodec112(self) -> None:

        pass  # LLM could not translate this method

    def testEncodeOverMaxSize0(self) -> None:

        pass  # LLM could not translate this method

    def testEncodeDecodeSmall(self) -> None:
        for i in range(12):
            data = [0] * i
            self.getRandom().nextBytes(data)
            enc = Base64.encodeBase640(data)
            self.assertTrue(
                '"' + "".join([chr(x) for x in enc]) + '" is Base64 data.',
                Base64.isBase641(enc),
            )
            data2 = Base64.decodeBase640(enc)
            self.assertListEqual(
                "".join([chr(x) for x in data])
                + " equals "
                + "".join([chr(x) for x in data2]),
                data,
                data2,
            )

    def testEncodeDecodeRandom(self) -> None:
        for i in range(1, 5):
            data: typing.List[int] = [0] * (self.getRandom().nextInt(10000) + 1)
            self.getRandom().nextBytes(data)
            enc: typing.List[int] = Base64.encodeBase640(data)
            self.assertTrue(Base64.isBase641(enc))
            data2: typing.List[int] = Base64.decodeBase640(enc)
            self.assertArrayEquals(data, data2)

    def testEmptyBase64(self) -> None:
        empty: typing.List[int] = []
        result: typing.List[int] = Base64.encodeBase640(empty)
        self.assertEqual("empty base64 encode", 0, result.length)
        self.assertIsNone("empty base64 encode", Base64.encodeBase640(None))
        result = Base64.Base645().encode1(empty, 0, 1)
        self.assertEqual("empty base64 encode", 0, result.length)
        self.assertIsNone("empty base64 encode", Base64.Base645().encode1(None, 0, 1))

        empty = [0] * 0
        result = Base64.decodeBase640(empty)
        self.assertEqual("empty base64 decode", 0, result.length)
        self.assertIsNone("empty base64 encode", Base64.decodeBase640(None))

    def testDecodeWithWhitespace(self) -> None:

        pass  # LLM could not translate this method

    def testDecodePadOnlyChunked(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "", Base64.decodeBase640("====\n".encode(self.__CHARSET_UTF8)).decode()
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("===\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("==\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("=\n".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(0, len(Base64.decodeBase640("\n".encode(self.__CHARSET_UTF8))))

    def testDecodePadOnly(self) -> None:
        self.assertEqual(
            0, len(Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "", Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)).decode()
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("===".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(0, len(Base64.decodeBase640("==".encode(self.__CHARSET_UTF8))))
        self.assertEqual(0, len(Base64.decodeBase640("=".encode(self.__CHARSET_UTF8))))
        self.assertEqual(0, len(Base64.decodeBase640("".encode(self.__CHARSET_UTF8))))

    def testDecodePadMarkerIndex3(self) -> None:
        self.assertEqual(
            "AA",
            str(
                Base64.decodeBase640("QUE=".encode(self.__CHARSET_UTF8)),
                self.__CHARSET_UTF8,
            ),
        )
        self.assertEqual(
            "AAA",
            str(
                Base64.decodeBase640("QUFB".encode(self.__CHARSET_UTF8)),
                self.__CHARSET_UTF8,
            ),
        )

    def testDecodePadMarkerIndex2(self) -> None:
        self.assertEqual(
            "A", str(Base64.decodeBase640("QQ==".encode(self.__CHARSET_UTF8)))
        )

    def testConstructor_Int_ByteArray_Boolean_UrlSafe(self) -> None:
        base64 = Base64.Base641(64, [9], True)
        encoded = base64.encode0(BaseNTestData.DECODED)
        expectedResult = Base64TestData.ENCODED_64_CHARS_PER_LINE
        expectedResult = expectedResult.replace("=", "")  # url-safe has no
        expectedResult = expectedResult.replace("\n", "\t")
        expectedResult = expectedResult.replace("+", "-")
        expectedResult = expectedResult.replace("/", "_")
        result = StringUtils.newStringUtf8(encoded)
        self.assertEqual("new Base64(64, \\t, true)", result, expectedResult)

    def testConstructor_Int_ByteArray_Boolean(self) -> None:
        base64 = Base64.Base641(65, [9], False)
        encoded = base64.encode0(BaseNTestData.DECODED)
        expectedResult = Base64TestData.ENCODED_64_CHARS_PER_LINE
        expectedResult = expectedResult.replace("\n", "\t")
        result = StringUtils.newStringUtf8(encoded)
        self.assertEqual("new Base64(65, \\t, false)", expectedResult, result)

    def testConstructors(self) -> None:
        base64: Base64
        base64 = Base64.Base645()
        base64 = Base64.Base643(-1)
        base64 = Base64.Base642(-1, [])
        base64 = Base64.Base642(64, [])
        try:
            base64 = Base64.Base642(-1, ["A"])  # TODO do we need to
            self.fail("Should have rejected attempt to use 'A' as a line separator")
        except ValueError as ignored:
            pass
        try:
            base64 = Base64.Base642(64, ["A"])
            self.fail("Should have rejected attempt to use 'A' as a line separator")
        except ValueError as ignored:
            pass
        try:
            base64 = Base64.Base642(64, ["="])
            self.fail("Should have rejected attempt to use '=' as a line separator")
        except ValueError as ignored:
            pass
        base64 = Base64.Base642(64, ["$"])  # OK
        try:
            base64 = Base64.Base642(64, ["A", "$"])
            self.fail("Should have rejected attempt to use 'A$' as a line separator")
        except ValueError as ignored:
            pass
        base64 = Base64.Base642(64, [" ", "$", "\n", "\r", "\t"])  # OK
        self.assertIsNotNone(base64)

    def testCodeIntegerNull(self) -> None:
        try:
            Base64.encodeInteger(None)
            self.fail(
                "Exception not thrown when passing in null to encodeInteger(BigInteger)"
            )
        except RuntimeError as npe:
            pass
        except Exception as e:
            self.fail(
                "Incorrect Exception caught when passing in null to encodeInteger(BigInteger)"
            )

    def testCodeIntegerEdgeCases(self) -> None:

        pass  # LLM could not translate this method

    def testCodeInteger4(self) -> None:

        pass  # LLM could not translate this method

    def testCodeInteger3(self) -> None:

        pass  # LLM could not translate this method

    def testCodeInteger2(self) -> None:

        pass  # LLM could not translate this method

    def testCodeInteger1(self) -> None:

        pass  # LLM could not translate this method

    def testCodec68(self) -> None:

        pass  # LLM could not translate this method

    def testChunkedEncodeMultipleOf76(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeWithInnerPad(self) -> None:

        pass  # LLM could not translate this method

    def testBase64(self) -> None:

        pass  # LLM could not translate this method

    def testIsStringBase64(self) -> None:

        pass  # LLM could not translate this method

    def getRandom(self) -> random.Random:
        return self.__random

    @staticmethod
    def __assertBase64DecodingOfTrailingBits(nbits: int) -> None:

        pass  # LLM could not translate this method

    def __toString(self, data: typing.List[int]) -> str:

        pass  # LLM could not translate this method

    def __testEncodeDecode(self, plainText: str) -> None:

        pass  # LLM could not translate this method

    def __testDecodeEncode(self, encodedText: str) -> None:

        pass  # LLM could not translate this method

    def __testEncodeOverMaxSize1(self, maxSize: int) -> None:

        pass  # LLM could not translate this method
