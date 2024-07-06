from __future__ import annotations
import copy
import re
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.codec.BinaryDecoder import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Context:

    modulus: int = 0

    currentLinePos: int = 0

    eof: bool = False

    readPos: int = 0

    pos: int = 0

    buffer: typing.List[int] = None

    lbitWorkArea: int = 0

    ibitWorkArea: int = 0

    def toString(self) -> str:
        return f"{self.getClass().getSimpleName()}[buffer={Arrays.toString(self.buffer)}, currentLinePos={self.currentLinePos}, eof={self.eof}, ibitWorkArea={self.ibitWorkArea}, lbitWorkArea={self.lbitWorkArea}, modulus={self.modulus}, pos={self.pos}, readPos={self.readPos}]"

    def __init__(self) -> None:
        pass


class BaseNCodec(BinaryDecoder, BinaryEncoder, ABC):

    _lineLength: int = 0

    _pad: int = 0

    CHUNK_SEPARATOR: typing.List[int] = [13, 10]
    _DECODING_POLICY_DEFAULT: CodecPolicy = CodecPolicy.LENIENT
    _PAD_DEFAULT: int = 61
    _MASK_8BITS: int = 0xFF
    PEM_CHUNK_SIZE: int = 64
    MIME_CHUNK_SIZE: int = 76
    EOF: int = -1
    __decodingPolicy: CodecPolicy = None

    __chunkSeparatorLength: int = 0

    __encodedBlockSize: int = 0

    __unencodedBlockSize: int = 0

    __MAX_BUFFER_SIZE: int = Integer.MAX_VALUE - 8
    __DEFAULT_BUFFER_SIZE: int = 8192
    __DEFAULT_BUFFER_RESIZE_FACTOR: int = 2
    _PAD: int = _PAD_DEFAULT

    def isStrictDecoding(self) -> bool:
        return self.__decodingPolicy == CodecPolicy.STRICT

    def isInAlphabet2(self, basen: str) -> bool:
        return self.isInAlphabet1(StringUtils.getBytesUtf8(basen), True)

    def isInAlphabet1(self, arrayOctet: typing.List[int], allowWSPad: bool) -> bool:
        for octet in arrayOctet:
            if not self._isInAlphabet0(octet) and (
                not allowWSPad or (octet != self._pad) and not self._isWhiteSpace(octet)
            ):
                return False
        return True

    def getEncodedLength(self, pArray: typing.List[int]) -> int:
        len = (
            (pArray.length + self.__unencodedBlockSize - 1) / self.__unencodedBlockSize
        ) * self.__encodedBlockSize
        if self._lineLength > 0:  # We're using chunking
            len += (
                (len + self._lineLength - 1) / self._lineLength
            ) * self.__chunkSeparatorLength
        return len

    def _getDefaultBufferSize(self) -> int:
        return self.__DEFAULT_BUFFER_SIZE

    def getCodecPolicy(self) -> CodecPolicy:
        return self.__decodingPolicy

    def _ensureBufferSize(self, size: int, context: Context) -> typing.List[int]:
        if context.buffer is None:
            context.buffer = [0] * max(size, self._getDefaultBufferSize())
            context.pos = 0
            context.readPos = 0
        elif context.pos + size - context.buffer.length > 0:
            return self.__resizeBuffer(context, context.pos + size)
        return context.buffer

    def encodeToString(self, pArray: typing.List[int]) -> str:
        return StringUtils.newStringUtf8(self.encode0(pArray))

    def encodeAsString(self, pArray: typing.List[int]) -> str:
        return StringUtils.newStringUtf8(self.encode0(pArray))

    def encode3(self, obj: typing.Any) -> typing.Any:
        if not isinstance(obj, typing.List[int]):
            raise EncoderException(
                "Parameter supplied to Base-N encode is not a byte[]", None
            )
        return self.encode0(obj)

    def encode1(
        self, pArray: typing.List[int], offset: int, length: int
    ) -> typing.List[int]:
        if pArray is None or pArray.length == 0:
            return pArray
        context = Context()
        self.encode2(pArray, offset, length, context)
        self.encode2(pArray, offset, self.EOF, context)  # Notify encoder of EOF.
        buf = [0] * (context.pos - context.readPos)
        self.readResults(buf, 0, buf.length, context)
        return buf

    def encode0(self, pArray: typing.List[int]) -> typing.List[int]:
        if pArray is None or pArray.length == 0:
            return pArray
        return self.encode1(pArray, 0, pArray.length)

    def decode3(self, pArray: str) -> typing.List[int]:
        return self.decode0(StringUtils.getBytesUtf8(pArray))

    def decode2(self, obj: typing.Any) -> typing.Any:
        if isinstance(obj, bytes):
            return self.decode0(obj)
        if isinstance(obj, str):
            return self.decode3(obj)
        raise DecoderException(
            "Parameter supplied to Base-N decode is not a byte[] or a String", None
        )

    def decode0(self, pArray: typing.List[int]) -> typing.List[int]:
        if pArray is None or len(pArray) == 0:
            return pArray
        context = Context()
        self.decode1(pArray, 0, len(pArray), context)
        self.decode1(pArray, 0, self.EOF, context)  # Notify decoder of EOF.
        result = [0] * context.pos
        self.readResults(result, 0, len(result), context)
        return result

    def _containsAlphabetOrPad(self, arrayOctet: typing.List[int]) -> bool:
        if arrayOctet is None:
            return False
        for element in arrayOctet:
            if self._pad == element or self._isInAlphabet0(element):
                return True
        return False

    def __init__(
        self,
        constructorId: int,
        unencodedBlockSize: int,
        encodedBlockSize: int,
        lineLength: int,
        chunkSeparatorLength: int,
        pad: int,
        decodingPolicy: CodecPolicy,
    ) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def _isWhiteSpace(byteToCheck: int) -> bool:
        return byteToCheck in [ord(" "), ord("\n"), ord("\r"), ord("\t")]

    @staticmethod
    def getChunkSeparator() -> typing.List[int]:
        return BaseNCodec.CHUNK_SEPARATOR.copy()

    @staticmethod
    def __resizeBuffer(context: Context, minCapacity: int) -> typing.List[int]:
        oldCapacity: int = context.buffer.length
        newCapacity: int = oldCapacity * BaseNCodec.__DEFAULT_BUFFER_RESIZE_FACTOR
        if BaseNCodec.__compareUnsigned(newCapacity, minCapacity) < 0:
            newCapacity = minCapacity
        if BaseNCodec.__compareUnsigned(newCapacity, BaseNCodec.__MAX_BUFFER_SIZE) > 0:
            newCapacity = BaseNCodec.__createPositiveCapacity(minCapacity)

        b: typing.List[int] = [0] * newCapacity
        System.arraycopy(context.buffer, 0, b, 0, context.buffer.length)
        context.buffer = b
        return b

    @staticmethod
    def __createPositiveCapacity(minCapacity: int) -> int:

        pass  # LLM could not translate this method

    @staticmethod
    def __compareUnsigned(x: int, y: int) -> int:
        return (x + 0x80000000) - (y + 0x80000000)

    def readResults(
        self, b: typing.List[int], bPos: int, bAvail: int, context: Context
    ) -> int:

        pass  # LLM could not translate this method

    def hasData(self, context: Context) -> bool:
        return context.pos > context.readPos

    def available(self, context: Context) -> int:

        pass  # LLM could not translate this method

    def _isInAlphabet0(self, value: int) -> bool:
        return self.isInAlphabet0(value)

    def encode2(
        self, pArray: typing.List[int], i: int, length: int, context: Context
    ) -> None:
        pass

    def decode1(
        self, pArray: typing.List[int], i: int, length: int, context: Context
    ) -> None:
        pass
