from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class RFC1522Codec(ABC):

    # Class Fields Begin
    _SEP: str = None
    _POSTFIX: str = None
    _PREFIX: str = None
    # Class Fields End

    # Class Methods Begin
    def _decodeText(self, text: str) -> str:
        pass

    def _encodeText1(self, text: str, charsetName: str) -> str:
        pass

    def _encodeText0(self, text: str, charset: str) -> str:
        pass

    def _doDecoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def _doEncoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def _getEncoding(self) -> str:
        pass

    # Class Methods End
