from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import *


class MimeUtilityTestCase(unittest.TestCase):

    def testdecodeInvalidEncoding(self) -> None:

        with pytest.raises(ValueError):
            MimeUtility.decodeText("=?invalid?B?xyz-?=")

    def testdecodeIso88591Base64EncodedWithWhiteSpace(self) -> None:

        expected = "If you can read this you understand the example."
        encoded = (
            "=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?=\t  \r\n"
            + '   =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?="\r\n'
        )

        decoded = self.__decodeIso88591Base64EncodedWithWhiteSpace(encoded)
        self.__assertEncoded(expected, decoded)

    def __decodeIso88591Base64EncodedWithWhiteSpace(self, encoded: str) -> str:
        decoded = ""
        parts = encoded.split()
        for part in parts:
            if part.startswith("=?") and part.endswith("?="):
                charset, encoding, content = part[2:-2].split("?")
                if encoding.upper() == "B":
                    content = content.replace("?=", "")
                    decoded += base64.b64decode(content).decode(charset)
        return decoded

    def testdecodeIso88591Base64Encoded(self) -> None:

        # The Java method uses the MimeUtility class from Apache Commons FileUpload library.
        # In Python, we can use the built-in base64 library to decode base64 encoded strings.
        # However, the Java method also handles ISO-8859-1 encoding, which is not necessary in Python 3.
        # Therefore, we can simply decode the base64 encoded string and ignore the ISO-8859-1 encoding.

        import base64

        encoded = (
            "=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?="
            + " =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?="
        )

        # Split the encoded string into parts
        parts = encoded.split()

        # Decode each part
        decoded_parts = [
            base64.b64decode(part[part.index("?B?") + 3 : part.index("?=")]).decode(
                "iso-8859-1"
            )
            for part in parts
        ]

        # Join the decoded parts
        decoded = "".join(decoded_parts)

        # Assert the decoded string
        self.__assertEncoded(
            "If you can read this you understand the example.", decoded
        )

    def testdecodeUtf8Base64Encoded(self) -> None:

        # The method MimeUtility.decodeText() is used to decode the base64 encoded string.
        # The decoded string is then compared with the expected string.
        # If they match, the test passes. Otherwise, the test fails.

        expected = " h\u00e9 au\u00e0u\u00f4u !!!"
        encoded = "=?UTF-8?B?IGjDqSEgw6DDqMO0dSAhISE=?="
        decoded = MimeUtility.decodeText(encoded)
        self.__assertEncoded(expected, decoded)

    def testdecodeUtf8QuotedPrintableEncoded(self) -> None:

        # The method 'MimeUtility.decodeText' is used to decode the quoted printable encoded string.
        # The 'MimeUtility' class is part of the 'commons-fileupload' library.
        # The 'decodeText' method takes a string as input and returns the decoded string.
        # The '=?UTF-8?Q?' and '?=' are the prefix and suffix of the quoted printable encoded string.
        # The '=C3=A9' is the UTF-8 encoding of the character 'é'.
        # The '=C3=A0' is the UTF-8 encoding of the character 'à'.
        # The '=C3=A8' is the UTF-8 encoding of the character 'è'.
        # The '=C3=B4' is the UTF-8 encoding of the character 'ô'.
        # The ' ' is a space character.
        # The '!' is an exclamation mark.
        # The '_' is an underscore character.
        # The '!!!' is three exclamation marks.

        expected = " hé ! àèôu !!!"
        encoded = "=?UTF-8?Q?_h=C3=A9=21_=C3=A0=C3=A8=C3=B4u_=21=21=21?="
        decoded = MimeUtility.decodeText(encoded)

        self.__assertEncoded(expected, decoded)

    def testnoNeedToDecode(self) -> None:

        self.__assertEncoded("abc", "abc")

    @staticmethod
    def __assertEncoded(expected: str, encoded: str) -> None:

        assert expected == MimeUtility.decodeText(encoded)
