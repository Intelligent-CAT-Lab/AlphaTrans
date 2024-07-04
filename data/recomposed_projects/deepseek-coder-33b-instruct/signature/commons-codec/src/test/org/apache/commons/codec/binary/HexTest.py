from __future__ import annotations
import re
import random
import sys
import decimal
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

        # Create an instance of Hex with UTF_8 charset
        hex_instance = Hex(1, None, "UTF-8")

        # Assert that the charset name is 'UTF-8'
        self.assertEqual("UTF-8", hex_instance.getCharsetName())

    def testGetCharset(self) -> None:

        # StandardCharsets.UTF_8 is equivalent to 'utf-8' in Python
        self.assertEqual("utf-8", Hex(1, None, "utf-8").getCharset())

    def testEncodeStringEmpty(self) -> None:

        # Create an instance of Hex class
        hex_instance = Hex(2, None, None)

        # Call the encode2 method with an empty string
        result = hex_instance.encode2("")

        # Assert that the result is an empty list
        self.assertEqual(result, [])

    def testEncodeHexReadOnlyByteBuffer(self) -> None:

        # Create a bytearray with a single byte value of 10
        data = bytearray([10])

        # Call the encodeHex6 method
        chars = Hex.encodeHex6(data)

        # Convert the list of characters to a string
        result = "".join(chars)

        # Assert that the result is equal to "0a"
        self.assertEqual("0a", result)

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase(self) -> None:

        bb = self._allocate(4)
        bb[1] = (10).to_bytes(1, byteorder="big")
        bb = bb[1:2]
        self.assertEqual("0A", Hex.encodeHexString3(bb, False))
        self.assertEqual(0, len(bb))

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase(self) -> None:

        bb = self._allocate(4)
        bb[1] = (10).to_bytes(1, byteorder="big")
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

        self.assertEqual("0A", self.encodeHexString1([10], False))

    def testEncodeHexByteString_ByteArrayBoolean_ToLowerCase(self) -> None:

        self.assertEqual("0a", self.encodeHexString1([10], True))

    def testEncodeHexByteString_ByteArrayOfZeroes(self) -> None:

        c = Hex.encodeHexString0([0] * 36)
        self.assertEqual(
            "000000000000000000000000000000000000000000000000000000000000000000000000",
            c,
        )

    def testEncodeHexByteString_ByteBufferOfZeroesWithLimit(self) -> None:

        # Create a bytearray with capacity 36
        bb = bytearray(36)

        # Set the limit to 3
        bb = bb[:3]

        # Encode the bytearray to hexadecimal string
        hex_str = Hex.encodeHexString2(bb)

        # Assert that the hexadecimal string is "000000"
        self.assertEqual("000000", hex_str)

        # Assert that there are no remaining elements in the bytearray
        self.assertEqual(0, len(bb))

        # Set the position to 1 and limit to 3
        bb = bb[1:3]

        # Encode the bytearray to hexadecimal string
        hex_str = Hex.encodeHexString2(bb)

        # Assert that the hexadecimal string is "0000"
        self.assertEqual("0000", hex_str)

        # Assert that there are no remaining elements in the bytearray
        self.assertEqual(0, len(bb))

    def testEncodeHexByteString_ByteBufferOfZeroes(self) -> None:

        # Create a bytearray of zeroes with the desired capacity
        data = bytearray(36)

        # Call the encodeHexString2 method
        c = Hex.encodeHexString2(data)

        # Assert that the result is as expected
        self.assertEqual(
            "000000000000000000000000000000000000000000000000000000000000000000000000",
            c,
        )

    def testEncodeHexPartialInputOverbounds(self) -> None:

        data = "hello world".encode("utf-8")

        with self.assertRaises(ArrayIndexOutOfBoundsException):
            hex = Hex.encodeHex3(data, 9, 10, True)
            self.assertEqual(list("64"), hex)

    def testEncodeHexPartialInputUnderbounds(self) -> None:

        data = "hello world".encode("utf-8")

        with pytest.raises(ArrayIndexOutOfBoundsException):
            hex = Hex.encodeHex3(data, -2, 10, True)
            self.assertEqual(list("64"), hex)

    def testEncodeHexPartialInput(self) -> None:

        data = "hello world".encode("utf-8")

        hex = Hex.encodeHex3(data, 0, 0, True)
        self.assertEqual(hex, [])

        hex = Hex.encodeHex3(data, 0, 1, True)
        self.assertEqual(hex, list("68"))

        hex = Hex.encodeHex3(data, 0, 1, False)
        self.assertEqual(hex, list("68"))

        hex = Hex.encodeHex3(data, 2, 4, True)
        self.assertEqual(hex, list("6c6c6f20"))

        hex = Hex.encodeHex3(data, 2, 4, False)
        self.assertEqual(hex, list("6C6C6F20"))

        hex = Hex.encodeHex3(data, 10, 1, True)
        self.assertEqual(hex, list("64"))

        hex = Hex.encodeHex3(data, 10, 1, False)
        self.assertEqual(hex, list("64"))

    def testEncodeHex_ByteBufferWithLimit(self) -> None:

        bb = self._allocate(16)
        for i in range(16):
            bb[i] = i
        bb = bb[:16]
        expected = "000102030405060708090a0b0c0d0e0f"
        for i in range(15):
            sub_bb = bb[i : i + 2]
            encoded = "".join(Hex.encodeHex6(sub_bb))
            assert encoded == expected[i * 2 : i * 2 + 4]
            assert len(sub_bb) == 0

    def testEncodeHex_ByteBufferOfZeroes(self) -> None:

        c = Hex.encodeHex6(self._allocate(36))
        self.assertEqual(
            "000000000000000000000000000000000000000000000000000000000000000000000000",
            "".join(c),
        )

    def testEncodeHexByteBufferHelloWorldUpperCaseHex(self) -> None:

        b = self.__getByteBufferUtf8("Hello World")
        expected = "48656C6C6F20576F726C64"
        actual = Hex.encodeHex6(b)
        self.assertEqual(expected.lower(), "".join(actual))
        self.assertEqual(0, len(b))
        b = self.__getByteBufferUtf8("Hello World")
        actual = Hex.encodeHex7(b, True)
        self.assertEqual(expected.lower(), "".join(actual))
        self.assertEqual(0, len(b))
        b = self.__getByteBufferUtf8("Hello World")
        actual = Hex.encodeHex7(b, False)
        self.assertEqual(expected, "".join(actual))
        self.assertEqual(0, len(b))

    def testEncodeHexByteBufferHelloWorldLowerCaseHex(self) -> None:

        # Create a bytearray from the string "Hello World"
        b = bytearray("Hello World", "utf-8")

        # Expected result
        expected = "48656c6c6f20576f726c64"

        # Call the encodeHex6 method
        actual = Hex.encodeHex6(b)

        # Convert the list of strings to a string
        actual_str = "".join(actual)

        # Check if the actual result is equal to the expected result
        self.assertEqual(expected, actual_str)

        # Check if the remaining bytes in the bytearray is 0
        self.assertEqual(0, len(b))

        # Reset the bytearray position
        b = bytearray("Hello World", "utf-8")

        # Call the encodeHex7 method with toLowerCase set to True
        actual = Hex.encodeHex7(b, True)

        # Convert the list of strings to a string
        actual_str = "".join(actual)

        # Check if the actual result is equal to the expected result
        self.assertEqual(expected, actual_str)

        # Check if the remaining bytes in the bytearray is 0
        self.assertEqual(0, len(b))

        # Reset the bytearray position
        b = bytearray("Hello World", "utf-8")

        # Call the encodeHex7 method with toLowerCase set to False
        actual = Hex.encodeHex7(b, False)

        # Convert the list of strings to a string
        actual_str = "".join(actual)

        # Check if the actual result is equal to the expected result
        self.assertEqual(expected.upper(), actual_str)

        # Check if the remaining bytes in the bytearray is 0
        self.assertEqual(0, len(b))

    def testEncodeHexByteBufferEmpty(self) -> None:

        # Testing Hex.encodeHex6
        assert Hex.encodeHex6(self._allocate(0)) == []

        # Testing Hex.encode1
        assert Hex(2, None, None).encode1(self._allocate(0)) == []

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
        self.assertEqual(expected, "".join(actual))
        actual = Hex.encodeHex1(b, True)
        self.assertEqual(expected, "".join(actual))
        actual = Hex.encodeHex1(b, False)
        self.assertNotEqual(expected, "".join(actual))

    def testEncodeHexByteArrayEmpty(self) -> None:

        # Testing encodeHex0 method
        self.assertEqual([], Hex.encodeHex0([]))

        # Testing encode0 method
        self.assertEqual([], Hex(2, None, None).encode0([]))

    def testEncodeDecodeHexCharArrayRandomToOutput(self) -> None:

        for i in range(5, 0, -1):
            data = os.urandom(random.randint(1, 10000))

            lowerEncodedChars = [""] * (len(data) * 2)
            Hex.encodeHex4(data, 0, len(data), True, lowerEncodedChars, 0)
            decodedLowerCaseBytes = Hex.decodeHex0(lowerEncodedChars)
            self.assertEqual(data, decodedLowerCaseBytes)

            upperEncodedChars = [""] * (len(data) * 2)
            Hex.encodeHex4(data, 0, len(data), False, upperEncodedChars, 0)
            decodedUpperCaseBytes = Hex.decodeHex0(upperEncodedChars)
            self.assertEqual(data, decodedUpperCaseBytes)

    def testEncodeDecodeHexCharArrayRandom(self) -> None:

        hex = Hex(2, None, None)
        for i in range(5, 0, -1):
            data = bytearray(os.urandom(random.randint(1, 10000)))

            encoded_chars = Hex.encodeHex0(data)
            decoded_bytes = Hex.decodeHex0(encoded_chars)
            self.assertEqual(data, decoded_bytes)

            encoded_string_bytes = hex.encode0(data)
            decoded_bytes = hex.decode0(encoded_string_bytes)
            self.assertEqual(data, decoded_bytes)

            data_string = "".join(encoded_chars)
            encoded_string_chars = hex.encode2(data_string)
            decoded_bytes = hex.decode2(encoded_string_chars)
            self.assertEqual(StringUtils.getBytesUtf8(data_string), decoded_bytes)

            data_string = "".join(encoded_chars)
            encoded_string_chars = hex.encode2(data_string)
            decoded_bytes = hex.decode2("".join(encoded_string_chars))
            self.assertEqual(StringUtils.getBytesUtf8(data_string), decoded_bytes)

    def testEncodeClassCastException(self) -> None:

        try:
            Hex(2, None, None).encode2([65])
            self.fail("An exception wasn't thrown when trying to encode.")
        except EncoderException:
            pass

    def testEncodeByteBufferObjectEmpty(self) -> None:

        # Create an instance of Hex class
        hex_obj = Hex(2, None, None)

        # Call the allocate method to get an empty byte buffer
        byte_buffer = self._allocate(0)

        # Encode the byte buffer using the encode2 method
        encoded_buffer = hex_obj.encode2(byte_buffer)

        # Convert the encoded buffer to a list of characters
        encoded_buffer_chars = list(encoded_buffer)

        # Assert that the encoded buffer is empty
        self.assertEqual([], encoded_buffer_chars)

    def testEncodeByteBufferAllocatedButEmpty(self) -> None:

        pass  # LLM could not translate this method

    def testEncodeByteBufferEmpty(self) -> None:

        # Create an instance of Hex class
        hex_instance = Hex(2, None, None)

        # Call the allocate method to get an empty byte array
        empty_byte_array = self._allocate(0)

        # Call the encode1 method with the empty byte array
        result = hex_instance.encode1(empty_byte_array)

        # Assert that the result is an empty list
        self.assertEqual(result, [])

    def testEncodeByteArrayObjectEmpty(self) -> None:

        # Create an instance of Hex with default parameters
        hex_instance = Hex(2, None, None)

        # Call the encode2 method with an empty byte array
        result = hex_instance.encode2(bytearray([]))

        # Assert that the result is an empty list
        self.assertEqual(list(result), [])

    def testEncodeByteArrayEmpty(self) -> None:

        # Create an instance of Hex class
        hex_instance = Hex(2, None, None)

        # Call the encode0 method with an empty byte array
        result = hex_instance.encode0(bytearray())

        # Assert that the result is also an empty byte array
        self.assertEqual(bytearray(), result)

    def testDecodeByteBufferWithLimit(self) -> None:

        bb = self.__getByteBufferUtf8("000102030405060708090a0b0c0d0e0f")
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        for i in range(15):
            bb.position = i * 2
            bb.limit = i * 2 + 4
            self.assertEqual(
                "".join(map(str, expected[i : i + 2])),
                "".join(map(str, Hex(2, None, None).decode1(bb))),
            )
            self.assertEqual(0, bb.remaining())

    def testDecodeStringEmpty(self) -> None:

        # Create an instance of Hex class
        hex_instance = Hex(2, None, None)

        # Call the decode2 method with an empty string
        result = hex_instance.decode2("")

        # Assert that the result is an empty byte array
        self.assertEqual(result, bytearray())

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
        with pytest.raises(DecoderException):
            Hex.decodeHex1(list("aabbccddeeff"), out, 0)

    def testDecodeHexCharArrayOddCharacters5(self) -> None:
        self.__checkDecodeHexCharArrayOddCharacters0(["A", "B", "C", "D", "E"])

    def testDecodeHexCharArrayOddCharacters3(self) -> None:
        self.__checkDecodeHexCharArrayOddCharacters0(["A", "B", "C"])

    def testDecodeHexStringOddCharacters1(self) -> None:

        self.__checkDecodeHexCharArrayOddCharacters1("A")

    def testDecodeHexCharArrayOddCharacters1(self) -> None:
        self.__checkDecodeHexCharArrayOddCharacters0(["A"])

    def testDecodeClassCastException(self) -> None:

        try:
            Hex(2, None, None).decode2([65])
            self.fail("An exception wasn't thrown when trying to decode.")
        except DecoderException:
            pass

    def testDecodeHexStringEmpty(self) -> None:

        # The Hex.decodeHex2 method is not implemented in the provided partial Python translation.
        # Assuming it's a static method in the Hex class, we can call it directly.
        # If it's not a static method, you need to create an instance of the Hex class.

        self.assertEqual([], Hex.decodeHex2(""))

    def testDecodeHexCharArrayEmpty(self) -> None:

        # The Java code is using the assertArrayEquals method from JUnit to compare two arrays.
        # In Python, we can use the built-in list comparison to achieve the same result.
        self.assertEqual([], Hex.decodeHex0([]))

    def testDecodeByteBufferWithLimitOddCharacters(self) -> None:

        bb = self._allocate(10)
        bb[1] = 65
        bb.position = 1
        bb.limit = 2
        self.__checkDecodeHexByteBufferOddCharacters(bb)

    def testDecodeByteBufferOddCharacters(self) -> None:

        bb = self._allocate(1)
        bb[0] = 65
        self.__checkDecodeHexByteBufferOddCharacters(bb)

    def testDecodeByteBufferObjectEmpty(self) -> None:

        # Create an instance of Hex class
        hex_obj = Hex(2, None, None)

        # Call the allocate method
        byte_buffer = self._allocate(0)

        # Call the decode2 method
        decoded_bytes = hex_obj.decode2(byte_buffer)

        # Assert that the decoded bytes are equal to an empty byte array
        self.assertEqual(bytearray([]), decoded_bytes)

    def testDecodeByteBufferAllocatedButEmpty(self) -> None:

        bb = self._allocate(10)
        bb.flip()
        self.assertListEqual([], Hex(2, None, None).decode1(bb))
        self.assertEqual(0, bb.remaining())

    def testDecodeByteBufferEmpty(self) -> None:

        # Create an instance of Hex class
        hex_instance = Hex(2, None, None)

        # Call the allocate method to get an empty buffer
        buffer = self._allocate(0)

        # Call the decode1 method with the empty buffer
        result = hex_instance.decode1(buffer)

        # Assert that the result is an empty list
        self.assertEqual(result, [])

    def testDecodeByteArrayOddCharacters(self) -> None:

        try:
            Hex(2, None, None).decode0([65])
            self.fail(
                "An exception wasn't thrown when trying to decode an odd number of characters"
            )
        except DecoderException:
            pass

    def testDecodeByteArrayObjectEmpty(self) -> None:

        # Create an instance of Hex with default parameters
        hex_instance = Hex(2, None, None)

        # Call the decode2 method with an empty byte array
        result = hex_instance.decode2(bytearray(b""))

        # Assert that the result is an empty byte array
        self.assertEqual(bytearray(b""), result)

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

        # Create an instance of Hex with default charset
        hex_instance = Hex(2, None, None)

        # Check if the default charset name is in the string representation of the Hex instance
        self.assertTrue(hex_instance.toString().find(Hex.DEFAULT_CHARSET_NAME) >= 0)

    def testCustomCharsetBadName(self) -> None:
        with pytest.raises(UnsupportedCharsetException):
            Hex.Hex0(self.__BAD_ENCODING_NAME)

    def testCustomCharset0(self) -> None:

        for name in unicodedata.ucd.normalized_property("name"):
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
        assert expectedHexStringBytes == actualEncodedBytes

        actualStringFromBytes = actualEncodedBytes.decode(name)
        assert (
            expectedHexString == actualStringFromBytes
        ), f"{name}, expectedHexString={expectedHexString}, actualStringFromBytes={actualStringFromBytes}"

        utf8Codec = Hex(2, None, None)
        expectedHexString = "48656c6c6f20576f726c64"
        decodedUtf8Bytes = utf8Codec.decode2(expectedHexString)
        actualStringFromBytes = decodedUtf8Bytes.decode(utf8Codec.getCharset())
        assert sourceString == actualStringFromBytes

        decodedCustomBytes = customCodec.decode0(actualEncodedBytes)
        actualStringFromBytes = decodedCustomBytes.decode(name)
        assert sourceString == actualStringFromBytes

    def __log1(self, t: BaseException) -> None:
        if self.__LOG:
            import traceback

            traceback.print_exception(t)
            sys.stdout.flush()

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
        bb = bytearray(bytes)
        return bb
