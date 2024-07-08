from __future__ import annotations
import copy
import re
from io import BytesIO
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringDecoder import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.net.Utils import *


class URLCodec(BinaryDecoder, BinaryEncoder, StringDecoder, StringEncoder):

    _WWW_FORM_URL: typing.List[bool] = None

    _ESCAPE_CHAR: int = 37
    _charset: str = ""

    __WWW_FORM_URL_SAFE: typing.List[bool] = [False] * 256

    @staticmethod
    def run_static_init():
        for i in range(ord("a"), ord("z") + 1):
            URLCodec.__WWW_FORM_URL_SAFE[i] = True
        for i in range(ord("A"), ord("Z") + 1):
            URLCodec.__WWW_FORM_URL_SAFE[i] = True
        for i in range(ord("0"), ord("9") + 1):
            URLCodec.__WWW_FORM_URL_SAFE[i] = True
        URLCodec.__WWW_FORM_URL_SAFE[ord("-")] = True
        URLCodec.__WWW_FORM_URL_SAFE[ord("_")] = True
        URLCodec.__WWW_FORM_URL_SAFE[ord(".")] = True
        URLCodec.__WWW_FORM_URL_SAFE[ord("*")] = True
        URLCodec.__WWW_FORM_URL_SAFE[ord(" ")] = True

        URLCodec._WWW_FORM_URL = URLCodec.__WWW_FORM_URL_SAFE.copy()

    def getEncoding(self) -> str:
        return self._charset

    def getDefaultCharset(self) -> str:
        return self._charset

    def decode3(self, obj: typing.Any) -> typing.Any:
        if obj is None:
            return None
        if isinstance(obj, bytes):
            return self.decode0(obj)
        if isinstance(obj, str):
            return self.decode2(obj)
        raise DecoderException(
            f"Objects of type {obj.__class__.__name__} cannot be URL decoded", None
        )

    def encode3(self, obj: typing.Any) -> typing.Any:
        if obj is None:
            return None
        if isinstance(obj, bytes):
            return self.encode0(obj)
        if isinstance(obj, str):
            return self.encode2(obj)
        raise EncoderException(
            f"Objects of type {obj.__class__.__name__} cannot be URL encoded", None
        )

    def decode2(self, str: str) -> str:
        if str is None:
            return None
        try:
            return self.decode1(str, self.getDefaultCharset())
        except ValueError as e:
            raise DecoderException(e.getMessage(), e)

    def decode1(self, str: str, charsetName: str) -> str:
        if str is None:
            return None
        return str(self.decode0(StringUtils.getBytesUsAscii(str)), charsetName)

    def encode2(self, str: str) -> str:
        if str is None:
            return None
        try:
            return self.encode1(str, self.getDefaultCharset())
        except ValueError as e:
            raise EncoderException(e.getMessage(), e)

    def encode1(self, str: str, charsetName: str) -> str:
        if str is None:
            return None
        return StringUtils.newStringUsAscii(self.encode0(str.encode(charsetName)))

    def decode0(self, bytes: typing.List[int]) -> typing.List[int]:
        return URLCodec.decodeUrl(bytes)

    def encode0(self, bytes: typing.List[int]) -> typing.List[int]:
        return URLCodec.encodeUrl(URLCodec.__WWW_FORM_URL_SAFE, bytes)

    @staticmethod
    def decodeUrl(bytes: typing.List[int]) -> typing.List[int]:
        if bytes is None:
            return None
        buffer = io.BytesIO()
        for i in range(len(bytes)):
            b = bytes[i]
            if b == ord("+"):
                buffer.write(ord(" "))
            elif b == URLCodec._ESCAPE_CHAR:
                try:
                    u = Utils.digit16(bytes[i + 1])
                    l = Utils.digit16(bytes[i + 2])
                    buffer.write((u << 4) + l)
                except IndexError as e:
                    raise DecoderException("Invalid URL encoding: ", e)
            else:
                buffer.write(b)
        return buffer.getvalue()

    @staticmethod
    def encodeUrl(
        urlsafe: typing.List[bool], bytes: typing.List[int]
    ) -> typing.List[int]:
        if bytes is None:
            return None
        if urlsafe is None:
            urlsafe = URLCodec.__WWW_FORM_URL_SAFE
        buffer = io.BytesIO()
        for c in bytes:
            b = c
            if b < 0:
                b = 256 + b
            if urlsafe[b]:
                if b == ord(" "):
                    b = ord("+")
                buffer.write(bytes([b]))
            else:
                buffer.write(bytes([URLCodec._ESCAPE_CHAR]))
                hex1 = Utils.hexDigit(b >> 4)
                hex2 = Utils.hexDigit(b)
                buffer.write(bytes([ord(hex1)]))
                buffer.write(bytes([ord(hex2)]))
        return buffer.getvalue()

    @staticmethod
    def URLCodec1() -> URLCodec:
        return URLCodec(CharEncoding.UTF_8)

    def __init__(self, charset: str) -> None:
        self._charset = charset


URLCodec.run_static_init()
