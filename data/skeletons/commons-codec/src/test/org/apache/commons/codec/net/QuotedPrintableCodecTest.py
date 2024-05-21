from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.net.QuotedPrintableCodec import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CharEncoding import *
import typing
from typing import *
import io

# Imports End


class QuotedPrintableCodecTest:

    # Class Fields Begin
    SWISS_GERMAN_STUFF_UNICODE: typing.List[int] = None
    RUSSIAN_STUFF_UNICODE: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    def testFinalBytes(self) -> None:
        pass

    def testUltimateSoftBreak(self) -> None:
        pass

    def testTrailingSpecial(self) -> None:
        pass

    def testSkipNotEncodedCRLF(self) -> None:
        pass

    def testSoftLineBreakEncode(self) -> None:
        pass

    def testSoftLineBreakDecode(self) -> None:
        pass

    def testDefaultEncoding(self) -> None:
        pass

    def testDecodeObjects(self) -> None:
        pass

    def testInvalidEncoding(self) -> None:
        pass

    def testEncodeObjects(self) -> None:
        pass

    def testDecodeStringWithNull(self) -> None:
        pass

    def testEncodeStringWithNull(self) -> None:
        pass

    def testDecodeWithNullArray(self) -> None:
        pass

    def testEncodeUrlWithNullBitSet(self) -> None:
        pass

    def testEncodeNull(self) -> None:
        pass

    def testDecodeInvalid(self) -> None:
        pass

    def testEncodeDecodeNull(self) -> None:
        pass

    def testUnsafeEncodeDecode(self) -> None:
        pass

    def testSafeCharEncodeDecode(self) -> None:
        pass

    def testBasicEncodeDecode(self) -> None:
        pass

    def testUTF8RoundTrip(self) -> None:
        pass

    def __constructString(self, unicodeChars: typing.List[int]) -> str:
        pass

    # Class Methods End
