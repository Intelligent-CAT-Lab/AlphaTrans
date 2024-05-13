# Imports Begin
from src.main.org.apache.commons.fileupload.util.mime.QuotedPrintableDecoder import *

# Imports End


class QuotedPrintableDecoderTestCase:

    # Class Fields Begin
    __US_ASCII_CHARSET: str = None
    # Class Fields End

    # Class Methods Begin
    def truncatedEscape(self) -> None:
        pass

    def invalidSoftBreak2(self) -> None:
        pass

    def invalidSoftBreak1(self) -> None:
        pass

    def softLineBreakDecode(self) -> None:
        pass

    def invalidCharDecode(self) -> None:
        pass

    def unsafeDecodeLowerCase(self) -> None:
        pass

    def unsafeDecode(self) -> None:
        pass

    def invalidQuotedPrintableEncoding(self) -> None:
        pass

    def basicEncodeDecode(self) -> None:
        pass

    def plainDecode(self) -> None:
        pass

    def emptyDecode(self) -> None:
        pass

    @staticmethod
    def __assertIOException(messageText: str, encoded: str) -> None:
        pass

    @staticmethod
    def __assertEncoded(clearText: str, encoded: str) -> None:
        pass

    # Class Methods End
