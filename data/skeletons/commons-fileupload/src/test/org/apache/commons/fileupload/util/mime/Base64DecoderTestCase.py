from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.util.mime.Base64Decoder import *
import unittest
import os
import io

# Imports End


class Base64DecoderTestCase(unittest.TestCase):

    # Class Fields Begin
    __US_ASCII_CHARSET: str = None
    # Class Fields End

    # Class Methods Begin
    def nonASCIIcharacter_test0_decomposed(self) -> None:
        pass

    def badLength_test0_decomposed(self) -> None:
        pass

    def badPaddingLeading2_test0_decomposed(self) -> None:
        pass

    def badPaddingLeading1_test0_decomposed(self) -> None:
        pass

    def badPadding_test0_decomposed(self) -> None:
        pass

    def decodeTrailing3_test0_decomposed(self) -> None:
        pass

    def decodeTrailing2_test0_decomposed(self) -> None:
        pass

    def decodeTrailing1_test0_decomposed(self) -> None:
        pass

    def decodeTrailingJunk_test0_decomposed(self) -> None:
        pass

    def truncatedString_test0_decomposed(self) -> None:
        pass

    def nonBase64Bytes_test0_decomposed(self) -> None:
        pass

    def decodeWithInnerPad_test0_decomposed(self) -> None:
        pass

    def rfc4648Section10Decode_test0_decomposed(self) -> None:
        pass

    @staticmethod
    def __assertIOException(messageText: str, encoded: str) -> None:
        pass

    @staticmethod
    def __assertEncoded(clearText: str, encoded: str) -> None:
        pass

    # Class Methods End
