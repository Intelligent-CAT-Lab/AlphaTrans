from __future__ import annotations
import re
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
    __strict: bool = None
    __charset: str = None

    def encode4(self, sourceStr: str, sourceCharset: str) -> str:

        if sourceStr is None:
            return None

        return StringUtils.newStringUsAscii(
            self.encode0(sourceStr.encode(sourceCharset))
        )

    def encode3(self, sourceStr: str, sourceCharset: str) -> str:

        if sourceStr is None:
            return None

        # Convert the source string to bytes using the specified charset
        byte_str = sourceStr.encode(sourceCharset)

        # Call the encode0 method with the byte string
        encoded_bytes = self.encode0(byte_str)

        # Convert the encoded bytes to a string using the newStringUsAscii method from StringUtils
        return StringUtils.newStringUsAscii(encoded_bytes)

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
        if isinstance(obj, bytes):
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

        try:
            return self.decode1(sourceStr, self.getCharset())
        except DecoderException as e:
            print("DecoderException occurred: ", e)
            raise

    def decode2(self, sourceStr: str, sourceCharset: str) -> str:

        if sourceStr is None:
            return None

        return self.decode0(StringUtils.getBytesUsAscii(sourceStr)).decode(
            sourceCharset
        )

    def decode1(self, sourceStr: str, sourceCharset: str) -> str:

        if sourceStr is None:
            return None

        # Assuming getBytesUsAscii is a static method in StringUtils class
        bytes = StringUtils.getBytesUsAscii(sourceStr)

        # Assuming decode0 is a method in the same class
        decoded_bytes = self.decode0(bytes)

        return "".join(map(chr, decoded_bytes))

    def encode1(self, sourceStr: str) -> str:

        return self.encode3(sourceStr, self.getCharset())

    def decode0(self, bytes: typing.List[int]) -> typing.List[int]:

        def decodeQuotedPrintable(bytes: typing.List[int]) -> typing.List[int]:
            pass

        return decodeQuotedPrintable(bytes)

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
                    buffer.write(((u << 4) + l).to_bytes(2, byteorder="big"))
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

        if bytes is None:
            return None
        if printable is None:
            printable = QuotedPrintableCodec.__PRINTABLE_CHARS

        buffer = BytesIO()
        bytesLength = len(bytes)

        if strict:
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

                    buffer.write(bytes([QuotedPrintableCodec.__ESCAPE_CHAR]))
                    buffer.write(bytes([QuotedPrintableCodec.__CR]))
                    buffer.write(bytes([QuotedPrintableCodec.__LF]))
                    pos = 1

            b = QuotedPrintableCodec.__getUnsignedOctet(bytesLength - 3, bytes)
            encode = not printable[b] or QuotedPrintableCodec.__isWhitespace(b)
            pos += QuotedPrintableCodec.__encodeByte(b, encode, buffer)

            if pos > QuotedPrintableCodec.__SAFE_LENGTH - 2:
                buffer.write(bytes([QuotedPrintableCodec.__ESCAPE_CHAR]))
                buffer.write(bytes([QuotedPrintableCodec.__CR]))
                buffer.write(bytes([QuotedPrintableCodec.__LF]))
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
        else:
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

        buffer.write(bytes([QuotedPrintableCodec.__ESCAPE_CHAR]))
        hex1 = Utils.hexDigit(b >> 4)
        hex2 = Utils.hexDigit(b)
        buffer.write(hex1.encode())
        buffer.write(hex2.encode())
        return 3
