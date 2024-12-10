from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder import *
import unittest
import os
import io

# Imports End


class QuotedPrintableDecoderTestCase(unittest.TestCase):

    # Class Fields Begin
    __US_ASCII_CHARSET: str = None
    # Class Fields End

    # Class Methods Begin
    def truncatedEscape_test0_decomposed(self) -> None:
        pass

    def invalidSoftBreak2_test0_decomposed(self) -> None:
        pass

    def invalidSoftBreak1_test0_decomposed(self) -> None:
        pass

    def softLineBreakDecode_test0_decomposed(self) -> None:
        pass

    def invalidCharDecode_test0_decomposed(self) -> None:
        pass

    def unsafeDecodeLowerCase_test0_decomposed(self) -> None:
        pass

    def unsafeDecode_test0_decomposed(self) -> None:
        pass

    def invalidQuotedPrintableEncoding_test0_decomposed(self) -> None:
        pass

    def basicEncodeDecode_test0_decomposed(self) -> None:
        pass

    def plainDecode_test0_decomposed(self) -> None:
        pass

    def emptyDecode_test0_decomposed(self) -> None:
        pass

    @staticmethod
    def __assertIOException(messageText: str, encoded: str) -> None:
        pass

    @staticmethod
    def __assertEncoded(clearText: str, encoded: str) -> None:
        pass

    # Class Methods End
