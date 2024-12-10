from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.BinaryEncoder import *
from src.main.org.apache.commons.codec.BinaryDecoder import *
import os
import typing
from typing import *
import io
from abc import ABC

# Imports End


class Context:

    # Class Fields Begin
    ibitWorkArea: int = None
    lbitWorkArea: int = None
    buffer: typing.List[int] = None
    pos: int = None
    readPos: int = None
    eof: bool = None
    currentLinePos: int = None
    modulus: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End


class BaseNCodec(BinaryDecoder, BinaryEncoder, ABC):

    # Class Fields Begin
    EOF: int = None
    MIME_CHUNK_SIZE: int = None
    PEM_CHUNK_SIZE: int = None
    __DEFAULT_BUFFER_RESIZE_FACTOR: int = None
    __DEFAULT_BUFFER_SIZE: int = None
    __MAX_BUFFER_SIZE: int = None
    _MASK_8BITS: int = None
    _PAD_DEFAULT: int = None
    _DECODING_POLICY_DEFAULT: CodecPolicy = None
    CHUNK_SEPARATOR: typing.List[int] = None
    _PAD: int = None
    _pad: int = None
    __unencodedBlockSize: int = None
    __encodedBlockSize: int = None
    _lineLength: int = None
    __chunkSeparatorLength: int = None
    __decodingPolicy: CodecPolicy = None
    # Class Fields End

    # Class Methods Begin
    def encode(self, obj: typing.Any) -> typing.Any:
        pass

    def encode(self, pArray: typing.List[int]) -> typing.List[int]:
        pass

    def decode(self, obj: typing.Any) -> typing.Any:
        pass

    def decode(self, pArray: typing.List[int]) -> typing.List[int]:
        pass

    def isStrictDecoding(self) -> bool:
        pass

    def isInAlphabet2(self, basen: str) -> bool:
        pass

    def isInAlphabet1(self, arrayOctet: typing.List[int], allowWSPad: bool) -> bool:
        pass

    def getEncodedLength(self, pArray: typing.List[int]) -> int:
        pass

    def _getDefaultBufferSize(self) -> int:
        pass

    def getCodecPolicy(self) -> CodecPolicy:
        pass

    def _ensureBufferSize(self, size: int, context: Context) -> typing.List[int]:
        pass

    def encodeToString(self, pArray: typing.List[int]) -> str:
        pass

    def encodeAsString(self, pArray: typing.List[int]) -> str:
        pass

    def encode3(self, obj: typing.Any) -> typing.Any:
        pass

    def encode1(
        self, pArray: typing.List[int], offset: int, length: int
    ) -> typing.List[int]:
        pass

    def encode0(self, pArray: typing.List[int]) -> typing.List[int]:
        pass

    def decode3(self, pArray: str) -> typing.List[int]:
        pass

    def decode2(self, obj: typing.Any) -> typing.Any:
        pass

    def decode0(self, pArray: typing.List[int]) -> typing.List[int]:
        pass

    def _containsAlphabetOrPad(self, arrayOctet: typing.List[int]) -> bool:
        pass

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
        pass

    @staticmethod
    def _isWhiteSpace(byteToCheck: int) -> bool:
        pass

    @staticmethod
    def getChunkSeparator() -> typing.List[int]:
        pass

    @staticmethod
    def __resizeBuffer(context: Context, minCapacity: int) -> typing.List[int]:
        pass

    @staticmethod
    def __createPositiveCapacity(minCapacity: int) -> int:
        pass

    @staticmethod
    def __compareUnsigned(x: int, y: int) -> int:
        pass

    def readResults(
        self, b: typing.List[int], bPos: int, bAvail: int, context: Context
    ) -> int:
        pass

    def hasData(self, context: Context) -> bool:
        pass

    def available(self, context: Context) -> int:
        pass

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

    # Class Methods End
