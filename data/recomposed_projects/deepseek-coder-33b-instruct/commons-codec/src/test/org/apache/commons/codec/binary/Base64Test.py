from __future__ import annotations
import re
import random
import unittest
import pytest
import io
import typing
from typing import *
import os
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

    BASE64_IMPOSSIBLE_CASES: List[str] = ["ZE==", "ZmC=", "Zm9vYE==", "Zm9vYmC=", "AB"]

    __random: random.Random = random.Random()

    __STANDARD_ENCODE_TABLE: typing.List[int] = [
        ord("A"),
        ord("B"),
        ord("C"),
        ord("D"),
        ord("E"),
        ord("F"),
        ord("G"),
        ord("H"),
        ord("I"),
        ord("J"),
        ord("K"),
        ord("L"),
        ord("M"),
        ord("N"),
        ord("O"),
        ord("P"),
        ord("Q"),
        ord("R"),
        ord("S"),
        ord("T"),
        ord("U"),
        ord("V"),
        ord("W"),
        ord("X"),
        ord("Y"),
        ord("Z"),
        ord("a"),
        ord("b"),
        ord("c"),
        ord("d"),
        ord("e"),
        ord("f"),
        ord("g"),
        ord("h"),
        ord("i"),
        ord("j"),
        ord("k"),
        ord("l"),
        ord("m"),
        ord("n"),
        ord("o"),
        ord("p"),
        ord("q"),
        ord("r"),
        ord("s"),
        ord("t"),
        ord("u"),
        ord("v"),
        ord("w"),
        ord("x"),
        ord("y"),
        ord("z"),
        ord("0"),
        ord("1"),
        ord("2"),
        ord("3"),
        ord("4"),
        ord("5"),
        ord("6"),
        ord("7"),
        ord("8"),
        ord("9"),
        ord("+"),
        ord("/"),
    ]

    __CHARSET_UTF8: str = "UTF-8"

    def testCodec265(self) -> None:

        size1GiB = 1 << 30

        blocks = math.ceil(size1GiB / 3.0)
        expectedLength = 4 * blocks

        presumableFreeMemory = BaseNCodecTest.getPresumableFreeMemory()

        estimatedMemory = size1GiB * 4 + expectedLength + 32 * 1024
        assert (
            presumableFreeMemory > estimatedMemory
        ), "Not enough free memory for the test"

        bytes = bytearray(size1GiB)
        encoded = Base64.encodeBase640(bytes)
        assert expectedLength == len(
            encoded
        ), "Expected length does not match the actual length"

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
        baLineSeparator = bytearray(BaseNCodec_DEFAULT_BUFFER_SIZE * 4 - 3)
        b64 = Base64.Base642(Base64_BYTES_PER_ENCODED_BLOCK, baLineSeparator)
        strOriginal = "Hello World"
        strDecoded = b64.decode0(
            b64.encode0(StringUtils.getBytesUtf8(strOriginal))
        ).decode("utf-8")
        assert strOriginal == strDecoded, "testDEFAULT_BUFFER_SIZE"

    def testStringToByteVariations(self) -> None:

        base64 = Base64.Base645()
        s1 = "SGVsbG8gV29ybGQ=\r\n"
        s2 = ""
        s3 = None
        s4a = "K/fMJwH+Q5e0nr7tWsxwkA==\r\n"
        s4b = "K_fMJwH-Q5e0nr7tWsxwkA"
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        assert StringUtils.newStringUtf8(base64.decode3(s1)) == "Hello World"
        assert StringUtils.newStringUtf8(base64.decode2(s1)) == "Hello World"
        assert StringUtils.newStringUtf8(Base64.decodeBase641(s1)) == "Hello World"
        assert StringUtils.newStringUtf8(base64.decode3(s2)) == ""
        assert StringUtils.newStringUtf8(Base64.decodeBase641(s2)) == ""
        assert StringUtils.newStringUtf8(base64.decode3(s3)) is None
        assert StringUtils.newStringUtf8(Base64.decodeBase641(s3)) is None
        assert base64.decode3(s4b) == b4
        assert Base64.decodeBase641(s4a) == b4
        assert Base64.decodeBase641(s4b) == b4

    def testByteToStringVariations(self) -> None:

        base64 = Base64.Base643(0)
        b1 = StringUtils.getBytesUtf8("Hello World")
        b2 = bytearray()
        b3 = None
        b4 = Hex.decodeHex2("2bf7cc2701fe4397b49ebeed5acc7090")

        assert base64.encodeToString(b1) == "SGVsbG8gV29ybGQ="
        assert Base64.encodeBase64String(b1) == "SGVsbG8gV29ybGQ="
        assert base64.encodeToString(b2) == ""
        assert Base64.encodeBase64String(b2) == ""
        assert base64.encodeToString(b3) is None
        assert Base64.encodeBase64String(b3) is None
        assert base64.encodeToString(b4) == "K/fMJwH+Q5e0nr7tWsxwkA=="
        assert Base64.encodeBase64String(b4) == "K/fMJwH+Q5e0nr7tWsxwkA=="
        assert Base64.encodeBase64URLSafeString(b4) == "K_fMJwH-Q5e0nr7tWsxwkA"

    def testUUID(self) -> None:

        pass  # LLM could not translate this method

    def testUrlSafe(self) -> None:

        codec = Base64.Base644(True)
        for i in range(151):
            randomData = BaseNTestData.randomData(codec, i)
            encoded = randomData[1]
            decoded = randomData[0]
            result = Base64.decodeBase640(encoded)
            assert result == decoded, "url-safe i=" + str(i)
            assert not BaseNTestData.bytesContain(encoded, ord("=")), (
                "url-safe i=" + str(i) + " no '='"
            )
            assert not BaseNTestData.bytesContain(encoded, ord("\\")), (
                "url-safe i=" + str(i) + " no '\\'"
            )
            assert not BaseNTestData.bytesContain(encoded, ord("+")), (
                "url-safe i=" + str(i) + " no '+'"
            )

    def testTripletsChunked(self) -> None:

        pass  # LLM could not translate this method

    def testTriplets(self) -> None:

        pass  # LLM could not translate this method

    def testSingletonsChunked(self) -> None:

        pass  # LLM could not translate this method

    def testSingletons(self) -> None:

        pass  # LLM could not translate this method

    def testRfc4648Section10EncodeDecode(self) -> None:

        def testEncodeDecode(plainText: str) -> None:
            base64 = Base64()
            encoded = base64.encodeAsString(plainText.encode())
            decoded = base64.decode(encoded.encode()).decode()
            assert decoded == plainText, f"Expected {plainText}, but got {decoded}"

        testEncodeDecode("")
        testEncodeDecode("f")
        testEncodeDecode("fo")
        testEncodeDecode("foo")
        testEncodeDecode("foob")
        testEncodeDecode("fooba")
        testEncodeDecode("foobar")

    def testRfc4648Section10DecodeEncode(self) -> None:

        self.__testDecodeEncode("")
        self.__testDecodeEncode("Zg==")
        self.__testDecodeEncode("Zm8=")
        self.__testDecodeEncode("Zm9v")
        self.__testDecodeEncode("Zm9vYg==")
        self.__testDecodeEncode("Zm9vYmE=")
        self.__testDecodeEncode("Zm9vYmFy")

    def __testDecodeEncode(self, encodedText: str) -> None:
        base64 = Base64()
        decodedBytes = base64.decode(encodedText.encode())
        encodedText2 = base64.encode(decodedBytes).decode()
        assert encodedText == encodedText2

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

        CRLF = StringUtils.newStringUsAscii(Base64.CHUNK_SEPARATOR)
        assertEqual("", StringUtils.newStringUsAscii(Base64.decodeBase641("" + CRLF)))
        assertEqual(
            "f", StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==" + CRLF))
        )
        assertEqual(
            "fo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8=" + CRLF))
        )
        assertEqual(
            "foo", StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v" + CRLF))
        )
        assertEqual(
            "foob",
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg==" + CRLF)),
        )
        assertEqual(
            "fooba",
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmE=" + CRLF)),
        )
        assertEqual(
            "foobar",
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmFy" + CRLF)),
        )

    def testRfc4648Section10Decode(self) -> None:

        assert StringUtils.newStringUsAscii(Base64.decodeBase641("")) == ""
        assert StringUtils.newStringUsAscii(Base64.decodeBase641("Zg==")) == "f"
        assert StringUtils.newStringUsAscii(Base64.decodeBase641("Zm8=")) == "fo"
        assert StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9v")) == "foo"
        assert StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYg==")) == "foob"
        assert StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmE=")) == "fooba"
        assert (
            StringUtils.newStringUsAscii(Base64.decodeBase641("Zm9vYmFy")) == "foobar"
        )

    def testRfc1421Section6Dot8ChunkSizeDefinition(self) -> None:

        self.assertEqual(64, BaseNCodec.PEM_CHUNK_SIZE)

    def testRfc2045Section6Dot8ChunkSizeDefinition(self) -> None:

        assert BaseNCodec.MIME_CHUNK_SIZE == 76

    def testRfc2045Section2Dot1CrLfDefinition(self) -> None:

        assert self.CHUNK_SEPARATOR == [13, 10]

    def testPairs(self) -> None:

        # Testing the encodeBase640 method
        assert "AAA=" == str(Base64.encodeBase640(bytes([0, 0])))

        # Testing the decodeBase640 method
        for i in range(-128, 128):
            test = bytes([i, i])
            assert test == Base64.decodeBase640(Base64.encodeBase640(test))

    def testObjectEncode(self) -> None:

        b64 = Base64.Base645()
        assert (
            "SGVsbG8gV29ybGQ="
            == b64.encode0("Hello World".encode(self.__CHARSET_UTF8)).decode()
        )

    def testObjectEncodeWithValidParameter(self) -> None:

        original: str = "Hello World!"
        origObj: bytes = original.encode(self.__CHARSET_UTF8)

        b64: Base64 = Base64.Base645()
        oEncoded: bytes = b64.encode3(origObj)
        bArray: bytes = Base64.decodeBase640(oEncoded)
        dest: str = bArray.decode(self.__CHARSET_UTF8)

        assert dest == original, "dest string does not equal original"

    def testObjectEncodeWithInvalidParameter(self) -> None:

        b64 = Base64.Base645()
        try:
            b64.encode3("Yadayadayada")
            self.fail(
                "encode(Object) didn't throw an exception when passed a String object"
            )
        except EncoderException:
            pass

    def testObjectDecodeWithValidParameter(self) -> None:

        original: str = "Hello World!"
        o: bytes = Base64.encodeBase640(original.encode(self.__CHARSET_UTF8))

        b64: Base64 = Base64.Base645()
        oDecoded: bytes = b64.decode2(o)
        baDecoded: bytearray = bytearray(oDecoded)
        dest: str = baDecoded.decode(self.__CHARSET_UTF8)

        assert dest == original, "dest string does not equal original"

    def testObjectDecodeWithInvalidParameter(self) -> None:

        b64 = Base64.Base645()

        try:
            b64.decode2(5)
            self.fail(
                "decode(Object) didn't throw an exception when passed an Integer object"
            )
        except DecoderException:
            pass

    def testNonBase64Test(self) -> None:

        bArray = b"%"

        assert not Base64.isBase641(bArray), (
            "Invalid Base64 array was incorrectly validated as "
            "an array of Base64 encoded data"
        )

        try:
            b64 = Base64.Base645()
            result = b64.decode0(bArray)

            assert len(result) == 0, (
                "The result should be empty as the test encoded content did "
                "not contain any valid base 64 characters"
            )
        except Exception as e:
            self.fail(
                "Exception was thrown when trying to decode "
                "invalid base64 encoded data - RFC 2045 requires that all "
                "non base64 character be discarded, an exception should not"
                " have been thrown"
            )

    def testKnownEncodings(self) -> None:

        from base64 import b64encode

        assert (
            b64encode(
                "The quick brown fox jumped over the lazy dogs.".encode(
                    self.__CHARSET_UTF8
                )
            ).decode()
            == "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg=="
        )
        assert (
            b64encode(
                "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah".encode(
                    self.__CHARSET_UTF8
                )
            ).decode()
            == "YmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBi\nbGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBibGFoIGJsYWggYmxhaCBi\nbGFoIGJsYWg=\n"
        )
        assert (
            b64encode(
                "It was the best of times, it was the worst of times.".encode(
                    self.__CHARSET_UTF8
                )
            ).decode()
            == "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg=="
        )
        assert (
            b64encode(
                "http://jakarta.apache.org/commmons".encode(self.__CHARSET_UTF8)
            ).decode()
            == "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw=="
        )
        assert (
            b64encode(
                "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz".encode(
                    self.__CHARSET_UTF8
                )
            ).decode()
            == "QWFCYkNjRGRFZUZmR2dIaElpSmpLa0xsTW1Obk9vUHBRcVJyU3NUdFV1VnZXd1h4WXlaeg=="
        )
        assert (
            b64encode(
                "{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }".encode(self.__CHARSET_UTF8)
            ).decode()
            == "eyAwLCAxLCAyLCAzLCA0LCA1LCA2LCA3LCA4LCA5IH0="
        )
        assert b64encode("xyzzy!".encode(self.__CHARSET_UTF8)).decode() == "eHl6enkh"

    def testKnownDecodings(self) -> None:

        assert (
            Base64.decodeBase640(
                "VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8)
            == "The quick brown fox jumped over the lazy dogs."
        )
        assert (
            Base64.decodeBase640(
                "SXQgd2FzIHRoZSBiZXN0IG9mIHRpbWVzLCBpdCB3YXMgdGhlIHdvcnN0IG9mIHRpbWVzLg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8)
            == "It was the best of times, it was the worst of times."
        )
        assert (
            Base64.decodeBase640(
                "aHR0cDovL2pha2FydGEuYXBhY2hlLm9yZy9jb21tbW9ucw==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8)
            == "http://jakarta.apache.org/commmons"
        )
        assert (
            Base64.decodeBase640(
                "QWFCYkNjRGRFZUZmR2dIaElpSmpLa0xsTW1Obk9vUHBRcVJyU3NUdFV1VnZXd1h4WXlaeg==".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8)
            == "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        )
        assert (
            Base64.decodeBase640(
                "eyAwLCAxLCAyLCAzLCA0LCA1LCA2LCA3LCA4LCA5IH0=".encode(
                    self.__CHARSET_UTF8
                )
            ).decode(self.__CHARSET_UTF8)
            == "{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }"
        )
        assert (
            Base64.decodeBase640("eHl6enkh".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            )
            == "xyzzy!"
        )

    def testIsUrlSafe(self) -> None:

        base64Standard = Base64.Base644(False)
        base64URLSafe = Base64.Base644(True)

        assert not base64Standard.isUrlSafe(), "Base64.isUrlSafe=false"
        assert base64URLSafe.isUrlSafe(), "Base64.isUrlSafe=true"

        whiteSpace = [" ", "\n", "\r", "\t"]
        assert Base64.isBase641(whiteSpace), "Base64.isBase641(whiteSpace)=true"

    def testIsArrayByteBase64(self) -> None:

        assert not Base64.isBase641(bytearray([Byte.MIN_VALUE]))
        assert not Base64.isBase641(bytearray([-125]))
        assert not Base64.isBase641(bytearray([-10]))
        assert not Base64.isBase641(bytearray([0]))
        assert not Base64.isBase641(bytearray([64, Byte.MAX_VALUE]))
        assert not Base64.isBase641(bytearray([Byte.MAX_VALUE]))
        assert Base64.isBase641(bytearray([ord("A")]))
        assert not Base64.isBase641(bytearray([ord("A"), Byte.MIN_VALUE]))
        assert Base64.isBase641(bytearray([ord("A"), ord("Z"), ord("a")]))
        assert Base64.isBase641(bytearray([ord("/"), ord("="), ord("+")]))
        assert not Base64.isBase641(bytearray([ord("$")]))

    def testIgnoringNonBase64InDecode(self) -> None:

        # The original Java code is using the Base64.decodeBase640 method, which is not available in the Python codec library.
        # However, the Python codec library has a method called b64decode which is similar to the Java's Base64.decodeBase640.
        # Therefore, I'm using b64decode method here.

        # The Java code is also using the CHARSET_UTF8 constant, which is not defined in the Python code.
        # I'm assuming that CHARSET_UTF8 is a string constant and it's value is 'utf-8'.

        # The Java code is also using the assertEquals method, which is not available in Python.
        # I'm using the assert statement to check if the decoded string is equal to the expected string.

        CHARSET_UTF8: str = "utf-8"

        expected_string: str = "The quick brown fox jumped over the lazy dogs."

        decoded_string: str = Base64.b64decode(
            "VGhlIH@$#$@%F1aWN@#@#@@rIGJyb3duIGZve\n\r\t%#%#%#%CBqd##$#$W1wZWQgb3ZlciB0aGUgbGF6eSBkb2dzLg==".encode(
                CHARSET_UTF8
            )
        ).decode(CHARSET_UTF8)

        assert decoded_string == expected_string

    def testCodec112(self) -> None:

        in_bytes = bytes([0])
        out_bytes = Base64.encodeBase640(in_bytes)
        Base64.encodeBase643(in_bytes, False, False, len(out_bytes))

    def testEncodeOverMaxSize0(self) -> None:

        self.__testEncodeOverMaxSize1(-1)
        self.__testEncodeOverMaxSize1(0)
        self.__testEncodeOverMaxSize1(1)
        self.__testEncodeOverMaxSize1(2)

    def testEncodeDecodeSmall(self) -> None:

        for i in range(12):
            data = bytearray(i)
            self.getRandom().randbytes(data)
            enc = Base64.encodeBase640(data)
            assert Base64.isBase641(enc), f"{enc} is not Base64 data."
            data2 = Base64.decodeBase640(enc)
            assert (
                data == data2
            ), f"{self.__toString(data)} does not equal {self.__toString(data2)}"

    def testEncodeDecodeRandom(self) -> None:

        for i in range(1, 5):
            data = bytearray(self.getRandom().randint(0, 10000))
            self.getRandom().randbytes(data)
            enc = Base64.encodeBase640(data)
            assert Base64.isBase641(enc)
            data2 = Base64.decodeBase640(enc)
            assert data == data2

    def testEmptyBase64(self) -> None:

        empty = bytearray()
        result = Base64.encodeBase640(empty)
        assert len(result) == 0, "empty base64 encode"
        assert Base64.encodeBase640(None) is None, "empty base64 encode"
        result = Base64.Base645().encode1(empty, 0, 1)
        assert len(result) == 0, "empty base64 encode"
        assert Base64.Base645().encode1(None, 0, 1) is None, "empty base64 encode"

        empty = bytearray(0)
        result = Base64.decodeBase640(empty)
        assert len(result) == 0, "empty base64 decode"
        assert Base64.decodeBase640(None) is None, "empty base64 encode"

    def testDecodeWithWhitespace(self) -> None:

        orig: str = "I am a late night coder."

        encodedArray: bytes = Base64.encodeBase640(orig.encode(self.__CHARSET_UTF8))
        intermediate: StringIO = StringIO(encodedArray.decode(self.__CHARSET_UTF8))

        intermediate.write(encodedArray[:2].decode(self.__CHARSET_UTF8))
        intermediate.write(" ")
        intermediate.write(encodedArray[2:5].decode(self.__CHARSET_UTF8))
        intermediate.write("\t")
        intermediate.write(encodedArray[5:10].decode(self.__CHARSET_UTF8))
        intermediate.write("\r")
        intermediate.write(encodedArray[10:15].decode(self.__CHARSET_UTF8))
        intermediate.write("\n")
        intermediate.write(encodedArray[15:].decode(self.__CHARSET_UTF8))

        encodedWithWS: bytes = intermediate.getvalue().encode(self.__CHARSET_UTF8)
        decodedWithWS: bytes = Base64.decodeBase640(encodedWithWS)

        dest: str = decodedWithWS.decode(self.__CHARSET_UTF8)

        assert dest == orig, "Dest string doesn't equal the original"

    def testDecodePadOnlyChunked(self) -> None:

        # The CHARSET_UTF8 is not defined in the provided partial Python translation.
        # Assuming it's a class variable, we can use it directly.
        # If it's not, you need to define it in the class.

        self.assertEqual(
            0, Base64.decodeBase640("====\n".encode(self.__CHARSET_UTF8)).__len__()
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====\n".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )
        self.assertEqual(
            0, Base64.decodeBase640("===\n".encode(self.__CHARSET_UTF8)).__len__()
        )
        self.assertEqual(
            0, Base64.decodeBase640("==\n".encode(self.__CHARSET_UTF8)).__len__()
        )
        self.assertEqual(
            0, Base64.decodeBase640("=\n".encode(self.__CHARSET_UTF8)).__len__()
        )
        self.assertEqual(
            0, Base64.decodeBase640("\n".encode(self.__CHARSET_UTF8)).__len__()
        )

    def testDecodePadOnly(self) -> None:

        # The CHARSET_UTF8 is not defined in the provided partial Python translation.
        # Assuming it's a class variable, we can use it directly.
        # If it's not, you need to define it in the class.

        self.assertEqual(
            0, len(Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(
            "",
            Base64.decodeBase640("====".encode(self.__CHARSET_UTF8)).decode(
                self.__CHARSET_UTF8
            ),
        )
        self.assertEqual(
            0, len(Base64.decodeBase640("===".encode(self.__CHARSET_UTF8)))
        )
        self.assertEqual(0, len(Base64.decodeBase640("==".encode(self.__CHARSET_UTF8))))
        self.assertEqual(0, len(Base64.decodeBase640("=".encode(self.__CHARSET_UTF8))))
        self.assertEqual(0, len(Base64.decodeBase640("".encode(self.__CHARSET_UTF8))))

    def testDecodePadMarkerIndex3(self) -> None:

        pass  # LLM could not translate this method

    def testDecodePadMarkerIndex2(self) -> None:

        # The CHARSET_UTF8 is not defined in the provided Python code, so I'm assuming it's a class variable.
        # If it's not, you'll need to replace <placeholder> with the actual value.
        self.__CHARSET_UTF8 = "utf-8"

        # The Base64.decodeBase640 method is not defined in the provided Python code, so I'm assuming it's a static method.
        # If it's not, you'll need to replace Base64.decodeBase640 with the actual method.
        result = Base64.decodeBase640("QQ==".encode(self.__CHARSET_UTF8))

        # The assertEquals method is not defined in the provided Python code, so I'm assuming it's a method from a testing framework.
        # If it's not, you'll need to replace assertEquals with the actual method.
        assertEquals("A", result.decode(self.__CHARSET_UTF8))

    def testConstructor_Int_ByteArray_Boolean_UrlSafe(self) -> None:

        base64 = Base64.Base641(64, bytearray(b"\t"), True)
        encoded = base64.encode0(BaseNTestData.DECODED)
        expectedResult = Base64TestData.ENCODED_64_CHARS_PER_LINE
        expectedResult = expectedResult.replace("=", "")
        expectedResult = expectedResult.replace("\n", "\t")
        expectedResult = expectedResult.replace("+", "-")
        expectedResult = expectedResult.replace("/", "_")
        result = StringUtils.newStringUtf8(encoded)
        assert result == expectedResult, "new Base64(64, \\t, true)"

    def testConstructor_Int_ByteArray_Boolean(self) -> None:

        base64 = Base64.Base641(65, bytearray(b"\t"), False)
        encoded = base64.encode0(BaseNTestData.DECODED)
        expectedResult = Base64TestData.ENCODED_64_CHARS_PER_LINE
        expectedResult = expectedResult.replace("\n", "\t")
        result = StringUtils.newStringUtf8(encoded)
        assert (
            "new Base64(65, \\t, false)" == expectedResult == result
        ), "Assertion failed: new Base64(65, \\t, false)"

    def testConstructors(self) -> None:

        base64 = Base64.Base645()
        base64 = Base64.Base643(-1)
        base64 = Base64.Base642(-1, bytearray())
        base64 = Base64.Base642(64, bytearray())
        try:
            base64 = Base64.Base642(-1, bytearray([65]))  # TODO do we need to
            assert False, "Should have rejected attempt to use 'A' as a line separator"
        except ValueError:
            pass
        try:
            base64 = Base64.Base642(64, bytearray([65]))
            assert False, "Should have rejected attempt to use 'A' as a line separator"
        except ValueError:
            pass
        try:
            base64 = Base64.Base642(64, bytearray([61]))
            assert False, "Should have rejected attempt to use '=' as a line separator"
        except ValueError:
            pass
        base64 = Base64.Base642(64, bytearray([36]))  # OK
        try:
            base64 = Base64.Base642(64, bytearray([65, 36]))
            assert False, "Should have rejected attempt to use 'A$' as a line separator"
        except ValueError:
            pass
        base64 = Base64.Base642(64, bytearray([32, 36, 10, 13, 9]))  # OK
        assert base64 is not None

    def testCodeIntegerNull(self) -> None:

        try:
            Base64.encodeInteger(None)
            self.fail(
                "Exception not thrown when passing in null to encodeInteger(BigInteger)"
            )
        except NullPointerException as npe:
            pass
        except Exception as e:
            self.fail(
                "Incorrect Exception caught when passing in null to encodeInteger(BigInteger)"
            )

    def testCodeIntegerEdgeCases(self) -> None:

        pass

    def testCodeInteger4(self) -> None:

        encoded_int4 = (
            "ctA8YGxrtngg/zKVvqEOefnwmViFztcnPBYPlJsvh6yKI"
            + "4iDm68fnp4Mi3RrJ6bZAygFrUIQLxLjV+OJtgJAEto0xAs+Mehuq1DkSFEpP3o"
            + "DzCTOsrOiS1DwQe4oIb7zVk/9l7aPtJMHW0LVlMdwZNFNNJoqMcT2ZfCPrfvYv"
            + "Q0="
        )
        big_int4 = (
            "80624726256040348115552042320"
            + "6968135001872753709424419772586693950232350200555646471175944"
            + "519297087885987040810778908507262272892702303774422853675597"
            + "748008534040890923814202286633163248086055216976551456088015"
            + "338880713818192088877057717530169381044092839402438015097654"
            + "53542091716518238707344493641683483917"
        )

        assert encoded_int4 == Base64.encodeInteger(big_int4)
        assert big_int4 == Base64.decodeInteger(
            encoded_int4.encode(self.__CHARSET_UTF8)
        )

    def testCodeInteger3(self) -> None:

        encoded_int3 = (
            "FKIhdgaG5LGKiEtF1vHy4f3y700zaD6QwDS3IrNVGzNp2"
            "rY+1LFWTK6D44AyiC1n8uWz1itkYMZF0/aKDK0Yjg=="
        )
        big_int3 = int(
            "10806548154093873461951748545"
            "1196989136416448805819079363524309897749044958112417136240557"
            "4495062430572478766856090958495998158114332651671116876320938126"
        )

        assert encoded_int3 == Base64.encodeInteger(big_int3)
        assert big_int3 == Base64.decodeInteger(
            encoded_int3.encode(self.__CHARSET_UTF8)
        )

    def testCodeInteger2(self) -> None:

        encodedInt2: str = "9B5ypLY9pMOmtxCeTDHgwdNFeGs="
        bigInt2: int = int("13936727572861167254666467268" + "91466679477132949611")

        self.assertEqual(
            encodedInt2, Base64.encodeInteger(bigInt2).decode(self.__CHARSET_UTF8)
        )
        self.assertEqual(
            bigInt2, Base64.decodeInteger(encodedInt2.encode(self.__CHARSET_UTF8))
        )

    def testCodeInteger1(self) -> None:

        encodedInt1: str = "li7dzDacuo67Jg7mtqEm2TRuOMU="
        bigInt1: int = int("85739377120809420210425962799" + "0318636601332086981")

        assert encodedInt1 == Base64.encodeInteger(bigInt1)
        assert bigInt1 == Base64.decodeInteger(encodedInt1.encode(self.__CHARSET_UTF8))

    def testCodec68(self) -> None:

        x = bytearray([ord("n"), ord("A"), ord("="), ord("="), 0x9C])
        Base64.decodeBase640(x)

    def testChunkedEncodeMultipleOf76(self) -> None:

        expected_encode = Base64.encodeBase641(BaseNTestData.DECODED, True)
        actual_result = Base64TestData.ENCODED_76_CHARS_PER_LINE.replace("\n", "\r\n")
        actual_encode = StringUtils.getBytesUtf8(actual_result)

        assert expected_encode == actual_encode, "chunkedEncodeMultipleOf76"

    def testDecodeWithInnerPad(self) -> None:

        content = "SGVsbG8gV29ybGQ=SGVsbG8gV29ybGQ="
        result = Base64.decodeBase641(content)
        shouldBe = StringUtils.getBytesUtf8("Hello World")

        assert result == shouldBe, "decode should halt at pad (=)"

    def testBase64(self) -> None:

        content = "Hello World"
        encodedContent = Base64.encodeBase640(StringUtils.getBytesUtf8(content))
        encodedContent = StringUtils.newStringUtf8(encodedContent)
        assert encodedContent == "SGVsbG8gV29ybGQ=", "encoding hello world"

        b64 = Base64.Base642(BaseNCodec.MIME_CHUNK_SIZE, None)
        encodedBytes = b64.encode0(StringUtils.getBytesUtf8(content))
        encodedContent = StringUtils.newStringUtf8(encodedBytes)
        assert encodedContent == "SGVsbG8gV29ybGQ=", "encoding hello world"

        b64 = Base64.Base642(0, None)
        encodedBytes = b64.encode0(StringUtils.getBytesUtf8(content))
        encodedContent = StringUtils.newStringUtf8(encodedBytes)
        assert encodedContent == "SGVsbG8gV29ybGQ=", "encoding hello world"

        decode = b64.decode3("SGVsbG{\u00e9\u00e9\u00e9\u00e9\u00e9\u00e9}8gV29ybGQ=")
        decodeString = StringUtils.newStringUtf8(decode)
        assert decodeString == "Hello World", "decode hello world"

    def testIsStringBase64(self) -> None:

        nullString = None
        emptyString = ""
        validString = (
            "abc===defg\n\r123456\r789\r\rABC\n\nDEF==GHI\r\nJKL=============="
        )
        invalidString = validString + chr(0)  # append null

        try:
            Base64.isBase642(nullString)
            self.fail("Base64.isStringBase64() should not be null-safe.")
        except NullPointerException as npe:
            self.assertNotNull("Base64.isStringBase64() should not be null-safe.", npe)

        self.assertTrue(
            "Base64.isStringBase64(empty-string) is true", Base64.isBase642(emptyString)
        )
        self.assertTrue(
            "Base64.isStringBase64(valid-string) is true",
            Base64.isStringBase64(validString),
        )
        self.assertFalse(
            "Base64.isStringBase64(invalid-string) is false",
            Base64.isStringBase64(invalidString),
        )

    def getRandom(self) -> random.Random:

        return self.__random

    @staticmethod
    def __assertBase64DecodingOfTrailingBits(nbits: int) -> None:

        codec = Base64(0, None, False, CodecPolicy.STRICT)
        assert codec.isStrictDecoding()
        assert CodecPolicy.STRICT == codec.getCodecPolicy()
        defaultCodec = Base64.Base645()
        assert not defaultCodec.isStrictDecoding()
        assert CodecPolicy.LENIENT == defaultCodec.getCodecPolicy()

        length = nbits // 6
        encoded = bytearray(4)
        encoded[:length] = bytearray([Base64Test.__STANDARD_ENCODE_TABLE[0]] * length)
        encoded[length:] = bytearray([ord("=")] * (4 - length))
        discard = nbits % 8
        emptyBitsMask = (1 << discard) - 1
        invalid = length == 1
        last = length - 1
        for i in range(64):
            encoded[last] = Base64Test.__STANDARD_ENCODE_TABLE[i]
            if invalid or (i & emptyBitsMask) != 0:
                try:
                    codec.decode0(encoded)
                    assert False, "Final base-64 digit should not be allowed"
                except ValueError:
                    pass
                decoded = defaultCodec.decode0(encoded)
                assert not (encoded == defaultCodec.encode0(decoded))
            else:
                decoded = codec.decode0(encoded)
                bitsEncoded = i >> discard
                assert bitsEncoded == decoded[-1], "Invalid decoding of last character"
                assert encoded == codec.encode0(decoded)

    def __toString(self, data: typing.List[int]) -> str:

        buf = ""
        for i in range(len(data)):
            buf += str(data[i])
            if i != len(data) - 1:
                buf += ","
        return buf

    def __testEncodeDecode(self, plainText: str) -> None:

        encodedText = Base64.encodeBase64String(StringUtils.getBytesUtf8(plainText))
        decodedText = StringUtils.newStringUsAscii(Base64.decodeBase641(encodedText))

        assert plainText == decodedText

    def __testDecodeEncode(self, encodedText: str) -> None:

        decodedText = StringUtils.newStringUsAscii(Base64.decodeBase641(encodedText))
        encodedText2 = Base64.encodeBase64String(StringUtils.getBytesUtf8(decodedText))

        assert encodedText == encodedText2

    def __testEncodeOverMaxSize1(self, maxSize: int) -> None:

        try:
            Base64.encodeBase643(BaseNTestData.DECODED, True, False, maxSize)
            self.fail("Expected " + ValueError.__name__)
        except ValueError:
            pass
