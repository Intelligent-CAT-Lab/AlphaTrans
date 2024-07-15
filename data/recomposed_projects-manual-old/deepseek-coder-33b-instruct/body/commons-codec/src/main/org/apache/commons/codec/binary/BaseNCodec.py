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
        return "{}[buffer={}, currentLinePos={}, eof={}, ibitWorkArea={}, lbitWorkArea={}, modulus={}, pos={}, readPos={}]".format(
            self.__class__.__name__,
            str(self.buffer),
            self.currentLinePos,
            self.eof,
            self.ibitWorkArea,
            self.lbitWorkArea,
            self.modulus,
            self.pos,
            self.readPos,
        )

    def __init__(self) -> None:
        pass


class BaseNCodec(BinaryDecoder, BinaryEncoder, ABC):

    _lineLength: int = 0

    _pad: int = 0

    _PAD: int = ord("=")
    CHUNK_SEPARATOR: typing.List[int] = [ord("\r"), ord("\n")]
    _DECODING_POLICY_DEFAULT: CodecPolicy = CodecPolicy.LENIENT
    _PAD_DEFAULT: int = ord("=")
    _MASK_8BITS: int = 0xFF
    PEM_CHUNK_SIZE: int = 64
    MIME_CHUNK_SIZE: int = 76
    EOF: int = -1
    __decodingPolicy: CodecPolicy = None

    __chunkSeparatorLength: int = 0

    __encodedBlockSize: int = 0

    __unencodedBlockSize: int = 0

    __MAX_BUFFER_SIZE: int = (2**31) - 1 - 8
    __DEFAULT_BUFFER_SIZE: int = 8192
    __DEFAULT_BUFFER_RESIZE_FACTOR: int = 2

    def isStrictDecoding(self) -> bool:
        return self.__decodingPolicy == CodecPolicy.STRICT

    def isInAlphabet2(self, basen: str) -> bool:

        return self.isInAlphabet1(StringUtils.getBytesUtf8(basen), True)

    def isInAlphabet1(self, arrayOctet: typing.List[int], allowWSPad: bool) -> bool:

        for octet in arrayOctet:
            if not self._isInAlphabet0(octet) and (
                not allowWSPad or (octet != self._pad and not self._isWhiteSpace(octet))
            ):
                return False
        return True

    def getEncodedLength(self, pArray: typing.List[int]) -> int:

        len = (
            (len(pArray) + self.__unencodedBlockSize - 1) // self.__unencodedBlockSize
        ) * self.__encodedBlockSize
        if self._lineLength > 0:  # We're using chunking
            len += (
                (len + self._lineLength - 1) // self._lineLength
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

        elif context.pos + size - len(context.buffer) > 0:
            return self.__resizeBuffer(context, context.pos + size)

        return context.buffer

    def encodeToString(self, pArray: typing.List[int]) -> str:
        return StringUtils.newStringUtf8(self.encode0(pArray))

    def encodeAsString(self, pArray: typing.List[int]) -> str:
        return StringUtils.newStringUtf8(self.encode0(pArray))

    def encode3(self, obj: typing.Any) -> typing.Any:
        if not isinstance(obj, list):
            raise EncoderException(
                "Parameter supplied to Base-N encode is not a byte[]", None
            )
        return self.encode0(obj)

    def encode1(
        self, pArray: typing.List[int], offset: int, length: int
    ) -> typing.List[int]:
        if pArray is None or len(pArray) == 0:
            return pArray
        context = Context()
        self.encode2(pArray, offset, length, context)
        self.encode2(pArray, offset, self.EOF, context)
        buf = [0] * (context.pos - context.readPos)
        self.readResults(buf, 0, len(buf), context)
        return buf

    def encode0(self, pArray: typing.List[int]) -> typing.List[int]:
        if pArray is None or len(pArray) == 0:
            return pArray
        return self.encode1(pArray, 0, len(pArray))

    def decode3(self, pArray: str) -> typing.List[int]:
        return self.decode0(StringUtils.getBytesUtf8(pArray))

    def decode2(self, obj: typing.Any) -> typing.Any:
        if isinstance(obj, bytearray):
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

        self.__unencodedBlockSize = unencodedBlockSize
        self.__encodedBlockSize = encodedBlockSize
        useChunking = lineLength > 0 and chunkSeparatorLength > 0
        self._lineLength = lineLength if useChunking else 0
        self.__chunkSeparatorLength = chunkSeparatorLength
        if constructorId == 0:
            self._pad = self._PAD_DEFAULT
        else:
            self._pad = pad

        if constructorId == 2:
            self.__decodingPolicy = (
                decodingPolicy
                if decodingPolicy is not None
                else self._DECODING_POLICY_DEFAULT
            )
        else:
            self.__decodingPolicy = self._DECODING_POLICY_DEFAULT

    @staticmethod
    def _isWhiteSpace(byteToCheck: int) -> bool:

        if byteToCheck in [ord(" "), ord("\n"), ord("\r"), ord("\t")]:
            return True
        else:
            return False

    @staticmethod
    def getChunkSeparator() -> typing.List[int]:
        return BaseNCodec.CHUNK_SEPARATOR.copy()

    @staticmethod
    def __resizeBuffer(context: Context, minCapacity: int) -> typing.List[int]:

        oldCapacity = len(context.buffer)
        newCapacity = oldCapacity * BaseNCodec.__DEFAULT_BUFFER_RESIZE_FACTOR
        if BaseNCodec.__compareUnsigned(newCapacity, minCapacity) < 0:
            newCapacity = minCapacity
        if BaseNCodec.__compareUnsigned(newCapacity, BaseNCodec.__MAX_BUFFER_SIZE) > 0:
            newCapacity = BaseNCodec.__createPositiveCapacity(minCapacity)

        b = [0] * newCapacity
        b[:oldCapacity] = context.buffer
        context.buffer = b
        return b

    @staticmethod
    def __createPositiveCapacity(minCapacity: int) -> int:

        pass  # LLM could not translate this method

    @staticmethod
    def __compareUnsigned(x: int, y: int) -> int:
        return (x + (2**31)) - (y + (2**31))

    def readResults(
        self, b: typing.List[int], bPos: int, bAvail: int, context: Context
    ) -> int:
        if self.hasData(context):
            len = min(self.available(context), bAvail)
            b[bPos : bPos + len] = context.buffer[
                context.readPos : context.readPos + len
            ]
            context.readPos += len
            if not self.hasData(context):
                context.pos = context.readPos = 0
            return len
        return context.eof if context.eof else 0

    def hasData(self, context: Context) -> bool:
        return context.pos > context.readPos

    def available(self, context: Context) -> int:
        return context.pos - context.readPos if self.hasData(context) else 0

    def _isInAlphabet0(self, value: int) -> bool:
        pass

    def encode2(
        self, pArray: typing.List[int], i: int, length: int, context: Context
    ) -> None:
        pass

    def decode1(
        self, pArray: typing.List[int], i: int, length: int, context: Context
    ) -> None:
        pass
