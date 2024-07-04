from __future__ import annotations
import re
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.util.mime.Base64Decoder import *


class Base64DecoderTestCase(unittest.TestCase):

    __US_ASCII_CHARSET: str = "US-ASCII"

    def testnonASCIIcharacter(self) -> None:

        self.__assertEncoded("f", "Zg=�=")  # A-grave
        self.__assertEncoded("f", "Zg=\u0100=")

    def testbadLength(self) -> None:

        self.__assertIOException("truncated", "Zm8==")

    def testbadPaddingLeading2(self) -> None:

        self.__assertIOException(
            "incorrect padding, first two bytes cannot be padding", "===="
        )

    def testbadPaddingLeading1(self) -> None:

        self.__assertIOException(
            "incorrect padding, first two bytes cannot be padding", "=A=="
        )

    def testbadPadding(self) -> None:

        self.__assertIOException("incorrect padding, 4th byte", "Zg=a")

    def testdecodeTrailing3(self) -> None:

        self.__assertIOException("truncated", "Zm9vYmFy123")

    def testdecodeTrailing2(self) -> None:

        self.__assertIOException("truncated", "Zm9vYmFy12")

    def testdecodeTrailing1(self) -> None:

        self.__assertIOException("truncated", "Zm9vYmFy1")

    def testdecodeTrailingJunk(self) -> None:

        self.__assertEncoded("foobar", "Zm9vYmFy!!!")

    def testtruncatedString(self) -> None:

        data = [ord("n")]
        out = io.BytesIO()

        try:
            Base64Decoder.decode(data, out)
        except IOError as e:
            assert str(e) == "Invalid Base64 input: truncated"

    def testnonBase64Bytes(self) -> None:

        self.__assertEncoded("Hello World", "S?G1Vsb 8g\rV\t\n29ybGQ*=")

    def testdecodeWithInnerPad(self) -> None:

        clearText = "Hello WorldHello World"
        encoded = "SGVsbG8gV29ybGQ=SGVsbG8gV29ybGQ="

        self.__assertEncoded(clearText, encoded)

    def testrfc4648Section10Decode(self) -> None:

        self.__assertEncoded("", "")
        self.__assertEncoded("f", "Zg==")
        self.__assertEncoded("fo", "Zm8=")
        self.__assertEncoded("foo", "Zm9v")
        self.__assertEncoded("foob", "Zm9vYg==")
        self.__assertEncoded("fooba", "Zm9vYmE=")
        self.__assertEncoded("foobar", "Zm9vYmFy")

    @staticmethod
    def __assertIOException(messageText: str, encoded: str) -> None:

        out = io.BytesIO()
        encodedData = encoded.encode(Base64DecoderTestCase.__US_ASCII_CHARSET)
        try:
            Base64Decoder.decode(list(encodedData), out)
            pytest.fail("Expected IOException")
        except IOError as e:
            em = str(e)
            assert messageText in em, f"Expected to find {messageText} in '{em}'"

    @staticmethod
    def __assertEncoded(clearText: str, encoded: str) -> None:

        expected = clearText.encode(Base64DecoderTestCase.__US_ASCII_CHARSET)

        out = io.BytesIO()
        encodedData = encoded.encode(Base64DecoderTestCase.__US_ASCII_CHARSET)
        Base64Decoder.decode(encodedData, out)
        actual = out.getvalue()

        assert expected == actual
