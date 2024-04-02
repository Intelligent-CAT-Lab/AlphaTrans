# Imports Begin
from src.main.org.apache.commons.fileupload.util.mime.Base64Decoder import *
import unittest
from io import BytesIO

# Imports End


class Base64DecoderTestCase(unittest.TestCase):

    # Class Fields Begin
    __US_ASCII_CHARSET: str = "US-ASCII"
    # Class Fields End

    # Class Methods Begin
    def nonASCIIcharacter(self) -> None:

        self.assertTrue(self.__assertEncoded("f", "Zg=�="))
        self.assertTrue(self.__assertEncoded("f", "Zg=\u0100="))

    def badLength(self) -> None:

        self.assertIOException("truncated", "Zm8==")

    def badPaddingLeading2(self) -> None:

        self.assertIOException(
            "incorrect padding, first two bytes cannot be padding", "===="
        )

    def badPaddingLeading1(self) -> None:

        self.assertIOException(
            "incorrect padding, first two bytes cannot be padding", "=A=="
        )

    def badPadding(self) -> None:

        self.assertIOException("incorrect padding, 4th byte", "Zg=a")

    def decodeTrailing3(self) -> None:

        self.assertIOException("truncated", "Zm9vYmFy123")

    def decodeTrailing2(self) -> None:

        self.assertIOException("truncated", "Zm9vYmFy12")

    def decodeTrailing1(self) -> None:

        self.__assertIOException("truncated", "Zm9vYmFy1")

    def decodeTrailingJunk(self) -> None:

        self.assertTrue(__assertEncoded("foobar", "Zm9vYmFy!!!"))

    def truncatedString(self) -> None:

        x = bytearray(b"n")
        self.assertTrue(Base64Decoder.decode(x, io.BytesIO()))

    def nonBase64Bytes(self) -> None:

        self.assertTrue(
            self.__assertEncoded("Hello World", "S?G i VsbG 8g\rV\t\n29ybGQ*=")
        )

    def decodeWithInnerPad(self) -> None:

        self.assertTrue(
            self.__assertEncoded(
                "Hello WorldHello World", "SGVsbG8gV29ybGQ=SGVsbG8gV29ybGQ="
            )
        )

    def rfc4648Section10Decode(self) -> None:

        self.assertTrue(__assertEncoded("", ""))
        self.assertTrue(__assertEncoded("f", "Zg=="))
        self.assertTrue(__assertEncoded("fo", "Zm8="))
        self.assertTrue(__assertEncoded("foo", "Zm9v"))
        self.assertTrue(__assertEncoded("foob", "Zm9vYg=="))
        self.assertTrue(__assertEncoded("fooba", "Zm9vYmE="))
        self.assertTrue(__assertEncoded("foobar", "Zm9vYmFy"))

    @staticmethod
    def __assertIOException(messageText: str, encoded: str) -> None:

        out = io.BytesIO()
        encodedData = encoded.encode(Base64Decoder.self.__US_ASCII_CHARSET)
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

        expected = clearText.encode(MyTestCase.self.__US_ASCII_CHARSET)
        out = io.BytesIO()
        encodedData = encoded.encode(MyTestCase.self.__US_ASCII_CHARSET)
        Base64Decoder.decode(encodedData, out)
        actual = out.getvalue()
        TestCase.self.assertTrue(TestCase(), expected == actual)

    # Class Methods End
