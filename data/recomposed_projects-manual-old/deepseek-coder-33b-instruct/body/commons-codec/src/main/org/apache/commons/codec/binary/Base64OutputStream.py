from __future__ import annotations
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.Base64 import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.BaseNCodecOutputStream import *


class Base64OutputStream(BaseNCodecOutputStream):

    def __init__(
        self,
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        doEncode: bool,
        lineLength: int,
        lineSeparator: typing.List[int],
        decodingPolicy: CodecPolicy,
    ) -> None:

        super().__init__(
            out, Base64(lineLength, lineSeparator, False, decodingPolicy), doEncode
        )

    @staticmethod
    def Base64OutputStream2(
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        doEncode: bool,
        lineLength: int,
        lineSeparator: typing.List[int],
    ) -> BaseNCodecOutputStream:

        base64 = Base64.Base642(lineLength, lineSeparator)
        return BaseNCodecOutputStream(out, base64, doEncode)

    @staticmethod
    def Base64OutputStream1(
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter], doEncode: bool
    ) -> BaseNCodecOutputStream:

        return BaseNCodecOutputStream(out, Base64.Base644(False), doEncode)

    @staticmethod
    def Base64OutputStream0(
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> BaseNCodecOutputStream:

        return Base64OutputStream.Base64OutputStream1(out, True)
