from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import *


class MimeUtilityTestCase:

    @pytest.mark.test
    def decodeInvalidEncoding(self) -> None:

        with pytest.raises(ValueError):
            MimeUtility.decodeText("=?invalid?B?xyz-?=")

    @pytest.mark.test
    def decodeIso88591Base64EncodedWithWhiteSpace(self) -> None:

        from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import (
            MimeUtility,
        )

        self.__assertEncoded(
            "If you can read this you understand the example.",
            "=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?=\t  \r\n"
            + '   =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?="\r\n',
        )

    @pytest.mark.test
    def decodeIso88591Base64Encoded(self) -> None:

        from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import (
            MimeUtility,
        )

        self.__assertEncoded(
            "If you can read this you understand the example.",
            "=?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?="
            + ' =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?="\r\n',
        )

    @pytest.mark.test
    def decodeUtf8Base64Encoded(self) -> None:

        from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import (
            MimeUtility,
        )

        self.__assertEncoded(" hé ! àèôu !!!", "=?UTF-8?B?IGjDqSEgw6DDqMO0dSAhISE=?=")

    @pytest.mark.test
    def decodeUtf8QuotedPrintableEncoded(self) -> None:

        from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import (
            MimeUtility,
        )

        expected = " hé au !!!"
        encoded = "=?UTF-8?Q?_h=C3=A9au_!!!?="

        assert expected == MimeUtility.decodeText(encoded)

    @pytest.mark.test
    def noNeedToDecode(self) -> None:

        from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import (
            MimeUtility,
        )

        self.__assertEncoded("abc", "abc")

    @staticmethod
    def __assertEncoded(expected: str, encoded: str) -> None:

        from src.main.org.apache.commons.fileupload.util.mime.MimeUtility import (
            MimeUtility,
        )

        assert expected == MimeUtility.decodeText(encoded)
