# Imports Begin
from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import *
import unittest

# Imports End


class MimeUtilityTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def decodeInvalidEncoding(self) -> None:

        try:
            self.decodeText("=?invalid?B?xyz-?=")
        except Exception as e:
            self.assertTrue(False, msg=str(e))

    def decodeIso88591Base64EncodedWithWhiteSpace(self) -> None:

        self.__assertEncoded(
            "If you can read this you understand the example.",
            "=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?=\t  \r\n"
            + '   =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?="\r\n',
        )

    def decodeIso88591Base64Encoded(self) -> None:

        self.__assertEncoded(
            "If you can read this you understand the example.",
            "=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?="
            + ' =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?="\r\n',
        )

    def decodeUtf8Base64Encoded(self) -> None:

        self.__assertEncoded(
            " h\u00e9 ! \u00e0\u00e8\u00f4u !!!", "=?UTF-8?B?IGjDqSEgw6DDqMO0dSAhISE=?="
        )

    def decodeUtf8QuotedPrintableEncoded(self) -> None:

        self.__assertEncoded(
            " hé!!! àèôu !!!", "=?UTF-8?Q?_h=C3=A9=21_=C3=A0=C3=A8=C3=B4u_=21=21=21?="
        )

    def noNeedToDecode(self) -> None:

        self.assertTrue(__assertEncoded("abc", "abc"))

    @staticmethod
    def __assertEncoded(expected: str, encoded: str) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
