from __future__ import annotations
import re
import os
from io import BytesIO
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder import *


class QuotedPrintableDecoderTestCase(unittest.TestCase):

    __US_ASCII_CHARSET: str = "US-ASCII"

    def testtruncatedEscape(self) -> None:
        self.__assertIOException("truncated", "=1")

    def testinvalidSoftBreak2(self) -> None:
        self.__assertIOException("CR must be followed by LF", "=\rn")

    def testinvalidSoftBreak1(self) -> None:
        self.__assertIOException("CR must be followed by LF", "=\r\r")

    def testsoftLineBreakDecode(self) -> None:
        self.__assertEncoded(
            "If you believe that truth=beauty, then surely mathematics is the most beautiful"
            + " branch of philosophy.",
            "If you believe that truth=3Dbeauty, then surely=20=\r\n"
            + "mathematics is the most beautiful branch of philosophy.",
        )

    def testinvalidCharDecode(self) -> None:
        with pytest.raises(Exception):
            self.__assertEncoded("=\r\n", "=3D=XD=XA")

    def testunsafeDecodeLowerCase(self) -> None:
        self.__assertEncoded("=\r\n", "=3d=0d=0a")

    def testunsafeDecode(self) -> None:
        self.__assertEncoded("=\r\n", "=3D=0D=0A")

    def testinvalidQuotedPrintableEncoding(self) -> None:
        self.__assertIOException(
            "truncated escape sequence",
            "YWJjMTIzXy0uKn4hQCMkJV4mKCkre31cIlxcOzpgLC9bXQ==",
        )

    def testbasicEncodeDecode(self) -> None:
        self.__assertEncoded("= Hello there =\r\n", "=3D Hello there =3D=0D=0A")

    def testplainDecode(self) -> None:
        self.__assertEncoded(
            "The quick brown fox jumps over the lazy dog.",
            "The quick brown fox jumps over the lazy dog.",
        )

    def testemptyDecode(self) -> None:
        self.__assertEncoded("", "")

    @staticmethod
    def __assertIOException(messageText: str, encoded: str) -> None:
        out = io.BytesIO(encoded.encode("US-ASCII"))
        encodedData = encoded.encode("US-ASCII")
        try:
            QuotedPrintableDecoder.decode(encodedData, out)
            self.fail("Expected IOException")
        except Exception as e:
            em = str(e)
            self.assertTrue(
                "Expected to find " + messageText + " in '" + em + "'",
                messageText in em,
            )

    @staticmethod
    def __assertEncoded(clearText: str, encoded: str) -> None:
        expected = clearText.encode(QuotedPrintableDecoderTestCase.__US_ASCII_CHARSET)

        out = io.BytesIO()
        encodedData = encoded.encode(QuotedPrintableDecoderTestCase.__US_ASCII_CHARSET)
        QuotedPrintableDecoder.decode(encodedData, out)
        actual = out.getvalue()

        assert expected == actual
