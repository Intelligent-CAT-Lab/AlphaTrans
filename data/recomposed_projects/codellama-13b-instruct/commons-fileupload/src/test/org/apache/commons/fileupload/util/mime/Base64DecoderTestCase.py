# Imports Begin
from src.main.org.apache.commons.fileupload.util.mime.Base64Decoder import *
import unittest
import io

# Imports End


class Base64DecoderTestCase(unittest.TestCase):

    # Class Fields Begin
    __US_ASCII_CHARSET: str = "US-ASCII"
    # Class Fields End

    # Class Methods Begin
    def nonASCIIcharacter(self) -> None:

        self.__assertEncoded("f", "Zg=À=")
        self.__assertEncoded("f", "Zg=\u0100=")

    def badLength(self) -> None:

        self.__assertIOException("truncated", "Zm8==")

    def badPaddingLeading2(self) -> None:

        self.__assertIOException(
            "incorrect padding, first two bytes cannot be padding", "===="
        )

    def badPaddingLeading1(self) -> None:

        self.__assertIOException(
            "incorrect padding, first two bytes cannot be padding", "=A=="
        )

    def badPadding(self) -> None:

        self.__assertIOException("incorrect padding, 4th byte", "Zg=a")

    def decodeTrailing3(self) -> None:

        self.__assertIOException("truncated", "Zm9vYmFy123")

    def decodeTrailing2(self) -> None:

        self.__assertIOException("truncated", "Zm9vYmFy12")

    def decodeTrailing1(self) -> None:

        self.__assertIOException("truncated", "Zm9vYmFy1")

    def decodeTrailingJunk(self) -> None:

        self.__assertEncoded("foobar", "Zm9vYmFy!!!")

    def truncatedString(self) -> None:

        x = b"n"
        self.decode(x, io.BytesIO())

    def nonBase64Bytes(self) -> None:

        self.__assertEncoded("Hello World", "S?G!V%sbG 8g\rV\t\n29ybGQ*=")

    def decodeWithInnerPad(self) -> None:

        self.__assertEncoded(
            "Hello WorldHello World", "SGVsbG8gV29ybGQ=SGVsbG8gV29ybGQ="
        )

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

        pass  # LLM could not translate method body

    @staticmethod
    def __assertEncoded(clearText: str, encoded: str) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
