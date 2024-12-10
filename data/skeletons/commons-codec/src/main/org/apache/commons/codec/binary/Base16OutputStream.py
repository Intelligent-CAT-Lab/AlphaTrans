from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.BaseNCodecOutputStream import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.Base16 import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class Base16OutputStream(BaseNCodecOutputStream):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def Base16OutputStream3(
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> Base16OutputStream:
        pass

    @staticmethod
    def Base16OutputStream2(
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter], doEncode: bool
    ) -> Base16OutputStream:
        pass

    @staticmethod
    def Base16OutputStream1(
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        doEncode: bool,
        lowerCase: bool,
    ) -> Base16OutputStream:
        pass

    def __init__(
        self,
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        doEncode: bool,
        lowerCase: bool,
        decodingPolicy: CodecPolicy,
    ) -> None:
        pass

    # Class Methods End
