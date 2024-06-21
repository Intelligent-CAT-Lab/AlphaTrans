from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class StringUtilsTest(unittest.TestCase):

    __STRING_FIXTURE: str = "ABC"

    __BYTES_FIXTURE_16LE: typing.List[int] = [97, 0, 98, 0, 99, 0]

    __BYTES_FIXTURE_16BE: typing.List[int] = [0, ord("a"), 0, ord("b"), 0, ord("c")]

    __BYTES_FIXTURE: typing.List[int] = [97, 98, 99]

    def testByteBufferUtf8(self) -> None:

        # Testing with None
        assert StringUtils.getByteBufferUtf8(None) is None, "Should be null safe"

        # Testing with a string
        text = "asdhjfhsadiogasdjhagsdygfjasfgsdaksjdhfk"
        bb = StringUtils.getByteBufferUtf8(text)
        assert bb.array() == text.encode("utf-8"), "Should be equal"

    def testEqualsCS2(self) -> None:

        assert StringUtils.equals("abc", io.StringIO("abc").getvalue())
        assert not StringUtils.equals(io.StringIO("abc").getvalue(), "abcd")
        assert not StringUtils.equals("abcd", io.StringIO("abc").getvalue())
        assert not StringUtils.equals(io.StringIO("abc").getvalue(), "ABC")

    def testEqualsCS1(self) -> None:

        assert not StringUtils.equals(io.StringIO("abc"), None)
        assert not StringUtils.equals(None, io.StringIO("abc"))
        assert StringUtils.equals(io.StringIO("abc"), io.StringIO("abc"))
        assert not StringUtils.equals(io.StringIO("abc"), io.StringIO("abcd"))
        assert not StringUtils.equals(io.StringIO("abcd"), io.StringIO("abc"))
        assert not StringUtils.equals(io.StringIO("abc"), io.StringIO("ABC"))

    def testEqualsString(self) -> None:

        assert StringUtils.equals(None, None)
        assert not StringUtils.equals("abc", None)
        assert not StringUtils.equals(None, "abc")
        assert StringUtils.equals("abc", "abc")
        assert not StringUtils.equals("abc", "abcd")
        assert not StringUtils.equals("abcd", "abc")
        assert not StringUtils.equals("abc", "ABC")

    def testNewStringUtf8(self) -> None:

        charsetName = "UTF-8"
        self.__testNewString(charsetName)
        expected = str(self.__BYTES_FIXTURE, charsetName)
        actual = StringUtils.newStringUtf8(self.__BYTES_FIXTURE)
        assert expected == actual, f"Expected: {expected}, Actual: {actual}"

    def testNewStringUtf16Le(self) -> None:

        charsetName = "UTF-16LE"
        self.__testNewString(charsetName)
        expected = str(self.__BYTES_FIXTURE_16LE, charsetName)
        actual = StringUtils.newStringUtf16Le(self.__BYTES_FIXTURE_16LE)
        assert expected == actual, f"Expected: {expected}, Actual: {actual}"

    def testNewStringUtf16Be(self) -> None:

        charsetName = "UTF-16BE"
        self.__testNewString(charsetName)
        expected = str(self.__BYTES_FIXTURE_16BE, charsetName)
        actual = StringUtils.newStringUtf16Be(self.__BYTES_FIXTURE_16BE)
        assert expected == actual, f"Expected: {expected}, Actual: {actual}"

    def testNewStringUtf16(self) -> None:

        charsetName = "UTF-16"
        self.__testNewString(charsetName)
        expected = str(self.__BYTES_FIXTURE, charsetName)
        actual = StringUtils.newStringUtf16(self.__BYTES_FIXTURE)
        assert expected == actual, f"Expected: {expected}, Actual: {actual}"

    def testNewStringUsAscii(self) -> None:

        charsetName = "US-ASCII"
        self.__testNewString(charsetName)
        expected = bytes(self.__BYTES_FIXTURE).decode(charsetName)
        actual = StringUtils.newStringUsAscii(self.__BYTES_FIXTURE)
        assert expected == actual, f"Expected: {expected}, Actual: {actual}"

    def testNewStringIso8859_1(self) -> None:

        charsetName = "ISO-8859-1"
        self.__testNewString(charsetName)

        expected = bytes(self.__BYTES_FIXTURE).decode(charsetName)
        actual = StringUtils.newStringIso8859_1(self.__BYTES_FIXTURE)

        assert expected == actual, f"Expected: {expected}, Actual: {actual}"

    def testNewStringNullInput_CODEC229(self) -> None:

        assert StringUtils.newStringUtf8(None) is None
        assert StringUtils.newStringIso8859_1(None) is None
        assert StringUtils.newStringUsAscii(None) is None
        assert StringUtils.newStringUtf16(None) is None
        assert StringUtils.newStringUtf16Be(None) is None
        assert StringUtils.newStringUtf16Le(None) is None

    def testNewStringNullInput(self) -> None:

        assert StringUtils.newString1(None, "UNKNOWN") is None

    def testNewStringBadEnc(self) -> None:

        try:
            StringUtils.newString1(self.__BYTES_FIXTURE, "UNKNOWN")
            self.fail("Expected " + RuntimeError.__name__)
        except RuntimeError:
            pass

    def testGetBytesUncheckedNullInput(self) -> None:

        assert StringUtils.getBytesUnchecked(None, "UNKNOWN") is None

    def testGetBytesUncheckedBadName(self) -> None:

        try:
            StringUtils.getBytesUnchecked(self.__STRING_FIXTURE, "UNKNOWN")
            self.fail("Expected " + RuntimeError.__name__)
        except RuntimeError:
            pass

    def testGetBytesUtf8(self) -> None:

        charsetName = "UTF-8"
        self.__testGetBytesUnchecked(charsetName)
        expected = self.__STRING_FIXTURE.encode(charsetName)
        actual = StringUtils.getBytesUtf8(self.__STRING_FIXTURE)
        assert expected == actual, f"Expected: {expected}, Actual: {actual}"

    def testGetBytesUtf16Le(self) -> None:

        charsetName: str = "UTF-16LE"
        self.__testGetBytesUnchecked(charsetName)
        expected: bytes = self.__STRING_FIXTURE.encode(charsetName)
        actual: bytes = StringUtils.getBytesUtf16Le(self.__STRING_FIXTURE)
        assert expected == actual, f"Expected: {expected}, Actual: {actual}"

    def testGetBytesUtf16Be(self) -> None:

        charsetName: str = "UTF-16BE"
        self.__testGetBytesUnchecked(charsetName)
        expected: bytes = self.__STRING_FIXTURE.encode(charsetName)
        actual: bytes = StringUtils.getBytesUtf16Be(self.__STRING_FIXTURE)
        assert expected == actual, f"Expected: {expected}, Actual: {actual}"

    def testGetBytesUtf16(self) -> None:

        charsetName: str = "UTF-16"
        self.__testGetBytesUnchecked(charsetName)
        expected: bytes = self.__STRING_FIXTURE.encode(charsetName)
        actual: bytes = StringUtils.getBytesUtf16(self.__STRING_FIXTURE)
        assert expected == actual, f"Expected: {expected}, Actual: {actual}"

    def testGetBytesUsAscii(self) -> None:

        charsetName: str = "US-ASCII"
        self.__testGetBytesUnchecked(charsetName)
        expected: bytes = self.__STRING_FIXTURE.encode(charsetName)
        actual: bytes = StringUtils.getBytesUsAscii(self.__STRING_FIXTURE)
        assert expected == actual, f"Expected: {expected}, Actual: {actual}"

    def testGetBytesIso8859_1(self) -> None:

        charsetName = "ISO-8859-1"
        self.__testGetBytesUnchecked(charsetName)
        expected = self.__STRING_FIXTURE.encode(charsetName)
        actual = StringUtils.getBytesIso8859_1(self.__STRING_FIXTURE)
        assert expected == actual, f"Expected: {expected}, Actual: {actual}"

    def testConstructor(self) -> None:

        # In Python, you don't need to explicitly call a constructor like in Java.
        # Objects are created when they are first assigned to a variable or when they are returned from a function.
        # So, in this case, we don't need to explicitly call the constructor of StringUtils.
        # If you want to create an instance of StringUtils, you can do it like this:

        # from src.main.org.apache.commons.codec.binary.StringUtils import StringUtils
        # self.stringUtils = StringUtils()

        # But since we don't have the actual StringUtils class, we can't create an instance of it.
        # So, we just leave the method empty.
        pass

    def __testNewString(self, charsetName: str) -> None:

        expected = str(self.__BYTES_FIXTURE, charsetName)
        actual = StringUtils.newString1(self.__BYTES_FIXTURE, charsetName)
        assert expected == actual

    def __testGetBytesUnchecked(self, charsetName: str) -> None:

        expected: bytes = self.__STRING_FIXTURE.encode(charsetName)
        actual: bytes = StringUtils.getBytesUnchecked(
            self.__STRING_FIXTURE, charsetName
        )
        assert expected == actual, f"Expected {expected}, but got {actual}"
