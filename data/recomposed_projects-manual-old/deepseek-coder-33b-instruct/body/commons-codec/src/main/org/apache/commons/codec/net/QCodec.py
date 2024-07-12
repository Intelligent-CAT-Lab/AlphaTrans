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
    __charset: str = ""

    @staticmethod
    def run_static_init():

        QCodec.__encodeBlanks = False
        QCodec.__UNDERSCORE = 95
        QCodec.__SPACE = 32
        QCodec.__PRINTABLE_CHARS = [False] * 256

        QCodec.__PRINTABLE_CHARS[ord(" ")] = True
        QCodec.__PRINTABLE_CHARS[ord("1")] = True
        QCodec.__PRINTABLE_CHARS[ord("2")] = True
        QCodec.__PRINTABLE_CHARS[ord("3")] = True
        QCodec.__PRINTABLE_CHARS[ord("4")] = True
        QCodec.__PRINTABLE_CHARS[ord("5")] = True
        QCodec.__PRINTABLE_CHARS[ord("6")] = True
        QCodec.__PRINTABLE_CHARS[ord("7")] = True
        QCodec.__PRINTABLE_CHARS[ord("8")] = True
        QCodec.__PRINTABLE_CHARS[ord("9")] = True
        QCodec.__PRINTABLE_CHARS[ord("0")] = True
        QCodec.__PRINTABLE_CHARS[ord(":")] = True
        QCodec.__PRINTABLE_CHARS[ord(";")] = True
        QCodec.__PRINTABLE_CHARS[ord("<")] = True
        QCodec.__PRINTABLE_CHARS[ord("=")] = True
        QCodec.__PRINTABLE_CHARS[ord(">")] = True
        QCodec.__PRINTABLE_CHARS[ord("?")] = True
        QCodec.__PRINTABLE_CHARS[ord("@")] = True
        QCodec.__PRINTABLE_CHARS[ord("A")] = True
        QCodec.__PRINTABLE_CHARS[ord("B")] = True
        QCodec.__PRINTABLE_CHARS[ord("C")] = True
        QCodec.__PRINTABLE_CHARS[ord("D")] = True
        QCodec.__PRINTABLE_CHARS[ord("E")] = True
        QCodec.__PRINTABLE_CHARS[ord("F")] = True
        QCodec.__PRINTABLE_CHARS[ord("G")] = True
        QCodec.__PRINTABLE_CHARS[ord("H")] = True
        QCodec.__PRINTABLE_CHARS[ord("I")] = True
        QCodec.__PRINTABLE_CHARS[ord("J")] = True
        QCodec.__PRINTABLE_CHARS[ord("K")] = True
        QCodec.__PRINTABLE_CHARS[ord("L")] = True
        QCodec.__PRINTABLE_CHARS[ord("M")] = True
        QCodec.__PRINTABLE_CHARS[ord("N")] = True
        QCodec.__PRINTABLE_CHARS[ord("O")] = True
        QCodec.__PRINTABLE_CHARS[ord("P")] = True
        QCodec.__PRINTABLE_CHARS[ord("Q")] = True
        QCodec.__PRINTABLE_CHARS[ord("R")] = True
        QCodec.__PRINTABLE_CHARS[ord("S")] = True
        QCodec.__PRINTABLE_CHARS[ord("T")] = True
        QCodec.__PRINTABLE_CHARS[ord("U")] = True
        QCodec.__PRINTABLE_CHARS[ord("V")] = True
        QCodec.__PRINTABLE_CHARS[ord("W")] = True
        QCodec.__PRINTABLE_CHARS[ord("X")] = True
        QCodec.__PRINTABLE_CHARS[ord("Y")] = True
        QCodec.__PRINTABLE_CHARS[ord("Z")] = True
        QCodec.__PRINTABLE_CHARS[ord("[")] = True
        QCodec.__PRINTABLE_CHARS[ord("\\")] = True
        QCodec.__PRINTABLE_CHARS[ord("]")] = True
        QCodec.__PRINTABLE_CHARS[ord("^")] = True
        QCodec.__PRINTABLE_CHARS[ord("_")] = True
        QCodec.__PRINTABLE_CHARS[ord("`")] = True
        QCodec.__PRINTABLE_CHARS[ord("a")] = True
        QCodec.__PRINTABLE_CHARS[ord("b")] = True
        QCodec.__PRINTABLE_CHARS[ord("c")] = True
        QCodec.__PRINTABLE_CHARS[ord("d")] = True
        QCodec.__PRINTABLE_CHARS[ord("e")] = True
        QCodec.__PRINTABLE_CHARS[ord("f")] = True
        QCodec.__PRINTABLE_CHARS[ord("g")] = True
        QCodec.__PRINTABLE_CHARS[ord("h")] = True
        QCodec.__PRINTABLE_CHARS[ord("i")] = True
        QCodec.__PRINTABLE_CHARS[ord("j")] = True
        QCodec.__PRINTABLE_CHARS[ord("k")] = True
        QCodec.__PRINTABLE_CHARS[ord("l")] = True
        QCodec.__PRINTABLE_CHARS[ord("m")] = True
        QCodec.__PRINTABLE_CHARS[ord("n")] = True
        QCodec.__PRINTABLE_CHARS[ord("o")] = True
        QCodec.__PRINTABLE_CHARS[ord("p")] = True
        QCodec.__PRINTABLE_CHARS[ord("q")] = True
        QCodec.__PRINTABLE_CHARS[ord("r")] = True
        QCodec.__PRINTABLE_CHARS[ord("s")] = True
        QCodec.__PRINTABLE_CHARS[ord("t")] = True
        QCodec.__PRINTABLE_CHARS[ord("u")] = True
        QCodec.__PRINTABLE_CHARS[ord("v")] = True
        QCodec.__PRINTABLE_CHARS[ord("w")] = True
        QCodec.__PRINTABLE_CHARS[ord("x")] = True
        QCodec.__PRINTABLE_CHARS[ord("y")] = True
        QCodec.__PRINTABLE_CHARS[ord("z")] = True
        QCodec.__PRINTABLE_CHARS[ord("{")] = True
        QCodec.__PRINTABLE_CHARS[ord("|")] = True
        QCodec.__PRINTABLE_CHARS[ord("}")] = True
        QCodec.__PRINTABLE_CHARS[ord("~")] = True

    def _doDecoding(self, bytes: typing.List[int]) -> typing.List[int]:

        if bytes is None:
            return None

        has_underscores = any(b == self.__UNDERSCORE for b in bytes)

        if has_underscores:
            tmp = [b if b != self.__UNDERSCORE else self.__SPACE for b in bytes]
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
            + obj.__class__.__name__
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
            + obj.__class__.__name__
            + " cannot be encoded using Q codec",
            None,
        )

    def decode0(self, str: str) -> str:

        if str is None:
            return None

        try:
            return self._decodeText(str)
        except DecoderException as e:
            raise DecoderException(e.args[0], e)

    def encode2(self, sourceStr: str) -> str:
        if sourceStr is None:
            return None
        return self.encode0(sourceStr, self.getCharset())

    def encode1(self, sourceStr: str, sourceCharset: str) -> str:
        if sourceStr is None:
            return None
        try:
            return self._encodeText1(sourceStr, sourceCharset)
        except ValueError as e:
            raise EncoderException(e.getMessage(), e)

    def encode0(self, sourceStr: str, sourceCharset: str) -> str:
        if sourceStr is None:
            return None
        return self._encodeText0(sourceStr, sourceCharset)

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


QCodec.run_static_init()
