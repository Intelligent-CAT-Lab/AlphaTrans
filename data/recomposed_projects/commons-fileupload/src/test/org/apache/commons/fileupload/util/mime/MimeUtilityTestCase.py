# Imports Begin
import unittest

# Imports End


class MimeUtilityTestCase(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def decodeInvalidEncoding(self) -> None:

        try:
            MimeUtility.decodeText("=?invalid?B?xyz-?=")
        except Exception as e:
            print(e)

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

        expected = " h\u00e9! \u00e0\u00e8\u00f4u !!!".encode("utf-8").decode("base64")
        encoded = "=?UTF-8?B?IGjDqSEgw6DDqMO0dSAhISE=?="
        self.__assertEncoded(expected, encoded)

    def decodeUtf8QuotedPrintableEncoded(self) -> None:

        self.__assertEncoded(
            " h\u00e9! \u00e0\u00e8\u00f4u !!!",
            "=?UTF-8?Q?_h=C3=A9!_=C3=A0=C3=A8=C3=B4u_!!!?=",
        )

    def noNeedToDecode(self) -> None:

        self.__assertEncoded("abc", "abc")

    @staticmethod
    def __assertEncoded(expected: str, encoded: str) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
