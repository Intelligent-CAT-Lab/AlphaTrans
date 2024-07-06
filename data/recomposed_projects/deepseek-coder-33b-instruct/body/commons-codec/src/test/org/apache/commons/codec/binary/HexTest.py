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

    __BAD_ENCODING_NAME: str = "UNKNOWN"

    def testRequiredCharset(self) -> None:

        self.__testCustomCharset1("UTF-8", "testRequiredCharset")
        self.__testCustomCharset1("UTF-16", "testRequiredCharset")
        self.__testCustomCharset1("UTF-16BE", "testRequiredCharset")
        self.__testCustomCharset1("UTF-16LE", "testRequiredCharset")
        self.__testCustomCharset1("US-ASCII", "testRequiredCharset")
        self.__testCustomCharset1("ISO8859_1", "testRequiredCharset")

    def testGetCharsetName(self) -> None:

        # Create an instance of Hex class with constructorId=1, charsetName=None and charset=StandardCharsets.UTF_8
        hex_instance = Hex(1, None, StandardCharsets.UTF_8)

        # Assert that the charset name returned by the getCharsetName method is equal to the name of StandardCharsets.UTF_8
        self.assertEqual(StandardCharsets.UTF_8.name, hex_instance.getCharsetName())

    def testGetCharset(self) -> None:

        from java.nio.charset import StandardCharsets

        self.assertEqual(
            StandardCharsets.UTF_8, Hex(1, None, StandardCharsets.UTF_8).getCharset()
        )

    def testEncodeStringEmpty(self) -> None:

        self.assertEqual([], list(Hex(2, None, None).encode2("")))

    def testEncodeHexReadOnlyByteBuffer(self) -> None:

        from src.main.org.apache.commons.codec.binary.Hex import Hex
        from array import array

        data = array("b", [10])
        chars = Hex.encodeHex6(data)
        self.assertEqual("0a", "".join(chars))

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase(self) -> None:

        bb = self._allocate(4)
        bb[1] = 10
        bb = bb[1:2]
        self.assertEqual("0A", Hex.encodeHexString3(bb, False))
        self.assertEqual(0, len(bb))

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase(self) -> None:

        bb = self._allocate(4)
        bb[1] = 10
        bb = bb[1:2]
        self.assertEqual("0a", Hex.encodeHexString3(bb, True))
        self.assertEqual(0, len(bb))

    def testEncodeHexByteString_ByteBufferBoolean_ToUpperCase(self) -> None:

        bb = self._allocate(1)
        bb[0] = 10
        self.assertEqual("0A", Hex.encodeHexString3(bb, False))

    def testEncodeHexByteString_ByteBufferBoolean_ToLowerCase(self) -> None:

        bb = self._allocate(1)
        bb[0] = 10
        self.assertEqual("0a", Hex.encodeHexString3(bb, True))

    def testEncodeHexByteString_ByteArrayBoolean_ToUpperCase(self) -> None:

        self.assertEqual("0A", Hex.encodeHexString1([10], False))

    def testEncodeHexByteString_ByteArrayBoolean_ToLowerCase(self) -> None:

        self.assertEqual("0a", Hex.encodeHexString1([10], True))

    def testEncodeHexByteString_ByteArrayOfZeroes(self) -> None:

        c = Hex.encodeHexString0([0] * 36)
        self.assertEqual(
            "000000000000000000000000000000000000000000000000000000000000000000000000",
            c,
        )

    def testEncodeHexByteString_ByteBufferOfZeroesWithLimit(self) -> None:

        bb = self._allocate(36)
        bb.limit(3)
        self.assertEqual("000000", Hex.encodeHexString2(bb))
        self.assertEqual(0, bb.remaining())
        bb.position(1)
        bb.limit(3)
        self.assertEqual("0000", Hex.encodeHexString2(bb))
        self.assertEqual(0, bb.remaining())

    def testEncodeHexByteString_ByteBufferOfZeroes(self) -> None:

        c = Hex.encodeHexString2(self._allocate(36))
        self.assertEqual(
            "0000000000000000000000000000000000000000000000000000000000000000000000000",
            c,
        )

    def testEncodeHexPartialInputOverbounds(self) -> None:

        data = "hello world".encode("utf-8")

        with pytest.raises(IndexError):
            hex = Hex.encodeHex3(data, 9, 10, True)
            self.assertEqual(list("64"), hex)

    def testEncodeHexPartialInputUnderbounds(self) -> None:

        data = "hello world".encode("utf-8")

        with pytest.raises(IndexError):
            hex = Hex.encodeHex3(data, -2, 10, True)
            self.assertEqual(list("64"), hex)

    def testEncodeHexPartialInput(self) -> None:

        data = "hello world".encode("utf-8")

        hex = Hex.encodeHex3(data, 0, 0, True)
        self.assertEqual(list(""), hex)

        hex = Hex.encodeHex3(data, 0, 1, True)
        self.assertEqual(list("68"), hex)

        hex = Hex.encodeHex3(data, 0, 1, False)
        self.assertEqual(list("68"), hex)

        hex = Hex.encodeHex3(data, 2, 4, True)
        self.assertEqual(list("6c6c6f20"), hex)

        hex = Hex.encodeHex3(data, 2, 4, False)
        self.assertEqual(list("6C6C6F20"), hex)

        hex = Hex.encodeHex3(data, 10, 1, True)
        self.assertEqual(list("64"), hex)

        hex = Hex.encodeHex3(data, 10, 1, False)
        self.assertEqual(list("64"), hex)

    def testEncodeHex_ByteBufferWithLimit(self) -> None:

        bb = self._allocate(16)
        for i in range(16):
            bb[i] = i
        expected = "000102030405060708090a0b0c0d0e0f"
        for i in range(15):
            bb = bb[i : i + 2]
            self.assertEqual(expected[i * 2 : i * 2 + 4], Hex.encodeHex6(bb))
            self.assertEqual(0, len(bb))

    def testEncodeHex_ByteBufferOfZeroes(self) -> None:

        c = Hex.encodeHex6(self._allocate(36))
        self.assertEqual(
            "0000000000000000000000000000000000000000000000000000000000000000000000000",
            "".join(c),
        )

    def testEncodeHexByteBufferHelloWorldUpperCaseHex(self) -> None:

        b = self.__getByteBufferUtf8("Hello World")
        expected = "48656C6C6F20576F726C64"
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

        b = self.__getByteBufferUtf8("Hello World")
        expected = "48656c6c6f20576f726c64"
        actual = Hex.encodeHex6(b)
        self.assertEqual("".join(actual), expected)
        self.assertEqual(0, b.remaining())
        b.flip()
        actual = Hex.encodeHex7(b, True)
        self.assertEqual("".join(actual), expected)
        self.assertEqual(0, b.remaining())
        b.flip()
        actual = Hex.encodeHex7(b, False)
        self.assertEqual("".join(actual), expected.upper())
        self.assertEqual(0, b.remaining())

    def testEncodeHexByteBufferEmpty(self) -> None:

        self.assertListEqual([], Hex.encodeHex6(self._allocate(0)))
        self.assertListEqual([], Hex(2, None, None).encode1(self._allocate(0)))

    def testEncodeHexByteArrayZeroes(self) -> None:

        c = Hex.encodeHex0([0] * 36)
        self.assertEqual(
            "000000000000000000000000000000000000000000000000000000000000000000000000",
            "".join(c),
        )

    def testEncodeHexByteArrayHelloWorldUpperCaseHex(self) -> None:

        b = StringUtils.getBytesUtf8("Hello World")
        expected = "48656C6C6F20576F726C64"
        actual = Hex.encodeHex0(b)
        self.assertNotEqual(expected, "".join(actual))
        actual = Hex.encodeHex1(b, True)
        self.assertNotEqual(expected, "".join(actual))
        actual = Hex.encodeHex1(b, False)
        self.assertEqual(expected, "".join(actual))

    def testEncodeHexByteArrayHelloWorldLowerCaseHex(self) -> None:

        b = StringUtils.getBytesUtf8("Hello World")
        expected = "48656c6c6f20576f726c64"
        actual = Hex.encodeHex0(b)
        self.assertEqual("".join(actual), expected)
        actual = Hex.encodeHex1(b, True)
        self.assertEqual("".join(actual), expected)
        actual = Hex.encodeHex1(b, False)
        self.assertNotEqual("".join(actual), expected)

    def testEncodeHexByteArrayEmpty(self) -> None:

        self.assertListEqual([], Hex.encodeHex0([]))
        self.assertListEqual([], Hex(2, None, None).encode0([]))

    def testEncodeDecodeHexCharArrayRandomToOutput(self) -> None:

        for i in range(5, 0, -1):
            data = bytearray(random.randint(0, 10000) + 1)
            for j in range(len(data)):
                data[j] = random.randint(0, 255)

            lowerEncodedChars = ["\0"] * (len(data) * 2)
            Hex.encodeHex4(data, 0, len(data), True, lowerEncodedChars, 0)
            decodedLowerCaseBytes = Hex.decodeHex0(lowerEncodedChars)
            self.assertEqual(list(data), decodedLowerCaseBytes)

            upperEncodedChars = ["\0"] * (len(data) * 2)
            Hex.encodeHex4(data, 0, len(data), False, upperEncodedChars, 0)
            decodedUpperCaseBytes = Hex.decodeHex0(upperEncodedChars)
            self.assertEqual(list(data), decodedUpperCaseBytes)

    def testEncodeDecodeHexCharArrayRandom(self) -> None:

        hex = Hex(2, None, None)
        for i in range(5, 0, -1):
            data = [0] * (random.randint(1, 10000) + 1)
            for j in range(len(data)):
                data[j] = random.randint(0, 255)

            encodedChars = Hex.encodeHex0(data)
            decodedBytes = Hex.decodeHex0(encodedChars)
            self.assertEqual(data, decodedBytes)

            encodedStringBytes = hex.encode0(data)
            decodedBytes = hex.decode0(encodedStringBytes)
            self.assertEqual(data, decodedBytes)

            dataString = "".join(encodedChars)
            encodedStringChars = hex.encode2(dataString)
            decodedBytes = hex.decode2(encodedStringChars)
            self.assertEqual(StringUtils.getBytesUtf8(dataString), decodedBytes)

            dataString = "".join(encodedChars)
            encodedStringChars = hex.encode2(dataString)
            decodedBytes = hex.decode2("".join(encodedStringChars))
            self.assertEqual(StringUtils.getBytesUtf8(dataString), decodedBytes)

    def testEncodeTypeError(self) -> None:

        try:
            Hex(2, None, None).encode2([65])
            self.fail("An exception wasn't thrown when trying to encode.")
        except EncoderException:
            pass

    def testEncodeByteBufferObjectEmpty(self) -> None:

        self.assertEqual([], (Hex(2, None, None).encode2(self._allocate(0))))

    def testEncodeByteBufferAllocatedButEmpty(self) -> None:

        bb = self._allocate(10)
        bb.flip()
        self.assertEqual(bytearray([]), Hex(2, None, None).encode1(bb))
        self.assertEqual(0, len(bb))

    def testEncodeByteBufferEmpty(self) -> None:

        self.assertEqual([], Hex(2, None, None).encode1(self._allocate(0)))

    def testEncodeByteArrayObjectEmpty(self) -> None:

        self.assertEqual([], list(Hex(2, None, None).encode2(bytearray([]))))

    def testEncodeByteArrayEmpty(self) -> None:

        self.assertEqual(
            bytearray([]), bytearray(self.Hex(2, None, None).encode0(bytearray([])))
        )

    def testDecodeByteBufferWithLimit(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeStringEmpty(self) -> None:

        try:
            self.assertEqual([], Hex(2, None, None).decode2(""))
        except DecoderException as e:
            self.fail(f"DecoderException raised: {str(e)}")

    def testDecodeHexStringOddCharacters(self) -> None:

        try:
            Hex(2, None, None).decode2("6")
            self.fail(
                "An exception wasn't thrown when trying to decode an odd number of characters"
            )
        except DecoderException:
            pass

    def testDecodeHexCharArrayOutBufferUnderSizedByOffset(self) -> None:

        out = [0] * 6
        Hex.decodeHex1(list("aabbccddeeff"), out, 1)

    def testDecodeHexCharArrayOutBufferUnderSized(self) -> None:

        out = [0] * 4
        data = list("aabbccddeeff")

        with pytest.raises(DecoderException):
            Hex.decodeHex1(data, out, 0)

    def testDecodeHexCharArrayOddCharacters5(self) -> None:

        self.__checkDecodeHexCharArrayOddCharacters0(["A", "B", "C", "D", "E"])

    def testDecodeHexCharArrayOddCharacters3(self) -> None:

        self.__checkDecodeHexCharArrayOddCharacters0(["A", "B", "C"])

    def testDecodeHexStringOddCharacters1(self) -> None:

        self.__checkDecodeHexCharArrayOddCharacters1("A")

    def testDecodeHexCharArrayOddCharacters1(self) -> None:

        self.__checkDecodeHexCharArrayOddCharacters0(["A"])

    def testDecodeTypeError(self) -> None:

        try:
            Hex(2, None, None).decode2([65])
            self.fail("An exception wasn't thrown when trying to decode.")
        except DecoderException:
            pass

    def testDecodeHexStringEmpty(self) -> None:

        self.assertEqual(Hex.decodeHex2(""), [])

    def testDecodeHexCharArrayEmpty(self) -> None:

        from src.main.org.apache.commons.codec.binary.Hex import Hex

        self.assertEqual([], Hex.decodeHex0([]))

    def testDecodeByteBufferWithLimitOddCharacters(self) -> None:

        bb = self._allocate(10)
        bb[1] = 65
        bb = memoryview(bb)[1:2]
        self.__checkDecodeHexByteBufferOddCharacters(bb)

    def testDecodeByteBufferOddCharacters(self) -> None:

        bb = self._allocate(1)
        bb[0] = 65
        self.__checkDecodeHexByteBufferOddCharacters(bb)

    def testDecodeByteBufferObjectEmpty(self) -> None:

        self.assertListEqual([], (self._decode2(self._allocate(0))))

    def testDecodeByteBufferAllocatedButEmpty(self) -> None:

        bb = self._allocate(10)
        bb = bytearray(bb)
        bb = memoryview(bb)
        bb.release()
        self.assertEqual(list(bb), [])
        self.assertEqual(len(bb), 0)

    def testDecodeByteBufferEmpty(self) -> None:

        self.assertListEqual([], Hex(2, None, None).decode1(self._allocate(0)))

    def testDecodeByteArrayOddCharacters(self) -> None:

        try:
            Hex(2, None, None).decode0([65])
            self.fail(
                "An exception wasn't thrown when trying to decode an odd number of characters"
            )
        except DecoderException:
            pass

    def testDecodeByteArrayObjectEmpty(self) -> None:

        try:
            self.assertEqual(bytearray([]), Hex(2, None, None).decode2(bytearray([])))
        except Exception as e:
            self.fail(f"testDecodeByteArrayObjectEmpty failed: {str(e)}")

    def testDecodeByteArrayEmpty(self) -> None:

        # Create an instance of Hex class
        hex_instance = Hex(2, None, None)

        # Call the decode0 method with an empty byte array
        result = hex_instance.decode0(bytearray())

        # Assert that the result is also an empty byte array
        self.assertEqual(bytearray(), result)

    def testDecodeBadCharacterPos1(self) -> None:

        try:
            Hex(2, None, None).decode2("0q")
            self.fail(
                "An exception wasn't thrown when trying to decode an illegal character"
            )
        except DecoderException:
            pass

    def testDecodeBadCharacterPos0(self) -> None:

        try:
            Hex(2, None, None).decode2("q0")
            self.fail(
                "An exception wasn't thrown when trying to decode an illegal character"
            )
        except DecoderException:
            pass

    def testCustomCharsetToString(self) -> None:

        hex_obj = Hex(2, None, None)
        self.assertTrue(hex_obj.toString().find(Hex.DEFAULT_CHARSET_NAME) >= 0)

    def testCustomCharsetBadName(self) -> None:
        with pytest.raises(ValueError):
            Hex.Hex0(self.__BAD_ENCODING_NAME)

    def testCustomCharset0(self) -> None:

        for name in Charset.availableCharsets().keys():
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
        actualEncodedBytes = customCodec.encode0(list(sourceBytes))
        expectedHexString = Hex.encodeHexString0(list(sourceBytes))
        expectedHexStringBytes = expectedHexString.encode(name)
        assert expectedHexStringBytes == actualEncodedBytes
        actualStringFromBytes = bytes(actualEncodedBytes).decode(name)
        assert (
            expectedHexString == actualStringFromBytes
        ), f"{name}, expectedHexString={expectedHexString}, actualStringFromBytes={actualStringFromBytes}"
        utf8Codec = Hex(2, None, None)
        expectedHexString = "48656c6c6f20576f726c64"
        decodedUtf8Bytes = utf8Codec.decode2(expectedHexString)
        actualStringFromBytes = bytes(decodedUtf8Bytes).decode(utf8Codec.getCharset())
        assert sourceString == actualStringFromBytes
        decodedCustomBytes = customCodec.decode0(actualEncodedBytes)
        actualStringFromBytes = bytes(decodedCustomBytes).decode(name)
        assert sourceString == actualStringFromBytes

    def __log1(self, t: BaseException) -> None:
        if self.__LOG:
            import traceback

            traceback.print_exception(type(t), t, t.__traceback__)
            print(file=sys.stdout, flush=True)

    def __log0(self, s: str) -> None:
        if self.__LOG:
            print(s)
            sys.stdout.flush()

    def __checkDecodeHexCharArrayOddCharacters1(self, data: str) -> None:

        try:
            Hex.decodeHex2(data)
            self.fail(
                "An exception wasn't thrown when trying to decode an odd number of characters"
            )
        except DecoderException:
            pass

    def __checkDecodeHexByteBufferOddCharacters(
        self, data: typing.Union[bytearray, memoryview]
    ) -> None:

        try:
            Hex(2, None, None).decode1(data)
            self.fail(
                "An exception wasn't thrown when trying to decode an odd number of characters"
            )
        except DecoderException:
            pass

    def __checkDecodeHexCharArrayOddCharacters0(self, data: typing.List[str]) -> None:

        try:
            Hex.decodeHex0(data)
            self.fail(
                "An exception wasn't thrown when trying to decode an odd number of characters"
            )
        except DecoderException:
            pass

    def __charsetSanityCheck(self, name: str) -> bool:

        source = "the quick brown dog jumped over the lazy fox"
        try:
            bytes_ = source.encode(name)
            str_ = bytes_.decode(name)
            equals = source == str_
            if not equals:
                self.__log0(
                    "FAILED charsetSanityCheck=Interesting Java charset oddity: Roundtrip"
                    + " failed for "
                    + name
                )
            return equals
        except (UnicodeEncodeError, UnicodeDecodeError) as e:
            if self.__LOG:
                self.__log0("FAILED charsetSanityCheck=" + name + ", e=" + str(e))
                self.__log1(e)
            return False

    def __getByteBufferUtf8(self, string: str) -> typing.Union[bytearray, memoryview]:

        bytes = string.encode("utf-8")
        bb = self._allocate(len(bytes))
        bb[:] = bytes
        return bb
