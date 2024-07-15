from __future__ import annotations
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.Base32 import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.BaseNCodecOutputStream import *


class Base32OutputStream(BaseNCodecOutputStream):

    def __init__(
        self,
        ouput: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        doEncode: bool,
        lineLength: int,
        lineSeparator: typing.List[int],
        decodingPolicy: CodecPolicy,
    ) -> None:
        super().__init__(
            ouput,
            Base32(
                lineLength, lineSeparator, False, BaseNCodec.PAD_DEFAULT, decodingPolicy
            ),
            doEncode,
        )

    @staticmethod
    def Base32OutputStream2(
        ouput: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        doEncode: bool,
        lineLength: int,
        lineSeparator: typing.List[int],
    ) -> BaseNCodecOutputStream:
        return BaseNCodecOutputStream(
            ouput, Base32.Base325(lineLength, lineSeparator), doEncode
        )

    @staticmethod
    def Base32OutputStream1(
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter], doEncode: bool
    ) -> BaseNCodecOutputStream:
        return BaseNCodecOutputStream(out, Base32.Base321(False), doEncode)

    @staticmethod
    def Base32OutputStream0(
        out: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter]
    ) -> BaseNCodecOutputStream:
        return Base32OutputStream.Base32OutputStream1(out, True)
