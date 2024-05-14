# Imports Begin
from src.main.org.apache.commons.codec.net.RFC1522Codec import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CharEncoding import *
import typing

# Imports End


class RFC1522CodecTest:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testDecodeInvalid(self) -> None:
        pass

    def testNullInput(self) -> None:
        pass

    def __assertExpectedDecoderException(self, s: str) -> None:
        pass

    # Class Methods End


class RFC1522TestCodec(RFC1522Codec):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _getEncoding(self) -> str:
        pass

    def _doEncoding(self, bytes: typing.List[int]) -> typing.List[int]:
        pass

    def _doDecoding(self, bytes: typing.List[int]) -> typing.List[int]:
        pass

    # Class Methods End
