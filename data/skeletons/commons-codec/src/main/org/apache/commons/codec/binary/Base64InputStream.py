from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.Base64 import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class Base64InputStream(BaseNCodecInputStream):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def __init__(
        self,
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        doEncode: bool,
        lineLength: int,
        lineSeparator: typing.List[int],
        decodingPolicy: CodecPolicy,
    ) -> None:
        pass

    @staticmethod
    def Base64InputStream2(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        doEncode: bool,
        lineLength: int,
        lineSeparator: typing.List[int],
    ) -> BaseNCodecInputStream:
        pass

    @staticmethod
    def Base64InputStream1(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader], doEncode: bool
    ) -> BaseNCodecInputStream:
        pass

    @staticmethod
    def Base64InputStream0(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> BaseNCodecInputStream:
        pass

    # Class Methods End
