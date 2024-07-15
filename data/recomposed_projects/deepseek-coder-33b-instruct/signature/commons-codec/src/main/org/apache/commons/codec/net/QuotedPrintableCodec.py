from __future__ import annotations
import re
import os
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringDecoder import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.net.Utils import *


class QuotedPrintableCodec:

    __SAFE_LENGTH: int = 73
    __LF: int = 10
    __CR: int = 13
    __SPACE: int = 32
    __TAB: int = 9
    __ESCAPE_CHAR: int = ord("=")
    __PRINTABLE_CHARS: typing.List[bool] = [False] * 256
    __strict: bool = False

    __charset: str = ""

    @staticmethod
    def run_static_init():

        QuotedPrintableCodec.__SPACE = 32
        QuotedPrintableCodec.__TAB = 9
        QuotedPrintableCodec.__PRINTABLE_CHARS = [False] * 256

        for i in range(33, 61):
            QuotedPrintableCodec.__PRINTABLE_CHARS[i] = True

        for i in range(62, 127):
            QuotedPrintableCodec.__PRINTABLE_CHARS[i] = True

        QuotedPrintableCodec.__PRINTABLE_CHARS[QuotedPrintableCodec.__TAB] = True
        QuotedPrintableCodec.__PRINTABLE_CHARS[QuotedPrintableCodec.__SPACE] = True

    def encode4(self, sourceStr: str, sourceCharset: str) -> str:

        if sourceStr is None:
            return None

        return StringUtils.newStringUsAscii(
            self.encode0(sourceStr.encode(sourceCharset))
        )

    def encode3(self, sourceStr: str, sourceCharset: str) -> str:
        if sourceStr is None:
            return None
        return StringUtils.newStringUsAscii(
            self.encode0(sourceStr.encode(sourceCharset))
        )

    def getDefaultCharset(self) -> str:
        return self.__charset

    def getCharset(self) -> str:
        return self.__charset

    def decode4(self, obj: typing.Any) -> typing.Any:

        if obj is None:
            return None
        if isinstance(obj, list):
            return self.decode0(obj)
        if isinstance(obj, str):
            return self.decode3(obj)
        raise DecoderException(
            "Objects of type "
            + type(obj).__name__
            + " cannot be quoted-printable decoded",
            None,
        )

    def encode2(self, obj: typing.Any) -> typing.Any:

        if obj is None:
            return None
        if isinstance(obj, list):
            return self.encode0(obj)
        if isinstance(obj, str):
            return self.encode1(obj)
        raise EncoderException(
            "Objects of type "
            + type(obj).__name__
            + " cannot be quoted-printable encoded",
            None,
        )

    def decode3(self, sourceStr: str) -> str:
        return self.decode1(sourceStr, self.getCharset())

    def decode2(self, sourceStr: str, sourceCharset: str) -> str:

        if sourceStr is None:
            return None

        bytes_ = self.decode0(StringUtils.getBytesUsAscii(sourceStr))
        return "".join(map(chr, bytes_))

    def decode1(self, sourceStr: str, sourceCharset: str) -> str:

        if sourceStr is None:
            return None

        byte_array = self.decode0(StringUtils.getBytesUsAscii(sourceStr))
        return "".join(map(chr, byte_array))

    def encode1(self, sourceStr: str) -> str:
        return self.encode3(sourceStr, self.getCharset())

    def decode0(self, bytes: typing.List[int]) -> typing.List[int]:
        return self.decodeQuotedPrintable(bytes)

    def encode0(self, bytes: typing.List[int]) -> typing.List[int]:
        return self.encodeQuotedPrintable2(self.__PRINTABLE_CHARS, bytes, self.__strict)

    @staticmethod
    def decodeQuotedPrintable(bytes: typing.List[int]) -> typing.List[int]:

        if bytes is None:
            return None

        buffer = BytesIO()

        for i in range(len(bytes)):
            b = bytes[i]

            if b == QuotedPrintableCodec.__ESCAPE_CHAR:
                try:
                    if bytes[i + 1] == QuotedPrintableCodec.__CR:
                        continue
                    u = Utils.digit16(bytes[i + 1])
                    l = Utils.digit16(bytes[i + 2])
                    buffer.write(((u << 4) + l).to_bytes(1, byteorder="big"))
                    i += 2
                except IndexError as e:
                    raise DecoderException("Invalid quoted-printable encoding", e)
            elif b != QuotedPrintableCodec.__CR and b != QuotedPrintableCodec.__LF:
                buffer.write(b.to_bytes(1, byteorder="big"))

        return list(buffer.getvalue())

    @staticmethod
    def encodeQuotedPrintable2(
        printable: typing.List[bool], bytes: typing.List[int], strict: bool
    ) -> typing.List[int]:

        QuotedPrintableCodec.__SAFE_LENGTH = 73
        QuotedPrintableCodec.__LF = 10
        QuotedPrintableCodec.__CR = 13
        QuotedPrintableCodec.__TAB = 9
        QuotedPrintableCodec.__ESCAPE_CHAR = ord("=")
        QuotedPrintableCodec.__PRINTABLE_CHARS = printable
        QuotedPrintableCodec.__strict = strict

        if bytes is None:
            return None
        if printable is None:
            printable = QuotedPrintableCodec.__PRINTABLE_CHARS
        buffer = BytesIO()
        bytesLength = len(bytes)

        if QuotedPrintableCodec.__strict:
            pos = 1
            for i in range(bytesLength - 3):
                b = QuotedPrintableCodec.__getUnsignedOctet(i, bytes)
                if pos < QuotedPrintableCodec.__SAFE_LENGTH:
                    pos += QuotedPrintableCodec.__encodeByte(
                        b, not printable[b], buffer
                    )
                else:
                    QuotedPrintableCodec.__encodeByte(
                        b,
                        not printable[b] or QuotedPrintableCodec.__isWhitespace(b),
                        buffer,
                    )

                    buffer.write(QuotedPrintableCodec.__ESCAPE_CHAR)
                    buffer.write(QuotedPrintableCodec.__CR)
                    buffer.write(QuotedPrintableCodec.__LF)
                    pos = 1
            b = QuotedPrintableCodec.__getUnsignedOctet(bytesLength - 3, bytes)
            encode = not printable[b] or (
                QuotedPrintableCodec.__isWhitespace(b)
                and pos > QuotedPrintableCodec.__SAFE_LENGTH - 5
            )
            pos += QuotedPrintableCodec.__encodeByte(b, encode, buffer)

            if pos > QuotedPrintableCodec.__SAFE_LENGTH - 2:
                buffer.write(QuotedPrintableCodec.__ESCAPE_CHAR)
                buffer.write(QuotedPrintableCodec.__CR)
                buffer.write(QuotedPrintableCodec.__LF)
            for i in range(bytesLength - 2, bytesLength):
                b = QuotedPrintableCodec.__getUnsignedOctet(i, bytes)
                encode = not printable[b] or (
                    i > bytesLength - 2 and QuotedPrintableCodec.__isWhitespace(b)
                )
                QuotedPrintableCodec.__encodeByte(b, encode, buffer)
        else:
            for c in bytes:
                b = c
                if b < 0:
                    b = 256 + b
                if printable[b]:
                    buffer.write(bytes([b]))
                else:
                    QuotedPrintableCodec.__encodeQuotedPrintable0(b, buffer)
        return list(buffer.getvalue())

    @staticmethod
    def encodeQuotedPrintable1(
        printable: typing.List[bool], bytes: typing.List[int]
    ) -> typing.List[int]:
        return QuotedPrintableCodec.encodeQuotedPrintable2(printable, bytes, False)

    @staticmethod
    def QuotedPrintableCodec4() -> QuotedPrintableCodec:
        return QuotedPrintableCodec(1, None, "UTF-8", False)

    @staticmethod
    def QuotedPrintableCodec3(strict: bool) -> QuotedPrintableCodec:
        return QuotedPrintableCodec(1, None, "UTF-8", strict)

    @staticmethod
    def QuotedPrintableCodec2(charset: str) -> QuotedPrintableCodec:
        return QuotedPrintableCodec(1, None, charset, False)

    @staticmethod
    def QuotedPrintableCodec0(charsetName: str) -> QuotedPrintableCodec:
        return QuotedPrintableCodec(1, None, charsetName, False)

    def __init__(
        self, constructorId: int, charsetName: str, charset: str, strict: bool
    ) -> None:

        if constructorId == 1:
            self.__charset = charset
            self.__strict = strict
        else:
            self.__charset = charset
            self.__strict = strict

    @staticmethod
    def __isWhitespace(b: int) -> bool:
        return b == QuotedPrintableCodec.__SPACE or b == QuotedPrintableCodec.__TAB

    @staticmethod
    def __encodeByte(
        b: int, encode: bool, buffer: typing.Union[io.BytesIO, bytearray]
    ) -> int:
        if encode:
            return QuotedPrintableCodec.__encodeQuotedPrintable0(b, buffer)
        buffer.write(bytes([b]))
        return 1

    @staticmethod
    def __getUnsignedOctet(index: int, bytes: typing.List[int]) -> int:
        b = bytes[index]
        if b < 0:
            b = 256 + b
        return b

    @staticmethod
    def __encodeQuotedPrintable0(
        b: int, buffer: typing.Union[io.BytesIO, bytearray]
    ) -> int:

        QuotedPrintableCodec.__ESCAPE_CHAR = 61  # ASCII value of '='
        buffer.write(QuotedPrintableCodec.__ESCAPE_CHAR.to_bytes(1, byteorder="big"))

        hex1 = Utils.hexDigit(b >> 4)
        hex2 = Utils.hexDigit(b)

        buffer.write(hex1.encode())
        buffer.write(hex2.encode())

        return 3


QuotedPrintableCodec.run_static_init()
