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
from src.main.org.apache.commons.codec.binary.BaseNCodecInputStream import *


class Base16InputStream(BaseNCodecInputStream):

    @staticmethod
    def Base16InputStream3(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> Base16InputStream:

        return Base16InputStream.Base16InputStream2(in_, False)

    @staticmethod
    def Base16InputStream2(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader], doEncode: bool
    ) -> Base16InputStream:

        return Base16InputStream.Base16InputStream1(in_, doEncode, False)

    @staticmethod
    def Base16InputStream1(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        doEncode: bool,
        lowerCase: bool,
    ) -> Base16InputStream:

        return Base16InputStream(in_, doEncode, lowerCase, CodecPolicy.LENIENT)

    def __init__(
        self,
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        doEncode: bool,
        lowerCase: bool,
        decodingPolicy: CodecPolicy,
    ) -> None:

        # Create an instance of Base16
        base16 = Base16(lowerCase, decodingPolicy)

        # Call the superclass's __init__ method
        super().__init__(in_, base16, doEncode)
