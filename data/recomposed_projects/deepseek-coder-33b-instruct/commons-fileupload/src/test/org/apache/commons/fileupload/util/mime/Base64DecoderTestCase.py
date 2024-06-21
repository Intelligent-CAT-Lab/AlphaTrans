from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.fileupload.util.mime.Base64Decoder import *


class Base64DecoderTestCase:

    __US_ASCII_CHARSET: str = "US-ASCII"

    @pytest.mark.test
    def testnonASCIIcharacter(self) -> None:

        self.__assertEncoded("f", "Zg=�=")  # A-grave
        self.__assertEncoded("f", "Zg=\u0100=")

    @pytest.mark.test
    def badLength(self) -> None:

        self.__assertIOException("truncated", "Zm8==")

    @pytest.mark.test
    def badPaddingLeading2(self) -> None:

        self.__assertIOException(
            "incorrect padding, first two bytes cannot be padding", "===="
        )

    @pytest.mark.test
    def badPaddingLeading1(self) -> None:

        self.__assertIOException(
            "incorrect padding, first two bytes cannot be padding", "=A=="
        )

    @pytest.mark.test
    def badPadding(self) -> None:

        self.__assertIOException("incorrect padding, 4th byte", "Zg=a")

    @pytest.mark.test
    def decodeTrailing3(self) -> None:

        self.__assertIOException("truncated", "Zm9vYmFy123")

    @pytest.mark.test
    def decodeTrailing2(self) -> None:

        self.__assertIOException("truncated", "Zm9vYmFy12")

    @pytest.mark.test
    def decodeTrailing1(self) -> None:

        self.__assertIOException("truncated", "Zm9vYmFy1")

    @pytest.mark.test
    def decodeTrailingJunk(self) -> None:

        self.__assertEncoded("foobar", "Zm9vYmFy!!!")

    @pytest.mark.test
    def truncatedString(self) -> None:

        data = [ord("n")]
        out = io.BytesIO()

        try:
            Base64Decoder.decode(data, out)
        except IOError as e:
            assert str(e) == "Invalid Base64 input: truncated"

    @pytest.mark.test
    def nonBase64Bytes(self) -> None:

        self.__assertEncoded("Hello World", "S?G1Vsb 8g\rV\t\n29ybGQ*=")

    @pytest.mark.test
    def decodeWithInnerPad(self) -> None:

        self.__assertEncoded(
            "Hello WorldHello World", "SGVsbG8gV29ybGQ=SGVsbG8gV29ybGQ="
        )

    @pytest.mark.test
    def rfc4648Section10Decode(self) -> None:

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
