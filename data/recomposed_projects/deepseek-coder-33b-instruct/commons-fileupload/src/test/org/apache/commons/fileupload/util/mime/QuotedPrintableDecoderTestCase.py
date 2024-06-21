from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder import *


class QuotedPrintableDecoderTestCase:

    __US_ASCII_CHARSET: str = "US-ASCII"

    @pytest.mark.test
    def truncatedEscape(self) -> None:

        self.__assertIOException("truncated", "=1")

    @pytest.mark.test
    def invalidSoftBreak2(self) -> None:

        self.__assertIOException("CR must be followed by LF", "=\rn")

    @pytest.mark.test
    def invalidSoftBreak1(self) -> None:

        self.__assertIOException("CR must be followed by LF", "=\r\r")

    @pytest.mark.test
    def softLineBreakDecode(self) -> None:

        clearText = (
            "If you believe that truth=beauty, then surely mathematics is the most beautiful"
            + " branch of philosophy."
        )
        encoded = (
            "If you believe that truth=3Dbeauty, then surely=20=\r\n"
            + "mathematics is the most beautiful branch of philosophy."
        )

        self.__assertEncoded(clearText, encoded)

    @pytest.mark.test
    def invalidCharDecode(self) -> None:

        with pytest.raises(IOException):
            self.__assertEncoded("=\r\n", "=3D=XD=XA")

    @pytest.mark.test
    def unsafeDecodeLowerCase(self) -> None:

        self.__assertEncoded("=\r\n", "=3d=0d=0a")

    @pytest.mark.test
    def unsafeDecode(self) -> None:

        self.__assertEncoded("=\r\n", "=3D=0D=0A")

    @pytest.mark.test
    def invalidQuotedPrintableEncoding(self) -> None:

        self.__assertIOException(
            "truncated escape sequence",
            "YWJjMTIzXy0uKn4hQCMkJV4mKCkre31cIlxcOzpgLC9bXQ==",
        )

    @pytest.mark.test
    def basicEncodeDecode(self) -> None:

        QuotedPrintableDecoderTestCase.__assertEncoded(
            "= Hello there =\r\n", "=3D Hello there =3D=0D=0A"
        )

    @pytest.mark.test
    def plainDecode(self) -> None:

        self.__assertEncoded(
            "The quick brown fox jumps over the lazy dog.",
            "The quick brown fox jumps over the lazy dog.",
        )

    @pytest.mark.test
    def emptyDecode(self) -> None:

        self.__assertEncoded("", "")

    @staticmethod
    def __assertIOException(messageText: str, encoded: str) -> None:

        out = io.BytesIO()
        encodedData = encoded.encode(QuotedPrintableDecoderTestCase.__US_ASCII_CHARSET)
        try:
            QuotedPrintableDecoder.decode(list(encodedData), out)
            pytest.fail("Expected IOException")
        except IOError as e:
            em = str(e)
            assert messageText in em, f"Expected to find {messageText} in '{em}'"

    @staticmethod
    def __assertEncoded(clearText: str, encoded: str) -> None:

        expected = clearText.encode(QuotedPrintableDecoderTestCase.__US_ASCII_CHARSET)

        out = io.BytesIO()
        encodedData = encoded.encode(QuotedPrintableDecoderTestCase.__US_ASCII_CHARSET)
        QuotedPrintableDecoder.decode(list(encodedData), out)
        actual = out.getvalue()

        assert expected == actual
