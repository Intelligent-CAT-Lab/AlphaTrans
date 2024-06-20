from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.util.mime.Base64Decoder import *
import unittest
import io

# Imports End


class Base64DecoderTestCase(unittest.TestCase):

    # Class Fields Begin
    __US_ASCII_CHARSET: str = None
    # Class Fields End

    # Class Methods Begin
    def nonASCIIcharacter(self) -> None:
        pass

    def badLength(self) -> None:
        pass

    def badPaddingLeading2(self) -> None:
        pass

    def badPaddingLeading1(self) -> None:
        pass

    def badPadding(self) -> None:
        pass

    def decodeTrailing3(self) -> None:
        pass

    def decodeTrailing2(self) -> None:
        pass

    def decodeTrailing1(self) -> None:
        pass

    def decodeTrailingJunk(self) -> None:
        pass

    def truncatedString(self) -> None:
        pass

    def nonBase64Bytes(self) -> None:
        pass

    def decodeWithInnerPad(self) -> None:
        pass

    def rfc4648Section10Decode(self) -> None:
        pass

    @staticmethod
    def __assertIOException(messageText: str, encoded: str) -> None:
        pass

    @staticmethod
    def __assertEncoded(clearText: str, encoded: str) -> None:
        pass

    # Class Methods End
