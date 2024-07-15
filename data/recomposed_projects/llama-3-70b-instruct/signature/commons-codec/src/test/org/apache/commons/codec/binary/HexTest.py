from __future__ import annotations
import re
import random
import sys
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.binary.Hex import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class HexTest(unittest.TestCase):

    __LOG: bool = False
    __BAD_ENCODING_NAME: str = "UNKNOWN"

    def testRequiredCharset(self) -> None:
        self.__testCustomCharset1("UTF-8", "testRequiredCharset")
        self.__testCustomCharset1("UTF-16", "testRequiredCharset")
        self.__testCustomCharset1("UTF-16BE", "testRequiredCharset")
        self.__testCustomCharset1("UTF-16LE", "testRequiredCharset")
        self.__testCustomCharset1("US-ASCII", "testRequiredCharset")
        self.__testCustomCharset1("ISO8859_1", "testRequiredCharset")

    def testGetCharsetName(self) -> None:
        self.assertEqual(
            StandardCharsets.UTF_8.name(),
            Hex(1, None, StandardCharsets.UTF_8).getCharsetName(),
        )

    def testGetCharset(self) -> None:
        self.assertEqual(
            StandardCharsets.UTF_8, Hex(1, None, StandardCharsets.UTF_8).getCharset()
        )

    def testEncodeStringEmpty(self) -> None:

        pass  # LLM could not translate this method

    def testEncodeHexReadOnlyByteBuffer(self) -> None:
        chars = Hex.encodeHex6(ByteBuffer.wrap(bytearray([10])).asReadOnlyBuffer())
        self.assertEqual("0a", str(chars))

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase(self) -> None:
        bb = self._allocate(4)
        bb[1] = 10
        bb = bb[1:2]
        self.assertEqual("0A", Hex.encodeHexString3(bb, False))
        self.assertEqual(0, len(bb))

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase(self) -> None:
        bb: typing.Union[bytearray, memoryview] = self._allocate(4)
        bb[1] = 10
        bb = bb[1:2]
        self.assertEqual("0a", Hex.encodeHexString3(bb, True))
        self.assertEqual(0, len(bb))

    def testEncodeHexByteString_ByteBufferBoolean_ToUpperCase(self) -> None:
        bb: typing.Union[bytearray, memoryview] = self._allocate(1)
        bb[0] = 10
        self.assertEqual("0A", Hex.encodeHexString3(bb, False))

    def testEncodeHexByteString_ByteBufferBoolean_ToLowerCase(self) -> None:
        bb: typing.Union[bytearray, memoryview] = self._allocate(1)
        bb[0] = 10
        self.assertEqual("0a", Hex.encodeHexString3(bb, True))

    def testEncodeHexByteString_ByteArrayBoolean_ToUpperCase(self) -> None:
        self.assertEqual("0A", Hex.encodeHexString1([10], False))

    def testEncodeHexByteString_ByteArrayBoolean_ToLowerCase(self) -> None:
        self.assertEqual("0a", Hex.encodeHexString1([10], True))

    def testEncodeHexByteString_ByteArrayOfZeroes(self) -> None:
        c: str = Hex.encodeHexString0([0] * 36)
        self.assertEqual(
            "000000000000000000000000000000000000000000000000000000000000000000000000",
            c,
        )

    def testEncodeHexByteString_ByteBufferOfZeroesWithLimit(self) -> None:
        bb: typing.Union[bytearray, memoryview] = self._allocate(36)
        bb[0:3] = b"\x00\x00\x00"
        self.assertEqual("000000", Hex.encodeHexString2(bb))
        self.assertEqual(0, len(bb))
        bb[1:3] = b"\x00\x00"
        self.assertEqual("0000", Hex.encodeHexString2(bb))
        self.assertEqual(0, len(bb))

    def testEncodeHexByteString_ByteBufferOfZeroes(self) -> None:
        c: str = Hex.encodeHexString2(self._allocate(36))
        self.assertEqual(
            "000000000000000000000000000000000000000000000000000000000000000000000000",
            c,
        )

    def testEncodeHexPartialInputOverbounds(self) -> None:
        data: typing.List[int] = "hello world".encode("utf-8")
        with pytest.raises(IndexError):
            hex: typing.List[str] = Hex.encodeHex3(data, 9, 10, True)
            assertArrayEquals("64".toCharArray(), hex)

    def testEncodeHexPartialInputUnderbounds(self) -> None:
        data: typing.List[int] = "hello world".encode("utf-8")
        with pytest.raises(IndexError):
            hex: typing.List[str] = Hex.encodeHex3(data, -2, 10, True)
            assertArrayEquals("64".toCharArray(), hex)

    def testEncodeHexPartialInput(self) -> None:
        data: typing.List[int] = "hello world".encode("utf-8")

        hex: typing.List[str] = Hex.encodeHex3(data, 0, 0, True)
        self.assertListEqual([], hex)

        hex = Hex.encodeHex3(data, 0, 1, True)
        self.assertListEqual(["6", "8"], hex)

        hex = Hex.encodeHex3(data, 0, 1, False)
        self.assertListEqual(["6", "8"], hex)

        hex = Hex.encodeHex3(data, 2, 4, True)
        self.assertListEqual(["6", "c", "6", "c", "6", "f", "2", "0"], hex)

        hex = Hex.encodeHex3(data, 2, 4, False)
        self.assertListEqual(["6", "C", "6", "C", "6", "F", "2", "0"], hex)

        hex = Hex.encodeHex3(data, 10, 1, True)
        self.assertListEqual(["6", "4"], hex)

        hex = Hex.encodeHex3(data, 10, 1, False)
        self.assertListEqual(["6", "4"], hex)

    def testEncodeHex_ByteBufferWithLimit(self) -> None:
        bb = self._allocate(16)
        for i in range(16):
            bb[i] = i
        bb = memoryview(bb)
        expected = "000102030405060708090a0b0c0d0e0f"
        for i in range(15):
            bb = bb[i : i + 2]
            self.assertEqual(expected[i * 2 : i * 2 + 4], "".join(Hex.encodeHex6(bb)))
            self.assertEqual(0, len(bb))

    def testEncodeHex_ByteBufferOfZeroes(self) -> None:
        c: typing.List[str] = Hex.encodeHex6(self._allocate(36))
        self.assertEqual(
            "000000000000000000000000000000000000000000000000000000000000000000000000",
            "".join(c),
        )

    def testEncodeHexByteBufferHelloWorldUpperCaseHex(self) -> None:
        b: typing.Union[bytearray, memoryview] = self.__getByteBufferUtf8("Hello World")
        expected: str = "48656C6C6F20576F726C64"
        actual: typing.List[str]
        actual = Hex.encodeHex6(b)
        self.assertEqual(expected.lower(), "".join(actual))
        self.assertEqual(0, b.remaining())
        b.flip()
        actual = Hex.encodeHex7(b, True)
        self.assertEqual(expected.lower(), "".join(actual))
        self.assertEqual(0, b.remaining())
        b.flip()
        actual = Hex.encodeHex7(b, False)
        self.assertEqual(expected, "".join(actual))
        self.assertEqual(0, b.remaining())

    def testEncodeHexByteBufferHelloWorldLowerCaseHex(self) -> None:
        b: typing.Union[bytearray, memoryview] = self.__getByteBufferUtf8("Hello World")
        expected: str = "48656c6c6f20576f726c64"
        actual: typing.List[str]
        actual = Hex.encodeHex6(b)
        self.assertEqual(expected, "".join(actual))
        self.assertEqual(0, b.remaining())
        b.flip()
        actual = Hex.encodeHex7(b, True)
        self.assertEqual(expected, "".join(actual))
        self.assertEqual(0, b.remaining())
        b.flip()
        actual = Hex.encodeHex7(b, False)
        self.assertEqual(expected.upper(), "".join(actual))
        self.assertEqual(0, b.remaining())

    def testEncodeHexByteBufferEmpty(self) -> None:
        assertArrayEquals([], Hex.encodeHex6(self._allocate(0)))
        assertArrayEquals([], Hex(2, None, None).encode1(self._allocate(0)))

    def testEncodeHexByteArrayZeroes(self) -> None:
        c = Hex.encodeHex0([0] * 36)
        self.assertEqual(
            "000000000000000000000000000000000000000000000000000000000000000000000000",
            "".join(c),
        )

    def testEncodeHexByteArrayHelloWorldUpperCaseHex(self) -> None:
        b: typing.List[int] = StringUtils.getBytesUtf8("Hello World")
        expected: str = "48656C6C6F20576F726C64"
        actual: typing.List[str]
        actual = Hex.encodeHex0(b)
        self.assertNotEqual(expected, "".join(actual))
        actual = Hex.encodeHex1(b, True)
        self.assertNotEqual(expected, "".join(actual))
        actual = Hex.encodeHex1(b, False)
        self.assertEqual(expected, "".join(actual))

    def testEncodeHexByteArrayHelloWorldLowerCaseHex(self) -> None:
        b: typing.List[int] = StringUtils.getBytesUtf8("Hello World")
        expected: str = "48656c6c6f20576f726c64"
        actual: typing.List[str]
        actual = Hex.encodeHex0(b)
        self.assertEqual(expected, "".join(actual))
        actual = Hex.encodeHex1(b, True)
        self.assertEqual(expected, "".join(actual))
        actual = Hex.encodeHex1(b, False)
        self.assertNotEqual(expected, "".join(actual))

    def testEncodeHexByteArrayEmpty(self) -> None:
        assertArrayEquals([], Hex.encodeHex0([]))
        assertArrayEquals([], Hex(2, None, None).encode0([]))

    def testEncodeDecodeHexCharArrayRandomToOutput(self) -> None:
        for i in range(5, 0, -1):
            data = [0] * (random.randint(0, 10000) + 1)
            random.shuffle(data)

            lowerEncodedChars = [0] * (len(data) * 2)
            Hex.encodeHex4(data, 0, len(data), True, lowerEncodedChars, 0)
            decodedLowerCaseBytes = Hex.decodeHex0(lowerEncodedChars)
            self.assertEqual(data, decodedLowerCaseBytes)

            upperEncodedChars = [0] * (len(data) * 2)
            Hex.encodeHex4(data, 0, len(data), False, upperEncodedChars, 0)
            decodedUpperCaseBytes = Hex.decodeHex0(upperEncodedChars)
            self.assertEqual(data, decodedUpperCaseBytes)

    def testEncodeDecodeHexCharArrayRandom(self) -> None:
        hex = Hex(2, None, None)
        for i in range(5, 0, -1):
            data = [0] * (ThreadLocalRandom.current().nextInt(10000) + 1)
            ThreadLocalRandom.current().nextBytes(data)

            encodedChars = Hex.encodeHex0(data)
            decodedBytes = Hex.decodeHex0(encodedChars)
            assertArrayEquals(data, decodedBytes)

            encodedStringBytes = hex.encode0(data)
            decodedBytes = hex.decode0(encodedStringBytes)
            assertArrayEquals(data, decodedBytes)

            dataString = "".join(encodedChars)
            encodedStringChars = hex.encode2(dataString)
            decodedBytes = hex.decode2(encodedStringChars)
            assertArrayEquals(StringUtils.getBytesUtf8(dataString), decodedBytes)

            dataString = "".join(encodedChars)
            encodedStringChars = hex.encode2(dataString)
            decodedBytes = hex.decode2("".join(encodedStringChars))
            assertArrayEquals(StringUtils.getBytesUtf8(dataString), decodedBytes)

    def testEncodeTypeError(self) -> None:
        with self.assertRaises(EncoderException):
            Hex(2, None, None).encode2([65])

    def testEncodeByteBufferObjectEmpty(self) -> None:

        pass  # LLM could not translate this method

    def testEncodeByteBufferAllocatedButEmpty(self) -> None:

        pass  # LLM could not translate this method

    def testEncodeByteBufferEmpty(self) -> None:

        pass  # LLM could not translate this method

    def testEncodeByteArrayObjectEmpty(self) -> None:

        pass  # LLM could not translate this method

    def testEncodeByteArrayEmpty(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeByteBufferWithLimit(self) -> None:
        bb = self.__getByteBufferUtf8("000102030405060708090a0b0c0d0e0f")
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        for i in range(15):
            bb.position(i * 2)
            bb.limit(i * 2 + 4)
            self.assertEqual(
                "".join([chr(x) for x in expected[i : i + 2]]),
                "".join([chr(x) for x in Hex(2, None, None).decode1(bb)]),
            )
            self.assertEqual(0, bb.remaining())

    def testDecodeStringEmpty(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeHexStringOddCharacters(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeHexCharArrayOutBufferUnderSizedByOffset(self) -> None:
        with self.assertRaises(DecoderException):
            out = [0] * 6
            Hex.decodeHex1("aabbccddeeff".toCharArray(), out, 1)

    def testDecodeHexCharArrayOutBufferUnderSized(self) -> None:
        with self.assertRaises(DecoderException):
            out = [0] * 4
            Hex.decodeHex1("aabbccddeeff".toCharArray(), out, 0)

    def testDecodeHexCharArrayOddCharacters5(self) -> None:
        self.__checkDecodeHexCharArrayOddCharacters0(["A", "B", "C", "D", "E"])

    def testDecodeHexCharArrayOddCharacters3(self) -> None:
        self.__checkDecodeHexCharArrayOddCharacters0(["A", "B", "C"])

    def testDecodeHexStringOddCharacters1(self) -> None:
        self.__checkDecodeHexCharArrayOddCharacters1("A")

    def testDecodeHexCharArrayOddCharacters1(self) -> None:
        self.__checkDecodeHexCharArrayOddCharacters0(["A"])

    def testDecodeTypeError(self) -> None:
        with self.assertRaises(DecoderException):
            Hex(2, None, None).decode2([65])

    def testDecodeHexStringEmpty(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeHexCharArrayEmpty(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeByteBufferWithLimitOddCharacters(self) -> None:
        bb: typing.Union[bytearray, memoryview] = self._allocate(10)
        bb[1] = 65
        bb.position(1)
        bb.limit(2)
        self.__checkDecodeHexByteBufferOddCharacters(bb)

    def testDecodeByteBufferOddCharacters(self) -> None:
        bb = self._allocate(1)
        bb[0] = 65
        self.__checkDecodeHexByteBufferOddCharacters(bb)

    def testDecodeByteBufferObjectEmpty(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeByteBufferAllocatedButEmpty(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeByteBufferEmpty(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeByteArrayOddCharacters(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeByteArrayObjectEmpty(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeByteArrayEmpty(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeBadCharacterPos1(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeBadCharacterPos0(self) -> None:
        with self.assertRaises(DecoderException):
            Hex(2, None, None).decode2("q0")

    def testCustomCharsetToString(self) -> None:
        self.assertTrue(
            Hex(2, None, None).toString().index(Hex.DEFAULT_CHARSET_NAME) >= 0
        )

    def testCustomCharsetBadName(self) -> None:
        with self.assertRaises(ValueError):
            Hex.Hex0(self.__BAD_ENCODING_NAME)

    def testCustomCharset0(self) -> None:
        for name in Charset.availableCharsets().keySet():
            self.__testCustomCharset1(name, "testCustomCharset")

    def _allocate(self, capacity: int) -> typing.Union[bytearray, memoryview]:
        return bytearray(capacity)

    def __testCustomCharset1(self, name: str, parent: str) -> None:
        if not self.__charsetSanityCheck(name):
            return
        self.__log0(parent + "=" + name)
        customCodec = Hex.Hex0(name)
        sourceString = "Hello World"
        sourceBytes = sourceString.encode(name)
        actualEncodedBytes = customCodec.encode0(sourceBytes)
        expectedHexString = Hex.encodeHexString0(sourceBytes)
        expectedHexStringBytes = expectedHexString.encode(name)
        assertArrayEquals(expectedHexStringBytes, actualEncodedBytes)
        actualStringFromBytes = actualEncodedBytes.decode(name)
        self.assertEqual(
            name
            + ", expectedHexString="
            + expectedHexString
            + ", actualStringFromBytes="
            + actualStringFromBytes,
            expectedHexString,
            actualStringFromBytes,
        )
        utf8Codec = Hex(2, None, None)
        expectedHexString = "48656c6c6f20576f726c64"
        decodedUtf8Bytes = utf8Codec.decode2(expectedHexString)
        actualStringFromBytes = decodedUtf8Bytes.decode(utf8Codec.getCharset())
        self.assertEqual(name, sourceString, actualStringFromBytes)
        decodedCustomBytes = customCodec.decode0(actualEncodedBytes)
        actualStringFromBytes = decodedCustomBytes.decode(name)
        self.assertEqual(name, sourceString, actualStringFromBytes)

    def __log1(self, t: BaseException) -> None:
        if self.__LOG:
            t.printStackTrace(System.out)
            System.out.flush()

    def __log0(self, s: str) -> None:
        if self.__LOG:
            print(s)
            sys.stdout.flush()

    def __checkDecodeHexCharArrayOddCharacters1(self, data: str) -> None:

        pass  # LLM could not translate this method

    def __checkDecodeHexByteBufferOddCharacters(
        self, data: typing.Union[bytearray, memoryview]
    ) -> None:

        pass  # LLM could not translate this method

    def __checkDecodeHexCharArrayOddCharacters0(self, data: typing.List[str]) -> None:

        pass  # LLM could not translate this method

    def __charsetSanityCheck(self, name: str) -> bool:
        source: str = "the quick brown dog jumped over the lazy fox"
        try:
            bytes: bytes = source.encode(name)
            str: str = bytes.decode(name)
            equals: bool = source == str
            if not equals:
                self.__log0(
                    "FAILED charsetSanityCheck=Interesting Java charset oddity: Roundtrip"
                    + " failed for "
                    + name
                )
            return equals
        except (ValueError, NotImplementedError) as e:
            if self.__LOG:
                self.__log0("FAILED charsetSanityCheck=" + name + ", e=" + e)
                self.__log1(e)
            return False

    def __getByteBufferUtf8(self, string: str) -> typing.Union[bytearray, memoryview]:
        bytes = string.encode("utf-8")
        bb = self._allocate(len(bytes))
        bb.put(bytes)
        bb.flip()
        return bb
