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
    __CHARSET_UTF8: str = "UTF-8"

    def testLenientDecoding(self) -> None:

        pass  # LLM could not translate this method

    def testStrictDecoding(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeSingleBytesOptimisation(self) -> None:
        context = Context()
        self.assertEqual(0, context.ibitWorkArea)
        self.assertIsNone(context.buffer)

        data = [0] * 1

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
        decodedBytes[0 : context.pos] = context.buffer[
            context.readPos : context.readPos + context.pos
        ]
        decoded = StringUtils.newStringUtf8(decodedBytes)

        self.assertEqual("Until next time!", decoded)

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

    def checkEncodeLengthBounds(self) -> None:

        pass  # LLM could not translate this method

    def testStringToByteVariations(self) -> None:

        pass  # LLM could not translate this method

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
            "000000", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 0])])
        )
        self.assertEqual(
            "000001", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 1])])
        )
        self.assertEqual(
            "000002", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 2])])
        )
        self.assertEqual(
            "000003", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 3])])
        )
        self.assertEqual(
            "000004", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 4])])
        )
        self.assertEqual(
            "000005", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 5])])
        )
        self.assertEqual(
            "000006", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 6])])
        )
        self.assertEqual(
            "000007", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 7])])
        )
        self.assertEqual(
            "000008", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 8])])
        )
        self.assertEqual(
            "000009", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 9])])
        )
        self.assertEqual(
            "00000A", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 10])])
        )
        self.assertEqual(
            "00000B", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 11])])
        )
        self.assertEqual(
            "00000C", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 12])])
        )
        self.assertEqual(
            "00000D", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 13])])
        )
        self.assertEqual(
            "00000E", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 14])])
        )
        self.assertEqual(
            "00000F", "".join([chr(x) for x in Base16.Base162().encode0([0, 0, 15])])
        )

    def testSingletons(self) -> None:
        self.assertEqual("00", str(Base16.Base162().encode0([0])))
        self.assertEqual("01", str(Base16.Base162().encode0([1])))
        self.assertEqual("02", str(Base16.Base162().encode0([2])))
        self.assertEqual("03", str(Base16.Base162().encode0([3])))
        self.assertEqual("04", str(Base16.Base162().encode0([4])))
        self.assertEqual("05", str(Base16.Base162().encode0([5])))
        self.assertEqual("06", str(Base16.Base162().encode0([6])))
        self.assertEqual("07", str(Base16.Base162().encode0([7])))
        self.assertEqual("08", str(Base16.Base162().encode0([8])))
        self.assertEqual("09", str(Base16.Base162().encode0([9])))
        self.assertEqual("0A", str(Base16.Base162().encode0([10])))
        self.assertEqual("0B", str(Base16.Base162().encode0([11])))
        self.assertEqual("0C", str(Base16.Base162().encode0([12])))
        self.assertEqual("0D", str(Base16.Base162().encode0([13])))
        self.assertEqual("0E", str(Base16.Base162().encode0([14])))
        self.assertEqual("0F", str(Base16.Base162().encode0([15])))
        self.assertEqual("10", str(Base16.Base162().encode0([16])))
        self.assertEqual("11", str(Base16.Base162().encode0([17])))
        self.assertEqual("12", str(Base16.Base162().encode0([18])))
        self.assertEqual("13", str(Base16.Base162().encode0([19])))
        self.assertEqual("14", str(Base16.Base162().encode0([20])))
        self.assertEqual("15", str(Base16.Base162().encode0([21])))
        self.assertEqual("16", str(Base16.Base162().encode0([22])))
        self.assertEqual("17", str(Base16.Base162().encode0([23])))
        self.assertEqual("18", str(Base16.Base162().encode0([24])))
        self.assertEqual("19", str(Base16.Base162().encode0([25])))
        self.assertEqual("1A", str(Base16.Base162().encode0([26])))
        self.assertEqual("1B", str(Base16.Base162().encode0([27])))
        self.assertEqual("1C", str(Base16.Base162().encode0([28])))
        self.assertEqual("1D", str(Base16.Base162().encode0([29])))
        self.assertEqual("1E", str(Base16.Base162().encode0([30])))
        self.assertEqual("1F", str(Base16.Base162().encode0([31])))
        self.assertEqual("20", str(Base16.Base162().encode0([32])))
        self.assertEqual("21", str(Base16.Base162().encode0([33])))
        self.assertEqual("22", str(Base16.Base162().encode0([34])))
        self.assertEqual("23", str(Base16.Base162().encode0([35])))
        self.assertEqual("24", str(Base16.Base162().encode0([36])))
        self.assertEqual("25", str(Base16.Base162().encode0([37])))
        self.assertEqual("26", str(Base16.Base162().encode0([38])))
        self.assertEqual("27", str(Base16.Base162().encode0([39])))
        self.assertEqual("28", str(Base16.Base162().encode0([40])))
        self.assertEqual("29", str(Base16.Base162().encode0([41])))
        self.assertEqual("2A", str(Base16.Base162().encode0([42])))
        self.assertEqual("2B", str(Base16.Base162().encode0([43])))
        self.assertEqual("2C", str(Base16.Base162().encode0([44])))
        self.assertEqual("2D", str(Base16.Base162().encode0([45])))
        self.assertEqual("2E", str(Base16.Base162().encode0([46])))
        self.assertEqual("2F", str(Base16.Base162().encode0([47])))
        self.assertEqual("30", str(Base16.Base162().encode0([48])))
        self.assertEqual("31", str(Base16.Base162().encode0([49])))
        self.assertEqual("32", str(Base16.Base162().encode0([50])))
        self.assertEqual("33", str(Base16.Base162().encode0([51])))
        self.assertEqual("34", str(Base16.Base162().encode0([52])))
        self.assertEqual("35", str(Base16.Base162().encode0([53])))
        self.assertEqual("36", str(Base16.Base162().encode0([54])))
        self.assertEqual("37", str(Base16.Base162().encode0([55])))
        self.assertEqual("38", str(Base16.Base162().encode0([56])))
        self.assertEqual("39", str(Base16.Base162().encode0([57])))
        self.assertEqual("3A", str(Base16.Base162().encode0([58])))
        self.assertEqual("3B", str(Base16.Base162().encode0([59])))
        self.assertEqual("3C", str(Base16.Base162().encode0([60])))
        self.assertEqual("3D", str(Base16.Base162().encode0([61])))
        self.assertEqual("3E", str(Base16.Base162().encode0([62])))
        self.assertEqual("3F", str(Base16.Base162().encode0([63])))
        self.assertEqual("40", str(Base16.Base162().encode0([64])))
        self.assertEqual("41", str(Base16.Base162().encode0([65])))
        self.assertEqual("42", str(Base16.Base162().encode0([66])))
        self.assertEqual("43", str(Base16.Base162().encode0([67])))
        self.assertEqual("44", str(Base16.Base162().encode0([68])))
        self.assertEqual("45", str(Base16.Base162().encode0([69])))
        self.assertEqual("46", str(Base16.Base162().encode0([70])))
        self.assertEqual("47", str(Base16.Base162().encode0([71])))
        self.assertEqual("48", str(Base16.Base162().encode0([72])))
        self.assertEqual("49", str(Base16.Base162().encode0([73])))
        self.assertEqual("4A", str(Base16.Base162().encode0([74])))
        self.assertEqual("4B", str(Base16.Base162().encode0([75])))
        self.assertEqual("4C", str(Base16.Base162().encode0([76])))
        self.assertEqual("4D", str(Base16.Base162().encode0([77])))
        self.assertEqual("4E", str(Base16.Base162().encode0([78])))
        self.assertEqual("4F", str(Base16.Base162().encode0([79])))
        self.assertEqual("50", str(Base16.Base162().encode0([80])))
        self.assertEqual("51", str(Base16.Base162().encode0([81])))
        self.assertEqual("52", str(Base16.Base162().encode0([82])))
        self.assertEqual("53", str(Base16.Base162().encode0([83])))
        self.assertEqual("54", str(Base16.Base162().encode0([84])))
        self.assertEqual("55", str(Base16.Base162().encode0([85])))
        self.assertEqual("56", str(Base16.Base162().encode0([86])))
        self.assertEqual("57", str(Base16.Base162().encode0([87])))
        self.assertEqual("58", str(Base16.Base162().encode0([88])))
        self.assertEqual("59", str(Base16.Base162().encode0([89])))
        self.assertEqual("5A", str(Base16.Base162().encode0([90])))
        self.assertEqual("5B", str(Base16.Base162().encode0([91])))
        self.assertEqual("5C", str(Base16.Base162().encode0([92])))
        self.assertEqual("5D", str(Base16.Base162().encode0([93])))
        self.assertEqual("5E", str(Base16.Base162().encode0([94])))
        self.assertEqual("5F", str(Base16.Base162().encode0([95])))
        self.assertEqual("60", str(Base16.Base162().encode0([96])))
        self.assertEqual("61", str(Base16.Base162().encode0([97])))
        self.assertEqual("62", str(Base16.Base162().encode0([98])))
        self.assertEqual("63", str(Base16.Base162().encode0([99])))
        self.assertEqual("64", str(Base16.Base162().encode0([100])))
        self.assertEqual("65", str(Base16.Base162().encode0([101])))
        self.assertEqual("66", str(Base16.Base162().encode0([102])))
        self.assertEqual("67", str(Base16.Base162().encode0([103])))
        self.assertEqual("68", str(Base16.Base162().encode0([104])))
        for i in range(-128, 128):
            test = [i]
            self.assertListEqual(
                test, Base16.Base162().decode0(Base16.Base162().encode0(test))
            )

    def testPairs(self) -> None:
        self.assertEqual("0000", str(Base16.Base162().encode0([0, 0])))
        self.assertEqual("0001", str(Base16.Base162().encode0([0, 1])))
        self.assertEqual("0002", str(Base16.Base162().encode0([0, 2])))
        self.assertEqual("0003", str(Base16.Base162().encode0([0, 3])))
        self.assertEqual("0004", str(Base16.Base162().encode0([0, 4])))
        self.assertEqual("0005", str(Base16.Base162().encode0([0, 5])))
        self.assertEqual("0006", str(Base16.Base162().encode0([0, 6])))
        self.assertEqual("0007", str(Base16.Base162().encode0([0, 7])))
        self.assertEqual("0008", str(Base16.Base162().encode0([0, 8])))
        self.assertEqual("0009", str(Base16.Base162().encode0([0, 9])))
        self.assertEqual("000A", str(Base16.Base162().encode0([0, 10])))
        self.assertEqual("000B", str(Base16.Base162().encode0([0, 11])))
        self.assertEqual("000C", str(Base16.Base162().encode0([0, 12])))
        self.assertEqual("000D", str(Base16.Base162().encode0([0, 13])))
        self.assertEqual("000E", str(Base16.Base162().encode0([0, 14])))
        self.assertEqual("000F", str(Base16.Base162().encode0([0, 15])))
        self.assertEqual("0010", str(Base16.Base162().encode0([0, 16])))
        self.assertEqual("0011", str(Base16.Base162().encode0([0, 17])))
        for i in range(-128, 128):
            test = [i, i]
            self.assertListEqual(
                test, Base16.Base162().decode0(Base16.Base162().encode0(test))
            )

    def testObjectEncode(self) -> None:
        b16 = Base16.Base162()
        self.assertEqual(
            "48656C6C6F20576F726C64",
            b16.encode0("Hello World".encode(self.__CHARSET_UTF8)),
        )

    def testObjectEncodeWithValidParameter(self) -> None:
        original: str = "Hello World!"
        origObj: typing.List[int] = original.encode(self.__CHARSET_UTF8)

        oEncoded: typing.List[int] = Base16.Base162().encode3(origObj)
        bArray: typing.List[int] = Base16.Base162().decode0(oEncoded)
        dest: str = bArray.decode(self.__CHARSET_UTF8)

        self.assertEqual("dest string does not equal original", original, dest)

    def testObjectEncodeWithInvalidParameter(self) -> None:
        b16 = Base16.Base162()
        try:
            b16.encode3("Yadayadayada")
            self.fail(
                "encode(Object) didn't throw an exception when passed a String object"
            )
        except EncoderException as e:
            pass

    def testObjectDecodeWithValidParameter(self) -> None:
        original: str = "Hello World!"
        o: typing.Any = Base16.Base162().encode0(original.encode(self.__CHARSET_UTF8))
        b16: Base16 = Base16.Base162()
        oDecoded: typing.Any = b16.decode2(o)
        baDecoded: typing.List[int] = oDecoded
        dest: str = baDecoded.decode()
        self.assertEqual("dest string does not equal original", original, dest)

    def testObjectDecodeWithInvalidParameter(self) -> None:

        pass  # LLM could not translate this method

    def testNonBase16Test(self) -> None:
        invalidEncodedChars = [b"/", b":", b"@", b"G", b"%", b"`", b"g"]

        encoded = [0] * 1
        for invalidEncodedChar in invalidEncodedChars:
            try:
                encoded[0] = invalidEncodedChar
                Base16.Base162().decode0(encoded)
                self.fail(
                    "ValueError should have been thrown when trying to decode"
                    " invalid Base16 char: " + chr(invalidEncodedChar)
                )
            except Exception as e:
                self.assertTrue(isinstance(e, ValueError))

    def testKnownEncodings(self) -> None:

        pass  # LLM could not translate this method

    def testKnownDecodings(self) -> None:

        pass  # LLM could not translate this method

    def testEncodeDecodeSmall(self) -> None:
        for i in range(12):
            data = [0] * i
            self.getRandom().nextBytes(data)
            enc = Base16.Base162().encode0(data)
            data2 = Base16.Base162().decode0(enc)
            assertArrayEquals(
                self.__toString(data) + " equals " + self.__toString(data2), data, data2
            )

    def testEncodeDecodeRandom(self) -> None:
        for i in range(1, 5):
            len = self.getRandom().nextInt(10000) + 1
            data = [0] * len
            self.getRandom().nextBytes(data)
            enc = Base16.Base162().encode0(data)
            data2 = Base16.Base162().decode0(enc)
            assertArrayEquals(data, data2)

    def testEmptyBase16(self) -> None:
        empty: typing.List[int] = []
        result: typing.List[int] = Base16.Base162().encode0(empty)
        self.assertEqual("empty Base16 encode", 0, len(result))
        self.assertIsNone("empty Base16 encode", Base16.Base162().encode0(None))
        result = Base16.Base162().encode1(empty, 0, 1)
        self.assertEqual("empty Base16 encode with offset", 0, len(result))
        self.assertIsNone(
            "empty Base16 encode with offset", Base16.Base162().encode0(None)
        )

        empty = []
        result = Base16.Base162().decode0(empty)
        self.assertEqual("empty Base16 decode", 0, len(result))
        self.assertIsNone("empty Base16 encode", Base16.Base162().decode0(None))

    def testConstructor_LowerCase_DecodingPolicy(self) -> None:
        base16 = Base16(False, CodecPolicy.STRICT)
        encoded = base16.encode0(BaseNTestData.DECODED)
        expectedResult = Base16TestData.ENCODED_UTF8_UPPERCASE
        result = StringUtils.newStringUtf8(encoded)
        self.assertEqual(
            "new base16(false, CodecPolicy.STRICT)", result, expectedResult
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
        x = [ord("n"), ord("H"), ord("="), ord("="), 0x9C]
        b16 = Base16.Base162()
        b16.decode0(x)

    def testBase16(self) -> None:
        content: str = "Hello World"
        encodedBytes: typing.List[int] = Base16.Base162().encode0(
            StringUtils.getBytesUtf8(content)
        )
        encodedContent: str = StringUtils.newStringUtf8(encodedBytes)
        self.assertEqual(
            "encoding hello world", "48656C6C6F20576F726C64", encodedContent
        )

        decodedBytes: typing.List[int] = Base16.Base162().decode0(encodedBytes)
        decodedContent: str = StringUtils.newStringUtf8(decodedBytes)
        self.assertEqual("decoding hello world", content, decodedContent)

    def getRandom(self) -> random.Random:
        return self.__random

    def __toString(self, data: typing.List[int]) -> str:
        buf = []
        for i in range(len(data)):
            buf.append(str(data[i]))
            if i != len(data) - 1:
                buf.append(",")
        return "".join(buf)
