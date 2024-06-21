from __future__ import annotations
import re
import random
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.binary.Base16 import *
from src.test.org.apache.commons.codec.binary.Base16TestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base16Test(unittest.TestCase):

    __random: random.Random = random.Random()

    __CHARSET_UTF8: str = "UTF-8"

    def testLenientDecoding(self) -> None:

        encoded = "aabbccdde"

        b16 = Base16(True, CodecPolicy.LENIENT)
        assert b16.getCodecPolicy() == CodecPolicy.LENIENT

        decoded = b16.decode0(StringUtils.getBytesUtf8(encoded))
        assert decoded == [0xAA, 0xBB, 0xCC, 0xDD]

    def testStrictDecoding(self) -> None:

        encoded = "aabbccdde"

        b16 = Base16(True, CodecPolicy.STRICT)
        assert CodecPolicy.STRICT == b16.getCodecPolicy()
        b16.decode0(StringUtils.getBytesUtf8(encoded))

    def testDecodeSingleBytesOptimisation(self) -> None:

        context = Context()
        assert context.ibitWorkArea == 0
        assert context.buffer is None

        data = bytearray(1)

        b16 = Base16.Base162()

        data[0] = ord("E")
        b16.decode1(data, 0, 1, context)
        assert context.ibitWorkArea == 15
        assert context.buffer is None

        data[0] = ord("F")
        b16.decode1(data, 0, 1, context)
        assert context.ibitWorkArea == 0

        assert context.buffer[0] == 0xEF

    def testDecodeSingleBytes(self) -> None:

        encoded = "556E74696C206E6578742074696D6521"

        context = Context()
        b16 = Base16.Base162()

        encoded_bytes = StringUtils.getBytesUtf8(encoded)

        b16.decode1(encoded_bytes, 0, 1, context)
        b16.decode1(encoded_bytes, 1, 1, context)  # yields "U"
        b16.decode1(encoded_bytes, 2, 1, context)
        b16.decode1(encoded_bytes, 3, 1, context)  # yields "n"

        b16.decode1(encoded_bytes, 4, 3, context)  # yields "t"
        b16.decode1(encoded_bytes, 7, 3, context)  # yields "il"
        b16.decode1(encoded_bytes, 10, 3, context)  # yields " "

        b16.decode1(encoded_bytes, 13, 19, context)  # yields "next time!"

        decoded_bytes = bytearray(context.pos)
        decoded_bytes[:] = context.buffer[
            context.readPos : context.readPos + context.pos
        ]
        decoded = StringUtils.newStringUtf8(decoded_bytes)

        assert decoded == "Until next time!"

    def testIsInAlphabet(self) -> None:

        b16 = Base16.Base161(True)
        assert not b16.isInAlphabet0(0)
        assert not b16.isInAlphabet0(1)
        assert not b16.isInAlphabet0(-1)
        assert not b16.isInAlphabet0(-15)
        assert not b16.isInAlphabet0(-16)
        assert not b16.isInAlphabet0(128)
        assert not b16.isInAlphabet0(255)

        b16 = Base16.Base161(True)
        for c in range(ord("0"), ord("9") + 1):
            assert b16.isInAlphabet0(c)
        for c in range(ord("a"), ord("f") + 1):
            assert b16.isInAlphabet0(c)
        for c in range(ord("A"), ord("F") + 1):
            assert not b16.isInAlphabet0(c)
        assert not b16.isInAlphabet0(ord("0") - 1)
        assert not b16.isInAlphabet0(ord("9") + 1)
        assert not b16.isInAlphabet0(ord("a") - 1)
        assert not b16.isInAlphabet0(ord("f") + 1)
        assert not b16.isInAlphabet0(ord("z") + 1)

        b16 = Base16.Base161(False)
        for c in range(ord("0"), ord("9") + 1):
            assert b16.isInAlphabet0(c)
        for c in range(ord("a"), ord("f") + 1):
            assert not b16.isInAlphabet0(c)
        for c in range(ord("A"), ord("F") + 1):
            assert b16.isInAlphabet0(c)
        assert not b16.isInAlphabet0(ord("0") - 1)
        assert not b16.isInAlphabet0(ord("9") + 1)
        assert not b16.isInAlphabet0(ord("A") - 1)
        assert not b16.isInAlphabet0(ord("F") + 1)
        assert not b16.isInAlphabet0(ord("Z") + 1)

    def checkEncodeLengthBounds(self) -> None:

        base16 = Base16.Base162()
        base16.encode1(bytearray(10), 0, 1 << 30)

    def testStringToByteVariations(self) -> None:

        base16 = Base16.Base162()
        s1 = "48656C6C6F20576F726C64"
        s2 = ""
        s3 = None

        assert StringUtils.newStringUtf8(base16.decode3(s1)) == "Hello World"
        assert StringUtils.newStringUtf8(base16.decode2(s1)) == "Hello World"
        assert StringUtils.newStringUtf8(base16.decode3(s1)) == "Hello World"
        assert StringUtils.newStringUtf8(base16.decode3(s2)) == ""
        assert StringUtils.newStringUtf8(base16.decode3(s2)) == ""
        assert StringUtils.newStringUtf8(base16.decode3(s3)) == None
        assert StringUtils.newStringUtf8(base16.decode3(s3)) == None

    def testByteToStringVariations(self) -> None:

        base16 = Base16.Base162()
        b1 = StringUtils.getBytesUtf8("Hello World")
        b2 = bytearray()
        b3 = None

        assert (
            base16.encodeToString(b1) == "48656C6C6F20576F726C64"
        ), "byteToString Hello World"
        assert (
            StringUtils.newStringUtf8(base16.encode0(b1)) == "48656C6C6F20576F726C64"
        ), "byteToString static Hello World"
        assert base16.encodeToString(b2) == "", 'byteToString ""'
        assert (
            StringUtils.newStringUtf8(base16.encode0(b2)) == ""
        ), 'byteToString static ""'
        assert base16.encodeToString(b3) is None, "byteToString null"
        assert (
            StringUtils.newStringUtf8(base16.encode0(b3)) is None
        ), "byteToString static null"

    def testTriplets(self) -> None:

        def check_equal(expected, actual):
            assert expected == actual, f"Expected {expected}, but got {actual}"

        check_equal("000000", Base16.Base162().encode0(bytearray([0, 0, 0])).decode())
        check_equal("000001", Base16.Base162().encode0(bytearray([0, 0, 1])).decode())
        check_equal("000002", Base16.Base162().encode0(bytearray([0, 0, 2])).decode())
        check_equal("000003", Base16.Base162().encode0(bytearray([0, 0, 3])).decode())
        check_equal("000004", Base16.Base162().encode0(bytearray([0, 0, 4])).decode())
        check_equal("000005", Base16.Base162().encode0(bytearray([0, 0, 5])).decode())
        check_equal("000006", Base16.Base162().encode0(bytearray([0, 0, 6])).decode())
        check_equal("000007", Base16.Base162().encode0(bytearray([0, 0, 7])).decode())
        check_equal("000008", Base16.Base162().encode0(bytearray([0, 0, 8])).decode())
        check_equal("000009", Base16.Base162().encode0(bytearray([0, 0, 9])).decode())
        check_equal("00000A", Base16.Base162().encode0(bytearray([0, 0, 10])).decode())
        check_equal("00000B", Base16.Base162().encode0(bytearray([0, 0, 11])).decode())
        check_equal("00000C", Base16.Base162().encode0(bytearray([0, 0, 12])).decode())
        check_equal("00000D", Base16.Base162().encode0(bytearray([0, 0, 13])).decode())
        check_equal("00000E", Base16.Base162().encode0(bytearray([0, 0, 14])).decode())
        check_equal("00000F", Base16.Base162().encode0(bytearray([0, 0, 15])).decode())

    def testSingletons(self) -> None:

        def assert_equal(expected: str, actual: str) -> None:
            assert expected == actual, f"Expected: {expected}, Actual: {actual}"

        def assert_array_equal(expected: bytearray, actual: bytearray) -> None:
            assert expected == actual, f"Expected: {expected}, Actual: {actual}"

        for i in range(0, 10):
            assert_equal(f"0{i}", Base16.Base162().encode0(bytearray([i])))

        for i in range(10, 36):
            assert_equal(
                f"{hex(i)[2:].upper()}", Base16.Base162().encode0(bytearray([i]))
            )

        for i in range(36, 62):
            assert_equal(
                f"{hex(i)[2:].upper()}", Base16.Base162().encode0(bytearray([i]))
            )

        for i in range(-128, 128):
            test = bytearray([i])
            assert_array_equal(
                test, Base16.Base162().decode0(Base16.Base162().encode0(test))
            )

    def testPairs(self) -> None:

        def assertEqual(expected, actual):
            assert expected == actual, f"Expected {expected}, but got {actual}"

        def assertArrayEquals(expected, actual):
            assert expected == actual, f"Expected {expected}, but got {actual}"

        assertEqual("0000", str(Base16.Base162().encode0(bytes([0, 0])), "utf-8"))
        assertEqual("0001", str(Base16.Base162().encode0(bytes([0, 1])), "utf-8"))
        assertEqual("0002", str(Base16.Base162().encode0(bytes([0, 2])), "utf-8"))
        assertEqual("0003", str(Base16.Base162().encode0(bytes([0, 3])), "utf-8"))
        assertEqual("0004", str(Base16.Base162().encode0(bytes([0, 4])), "utf-8"))
        assertEqual("0005", str(Base16.Base162().encode0(bytes([0, 5])), "utf-8"))
        assertEqual("0006", str(Base16.Base162().encode0(bytes([0, 6])), "utf-8"))
        assertEqual("0007", str(Base16.Base162().encode0(bytes([0, 7])), "utf-8"))
        assertEqual("0008", str(Base16.Base162().encode0(bytes([0, 8])), "utf-8"))
        assertEqual("0009", str(Base16.Base162().encode0(bytes([0, 9])), "utf-8"))
        assertEqual("000A", str(Base16.Base162().encode0(bytes([0, 10])), "utf-8"))
        assertEqual("000B", str(Base16.Base162().encode0(bytes([0, 11])), "utf-8"))
        assertEqual("000C", str(Base16.Base162().encode0(bytes([0, 12])), "utf-8"))
        assertEqual("000D", str(Base16.Base162().encode0(bytes([0, 13])), "utf-8"))
        assertEqual("000E", str(Base16.Base162().encode0(bytes([0, 14])), "utf-8"))
        assertEqual("000F", str(Base16.Base162().encode0(bytes([0, 15])), "utf-8"))
        assertEqual("0010", str(Base16.Base162().encode0(bytes([0, 16])), "utf-8"))
        assertEqual("0011", str(Base16.Base162().encode0(bytes([0, 17])), "utf-8"))

        for i in range(-128, 128):
            test = bytes([i, i])
            assertArrayEquals(
                test, Base16.Base162().decode0(Base16.Base162().encode0(test))
            )

    def testObjectEncode(self) -> None:

        b16 = Base16.Base162()
        result = b16.encode0("Hello World".encode(self.__CHARSET_UTF8))
        assertEqual("48656C6C6F20576F726C64", result.decode(self.__CHARSET_UTF8))

    def testObjectEncodeWithValidParameter(self) -> None:

        original: str = "Hello World!"
        origObj: bytes = original.encode(self.__CHARSET_UTF8)

        oEncoded: bytes = Base16.Base162().encode3(origObj)
        bArray: bytes = Base16.Base162().decode0(oEncoded)
        dest: str = bArray.decode(self.__CHARSET_UTF8)

        assert dest == original, "dest string does not equal original"

    def testObjectEncodeWithInvalidParameter(self) -> None:

        b16 = Base16.Base162()
        try:
            b16.encode3("Yadayadayada")
            self.fail(
                "encode(Object) didn't throw an exception when passed a String object"
            )
        except EncoderException:
            pass

    def testObjectDecodeWithValidParameter(self) -> None:

        original: str = "Hello World!"
        o: object = Base16.Base162().encode0(original.encode(self.__CHARSET_UTF8))

        b16: Base16 = Base16.Base162()
        oDecoded: object = b16.decode2(o)
        baDecoded: bytearray = bytearray(oDecoded)
        dest: str = baDecoded.decode(self.__CHARSET_UTF8)

        assert dest == original, "dest string does not equal original"

    def testObjectDecodeWithInvalidParameter(self) -> None:

        b16 = Base16.Base162()

        try:
            b16.decode2(5)
            self.fail(
                "decode(Object) didn't throw an exception when passed an Integer object"
            )
        except DecoderException:
            pass

    def testNonBase16Test(self) -> None:

        pass  # LLM could not translate this method

    def testKnownEncodings(self) -> None:

        self.assertEqual(
            "54686520717569636b2062726f776e20666f78206a756d706564206f76657220746865206c617a7920646f67732e",
            Base16.Base161(True)
            .encode0(
                "The quick brown fox jumped over the lazy dogs.".encode(
                    self.__CHARSET_UTF8
                )
            )
            .decode(),
        )
        self.assertEqual(
            "497420776173207468652062657374206f662074696d65732c206974207761732074686520776f727374206f662074696d65732e",
            Base16.Base161(True)
            .encode0(
                "It was the best of times, it was the worst of times.".encode(
                    self.__CHARSET_UTF8
                )
            )
            .decode(),
        )
        self.assertEqual(
            "687474703a2f2f6a616b617274612e6170616368652e6f72672f636f6d6d6f6e73",
            Base16.Base161(True)
            .encode0("http://jakarta.apache.org/commmons".encode(self.__CHARSET_UTF8))
            .decode(),
        )
        self.assertEqual(
            "4161426243634464456546664767486849694a6a4b6b4c6c4d6d4e6e4f6f50705171527253735474557556765777587859795a7a",
            Base16.Base161(True)
            .encode0(
                "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz".encode(
                    self.__CHARSET_UTF8
                )
            )
            .decode(),
        )
        self.assertEqual(
            "7b20302c20312c20322c20332c20342c20352c20362c20372c20382c2039207d",
            Base16.Base161(True)
            .encode0("{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }".encode(self.__CHARSET_UTF8))
            .decode(),
        )
        self.assertEqual(
            "78797a7a7921",
            Base16.Base161(True).encode0("xyzzy!".encode(self.__CHARSET_UTF8)).decode(),
        )

    def testKnownDecodings(self) -> None:

        self.assertEqual(
            "The quick brown fox jumped over the lazy dogs.",
            Base16.Base161(True)
            .decode0(
                bytes.fromhex(
                    "54686520717569636b2062726f776e20666f78206a756d706564206f76657220746865206c617a7920646f67732e"
                )
            )
            .decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "It was the best of times, it was the worst of times.",
            Base16.Base161(True)
            .decode0(
                bytes.fromhex(
                    "497420776173207468652062657374206f662074696d65732c206974207761732074686520776f727374206f662074696d65732e"
                )
            )
            .decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "http://jakarta.apache.org/commmons",
            Base16.Base161(True)
            .decode0(
                bytes.fromhex(
                    "687474703a2f2f6a616b617274612e6170616368652e6f72672f636f6d6d6d6f6e73"
                )
            )
            .decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz",
            Base16.Base161(True)
            .decode0(
                bytes.fromhex(
                    "4161426243634464456546664767486849694a6a4b6b4c6c4d6d4e6e4f6f50705171527253735474557556765777587859795a7a"
                )
            )
            .decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }",
            Base16.Base161(True)
            .decode0(
                bytes.fromhex(
                    "7b20302c20312c20322c20332c20342c20352c20362c20372c20382c2039207d"
                )
            )
            .decode(self.__CHARSET_UTF8),
        )
        self.assertEqual(
            "xyzzy1",
            Base16.Base161(True)
            .decode0(bytes.fromhex("78797a7a7921"))
            .decode(self.__CHARSET_UTF8),
        )

    def testEncodeDecodeSmall(self) -> None:

        for i in range(12):
            data = bytearray(i)
            self.getRandom().randbytes(data)
            enc = Base16.Base162().encode0(data)
            data2 = Base16.Base162().decode0(enc)
            assert (
                data == data2
            ), f"{self.__toString(data)} equals {self.__toString(data2)}"

    def testEncodeDecodeRandom(self) -> None:

        for i in range(1, 5):
            len = self.getRandom().randint(1, 10000)
            data = bytearray(len)
            for j in range(len):
                data[j] = self.getRandom().randint(0, 255)
            enc = Base16.Base162().encode0(data)
            data2 = Base16.Base162().decode0(enc)
            assert data == data2

    def testEmptyBase16(self) -> None:

        empty: bytearray = bytearray()
        result: bytearray = Base16.Base162().encode0(empty)
        assert len(result) == 0, "empty Base16 encode"
        assert Base16.Base162().encode0(None) is None, "empty Base16 encode"
        result = Base16.Base162().encode1(empty, 0, 1)
        assert len(result) == 0, "empty Base16 encode with offset"
        assert Base16.Base162().encode0(None) is None, "empty Base16 encode with offset"

        empty = bytearray(0)
        result = Base16.Base162().decode0(empty)
        assert len(result) == 0, "empty Base16 decode"
        assert Base16.Base162().decode0(None) is None, "empty Base16 decode"

    def testConstructor_LowerCase_DecodingPolicy(self) -> None:

        base16 = Base16(False, CodecPolicy.STRICT)
        encoded = base16.encode0(BaseNTestData.DECODED)
        expectedResult = Base16TestData.ENCODED_UTF8_UPPERCASE
        result = StringUtils.newStringUtf8(encoded)

        assert result == expectedResult, "new base16(false, CodecPolicy.STRICT)"

    def testConstructor_LowerCase(self) -> None:

        base16 = Base16.Base161(True)
        encoded = base16.encode0(BaseNTestData.DECODED)
        expectedResult = Base16TestData.ENCODED_UTF8_LOWERCASE
        result = StringUtils.newStringUtf8(encoded)

        assert expectedResult == result, "new Base16(true)"

    def testConstructors(self) -> None:

        # Calling Base16.Base162()
        Base16.Base162()

        # Calling Base16.Base161(false)
        Base16.Base161(False)

        # Calling Base16.Base161(true)
        Base16.Base161(True)

        # Calling new Base16(false, CodecPolicy.LENIENT)
        Base16(False, CodecPolicy.LENIENT)

        # Calling new Base16(false, CodecPolicy.STRICT)
        Base16(False, CodecPolicy.STRICT)

    def testCodec68(self) -> None:

        x = bytearray(b"nH==\x9c")
        b16 = Base16.Base162()
        b16.decode0(x)

    def testBase16(self) -> None:

        content = "Hello World"
        encoded_bytes = Base16.Base162().encode0(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        assert encoded_content == "48656C6C6F20576F726C64", "encoding hello world"

        decoded_bytes = Base16.Base162().decode0(encoded_bytes)
        decoded_content = StringUtils.newStringUtf8(decoded_bytes)
        assert decoded_content == content, "decoding hello world"

    def getRandom(self) -> random.Random:

        return self.__random

    def __toString(self, data: typing.List[int]) -> str:

        buf = io.StringIO()
        for i in range(len(data)):
            buf.write(str(data[i]))
            if i != len(data) - 1:
                buf.write(",")
        return buf.getvalue()
