from __future__ import annotations
import time
import re
import random
import os
import unittest
import pytest
import io
import typing
from typing import *
import unittest
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
    __CHARSET_UTF8: str = "utf-8"

    def testLenientDecoding(self) -> None:

        encoded = "aabbccdde"

        b16 = Base16(True, CodecPolicy.LENIENT)
        self.assertEqual(CodecPolicy.LENIENT, b16.getCodecPolicy())

        decoded = b16.decode0(StringUtils.getBytesUtf8(encoded))
        self.assertListEqual([0xAA, 0xBB, 0xCC, 0xDD], decoded)

    def testStrictDecoding(self) -> None:

        encoded = "aabbccdde"

        b16 = Base16(True, CodecPolicy.STRICT)
        self.assertEqual(CodecPolicy.STRICT, b16.getCodecPolicy())
        with self.assertRaises(ValueError):
            b16.decode0(StringUtils.getBytesUtf8(encoded))

    def testDecodeSingleBytesOptimisation(self) -> None:

        context = Context()
        self.assertEqual(0, context.ibitWorkArea)
        self.assertIsNone(context.buffer)

        data = bytearray(1)

        b16 = Base16.Base162()

        data[0] = ord("E")
        b16.decode1(data, 0, 1, context)
        self.assertEqual(15, context.ibitWorkArea)
        self.assertIsNone(context.buffer)

        data[0] = ord("F")
        b16.decode1(data, 0, 1, context)
        self.assertEqual(0, context.ibitWorkArea)

        self.assertEqual(0xEF, context.buffer[0])

    def testDecodeSingleBytes(self) -> None:

        encoded = "556E74696C206E6578742074696D6521"

        context = Context()
        b16 = Base16.Base162()

        encocdedBytes = StringUtils.getBytesUtf8(encoded)

        b16.decode1(encocdedBytes, 0, 1, context)
        b16.decode1(encocdedBytes, 1, 1, context)  # yields "U"
        b16.decode1(encocdedBytes, 2, 1, context)
        b16.decode1(encocdedBytes, 3, 1, context)  # yields "n"

        b16.decode1(encocdedBytes, 4, 3, context)  # yields "t"
        b16.decode1(encocdedBytes, 7, 3, context)  # yields "il"
        b16.decode1(encocdedBytes, 10, 3, context)  # yields " "

        b16.decode1(encocdedBytes, 13, 19, context)  # yields "next time!"

        decodedBytes = [0] * context.pos
        for i in range(context.pos):
            decodedBytes[i] = context.buffer[context.readPos + i]
        decoded = StringUtils.newStringUtf8(decodedBytes)

        self.assertEqual("Until next time2", decoded)

    def testIsInAlphabet(self) -> None:

        b16 = Base16.Base161(True)
        self.assertFalse(b16.isInAlphabet0(0))
        self.assertFalse(b16.isInAlphabet0(1))
        self.assertFalse(b16.isInAlphabet0(-1))
        self.assertFalse(b16.isInAlphabet0(-15))
        self.assertFalse(b16.isInAlphabet0(-16))
        self.assertFalse(b16.isInAlphabet0(128))
        self.assertFalse(b16.isInAlphabet0(255))

        b16 = Base16.Base161(True)
        for c in range(ord("0"), ord("9") + 1):
            self.assertTrue(b16.isInAlphabet0(c))
        for c in range(ord("a"), ord("f") + 1):
            self.assertTrue(b16.isInAlphabet0(c))
        for c in range(ord("A"), ord("F") + 1):
            self.assertFalse(b16.isInAlphabet0(c))
        self.assertFalse(b16.isInAlphabet0(ord("0") - 1))
        self.assertFalse(b16.isInAlphabet0(ord("9") + 1))
        self.assertFalse(b16.isInAlphabet0(ord("a") - 1))
        self.assertFalse(b16.isInAlphabet0(ord("f") + 1))
        self.assertFalse(b16.isInAlphabet0(ord("z") + 1))

        b16 = Base16.Base161(False)
        for c in range(ord("0"), ord("9") + 1):
            self.assertTrue(b16.isInAlphabet0(c))
        for c in range(ord("a"), ord("f") + 1):
            self.assertFalse(b16.isInAlphabet0(c))
        for c in range(ord("A"), ord("F") + 1):
            self.assertTrue(b16.isInAlphabet0(c))
        self.assertFalse(b16.isInAlphabet0(ord("0") - 1))
        self.assertFalse(b16.isInAlphabet0(ord("9") + 1))
        self.assertFalse(b16.isInAlphabet0(ord("A") - 1))
        self.assertFalse(b16.isInAlphabet0(ord("F") + 1))
        self.assertFalse(b16.isInAlphabet0(ord("Z") + 1))

    def testcheckEncodeLengthBounds(self) -> None:

        base16 = Base16.Base162()
        with pytest.raises(ValueError):
            base16.encode1([0] * 10, 0, 1 << 30)

    def testStringToByteVariations(self) -> None:

        base16 = Base16.Base162()
        s1 = "48656C6C6F20576F726C64"
        s2 = ""
        s3 = None

        self.assertEqual(
            "StringToByte Hello World",
            "Hello World",
            StringUtils.newStringUtf8(base16.decode3(s1)),
        )
        self.assertEqual(
            "StringToByte Hello World",
            "Hello World",
            StringUtils.newStringUtf8(base16.decode2(s1)),
        )
        self.assertEqual(
            "StringToByte static Hello World",
            "Hello World",
            StringUtils.newStringUtf8(base16.decode3(s1)),
        )
        self.assertEqual(
            'StringToByte ""', "", StringUtils.newStringUtf8(base16.decode3(s2))
        )
        self.assertEqual(
            'StringToByte static ""', "", StringUtils.newStringUtf8(base16.decode3(s2))
        )
        self.assertIsNone(
            "StringToByte null", StringUtils.newStringUtf8(base16.decode3(s3))
        )
        self.assertIsNone(
            "StringToByte static null", StringUtils.newStringUtf8(base16.decode3(s3))
        )

    def testByteToStringVariations(self) -> None:

        base16 = Base16.Base162()
        b1 = StringUtils.getBytesUtf8("Hello World")
        b2 = []
        b3 = None

        self.assertEqual(
            "byteToString Hello World",
            "48656C6C6F20576F726C64",
            base16.encodeToString(b1),
        )
        self.assertEqual(
            "byteToString static Hello World",
            "48656C6C6F20576F726C64",
            StringUtils.newStringUtf8(Base16.Base162().encode0(b1)),
        )
        self.assertEqual('byteToString ""', "", base16.encodeToString(b2))
        self.assertEqual(
            'byteToString static ""',
            "",
            StringUtils.newStringUtf8(Base16.Base162().encode0(b2)),
        )
        self.assertIsNone("byteToString null", base16.encodeToString(b3))
        self.assertIsNone(
            "byteToString static null",
            StringUtils.newStringUtf8(Base16.Base162().encode0(b3)),
        )

    def testTriplets(self) -> None:

        self.assertEqual(
            "000000", "".join(map(chr, Base16.Base162().encode0([0, 0, 0])))
        )
        self.assertEqual(
            "000001", "".join(map(chr, Base16.Base162().encode0([0, 0, 1])))
        )
        self.assertEqual(
            "000002", "".join(map(chr, Base16.Base162().encode0([0, 0, 2])))
        )
        self.assertEqual(
            "000003", "".join(map(chr, Base16.Base162().encode0([0, 0, 3])))
        )
        self.assertEqual(
            "000004", "".join(map(chr, Base16.Base162().encode0([0, 0, 4])))
        )
        self.assertEqual(
            "000005", "".join(map(chr, Base16.Base162().encode0([0, 0, 5])))
        )
        self.assertEqual(
            "000006", "".join(map(chr, Base16.Base162().encode0([0, 0, 6])))
        )
        self.assertEqual(
            "000007", "".join(map(chr, Base16.Base162().encode0([0, 0, 7])))
        )
        self.assertEqual(
            "000008", "".join(map(chr, Base16.Base162().encode0([0, 0, 8])))
        )
        self.assertEqual(
            "000009", "".join(map(chr, Base16.Base162().encode0([0, 0, 9])))
        )
        self.assertEqual(
            "00000A", "".join(map(chr, Base16.Base162().encode0([0, 0, 10])))
        )
        self.assertEqual(
            "00000B", "".join(map(chr, Base16.Base162().encode0([0, 0, 11])))
        )
        self.assertEqual(
            "00000C", "".join(map(chr, Base16.Base162().encode0([0, 0, 12])))
        )
        self.assertEqual(
            "00000D", "".join(map(chr, Base16.Base162().encode0([0, 0, 13])))
        )
        self.assertEqual(
            "00000E", "".join(map(chr, Base16.Base162().encode0([0, 0, 14])))
        )
        self.assertEqual(
            "00000F", "".join(map(chr, Base16.Base162().encode0([0, 0, 15])))
        )

    def testSingletons(self) -> None:

        def assert_equal(expected, actual):
            assert expected == actual, f"Expected: {expected}, Actual: {actual}"

        def assert_array_equal(expected, actual):
            assert expected == actual, f"Expected: {expected}, Actual: {actual}"

        assert_equal("00", "".join(chr(i) for i in Base16.Base162().encode0([0])))
        assert_equal("01", "".join(chr(i) for i in Base16.Base162().encode0([1])))
        assert_equal("02", "".join(chr(i) for i in Base16.Base162().encode0([2])))
        # ...
        assert_equal("67", "".join(chr(i) for i in Base16.Base162().encode0([103])))
        assert_equal("68", "".join(chr(i) for i in Base16.Base162().encode0([104])))

        for i in range(-128, 128):
            test = [i]
            assert_array_equal(
                test, Base16.Base162().decode0(Base16.Base162().encode0(test))
            )

    def testPairs(self) -> None:

        self.assertEqual("0000", "".join(map(chr, Base16.Base162().encode0([0, 0]))))
        self.assertEqual("0001", "".join(map(chr, Base16.Base162().encode0([0, 1]))))
        self.assertEqual("0002", "".join(map(chr, Base16.Base162().encode0([0, 2]))))
        self.assertEqual("0003", "".join(map(chr, Base16.Base162().encode0([0, 3]))))
        self.assertEqual("0004", "".join(map(chr, Base16.Base162().encode0([0, 4]))))
        self.assertEqual("0005", "".join(map(chr, Base16.Base162().encode0([0, 5]))))
        self.assertEqual("0006", "".join(map(chr, Base16.Base162().encode0([0, 6]))))
        self.assertEqual("0007", "".join(map(chr, Base16.Base162().encode0([0, 7]))))
        self.assertEqual("0008", "".join(map(chr, Base16.Base162().encode0([0, 8]))))
        self.assertEqual("0009", "".join(map(chr, Base16.Base162().encode0([0, 9]))))
        self.assertEqual("000A", "".join(map(chr, Base16.Base162().encode0([0, 10]))))
        self.assertEqual("000B", "".join(map(chr, Base16.Base162().encode0([0, 11]))))
        self.assertEqual("000C", "".join(map(chr, Base16.Base162().encode0([0, 12]))))
        self.assertEqual("000D", "".join(map(chr, Base16.Base162().encode0([0, 13]))))
        self.assertEqual("000E", "".join(map(chr, Base16.Base162().encode0([0, 14]))))
        self.assertEqual("000F", "".join(map(chr, Base16.Base162().encode0([0, 15]))))
        self.assertEqual("0010", "".join(map(chr, Base16.Base162().encode0([0, 16]))))
        self.assertEqual("0011", "".join(map(chr, Base16.Base162().encode0([0, 17]))))

        for i in range(-128, 128):
            test = [i, i]
            self.assertEqual(
                test, Base16.Base162().decode0(Base16.Base162().encode0(test))
            )

    def testObjectEncode(self) -> None:

        b16 = Base16.Base162()
        self.assertEqual(
            "48656C6C6F20576F726C64",
            b16.encode0("Hello World".encode(self.__CHARSET_UTF8)).decode(),
        )

    def testObjectEncodeWithValidParameter(self) -> None:

        original = "Hello World!"
        origObj = original.encode(self.__CHARSET_UTF8)

        oEncoded = Base16.Base162().encode3(origObj)
        bArray = Base16.Base162().decode0(oEncoded)
        dest = bArray.decode(self.__CHARSET_UTF8)

        self.assertEqual("dest string does not equal original", original, dest)

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

        original = "Hello World!"
        o = Base16.Base162().encode0(original.encode(self.__CHARSET_UTF8))

        b16 = Base16.Base162()
        oDecoded = b16.decode2(o)
        baDecoded = oDecoded
        dest = baDecoded.decode(self.__CHARSET_UTF8)

        self.assertEqual("dest string does not equal original", original, dest)

    def testObjectDecodeWithInvalidParameter(self) -> None:

        b16 = Base16.Base162()

        with pytest.raises(DecoderException):
            b16.decode2(5)

    def testNonBase16Test(self) -> None:

        invalidEncodedChars = [
            ord("/"),
            ord(":"),
            ord("@"),
            ord("G"),
            ord("%"),
            ord("`"),
            ord("g"),
        ]

        encoded = bytearray(1)
        for invalidEncodedChar in invalidEncodedChars:
            try:
                encoded[0] = invalidEncodedChar
                Base16.Base162().decode0(encoded)
                self.fail(
                    "ValueError should have been thrown when trying to decode"
                    + " invalid Base16 char: "
                    + chr(invalidEncodedChar)
                )
            except Exception as e:
                self.assertIsInstance(e, ValueError)

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
            .decode0(bytes.fromhex("78797a7a7931"))
            .decode(self.__CHARSET_UTF8),
        )

    def testEncodeDecodeSmall(self) -> None:

        for i in range(12):
            data = [0] * i
            self.getRandom().randbytes(data)
            enc = Base16.Base162().encode0(data)
            data2 = Base16.Base162().decode0(enc)
            self.assertEqual(
                self.__toString(data) + " equals " + self.__toString(data2), data, data2
            )

    def testEncodeDecodeRandom(self) -> None:

        for i in range(1, 5):
            len = self.getRandom().randint(1, 10000)
            data = bytearray(self.getRandom().getrandbits(8) for _ in range(len))
            enc = Base16.Base162().encode0(data)
            data2 = Base16.Base162().decode0(enc)
            self.assertEqual(data, data2)

    def testEmptyBase16(self) -> None:

        empty = bytearray()
        result = Base16.Base162().encode0(empty)
        self.assertEqual(len(result), 0, "empty Base16 encode")
        self.assertIsNone(Base16.Base162().encode0(None), "empty Base16 encode")
        result = Base16.Base162().encode1(empty, 0, 1)
        self.assertEqual(len(result), 0, "empty Base16 encode with offset")
        self.assertIsNone(
            Base16.Base162().encode0(None), "empty Base16 encode with offset"
        )

        empty = bytearray([])
        result = Base16.Base162().decode0(empty)
        self.assertEqual(len(result), 0, "empty Base16 decode")
        self.assertIsNone(Base16.Base162().decode0(None), "empty Base16 encode")

    def testConstructor_LowerCase_DecodingPolicy(self) -> None:

        base16 = Base16(False, CodecPolicy.STRICT)
        encoded = base16.encode0(BaseNTestData.DECODED)
        expectedResult = Base16TestData.ENCODED_UTF8_UPPERCASE
        result = StringUtils.newStringUtf8(encoded)
        self.assertEqual(
            result, expectedResult, "new base16(false, CodecPolicy.STRICT)"
        )

    def testConstructor_LowerCase(self) -> None:

        base16 = Base16.Base161(True)
        encoded = base16.encode0(BaseNTestData.DECODED)
        expectedResult = Base16TestData.ENCODED_UTF8_LOWERCASE
        result = StringUtils.newStringUtf8(encoded)
        self.assertEqual("new Base16(true)", expectedResult, result)

    def testConstructors(self) -> None:

        Base16.Base162()
        Base16.Base161(False)
        Base16.Base161(True)
        Base16(False, CodecPolicy.LENIENT)
        Base16(False, CodecPolicy.STRICT)

    def testCodec68(self) -> None:

        x = bytearray(b"nH==\x9c")
        b16 = Base16.Base162()
        with pytest.raises(RuntimeError):
            b16.decode0(x)

    def testBase16(self) -> None:

        content = "Hello World"
        encoded_bytes = Base16.Base162().encode0(StringUtils.getBytesUtf8(content))
        encoded_content = StringUtils.newStringUtf8(encoded_bytes)
        self.assertEqual(
            "encoding hello world", "48656C6C6F20576F726C64", encoded_content
        )

        decoded_bytes = Base16.Base162().decode0(encoded_bytes)
        decoded_content = StringUtils.newStringUtf8(decoded_bytes)
        self.assertEqual("decoding hello world", content, decoded_content)

    def getRandom(self) -> random.Random:
        return self.__random

    def __toString(self, data: typing.List[int]) -> str:

        buf = ""
        for i in range(len(data)):
            buf += str(data[i])
            if i != len(data) - 1:
                buf += ","
        return buf
