import pytest

# Imports Begin
import unittest
from io import BytesIO
from src.main.org.apache.commons.fileupload.util.mime.Base64Decoder import Base64Decoder

# Imports End


class Base64DecoderTestCase(unittest.TestCase):

    # Class Fields Begin
    __US_ASCII_CHARSET: str = "US-ASCII"
    # Class Fields End

    # Class Methods Begin

    @pytest.mark.test
    def testRfc4648Section10Decode(self) -> None:
        try:
            self.__assertEncoded("", "") 
            self.__assertEncoded("f", "Zg==")
            self.__assertEncoded("fo", "Zm8=")  
            self.__assertEncoded("foo", "Zm9v") 
            self.__assertEncoded("foob", "Zm9vYg==")
            self.__assertEncoded("fooba", "Zm9vYmE=")   
            self.__assertEncoded("foobar", "Zm9vYmFy") 
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testDecodeWithInnerPad(self) -> None:
        try:
            self.__assertEncoded(
                "Hello WorldHello World", "SGVsbG8gV29ybGQ=SGVsbG8gV29ybGQ="
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testNonBase64Bytes(self) -> None:
        try:
            self.__assertEncoded("Hello World", "S?G!V%sbG 8g\rV\t\n29ybGQ*=")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testTruncatedString(self) -> None:
        x = b'n'
        with self.assertRaises(Exception) as context:
            Base64Decoder.decode(x, BytesIO())
        
        self.assertTrue(isinstance(context.exception, IOError) or isinstance(context.exception, OSError))

    @pytest.mark.test
    def testDecodeTrailingJunk(self) -> None:
        try:
            self.__assertEncoded("foobar", "Zm9vYmFy!!!")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testDecodeTrailing1(self) -> None:
        try:
            self.__assertIOException("truncated", "Zm9vYmFy1")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testDecodeTrailing2(self) -> None:
        try:
            self.__assertIOException("truncated", "Zm9vYmFy12")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testDecodeTrailing3(self) -> None:
        try:
            self.__assertIOException("truncated", "Zm9vYmFy123")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testBadPadding(self) -> None:
        try:
            self.__assertIOException("incorrect padding, 4th byte", "Zg=a")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testBadPaddingLeading1(self) -> None:
        try:
            self.__assertIOException("incorrect padding, first two bytes cannot be padding", "=A==")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testBadPaddingLeading2(self) -> None:
        try:
            self.__assertIOException("incorrect padding, first two bytes cannot be padding", "====")
        except Exception as e:
            self.fail(str(e))

    @pytest.mark.test
    def testBadLength(self) -> None:
        try:
            self.__assertIOException("truncated", "Zm8==")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @pytest.mark.test
    def testNonASCIIcharacter(self) -> None:
        try:
            self.__assertEncoded("f", "Zg=À=")
            self.__assertEncoded("f", "Zg=\u0100=")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    @staticmethod
    def __assertIOException(messageText: str, encoded: str) -> None:
        out = BytesIO()
        encoded_data = encoded.encode(Base64DecoderTestCase.__US_ASCII_CHARSET)
        try:
            Base64Decoder.decode(encoded_data, out)
            Base64DecoderTestCase.fail("Expected IO-related Exception")
        except (IOError, OSError) as e:
            em = str(e)
            Base64DecoderTestCase.assertIn(messageText, em, f"Expected to find {messageText} in '{em}'") 
        # LLM could not translate method body

    @staticmethod
    def __assertEncoded(clearText: str, encoded: str) -> None:
        expected = clearText.encode(Base64DecoderTestCase.__US_ASCII_CHARSET)
        out = BytesIO()
        encoded_data = encoded.encode(Base64DecoderTestCase.__US_ASCII_CHARSET)
        Base64Decoder.decode(encoded_data, out)
        actual = out.getvalue()
        Base64DecoderTestCase.assertEqual(expected, actual)
        # LLM could not translate method body

    # Class Methods End
