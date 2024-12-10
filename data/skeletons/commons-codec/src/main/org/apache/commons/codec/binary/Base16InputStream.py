from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.Base16 import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class Base16InputStream(BaseNCodecInputStream):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def Base16InputStream3(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> Base16InputStream:
        pass

    @staticmethod
    def Base16InputStream2(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader], doEncode: bool
    ) -> Base16InputStream:
        pass

    @staticmethod
    def Base16InputStream1(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        doEncode: bool,
        lowerCase: bool,
    ) -> Base16InputStream:
        pass

    def __init__(
        self,
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        doEncode: bool,
        lowerCase: bool,
        decodingPolicy: CodecPolicy,
    ) -> None:
        pass

    # Class Methods End
