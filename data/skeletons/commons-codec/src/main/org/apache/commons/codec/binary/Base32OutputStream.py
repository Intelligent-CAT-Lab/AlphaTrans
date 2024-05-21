from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.BaseNCodecOutputStream import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.Base32 import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class Base32OutputStream(BaseNCodecOutputStream):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def __init__(
        self,
        ouput: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        doEncode: bool,
        lineLength: int,
        lineSeparator: typing.List[int],
        decodingPolicy: CodecPolicy,
    ) -> None:
        pass

    @staticmethod
    def Base32OutputStream2(
        ouput: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        doEncode: bool,
        lineLength: int,
        lineSeparator: typing.List[int],
    ) -> BaseNCodecOutputStream:
        pass

    @staticmethod
    def Base32OutputStream1(
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter], doEncode: bool
    ) -> BaseNCodecOutputStream:
        pass

    @staticmethod
    def Base32OutputStream0(
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> BaseNCodecOutputStream:
        pass

    # Class Methods End
