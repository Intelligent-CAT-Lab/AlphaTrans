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
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *


class Base32InputStream(BaseNCodecInputStream):

    def __init__(
        self,
        input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        doEncode: bool,
        lineLength: int,
        lineSeparator: typing.List[int],
        decodingPolicy: CodecPolicy,
    ) -> None:
        super(Base32InputStream, self).__init__(
            input,
            Base32(
                lineLength, lineSeparator, False, BaseNCodec.PAD_DEFAULT, decodingPolicy
            ),
            doEncode,
        )

    @staticmethod
    def Base32InputStream2(
        input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        doEncode: bool,
        lineLength: int,
        lineSeparator: typing.List[int],
    ) -> BaseNCodecInputStream:
        return BaseNCodecInputStream(
            input, Base32.Base325(lineLength, lineSeparator), doEncode
        )

    @staticmethod
    def Base32InputStream1(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader], doEncode: bool
    ) -> BaseNCodecInputStream:
        return BaseNCodecInputStream(in_, Base32.Base321(False), doEncode)

    @staticmethod
    def Base32InputStream0(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> BaseNCodecInputStream:
        return Base32InputStream.Base32InputStream1(in_, False)
