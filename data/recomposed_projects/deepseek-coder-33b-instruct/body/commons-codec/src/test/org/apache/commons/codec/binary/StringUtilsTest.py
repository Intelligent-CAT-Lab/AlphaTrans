from __future__ import annotations
import re
from abc import ABC
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.binary.StringUtils import *


class StringUtilsTest(unittest.TestCase):

    __STRING_FIXTURE: str = "ABC"
    __BYTES_FIXTURE_16LE: typing.List[int] = [ord("a"), 0, ord("b"), 0, ord("c"), 0]
    __BYTES_FIXTURE_16BE: typing.List[int] = [0, ord("a"), 0, ord("b"), 0, ord("c")]
    __BYTES_FIXTURE: typing.List[int] = [ord("a"), ord("b"), ord("c")]

    def testByteBufferUtf8(self) -> None:

        self.assertIsNone(StringUtils.getByteBufferUtf8(None), "Should be null safe")

        text = "asdhjfhsadiogasdjhagsdygfjasfgsdaksjdhfk"
        bb = StringUtils.getByteBufferUtf8(text)

        self.assertEqual(bb, bytearray(text.encode("utf-8")))

    def testEqualsCS2(self) -> None:

        self.assertTrue(StringUtils.equals("abc", "abc"))
        self.assertFalse(StringUtils.equals("abc", "abcd"))
        self.assertFalse(StringUtils.equals("abcd", "abc"))
        self.assertFalse(StringUtils.equals("abc", "ABC"))

    def testEqualsCS1(self) -> None:

        self.assertFalse(StringUtils.equals(StringBuilder("abc"), None))
        self.assertFalse(StringUtils.equals(None, StringBuilder("abc")))
        self.assertTrue(StringUtils.equals(StringBuilder("abc"), StringBuilder("abc")))
        self.assertFalse(
            StringUtils.equals(StringBuilder("abc"), StringBuilder("abcd"))
        )
        self.assertFalse(
            StringUtils.equals(StringBuilder("abcd"), StringBuilder("abc"))
        )
        self.assertFalse(StringUtils.equals(StringBuilder("abc"), StringBuilder("ABC")))

    def testEqualsString(self) -> None:

        self.assertTrue(StringUtils.equals(None, None))
        self.assertFalse(StringUtils.equals("abc", None))
        self.assertFalse(StringUtils.equals(None, "abc"))
        self.assertTrue(StringUtils.equals("abc", "abc"))
        self.assertFalse(StringUtils.equals("abc", "abcd"))
        self.assertFalse(StringUtils.equals("abcd", "abc"))
        self.assertFalse(StringUtils.equals("abc", "ABC"))

    def testNewStringUtf8(self) -> None:
        charsetName = "UTF-8"
        self.__testNewString(charsetName)
        expected = bytes(self.__BYTES_FIXTURE).decode(charsetName)
        actual = StringUtils.newStringUtf8(self.__BYTES_FIXTURE)
        self.assertEqual(expected, actual)

    def testNewStringUtf16Le(self) -> None:
        charsetName = "UTF-16LE"
        self.__testNewString(charsetName)
        expected = bytes(self.__BYTES_FIXTURE_16LE).decode(charsetName)
        actual = StringUtils.newStringUtf16Le(self.__BYTES_FIXTURE_16LE)
        self.assertEqual(expected, actual)

    def testNewStringUtf16Be(self) -> None:
        charsetName = "UTF-16BE"
        self.__testNewString(charsetName)
        expected = bytes(self.__BYTES_FIXTURE_16BE).decode(charsetName)
        actual = StringUtils.newStringUtf16Be(self.__BYTES_FIXTURE_16BE)
        self.assertEqual(expected, actual)

    def testNewStringUtf16(self) -> None:
        charsetName = "UTF-16"
        self.__testNewString(charsetName)
        expected = bytes(self.__BYTES_FIXTURE).decode(charsetName)
        actual = StringUtils.newStringUtf16(self.__BYTES_FIXTURE)
        self.assertEqual(expected, actual)

    def testNewStringUsAscii(self) -> None:
        charsetName = "US-ASCII"
        self.__testNewString(charsetName)
        expected = bytes(self.__BYTES_FIXTURE).decode(charsetName)
        actual = StringUtils.newStringUsAscii(self.__BYTES_FIXTURE)
        self.assertEqual(expected, actual)

    def testNewStringIso8859_1(self) -> None:
        charsetName = "ISO-8859-1"
        self.__testNewString(charsetName)
        expected = bytes(self.__BYTES_FIXTURE).decode(charsetName)
        actual = StringUtils.newStringIso8859_1(self.__BYTES_FIXTURE)
        self.assertEqual(expected, actual)

    def testNewStringNullInput_CODEC229(self) -> None:

        self.assertIsNone(StringUtils.newStringUtf8(None))
        self.assertIsNone(StringUtils.newStringIso8859_1(None))
        self.assertIsNone(StringUtils.newStringUsAscii(None))
        self.assertIsNone(StringUtils.newStringUtf16(None))
        self.assertIsNone(StringUtils.newStringUtf16Be(None))
        self.assertIsNone(StringUtils.newStringUtf16Le(None))

    def testNewStringNullInput(self) -> None:
        self.assertIsNone(StringUtils.newString1(None, "UNKNOWN"))

    def testNewStringBadEnc(self) -> None:
        try:
            StringUtils.newString1(self.__BYTES_FIXTURE, "UNKNOWN")
            self.fail("Expected " + RuntimeError.__name__)
        except RuntimeError:
            pass

    def testGetBytesUncheckedNullInput(self) -> None:
        self.assertIsNone(StringUtils.getBytesUnchecked(None, "UNKNOWN"))

    def testGetBytesUncheckedBadName(self) -> None:
        with pytest.raises(RuntimeError):
            StringUtils.getBytesUnchecked(self.__STRING_FIXTURE, "UNKNOWN")

    def testGetBytesUtf8(self) -> None:

        charsetName = "UTF-8"
        self.__testGetBytesUnchecked(charsetName)
        expected = [ord(c) for c in self.__STRING_FIXTURE.encode(charsetName)]
        actual = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.assertListEqual(expected, actual)

    def testGetBytesUtf16Le(self) -> None:

        charsetName = "UTF-16LE"
        self.__testGetBytesUnchecked(charsetName)
        expected = [ord(c) for c in self.__STRING_FIXTURE.encode(charsetName)]
        actual = StringUtils.getBytesUtf16Le(self.__STRING_FIXTURE)
        self.assertListEqual(expected, actual)

    def testGetBytesUtf16Be(self) -> None:

        charsetName = "UTF-16BE"
        self.__testGetBytesUnchecked(charsetName)
        expected = [ord(c) for c in self.__STRING_FIXTURE.encode(charsetName)]
        actual = StringUtils.getBytesUtf16Be(self.__STRING_FIXTURE)
        self.assertListEqual(expected, actual)

    def testGetBytesUtf16(self) -> None:

        charsetName = "UTF-16"
        self.__testGetBytesUnchecked(charsetName)
        expected = [ord(c) for c in self.__STRING_FIXTURE.encode(charsetName)]
        actual = StringUtils.getBytesUtf16(self.__STRING_FIXTURE)
        self.assertListEqual(expected, actual)

    def testGetBytesUsAscii(self) -> None:

        charsetName = "US-ASCII"
        self.__testGetBytesUnchecked(charsetName)
        expected = [ord(c) for c in self.__STRING_FIXTURE.encode(charsetName)]
        actual = StringUtils.getBytesUsAscii(self.__STRING_FIXTURE)
        self.assertListEqual(expected, actual)

    def testGetBytesIso8859_1(self) -> None:

        charsetName = "ISO-8859-1"
        self.__testGetBytesUnchecked(charsetName)
        expected = [ord(c) for c in self.__STRING_FIXTURE.encode(charsetName)]
        actual = StringUtils.getBytesIso8859_1(self.__STRING_FIXTURE)
        self.assertListEqual(expected, actual)

    def testConstructor(self) -> None:
        StringUtils()

    def __testNewString(self, charsetName: str) -> None:
        expected = bytes(self.__BYTES_FIXTURE).decode(charsetName)
        actual = StringUtils.newString1(self.__BYTES_FIXTURE, charsetName)
        self.assertEqual(expected, actual)

    def __testGetBytesUnchecked(self, charsetName: str) -> None:
        expected = [ord(c) for c in self.__STRING_FIXTURE.encode(charsetName)]
        actual = StringUtils.getBytesUnchecked(self.__STRING_FIXTURE, charsetName)
        self.assertListEqual(expected, actual)
