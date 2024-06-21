from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringDecoder import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.net.QuotedPrintableCodec import *
from src.main.org.apache.commons.codec.net.RFC1522Codec import *


class QCodec(StringDecoder, StringEncoder, RFC1522Codec):

    __encodeBlanks: bool = False

    __UNDERSCORE: int = 95

    __SPACE: int = 32

    __PRINTABLE_CHARS: typing.List[bool] = [False] * 256
    __charset: str = None

    def _doDecoding(self, bytes: typing.List[int]) -> typing.List[int]:

        if bytes is None:
            return None

        has_underscores = False
        for b in bytes:
            if b == self.__UNDERSCORE:
                has_underscores = True
                break

        if has_underscores:
            tmp = [0] * len(bytes)
            for i in range(len(bytes)):
                b = bytes[i]
                if b != self.__UNDERSCORE:
                    tmp[i] = b
                else:
                    tmp[i] = self.__SPACE
            return QuotedPrintableCodec.decodeQuotedPrintable(tmp)

        return QuotedPrintableCodec.decodeQuotedPrintable(bytes)

    def _doEncoding(self, bytes: typing.List[int]) -> typing.List[int]:

        if bytes is None:
            return None

        data = QuotedPrintableCodec.encodeQuotedPrintable1(
            self.__PRINTABLE_CHARS, bytes
        )

        if self.__encodeBlanks:
            for i in range(len(data)):
                if data[i] == self.__SPACE:
                    data[i] = self.__UNDERSCORE

        return data

    def _getEncoding(self) -> str:

        return "Q"

    def setEncodeBlanks(self, b: bool) -> None:

        self.__encodeBlanks = b

    def isEncodeBlanks(self) -> bool:

        return self.__encodeBlanks

    def getDefaultCharset(self) -> str:

        return self.__charset

    def getCharset(self) -> str:

        return self.__charset

    def decode1(self, obj: typing.Any) -> typing.Any:

        if obj is None:
            return None
        if isinstance(obj, str):
            return self.decode0(obj)
        raise DecoderException(
            "Objects of type "
            + type(obj).__name__
            + " cannot be decoded using Q codec",
            None,
        )

    def encode3(self, obj: typing.Any) -> typing.Any:

        if obj is None:
            return None
        if isinstance(obj, str):
            return self.encode2(obj)
        raise EncoderException(
            "Objects of type "
            + type(obj).__name__
            + " cannot be encoded using Q codec",
            None,
        )

    def decode0(self, str: str) -> str:

        if str is None:
            return None
        try:
            return self.decodeText(str)
        except UnsupportedEncodingException as e:
            raise DecoderException(e.getMessage(), e)

    def encode2(self, sourceStr: str) -> str:

        if sourceStr is None:
            return None
        return self.encode0(sourceStr, self.getCharset())

    def encode1(self, sourceStr: str, sourceCharset: str) -> str:

        if sourceStr is None:
            return None
        try:
            return self.encodeText1(sourceStr, sourceCharset)
        except UnsupportedEncodingException as e:
            raise EncoderException(e.getMessage(), e)

    def encode0(self, sourceStr: str, sourceCharset: str) -> str:

        if sourceStr is None:
            return None
        return self.encodeText0(sourceStr, sourceCharset)

    @staticmethod
    def QCodec2() -> QCodec:

        return QCodec(1, None, "UTF-8")

    @staticmethod
    def QCodec0(charsetName: str) -> QCodec:

        return QCodec(1, None, charsetName)

    def __init__(self, constructorId: int, charsetName: str, charset: str) -> None:

        if constructorId == 1:
            self.__charset = charset
        else:
            self.__charset = charset
