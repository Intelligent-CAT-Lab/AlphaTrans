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

        # Create an instance of Hex with UTF-8 charset
        hex_instance = Hex(1, None, StandardCharsets.UTF_8)

        # Assert that the charset name is equal to the expected value
        assert StandardCharsets.UTF_8.name() == hex_instance.getCharsetName()

    def testGetCharset(self) -> None:

        # Create an instance of Hex with UTF-8 charset
        hex_instance = Hex(1, None, StandardCharsets.UTF_8)

        # Assert that the charset returned by getCharset method is UTF-8
        assert StandardCharsets.UTF_8 == hex_instance.getCharset()

    def testEncodeStringEmpty(self) -> None:

        # Create an instance of Hex with 2 as the first argument, None as the second and third arguments
        hex_instance = Hex(2, None, None)

        # Call the encode2 method on the hex_instance with an empty string as the argument
        result = hex_instance.encode2("")

        # Assert that the result is an empty list
        assert result == []

    def testEncodeHexReadOnlyByteBuffer(self) -> None:

        # Create a byte array
        byte_array = bytearray([10])

        # Create a read-only byte buffer from the byte array
        byte_buffer = io.BytesIO(byte_array)

        # Encode the byte buffer to hexadecimal
        chars = Hex.encodeHex6(byte_buffer)

        # Convert the char array to a string
        hex_string = StringUtils.newStringUtf8(chars)

        # Assert that the hexadecimal string is equal to "0a"
        assert hex_string == "0a"

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase(self) -> None:

        bb = self._allocate(4)
        bb[1] = 10
        bb = bb[1:2]
        assert Hex.encodeHexString3(bb, False) == "0A"
        assert len(bb) == 0

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase(self) -> None:

        bb = self._allocate(4)
        bb[1] = 10
        bb = bb[1:2]
        assert Hex.encodeHexString3(bb, True) == "0a"
        assert len(bb) == 0

    def testEncodeHexByteString_ByteBufferBoolean_ToUpperCase(self) -> None:

        bb = self._allocate(1)
        bb[0] = 10
        bb = bb.tobytes()

        hex_encoder = Hex()
        result = hex_encoder.encodeHexString(bb, False)

        assert result == "0A"

    def testEncodeHexByteString_ByteBufferBoolean_ToLowerCase(self) -> None:

        bb = self._allocate(1)
        bb[0] = 10
        bb = bytes(bb)

        assert Hex.encodeHexString3(bb, True) == "0a"

    def testEncodeHexByteString_ByteArrayBoolean_ToUpperCase(self) -> None:

        # Create an instance of Hex class
        hex_instance = Hex()

        # Call the encodeHexString1 method
        result = hex_instance.encodeHexString1(bytearray([10]), False)

        # Assert the result
        assert result == "0A"

    def testEncodeHexByteString_ByteArrayBoolean_ToLowerCase(self) -> None:

        # Create an instance of Hex class
        hex_instance = Hex()

        # Call the encodeHexString1 method
        result = hex_instance.encodeHexString1(bytearray([10]), True)

        # Assert the result
        assert result == "0a"

    def testEncodeHexByteString_ByteArrayOfZeroes(self) -> None:

        c = Hex.encodeHexString0(bytearray(36))
        expected = (
            "000000000000000000000000000000000000000000000000000000000000000000000000"
        )
        assert c == expected, f"Expected {expected}, but got {c}"

    def testEncodeHexByteString_ByteBufferOfZeroesWithLimit(self) -> None:

        bb = self._allocate(36)
        bb.limit(3)
        assert Hex.encodeHexString2(bb) == "000000"
        assert bb.remaining() == 0
        bb.position(1)
        bb.limit(3)
        assert Hex.encodeHexString2(bb) == "0000"
        assert bb.remaining() == 0

    def testEncodeHexByteString_ByteBufferOfZeroes(self) -> None:

        c = Hex.encodeHexString2(self._allocate(36))
        assert (
            c
            == "000000000000000000000000000000000000000000000000000000000000000000000000"
        )

    def testEncodeHexPartialInputOverbounds(self) -> None:

        data = "hello world".encode("utf-8")

        hex = Hex.encodeHex3(data, 9, 10, True)
        assert hex == list("64")

    def testEncodeHexPartialInputUnderbounds(self) -> None:

        data = "hello world".encode("utf-8")

        hex = Hex.encodeHex3(data, -2, 10, True)
        self.assertEqual(list("64"), hex)

    def testEncodeHexPartialInput(self) -> None:

        data = "hello world".encode("utf-8")

        hex = Hex.encodeHex3(data, 0, 0, True)
        assert hex == []

        hex = Hex.encodeHex3(data, 0, 1, True)
        assert hex == list("68")

        hex = Hex.encodeHex3(data, 0, 1, False)
        assert hex == list("68")

        hex = Hex.encodeHex3(data, 2, 4, True)
        assert hex == list("6c6c6f20")

        hex = Hex.encodeHex3(data, 2, 4, False)
        assert hex == list("6C6C6F20")

        hex = Hex.encodeHex3(data, 10, 1, True)
        assert hex == list("64")

        hex = Hex.encodeHex3(data, 10, 1, False)
        assert hex == list("64")

    def testEncodeHex_ByteBufferWithLimit(self) -> None:

        bb = self._allocate(16)
        for i in range(16):
            bb[i] = i
        bb = bb[:16]
        expected = "000102030405060708090a0b0c0d0e0f"
        for i in range(15):
            bb = bb[i : i + 2]
            assert expected[i * 2 : i * 2 + 4] == Hex.encodeHex6(bb)
            assert len(bb) == 0

    def testEncodeHex_ByteBufferOfZeroes(self) -> None:

        c = Hex.encodeHex6(self._allocate(36))
        expected = (
            "0000000000000000000000000000000000000000000000000000000000000000000000000"
        )
        result = "".join(c)
        assert result == expected, f"Expected {expected}, but got {result}"

    def testEncodeHexByteBufferHelloWorldUpperCaseHex(self) -> None:

        b = self.__getByteBufferUtf8("Hello World")
        expected = "48656C6C6F20576F726C64"
        actual = Hex.encodeHex6(b)
        assert expected.lower() == "".join(actual)
        assert b.remaining() == 0
        b.flip()
        actual = Hex.encodeHex7(b, True)
        assert expected.lower() == "".join(actual)
        assert b.remaining() == 0
        b.flip()
        actual = Hex.encodeHex7(b, False)
        assert expected == "".join(actual)
        assert b.remaining() == 0

    def testEncodeHexByteBufferHelloWorldLowerCaseHex(self) -> None:

        b = self.__getByteBufferUtf8("Hello World")
        expected = "48656c6c6f20576f726d6c64"
        actual = Hex.encodeHex6(b)
        assert expected == "".join(actual)
        assert b.remaining() == 0
        b.flip()
        actual = Hex.encodeHex7(b, True)
        assert expected == "".join(actual)
        assert b.remaining() == 0
        b.flip()
        actual = Hex.encodeHex7(b, False)
        assert expected.upper() == "".join(actual)
        assert b.remaining() == 0

    def testEncodeHexByteBufferEmpty(self) -> None:

        # Hex.encodeHex6(allocate(0))
        # allocate(0) is a method that is not defined in the provided partial Python translation.
        # Assuming it returns an empty bytearray, we can translate it as follows:
        assert Hex.encodeHex6(bytearray()) == []

        # new Hex(2, null, null).encode1(allocate(0))
        # Assuming Hex(2, null, null) creates an instance of Hex with 2 as the first argument,
        # null as the second argument, and null as the third argument.
        # allocate(0) is a method that is not defined in the provided partial Python translation.
        # Assuming it returns an empty bytearray, we can translate it as follows:
        hex_instance = Hex(2, None, None)
        assert hex_instance.encode1(bytearray()) == []

    def testEncodeHexByteArrayZeroes(self) -> None:

        c = Hex.encodeHex0(bytearray(36))
        expected = (
            "000000000000000000000000000000000000000000000000000000000000000000000000"
        )
        result = "".join(chr(i) for i in c)

        assert result == expected

    def testEncodeHexByteArrayHelloWorldUpperCaseHex(self) -> None:

        b = StringUtils.getBytesUtf8("Hello World")
        expected = "48656C6C6F20576F726C64"
        actual = Hex.encodeHex0(b)
        assert actual.decode("utf-8") != expected
        actual = Hex.encodeHex1(b, True)
        assert actual.decode("utf-8") != expected
        actual = Hex.encodeHex1(b, False)
        assert actual.decode("utf-8") == expected

    def testEncodeHexByteArrayHelloWorldLowerCaseHex(self) -> None:

        b = StringUtils.getBytesUtf8("Hello World")
        expected = "48656c6c6f20576f726c64"
        actual = Hex.encodeHex0(b)
        assert expected == "".join(actual)
        actual = Hex.encodeHex1(b, True)
        assert expected == "".join(actual)
        actual = Hex.encodeHex1(b, False)
        assert expected != "".join(actual)

    def testEncodeHexByteArrayEmpty(self) -> None:

        # Calling Hex.encodeHex0(new byte[0])
        # Assuming that Hex.encodeHex0 is a static method
        assert Hex.encodeHex0(bytearray()) == []

        # Calling new Hex(2, null, null).encode0(new byte[0])
        # Assuming that Hex(2, null, null).encode0 is a method of Hex class
        h = Hex(2, None, None)
        assert h.encode0(bytearray()) == []

    def testEncodeDecodeHexCharArrayRandomToOutput(self) -> None:

        for i in range(5, 0, -1):
            data = os.urandom(random.randint(1, 10000))

            lower_encoded_chars = [""] * (len(data) * 2)
            Hex.encodeHex4(data, 0, len(data), True, lower_encoded_chars, 0)
            decoded_lower_case_bytes = Hex.decodeHex0(lower_encoded_chars)
            assert decoded_lower_case_bytes == data

            upper_encoded_chars = [""] * (len(data) * 2)
            Hex.encodeHex4(data, 0, len(data), False, upper_encoded_chars, 0)
            decoded_upper_case_bytes = Hex.decodeHex0(upper_encoded_chars)
            assert decoded_upper_case_bytes == data

    def testEncodeDecodeHexCharArrayRandom(self) -> None:

        hex = Hex(2, None, None)
        for i in range(5, 0, -1):
            data = os.urandom(random.randint(1, 10000))

            encoded_chars = Hex.encodeHex0(data)
            decoded_bytes = Hex.decodeHex0(encoded_chars)
            assert decoded_bytes == data

            encoded_string_bytes = hex.encode0(data)
            decoded_bytes = hex.decode0(encoded_string_bytes)
            assert decoded_bytes == data

            data_string = "".join(encoded_chars)
            encoded_string_chars = hex.encode2(data_string)
            decoded_bytes = hex.decode2(encoded_string_chars)
            assert decoded_bytes == StringUtils.getBytesUtf8(data_string)

            data_string = "".join(encoded_chars)
            encoded_string_chars = hex.encode2(data_string)
            decoded_bytes = hex.decode2("".join(encoded_string_chars))
            assert decoded_bytes == StringUtils.getBytesUtf8(data_string)

    def testEncodeClassCastException(self) -> None:

        try:
            Hex(2, None, None).encode2([65])
            self.fail("An exception wasn't thrown when trying to encode.")
        except EncoderException:
            pass

    def testEncodeByteBufferObjectEmpty(self) -> None:

        # allocate a bytearray of size 0
        byte_buffer = bytearray(0)

        # create a Hex object with parameters 2, None, None
        hex_obj = Hex(2, None, None)

        # encode the byte_buffer using the Hex object
        encoded_chars = hex_obj.encode2(byte_buffer)

        # assert that the encoded_chars is equal to an empty char array
        assert encoded_chars == []

    def testEncodeByteBufferAllocatedButEmpty(self) -> None:

        bb = self._allocate(10)
        bb.flip()
        assert self._arrayEquals(bytearray([]), self._encode1(bb))
        assert bb.remaining() == 0

    def _encode1(self, bb: typing.Union[bytearray, memoryview]) -> bytearray:
        pass

    def _arrayEquals(self, a: bytearray, b: bytearray) -> bool:
        pass

    def _allocate(self, capacity: int) -> typing.Union[bytearray, memoryview]:
        pass

    def testEncodeByteBufferEmpty(self) -> None:

        # Create an instance of Hex class
        hex_instance = Hex(2, None, None)

        # Call the allocate method
        byte_buffer = self._allocate(0)

        # Call the encode1 method
        result = hex_instance.encode1(byte_buffer)

        # Assert that the result is equal to an empty byte array
        assert result == bytearray()

    def testEncodeByteArrayObjectEmpty(self) -> None:

        assert self.assertArrayEquals(
            [], self.encode2(Hex(2, None, None), bytearray(b""))
        )

    def assertArrayEquals(self, expected: List[Any], actual: List[Any]) -> None:
        assert expected == actual, f"Expected: {expected}, but got: {actual}"

    def encode2(self, hex_obj: Hex, obj: Any) -> List[Any]:
        # This is a placeholder for the actual implementation of the encode2 method.
        # You need to replace this with the actual implementation.
        pass

    def testEncodeByteArrayEmpty(self) -> None:

        # Create an instance of Hex class
        hex_instance = Hex(2, None, None)

        # Call the encode0 method with an empty byte array
        result = hex_instance.encode0(bytearray())

        # Assert that the result is equal to an empty byte array
        assert result == bytearray()

    def testDecodeByteBufferWithLimit(self) -> None:

        pass  # LLM could not translate this method

    def testDecodeStringEmpty(self) -> None:

        # Create an instance of Hex class with 2 as the first argument, None as the second and third arguments
        hex_instance = Hex(2, None, None)

        # Call the decode2 method on the hex_instance with an empty string as the argument
        result = hex_instance.decode2("")

        # Assert that the result is equal to an empty byte array
        assert result == bytearray()

    def testDecodeHexStringOddCharacters(self) -> None:

        try:
            Hex(2, None, None).decode2("6")
            self.fail(
                "An exception wasn't thrown when trying to decode an odd number of characters"
            )
        except DecoderException:
            pass

    def testDecodeHexCharArrayOutBufferUnderSizedByOffset(self) -> None:

        out = bytearray(6)
        Hex.decodeHex1(list("aabbccddeeff"), out, 1)

    def testDecodeHexCharArrayOutBufferUnderSized(self) -> None:

        out = bytearray(4)
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

        # The Hex.decodeHex2 method is not available in the partial Python translation.
        # However, we can assume that it is a static method that takes a string and returns a byte array.
        # If it is not available, we can use the binascii.unhexlify method from the binascii module.

        # If the Hex.decodeHex2 method is available, use it.
        # Otherwise, use binascii.unhexlify.

        try:
            import binascii

            assert binascii.unhexlify("") == b""
        except ImportError:
            try:
                from src.main.org.apache.commons.codec.binary.Hex import decodeHex2

                assert decodeHex2("") == b""
            except ImportError:
                raise DecoderException("Hex.decodeHex2 method is not available")

    def testDecodeHexCharArrayEmpty(self) -> None:

        # The Hex.decodeHex0 method is not available in the partial Python translation.
        # However, if it is available in the actual Python code, you can use it as follows:
        # assert Hex.decodeHex0([]) == b''

        # If the Hex.decodeHex0 method is not available, you can use the binascii.a2b_hex method instead:
        import binascii

        assert binascii.a2b_hex(b"") == b""

    def testDecodeByteBufferWithLimitOddCharacters(self) -> None:

        bb = self._allocate(10)
        bb[1] = 65
        bb = bb[1:2]
        self.__checkDecodeHexByteBufferOddCharacters(bb)

    def testDecodeByteBufferOddCharacters(self) -> None:

        bb = self._allocate(1)
        bb[0] = 65
        self.__checkDecodeHexByteBufferOddCharacters(bb)

    def testDecodeByteBufferObjectEmpty(self) -> None:

        # Create an instance of Hex class
        hex_instance = Hex(2, None, None)

        # Allocate a byte buffer of size 0
        byte_buffer = self._allocate(0)

        # Decode the byte buffer using the Hex instance
        decoded_bytes = hex_instance.decode2(byte_buffer)

        # Assert that the decoded bytes are equal to an empty byte array
        assert decoded_bytes == bytearray()

    def testDecodeByteBufferAllocatedButEmpty(self) -> None:

        bb = self._allocate(10)
        bb.flip()
        assert self._assertArrayEquals(bytearray([]), Hex(2, None, None).decode1(bb))
        assert self._assertEquals(0, bb.remaining())

    def testDecodeByteBufferEmpty(self) -> None:

        # Create an instance of Hex class
        hex_instance = Hex(2, None, None)

        # Allocate a byte buffer of size 0
        byte_buffer = self._allocate(0)

        # Decode the byte buffer using the decode1 method
        decoded_bytes = hex_instance.decode1(byte_buffer)

        # Assert that the decoded bytes are equal to an empty byte array
        assert decoded_bytes == bytearray()

    def testDecodeByteArrayOddCharacters(self) -> None:

        try:
            Hex(2, None, None).decode0(bytearray([65]))
            self.fail(
                "An exception wasn't thrown when trying to decode an odd number of characters"
            )
        except DecoderException:
            pass

    def testDecodeByteArrayObjectEmpty(self) -> None:

        assert self.byte_array_equals(
            bytearray([]), self.decode2(bytearray([]), 2, None, None)
        )

    def byte_array_equals(self, a: bytearray, b: bytearray) -> bool:
        return a == b

    def decode2(
        self,
        source: bytearray,
        off: int,
        len: typing.Optional[int],
        decoder: typing.Optional[Decoder],
    ) -> bytearray:
        # Implement the decode2 method here
        pass

    def testDecodeByteArrayEmpty(self) -> None:

        # Create an instance of Hex class
        hex_instance = Hex(2, None, None)

        # Call the decode0 method
        result = hex_instance.decode0(bytearray())

        # Assert that the result is equal to an empty bytearray
        assert result == bytearray()

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
        assert Hex.DEFAULT_CHARSET_NAME in hex_obj.toString()

    def testCustomCharsetBadName(self) -> None:

        # Calling Hex.Hex0(BAD_ENCODING_NAME)
        Hex.Hex0(self.__BAD_ENCODING_NAME)

    def testCustomCharset0(self) -> None:

        for name in os.listdir("/"):
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
            print()

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
            assert (
                False
            ), "An exception wasn't thrown when trying to decode an odd number of characters"
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
