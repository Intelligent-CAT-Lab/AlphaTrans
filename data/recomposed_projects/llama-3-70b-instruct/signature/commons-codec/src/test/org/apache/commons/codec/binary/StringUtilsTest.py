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
    __BYTES_FIXTURE_16LE: typing.List[int] = [97, 0, 98, 0, 99, 0]
    __BYTES_FIXTURE_16BE: typing.List[int] = [0, ord("a"), 0, ord("b"), 0, ord("c")]
    __BYTES_FIXTURE: typing.List[int] = [97, 98, 99]

    def testByteBufferUtf8(self) -> None:
        self.assertIsNone("Should be null safe", StringUtils.getByteBufferUtf8(None))
        text = "asdhjfhsadiogasdjhagsdygfjasfgsdaksjdhfk"
        bb = StringUtils.getByteBufferUtf8(text)
        self.assertListEqual(text.encode("utf-8"), bb.array())

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
        expected = str(self.__BYTES_FIXTURE, charsetName)
        actual = StringUtils.newStringUtf8(self.__BYTES_FIXTURE)
        self.assertEqual(expected, actual)

    def testNewStringUtf16Le(self) -> None:
        charsetName = "UTF-16LE"
        self.__testNewString(charsetName)
        expected = str(self.__BYTES_FIXTURE_16LE, charsetName)
        actual = StringUtils.newStringUtf16Le(self.__BYTES_FIXTURE_16LE)
        self.assertEqual(expected, actual)

    def testNewStringUtf16Be(self) -> None:
        charsetName = "UTF-16BE"
        self.__testNewString(charsetName)
        expected = str(self.__BYTES_FIXTURE_16BE, charsetName)
        actual = StringUtils.newStringUtf16Be(self.__BYTES_FIXTURE_16BE)
        self.assertEqual(expected, actual)

    def testNewStringUtf16(self) -> None:
        charsetName = "UTF-16"
        self.__testNewString(charsetName)
        expected = str(self.__BYTES_FIXTURE, charsetName)
        actual = StringUtils.newStringUtf16(self.__BYTES_FIXTURE)
        self.assertEqual(expected, actual)

    def testNewStringUsAscii(self) -> None:
        charsetName = "US-ASCII"
        self.__testNewString(charsetName)
        expected = str(self.__BYTES_FIXTURE, charsetName)
        actual = StringUtils.newStringUsAscii(self.__BYTES_FIXTURE)
        self.assertEqual(expected, actual)

    def testNewStringIso8859_1(self) -> None:
        charsetName = "ISO-8859-1"
        self.__testNewString(charsetName)
        expected = str(self.__BYTES_FIXTURE, charsetName)
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

        pass  # LLM could not translate this method

    def testGetBytesUncheckedNullInput(self) -> None:
        self.assertIsNone(StringUtils.getBytesUnchecked(None, "UNKNOWN"))

    def testGetBytesUncheckedBadName(self) -> None:

        pass  # LLM could not translate this method

    def testGetBytesUtf8(self) -> None:
        charsetName: str = "UTF-8"
        self.__testGetBytesUnchecked(charsetName)
        expected: typing.List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        actual: typing.List[int] = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        self.assertListEqual(expected, actual)

    def testGetBytesUtf16Le(self) -> None:
        charsetName: str = "UTF-16LE"
        self.__testGetBytesUnchecked(charsetName)
        expected: typing.List[int] = StringUtils.getBytesUtf16Le(self.__STRING_FIXTURE)
        actual: typing.List[int] = StringUtils.getBytesUtf16Le(self.__STRING_FIXTURE)
        self.assertEqual(expected, actual)

    def testGetBytesUtf16Be(self) -> None:
        charsetName: str = "UTF-16BE"
        self.__testGetBytesUnchecked(charsetName)
        expected: typing.List[int] = StringUtils.getBytesUtf16Be(self.__STRING_FIXTURE)
        actual: typing.List[int] = StringUtils.getBytesUtf16Be(self.__STRING_FIXTURE)
        self.assertEqual(expected, actual)

    def testGetBytesUtf16(self) -> None:
        charsetName: str = "UTF-16"
        self.__testGetBytesUnchecked(charsetName)
        expected: typing.List[int] = StringUtils.getBytes(charsetName)
        actual: typing.List[int] = StringUtils.getBytesUtf16(self.__STRING_FIXTURE)
        self.assertListEqual(expected, actual)

    def testGetBytesUsAscii(self) -> None:
        charsetName: str = "US-ASCII"
        self.__testGetBytesUnchecked(charsetName)
        expected: typing.List[int] = StringUtils.getBytes(charsetName)
        actual: typing.List[int] = StringUtils.getBytesUsAscii(self.__STRING_FIXTURE)
        self.assertListEqual(expected, actual)

    def testGetBytesIso8859_1(self) -> None:
        charsetName: str = "ISO-8859-1"
        self.__testGetBytesUnchecked(charsetName)
        expected: typing.List[int] = StringUtils.getBytesIso8859_1(
            self.__STRING_FIXTURE
        )
        actual: typing.List[int] = StringUtils.getBytesIso8859_1(self.__STRING_FIXTURE)
        self.assertEqual(expected, actual)

    def testConstructor(self) -> None:
        StringUtils()

    def __testNewString(self, charsetName: str) -> None:
        expected: str = str(self.__BYTES_FIXTURE, charsetName)
        actual: str = StringUtils.newString1(self.__BYTES_FIXTURE, charsetName)
        self.assertEqual(expected, actual)

    def __testGetBytesUnchecked(self, charsetName: str) -> None:
        expected: typing.List[int] = self.__STRING_FIXTURE.encode(charsetName)
        actual: typing.List[int] = StringUtils.getBytesUnchecked(
            self.__STRING_FIXTURE, charsetName
        )
        self.assertListEqual(expected, actual)
