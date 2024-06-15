import pytest

# Imports Begin
import unittest
from io import BytesIO
from src.main.org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder import QuotedPrintableDecoder

# Imports End


class QuotedPrintableDecoderTestCase(unittest.TestCase):

    # Class Fields Begin
    __US_ASCII_CHARSET: str = "US-ASCII"
    # Class Fields End

    # Class Methods Begin
    @pytest.mark.test
    def testEmptyDecode(self) -> None:
        try:
            self.__assertEncoded("", "")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testPlainDecode(self) -> None:
        try:
            self.__assertEncoded(
                "The quick brown fox jumps over the lazy dog.",
                "The quick brown fox jumps over the lazy dog.",
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testBasicEncodeDecode(self) -> None:
        try:
            self.__assertEncoded("= Hello there =\r\n", "=3D Hello there =3D=0D=0A")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testInvalidQuotedPrintableEncoding(self) -> None:
        try:
            self.__assertIOException(
                "truncated escape sequence",
                "YWJjMTIzXy0uKn4hQCMkJV4mKCkre31cIlxcOzpgLC9bXQ==",
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testUnsafeDecode(self) -> None:
        try:
            self.__assertEncoded("=\r\n", "=3D=0D=0A")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testUnsafeDecodeLowerCase(self) -> None:
        try:
            self.__assertEncoded("=\r\n", "=3d=0d=0a")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testInvalidCharDecode(self) -> None:
        with self.assertRaises(Exception) as context:
            self.__assertEncoded("=\r\n", "=3D=XD=XA")
        self.assertTrue(isinstance(context.exception, IOError) or isinstance(context.exception, OSError))

    @pytest.mark.test
    def testSoftLineBreakDecode(self) -> None:
        try:
            self.__assertEncoded(
                "If you believe that truth=beauty, then surely mathematics is the most beautiful"
                    + " branch of philosophy.",
                "If you believe that truth=3Dbeauty, then surely=20=\r\n"
                    + "mathematics is the most beautiful branch of philosophy.",
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testInvalidSoftBreak1(self) -> None:
        try:
            self.__assertIOException("CR must be followed by LF", "=\r\r")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testInvalidSoftBreak2(self) -> None:
        try:
            self.__assertIOException("CR must be followed by LF", "=\rn")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testTruncatedEscape(self) -> None:
        try:
            self.__assertIOException("truncated", "=1")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")


    @staticmethod
    def __assertIOException(messageText: str, encoded: str) -> None:
        out = BytesIO()
        encoded_data = encoded.encode(QuotedPrintableDecoderTestCase.__US_ASCII_CHARSET)
        try:
            QuotedPrintableDecoder.decode(encoded_data, out)
            QuotedPrintableDecoderTestCase.fail("Expected IO-related Exception")
        except (IOError, OSError) as e:
            em = str(e)
            QuotedPrintableDecoderTestCase.assertIn(messageText, em, f"Expected to find {messageText} in '{em}'")
        # LLM could not translate method body

    @staticmethod
    def __assertEncoded(clearText: str, encoded: str) -> None:
        expected = clearText.encode(QuotedPrintableDecoderTestCase.__US_ASCII_CHARSET)
        out = BytesIO()
        encoded_data = encoded.encode(QuotedPrintableDecoderTestCase.__US_ASCII_CHARSET)
        QuotedPrintableDecoder.decode(encoded_data, out)
        actual = out.getvalue()
        QuotedPrintableDecoderTestCase.assertEqual(expected, actual)
        # LLM could not translate method body

    # Class Methods End
