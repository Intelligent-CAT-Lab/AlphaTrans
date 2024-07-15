from __future__ import annotations
import re
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

    __alwaysEncodeCharsMax: int = 0
    __alwaysEncodeCharsMin: int = 0
    __plusForSpace: bool = False

    __alwaysEncodeChars: typing.List[bool] = [False] * 256
    __ESCAPE_CHAR: int = 0x25

    def decode1(self, obj: typing.Any) -> typing.Any:
        if obj is None:
            return None
        if isinstance(obj, bytes):
            return self.decode0(obj)
        raise DecoderException(
            "Objects of type " + obj.__class__.__name__ + " cannot be Percent decoded",
            None,
        )

    def encode1(self, obj: typing.Any) -> typing.Any:
        if obj is None:
            return None
        if isinstance(obj, bytes):
            return self.encode0(obj)
        raise EncoderException(
            "Objects of type " + obj.__class__.__name__ + " cannot be Percent encoded",
            None,
        )

    def decode0(self, bytes: typing.List[int]) -> typing.List[int]:
        if bytes is None:
            return None

        buffer = ByteBuffer.allocate(self.__expectedDecodingBytes(bytes))
        for i in range(0, len(bytes)):
            b = bytes[i]
            if b == self.__ESCAPE_CHAR:
                try:
                    u = Utils.digit16(bytes[i + 1])
                    l = Utils.digit16(bytes[i + 2])
                    buffer.put((u << 4) + l)
                except IndexError as e:
                    raise DecoderException("Invalid percent decoding: ", e)
            elif self.__plusForSpace and b == "+":
                buffer.put(" ")
            else:
                buffer.put(b)
        return buffer.array()

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
        i = 0
        while i < len(bytes):
            b = bytes[i]
            i += 3 if b == self.__ESCAPE_CHAR else 1
            byteCount += 1
        return byteCount

    def __isAsciiChar(self, c: int) -> bool:
        return c >= 0

    def __inAlwaysEncodeCharsRange(self, c: int) -> bool:
        return c >= self.__alwaysEncodeCharsMin and c <= self.__alwaysEncodeCharsMax

    def __canEncode(self, c: int) -> bool:
        return not self.__isAsciiChar(c) or (
            self.__inAlwaysEncodeCharsRange(c) and self.__alwaysEncodeChars[c]
        )

    def __containsSpace(self, bytes: typing.List[int]) -> bool:

        pass  # LLM could not translate this method

    def __expectedEncodingBytes(self, bytes: typing.List[int]) -> int:
        byteCount = 0
        for b in bytes:
            byteCount += 3 if self.__canEncode(b) else 1
        return byteCount

    def __doEncode(
        self, bytes: typing.List[int], expectedLength: int, willEncode: bool
    ) -> typing.List[int]:
        buffer = io.BytesIO(expectedLength)
        for b in bytes:
            if willEncode and self.__canEncode(b):
                bb = b
                if bb < 0:
                    bb = 256 + bb
                hex1 = Utils.hexDigit(bb >> 4)
                hex2 = Utils.hexDigit(bb)
                buffer.write(bytes([self.__ESCAPE_CHAR, hex1, hex2]))
            elif self.__plusForSpace and b == ord(" "):
                buffer.write(b"+")
            else:
                buffer.write(bytes([b]))
        return buffer.getvalue()

    def __insertAlwaysEncodeChar(self, b: int) -> None:
        self.__alwaysEncodeChars[b] = True
        if b < self.__alwaysEncodeCharsMin:
            self.__alwaysEncodeCharsMin = b
        if b > self.__alwaysEncodeCharsMax:
            self.__alwaysEncodeCharsMax = b

    def __insertAlwaysEncodeChars(
        self, alwaysEncodeCharsArray: typing.List[int]
    ) -> None:
        if alwaysEncodeCharsArray is not None:
            for b in alwaysEncodeCharsArray:
                self.__insertAlwaysEncodeChar(b)
        self.__insertAlwaysEncodeChar(self.__ESCAPE_CHAR)
