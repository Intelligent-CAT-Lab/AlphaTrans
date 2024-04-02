# Imports Begin
from src.main.org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder import *
import unittest
import os
from io import BytesIO

# Imports End


class QuotedPrintableDecoderTestCase(unittest.TestCase):

    # Class Fields Begin
    __US_ASCII_CHARSET: str = "US-ASCII"
    # Class Fields End

    # Class Methods Begin
    def truncatedEscape(self) -> None:

        self.assertIOException("truncated", "=1")

    def invalidSoftBreak2(self) -> None:

        self.assertIOException("CR must be followed by LF", "=\rn")

    def invalidSoftBreak1(self) -> None:

        self.assertIOException("CR must be followed by LF", "=\r\r")

    def softLineBreakDecode(self) -> None:

        self.assertTrue(
            self.__assertEncoded(
                "If you believe that truth=beauty, then surely mathematics is the most beautiful"
                + " branch of philosophy.",
                "If you believe that truth=3Dbeauty, then surely=20=\r\n"
                + "mathematics is the most beautiful branch of philosophy.",
            )
        )

    def invalidCharDecode(self) -> None:

        self.assertTrue(self.__assertEncoded("=\r\n", "=3D=XD=XA"))

    def unsafeDecodeLowerCase(self) -> None:

        self.__assertEncoded("=\r\n", "=3d=0d=0a")

    def unsafeDecode(self) -> None:

        self.assertTrue(self.__assertEncoded("=\r\n", "=3D=0D=0A"))

    def invalidQuotedPrintableEncoding(self) -> None:

        self.assertTrue(
            __assertIOException(
                "truncated escape sequence",
                "YWJjMTIzXy0uKn4hQCMkJV4mKCkre31cIlxcOzpgLC9bXQ==",
            )
        )

    def basicEncodeDecode(self) -> None:

        self.assertTrue(
            self.__assertEncoded("= Hello there =\r\n", "=3D Hello there =3D=0D=0A")
        )

    def plainDecode(self) -> None:

        self.assertTrue(
            self.__assertEncoded(
                "The quick brown fox jumps over the lazy dog.",
                "The quick brown fox jumps over the lazy dog.",
            )
        )

    def emptyDecode(self) -> None:

        self.__assertEncoded("", "")

    @staticmethod
    def __assertIOException(messageText: str, encoded: str) -> None:

        pass  # LLM could not translate method body

    @staticmethod
    def __assertEncoded(clearText: str, encoded: str) -> None:

        expected = clearText.encode(TestClass.self.__US_ASCII_CHARSET)
        out = io.BytesIO()
        encodedData = encoded.encode(TestClass.self.__US_ASCII_CHARSET)
        QuotedPrintableDecoder.decode(encodedData, out)
        actual = out.getvalue()
        assert_that(actual).is_equal_to(expected)

    # Class Methods End
