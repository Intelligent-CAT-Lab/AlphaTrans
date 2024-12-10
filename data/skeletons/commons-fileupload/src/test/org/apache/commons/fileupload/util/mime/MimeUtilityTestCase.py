from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import *
import unittest
import os
import io

# Imports End


class MimeUtilityTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def decodeInvalidEncoding_test0_decomposed(self) -> None:
        pass

    def decodeIso88591Base64EncodedWithWhiteSpace_test0_decomposed(self) -> None:
        pass

    def decodeIso88591Base64Encoded_test0_decomposed(self) -> None:
        pass

    def decodeUtf8Base64Encoded_test0_decomposed(self) -> None:
        pass

    def decodeUtf8QuotedPrintableEncoded_test0_decomposed(self) -> None:
        pass

    def noNeedToDecode_test0_decomposed(self) -> None:
        pass

    @staticmethod
    def __assertEncoded(expected: str, encoded: str) -> None:
        pass

    # Class Methods End
