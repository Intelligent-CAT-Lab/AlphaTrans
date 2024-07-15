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
        self.__assertEncoded("f", "Zg=À=")  # A-grave
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
        with pytest.raises(Exception):
            x = [ord("n")]
            Base64Decoder.decode(x, io.BytesIO())

    def testnonBase64Bytes(self) -> None:
        self.__assertEncoded("Hello World", "S?G!V%sbG 8g\rV\t\n29ybGQ*=")

    def testdecodeWithInnerPad(self) -> None:
        self.__assertEncoded(
            "Hello WorldHello World", "SGVsbG8gV29ybGQ=SGVsbG8gV29ybGQ="
        )

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
        out = io.BytesIO(encoded.encode("utf-8"))
        encodedData = encoded.encode(Base64DecoderTestCase.__US_ASCII_CHARSET)
        try:
            Base64Decoder.decode(encodedData, out)
            self.fail("Expected IOException")
        except Exception as e:
            em = str(e)
            self.assertTrue(
                "Expected to find " + messageText + " in '" + em + "'",
                messageText in em,
            )

    @staticmethod
    def __assertEncoded(clearText: str, encoded: str) -> None:
        expected = clearText.encode(Base64DecoderTestCase.__US_ASCII_CHARSET)

        out = io.BytesIO()
        encodedData = encoded.encode(Base64DecoderTestCase.__US_ASCII_CHARSET)
        Base64Decoder.decode(encodedData, out)
        actual = out.getvalue()

        assert expected == actual
