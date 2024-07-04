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
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *


class Base64InputStream(BaseNCodecInputStream):

    def __init__(
        self,
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        doEncode: bool,
        lineLength: int,
        lineSeparator: typing.List[int],
        decodingPolicy: CodecPolicy,
    ) -> None:

        # Create a Base64 object
        base64 = Base64(lineLength, lineSeparator, False, decodingPolicy)

        # Call the superclass's constructor
        super().__init__(in_, base64, doEncode)

    @staticmethod
    def Base64InputStream2(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        doEncode: bool,
        lineLength: int,
        lineSeparator: typing.List[int],
    ) -> BaseNCodecInputStream:

        baseNCodec = Base64.Base642(lineLength, lineSeparator)
        return BaseNCodecInputStream(in_, baseNCodec, doEncode)

    @staticmethod
    def Base64InputStream1(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader], doEncode: bool
    ) -> BaseNCodecInputStream:

        baseNCodec = BaseNCodec(
            Base64.Base644(False),
            Base64.BYTES_PER_UNENCODED_BLOCK,
            Base64.BYTES_PER_ENCODED_BLOCK,
        )
        return BaseNCodecInputStream(in_, baseNCodec, doEncode)

    @staticmethod
    def Base64InputStream0(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> BaseNCodecInputStream:
        return Base64InputStream.Base64InputStream1(in_, False)
