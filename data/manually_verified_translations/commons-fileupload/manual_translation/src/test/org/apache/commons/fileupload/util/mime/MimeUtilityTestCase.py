from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import *


class MimeUtilityTestCase(unittest.TestCase):

    def testdecodeInvalidEncoding(self) -> None:

        with pytest.raises(ValueError):
            MimeUtility.decodeText("=?invalid?B?xyz-?=")

    def testdecodeIso88591Base64EncodedWithWhiteSpace(self) -> None:

        expected = "If you can read this you understand the example."
        encoded = (
            "=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?=\t  \r\n"
            + '   =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?="\r\n'
        )

        try:
            assert expected == MimeUtility.decodeText(encoded)
        except AssertionError:
            raise AssertionError("Expected and decoded text do not match")

    def testdecodeIso88591Base64Encoded(self) -> None:

        expected = "If you can read this you understand the example."
        encoded = (
            "=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?="
            + ' =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?="\r\n'
        )

        try:
            assert expected == MimeUtility.decodeText(encoded)
        except AssertionError:
            raise AssertionError("Expected and decoded text do not match")

    def testdecodeUtf8Base64Encoded(self) -> None:

        try:
            self.__assertEncoded(
                " h\u00e9! \u00e0\u00e8\u00f4u !!!",
                "=?UTF-8?B?IGjDqSEgw6DDqMO0dSAhISE=?="
            )
        except AssertionError:
            raise AssertionError("Expected and decoded text do not match")

    def testdecodeUtf8QuotedPrintableEncoded(self) -> None:

        try:
            self.__assertEncoded(
                " h\u00e9! \u00e0\u00e8\u00f4u !!!",
                "=?UTF-8?Q?_h=C3=A9!_=C3=A0=C3=A8=C3=B4u_!!!?="
            )
        except AssertionError:
            raise AssertionError("Expected and decoded text do not match")

    def testnoNeedToDecode(self) -> None:

        self.__assertEncoded("abc", "abc")

    @staticmethod
    def __assertEncoded(expected: str, encoded: str) -> None:

        try:
            assert expected == MimeUtility.decodeText(encoded)
        except AssertionError:
            raise AssertionError("Expected and decoded text do not match")
