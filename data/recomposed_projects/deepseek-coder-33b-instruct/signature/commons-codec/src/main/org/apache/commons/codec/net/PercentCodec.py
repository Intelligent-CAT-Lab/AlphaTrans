from __future__ import annotations
import re
import sys
from io import BytesIO
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.net.Utils import *


class PercentCodec(BinaryDecoder, BinaryEncoder):

    __alwaysEncodeCharsMax: int = Integer.MIN_VALUE
    __alwaysEncodeCharsMin: int = sys.maxsize
    __plusForSpace: bool = False

    __alwaysEncodeChars: typing.List[bool] = [False] * 256
    __ESCAPE_CHAR: int = ord("%")

    def decode1(self, obj: typing.Any) -> typing.Any:

        if obj is None:
            return None
        if isinstance(obj, list):
            return self.decode0(obj)
        raise DecoderException(
            "Objects of type " + type(obj).__name__ + " cannot be Percent decoded", None
        )

    def encode1(self, obj: typing.Any) -> typing.Any:

        if obj is None:
            return None
        if isinstance(obj, list):
            return self.encode0(obj)
        raise EncoderException(
            "Objects of type " + type(obj).__name__ + " cannot be Percent encoded", None
        )

    def decode0(self, bytes: typing.List[int]) -> typing.List[int]:

        if bytes is None:
            return None

        buffer = io.BytesIO()
        for i in range(len(bytes)):
            b = bytes[i]
            if b == self.__ESCAPE_CHAR:
                try:
                    u = Utils.digit16(bytes[i + 1])
                    l = Utils.digit16(bytes[i + 2])
                    buffer.write(bytes([(u << 4) + l]))
                    i += 2
                except IndexError as e:
                    raise DecoderException("Invalid percent decoding: ", e)
            elif self.__plusForSpace and b == ord("+"):
                buffer.write(bytes([ord(" ")]))
            else:
                buffer.write(bytes([b]))
        return list(buffer.getvalue())

    def encode0(self, bytes: typing.List[int]) -> typing.List[int]:

        if bytes is None:
            return None

        expectedEncodingBytes = self.__expectedEncodingBytes(bytes)
        willEncode = expectedEncodingBytes != len(bytes)
        if willEncode or (self.__plusForSpace and self.__containsSpace(bytes)):
            return self.__doEncode(bytes, expectedEncodingBytes, willEncode)
        return bytes

    def __init__(
        self,
        constructorId: int,
        plusForSpace: bool,
        alwaysEncodeChars: typing.List[int],
    ) -> None:

        if constructorId == 0:
            self.__plusForSpace = plusForSpace
            self.__insertAlwaysEncodeChars(alwaysEncodeChars)
        else:
            self.__plusForSpace = False
            self.__insertAlwaysEncodeChar(self.__ESCAPE_CHAR)

    def __expectedDecodingBytes(self, bytes: typing.List[int]) -> int:

        byteCount = 0
        for i in range(len(bytes)):
            b = bytes[i]
            if b == self.__ESCAPE_CHAR:
                i += 3
            else:
                i += 1
            byteCount += 1
        return byteCount

    def __isAsciiChar(self, c: int) -> bool:
        return c >= 0

    def __inAlwaysEncodeCharsRange(self, c: int) -> bool:
        return self.__alwaysEncodeChars[c]

    def __canEncode(self, c: int) -> bool:
        return not self.__isAsciiChar(c) or (
            self.__inAlwaysEncodeCharsRange(c) and self.__alwaysEncodeChars[c]
        )

    def __containsSpace(self, bytes: typing.List[int]) -> bool:
        for b in bytes:
            if b == 32:
                return True
        return False

    def __expectedEncodingBytes(self, bytes: typing.List[int]) -> int:

        byteCount = 0
        for b in bytes:
            byteCount += 3 if self.__canEncode(b) else 1
        return byteCount

    def __doEncode(
        self, bytes: typing.List[int], expectedLength: int, willEncode: bool
    ) -> typing.List[int]:

        buffer = bytearray(expectedLength)
        buffer_index = 0

        for b in bytes:
            if willEncode and self.__canEncode(b):
                bb = b
                if bb < 0:
                    bb = 256 + bb
                hex1 = Utils.hexDigit(bb >> 4)
                hex2 = Utils.hexDigit(bb)
                buffer[buffer_index] = self.__ESCAPE_CHAR
                buffer_index += 1
                buffer[buffer_index] = ord(hex1)
                buffer_index += 1
                buffer[buffer_index] = ord(hex2)
                buffer_index += 1
            elif self.__plusForSpace and b == ord(" "):
                buffer[buffer_index] = ord("+")
                buffer_index += 1
            else:
                buffer[buffer_index] = b
                buffer_index += 1

        return list(buffer)

    def __insertAlwaysEncodeChar(self, b: int) -> None:

        self.__alwaysEncodeChars[b] = True

        if self.__alwaysEncodeCharsMin is None or b < self.__alwaysEncodeCharsMin:
            self.__alwaysEncodeCharsMin = b

        if self.__alwaysEncodeCharsMax is None or b > self.__alwaysEncodeCharsMax:
            self.__alwaysEncodeCharsMax = b

    def __insertAlwaysEncodeChars(
        self, alwaysEncodeCharsArray: typing.List[int]
    ) -> None:

        if alwaysEncodeCharsArray is not None:
            for b in alwaysEncodeCharsArray:
                self.__insertAlwaysEncodeChar(b)

        self.__insertAlwaysEncodeChar(self.__ESCAPE_CHAR)
