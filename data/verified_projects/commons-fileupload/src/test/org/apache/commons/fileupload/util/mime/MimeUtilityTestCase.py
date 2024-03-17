# Imports Begin
import unittest
from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import MimeUtility

# Imports End


class MimeUtilityTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test_noNeedToDecode(self) -> None:
        try:
            self.__assertEncoded("abc", "abc")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def test_decodeUtf8QuotedPrintableEncoded(self) -> None:
        try:
            self.__assertEncoded(
                " h\u00e9! \u00e0\u00e8\u00f4u !!!",
                "=?UTF-8?Q?_h=C3=A9!_=C3=A0=C3=A8=C3=B4u_!!!?=",
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def test_decodeUtf8Base64Encoded(self) -> None:
        try:
            self.__assertEncoded(
                " h\u00e9! \u00e0\u00e8\u00f4u !!!",
                "=?UTF-8?B?IGjDqSEgw6DDqMO0dSAhISE=?="
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
        # LLM added redundant (and incorrect) test logic to this test.

    def test_decodeIso88591Base64Encoded(self) -> None:
        try:
            self.__assertEncoded(
                "If you can read this you understand the example.",
                "=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?="
                    + " =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?=\"\r\n",
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

    def test_decodeIso88591Base64EncodedWithWhiteSpace(self) -> None:
        try:
            self.__assertEncoded(
                "If you can read this you understand the example.",
                "=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?=\t  \r\n"
                    + "   =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?=\"\r\n",
            )
        except Exception as e:
            self.fail(f"An exception occurred: {e}")
    
    def test_decodeInvalidEncoding(self) -> None:
        with self.assertRaises(Exception) as context:
            MimeUtility.decodeText("=?invalid?B?xyz-?=")
        self.assertTrue(isinstance(context.exception, UnicodeEncodeError) or isinstance(context.exception, UnicodeDecodeError))




    @staticmethod
    def __assertEncoded(expected: str, encoded: str) -> None:
        unittest.TestCase().assertEqual(expected, MimeUtility.decodeText(encoded))

    # Class Methods End
