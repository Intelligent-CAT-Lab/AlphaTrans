from __future__ import annotations
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.Base16 import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.BaseNCodecOutputStream import *


class Base16OutputStream(BaseNCodecOutputStream):

    @staticmethod
    def Base16OutputStream3(
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> Base16OutputStream:
        return Base16OutputStream2(out, True)

    @staticmethod
    def Base16OutputStream2(
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter], doEncode: bool
    ) -> Base16OutputStream:
        return Base16OutputStream1(out, doEncode, False)

    @staticmethod
    def Base16OutputStream1(
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        doEncode: bool,
        lowerCase: bool,
    ) -> Base16OutputStream:
        return Base16OutputStream(out, doEncode, lowerCase, CodecPolicy.LENIENT)

    def __init__(
        self,
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        doEncode: bool,
        lowerCase: bool,
        decodingPolicy: CodecPolicy,
    ) -> None:
        super().__init__(out, Base16(lowerCase, decodingPolicy), doEncode)
