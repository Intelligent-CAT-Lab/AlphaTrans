from __future__ import annotations
import copy
import re
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.codec.CodecPolicy import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.main.org.apache.commons.codec.binary.StringUtils import *


class Base64(BaseNCodec):

    __DECODE_TABLE: typing.List[int] = None  # LLM could not translate this field

    __URL_SAFE_ENCODE_TABLE: typing.List[int] = [
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        97,
        98,
        99,
        100,
        101,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        109,
        110,
        111,
        112,
        113,
        114,
        115,
        116,
        117,
        118,
        119,
        120,
        121,
        122,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        45,
        95,
    ]
    __STANDARD_ENCODE_TABLE: typing.List[int] = [
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        97,
        98,
        99,
        100,
        101,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        109,
        110,
        111,
        112,
        113,
        114,
        115,
        116,
        117,
        118,
        119,
        120,
        121,
        122,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        43,
        47,
    ]
    __BYTES_PER_ENCODED_BLOCK: int = 4
    __BYTES_PER_UNENCODED_BLOCK: int = 3
    __BITS_PER_ENCODED_BYTE: int = 6
    __encodeSize: int = 0

    __decodeSize: int = 0

    __lineSeparator: typing.List[int] = None

    __decodeTable: typing.List[int] = __DECODE_TABLE
    __encodeTable: typing.List[int] = None

    __MASK_2BITS: int = 0x3
    __MASK_4BITS: int = 0xF
    __MASK_6BITS: int = 0x3F

    def _isInAlphabet0(self, octet: int) -> bool:
        return (
            octet >= 0
            and octet < len(self.__decodeTable)
            and self.__decodeTable[octet] != -1
        )

    @staticmethod
    def isArrayByteBase64(arrayOctet: typing.List[int]) -> bool:
        return Base64.isBase641(arrayOctet)

    def isUrlSafe(self) -> bool:
        return self.__encodeTable == self.__URL_SAFE_ENCODE_TABLE

    @staticmethod
    def Base645() -> Base64:
        return Base64.Base643(0)

    @staticmethod
    def Base644(urlSafe: bool) -> Base64:
        return Base64.Base641(MIME_CHUNK_SIZE, CHUNK_SEPARATOR, urlSafe)

    @staticmethod
    def Base643(lineLength: int) -> Base64:
        return Base642(lineLength, CHUNK_SEPARATOR)

    @staticmethod
    def Base642(lineLength: int, lineSeparator: typing.List[int]) -> Base64:
        return Base641(lineLength, lineSeparator, False)

    @staticmethod
    def Base641(
        lineLength: int, lineSeparator: typing.List[int], urlSafe: bool
    ) -> Base64:
        return Base64(lineLength, lineSeparator, urlSafe, DECODING_POLICY_DEFAULT)

    def __init__(
        self,
        lineLength: int,
        lineSeparator: typing.List[int],
        urlSafe: bool,
        decodingPolicy: CodecPolicy,
    ) -> None:
        super().__init__(
            2,
            Base64.__BYTES_PER_UNENCODED_BLOCK,
            Base64.__BYTES_PER_ENCODED_BLOCK,
            lineLength,
            0 if lineSeparator is None else len(lineSeparator),
            BaseNCodec._PAD_DEFAULT,
            decodingPolicy,
        )
        if lineSeparator is not None:
            if self._containsAlphabetOrPad(lineSeparator):
                sep = StringUtils.newStringUtf8(lineSeparator)
                raise ValueError(
                    "lineSeparator must not contain base64 characters: [" + sep + "]"
                )
            if lineLength > 0:
                self.__encodeSize = Base64.__BYTES_PER_ENCODED_BLOCK + len(
                    lineSeparator
                )
                self.__lineSeparator = lineSeparator.copy()
            else:
                self.__encodeSize = Base64.__BYTES_PER_ENCODED_BLOCK
                self.__lineSeparator = None
        else:
            self.__encodeSize = Base64.__BYTES_PER_ENCODED_BLOCK
            self.__lineSeparator = None
        self.__decodeSize = self.__encodeSize - 1
        self.__encodeTable = (
            Base64.__URL_SAFE_ENCODE_TABLE
            if urlSafe
            else Base64.__STANDARD_ENCODE_TABLE
        )

    @staticmethod
    def toIntegerBytes(bigInt: int) -> typing.List[int]:

        pass  # LLM could not translate this method

    @staticmethod
    def isBase642(base64: str) -> bool:
        return Base64.isBase641(StringUtils.getBytesUtf8(base64))

    @staticmethod
    def isBase641(arrayOctet: typing.List[int]) -> bool:

        pass  # LLM could not translate this method

    @staticmethod
    def isBase640(octet: int) -> bool:
        return octet == Base64.PAD_DEFAULT or (
            octet >= 0
            and octet < len(Base64.DECODE_TABLE)
            and Base64.DECODE_TABLE[octet] != -1
        )

    @staticmethod
    def encodeInteger(bigInteger: int) -> typing.List[int]:
        Objects.requireNonNull(bigInteger, "bigInteger")
        return encodeBase641(toIntegerBytes(bigInteger), false)

    @staticmethod
    def encodeBase64URLSafeString(binaryData: typing.List[int]) -> str:
        return StringUtils.newStringUsAscii(
            Base64.encodeBase642(binaryData, False, True)
        )

    @staticmethod
    def encodeBase64URLSafe(binaryData: typing.List[int]) -> typing.List[int]:
        return Base64.encodeBase642(binaryData, False, True)

    @staticmethod
    def encodeBase64String(binaryData: typing.List[int]) -> str:
        return StringUtils.newStringUsAscii(Base64.encodeBase641(binaryData, False))

    @staticmethod
    def encodeBase64Chunked(binaryData: typing.List[int]) -> typing.List[int]:
        return Base64.encodeBase641(binaryData, True)

    @staticmethod
    def encodeBase643(
        binaryData: typing.List[int], isChunked: bool, urlSafe: bool, maxResultSize: int
    ) -> typing.List[int]:
        if binaryData == None or len(binaryData) == 0:
            return binaryData

        b64 = (
            Base64.Base644(urlSafe)
            if isChunked
            else Base64.Base641(0, Base64.CHUNK_SEPARATOR, urlSafe)
        )
        len = b64.getEncodedLength(binaryData)
        if len > maxResultSize:
            raise ValueError(
                "Input array too big, the output array would be bigger ("
                + len
                + ") than the specified maximum size of "
                + maxResultSize
            )

        return b64.encode0(binaryData)

    @staticmethod
    def encodeBase642(
        binaryData: typing.List[int], isChunked: bool, urlSafe: bool
    ) -> typing.List[int]:
        return Base64.encodeBase643(binaryData, isChunked, urlSafe, Integer.MAX_VALUE)

    @staticmethod
    def encodeBase641(
        binaryData: typing.List[int], isChunked: bool
    ) -> typing.List[int]:
        return Base64.encodeBase642(binaryData, isChunked, False)

    @staticmethod
    def encodeBase640(binaryData: typing.List[int]) -> typing.List[int]:
        return Base64.encodeBase641(binaryData, False)

    @staticmethod
    def decodeInteger(pArray: typing.List[int]) -> int:
        return int.from_bytes(
            Base64.decodeBase640(pArray), byteorder="big", signed=True
        )

    @staticmethod
    def decodeBase641(base64String: str) -> typing.List[int]:
        return Base64.Base645().decode3(base64String)

    @staticmethod
    def decodeBase640(base64Data: typing.List[int]) -> typing.List[int]:
        return Base64.Base645().decode0(base64Data)

    def __validateTrailingCharacter(self) -> None:
        if self.isStrictDecoding():
            raise ValueError(
                "Strict decoding: Last encoded character (before the paddings if any) is a"
                + " valid base 64 alphabet but not a possible encoding. Decoding requires"
                + " at least two trailing 6-bit characters to create bytes."
            )

    def __validateCharacter(self, emptyBitsMask: int, context: Context) -> None:
        if self.isStrictDecoding() and (context.ibitWorkArea & emptyBitsMask) != 0:
            raise ValueError(
                "Strict decoding: Last encoded character (before the paddings if any) is a"
                + " valid base 64 alphabet but not a possible encoding. Expected the"
                + " discarded bits from the character to be zero."
            )

    def encode2(
        self, in_: typing.List[int], inPos: int, inAvail: int, context: Context
    ) -> None:
        if context.eof:
            return
        if inAvail < 0:
            context.eof = True
            if 0 == context.modulus and self._lineLength == 0:
                return  # no leftovers to process and not using chunking
            buffer = self._ensureBufferSize(self.__encodeSize, context)
            savedPos = context.pos
            match context.modulus:  # 0-2
                case 0:  # nothing to do here
                    pass
                case 1:  # 8 bits = 6 + 2
                    buffer[context.pos] = self.__encodeTable[
                        (context.ibitWorkArea >> 2) & self.__MASK_6BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.ibitWorkArea << 4) & self.__MASK_6BITS
                    ]
                    context.pos += 1
                    if self.__encodeTable == self.__STANDARD_ENCODE_TABLE:
                        buffer[context.pos] = self._pad
                        context.pos += 1
                        buffer[context.pos] = self._pad
                        context.pos += 1
                case 2:  # 16 bits = 6 + 6 + 4
                    buffer[context.pos] = self.__encodeTable[
                        (context.ibitWorkArea >> 10) & self.__MASK_6BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.ibitWorkArea >> 4) & self.__MASK_6BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.ibitWorkArea << 2) & self.__MASK_6BITS
                    ]
                    context.pos += 1
                    if self.__encodeTable == self.__STANDARD_ENCODE_TABLE:
                        buffer[context.pos] = self._pad
                        context.pos += 1
                case _:
                    raise RuntimeError("Impossible modulus " + context.modulus)
            context.currentLinePos += (
                context.pos - savedPos
            )  # keep track of current line position
            if self._lineLength > 0 and context.currentLinePos > 0:
                self.__lineSeparator.copy(
                    buffer, context.pos, 0, self.__lineSeparator.length
                )
                context.pos += self.__lineSeparator.length
        else:
            for i in range(inAvail):
                buffer = self._ensureBufferSize(self.__encodeSize, context)
                context.modulus = (
                    context.modulus + 1
                ) % self.__BYTES_PER_UNENCODED_BLOCK
                b = in_[inPos]
                inPos += 1
                if b < 0:
                    b += 256
                context.ibitWorkArea = (context.ibitWorkArea << 8) + b  #  BITS_PER_BYTE
                if 0 == context.modulus:  # 3 bytes = 24 bits = 4 * 6 bits to extract
                    buffer[context.pos] = self.__encodeTable[
                        (context.ibitWorkArea >> 18) & self.__MASK_6BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.ibitWorkArea >> 12) & self.__MASK_6BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        (context.ibitWorkArea >> 6) & self.__MASK_6BITS
                    ]
                    context.pos += 1
                    buffer[context.pos] = self.__encodeTable[
                        context.ibitWorkArea & self.__MASK_6BITS
                    ]
                    context.pos += 1
                    context.currentLinePos += self.__BYTES_PER_ENCODED_BLOCK
                    if (
                        self._lineLength > 0
                        and self._lineLength <= context.currentLinePos
                    ):
                        self.__lineSeparator.copy(
                            buffer, context.pos, 0, self.__lineSeparator.length
                        )
                        context.pos += self.__lineSeparator.length
                        context.currentLinePos = 0

    def decode1(
        self, in_: typing.List[int], inPos: int, inAvail: int, context: Context
    ) -> None:
        if context.eof:
            return
        if inAvail < 0:
            context.eof = True
        for i in range(inAvail):
            buffer = self._ensureBufferSize(self.__decodeSize, context)
            b = in_[inPos]
            inPos += 1
            if b == self._pad:
                context.eof = True
                break
            if b >= 0 and b < len(self.__DECODE_TABLE):
                result = self.__DECODE_TABLE[b]
                if result >= 0:
                    context.modulus = (
                        context.modulus + 1
                    ) % self.__BYTES_PER_ENCODED_BLOCK
                    context.ibitWorkArea = (
                        context.ibitWorkArea << self.__BITS_PER_ENCODED_BYTE
                    ) + result
                    if context.modulus == 0:
                        buffer[context.pos] = (
                            context.ibitWorkArea >> 16
                        ) & self._MASK_8BITS
                        context.pos += 1
                        buffer[context.pos] = (
                            context.ibitWorkArea >> 8
                        ) & self._MASK_8BITS
                        context.pos += 1
                        buffer[context.pos] = context.ibitWorkArea & self._MASK_8BITS
                        context.pos += 1
        if context.eof and context.modulus != 0:
            buffer = self._ensureBufferSize(self.__decodeSize, context)
            if context.modulus == 1:
                self.__validateTrailingCharacter()
            elif context.modulus == 2:
                self.__validateCharacter(self.__MASK_4BITS, context)
                context.ibitWorkArea = context.ibitWorkArea >> 4
                buffer[context.pos] = context.ibitWorkArea & self._MASK_8BITS
                context.pos += 1
            elif context.modulus == 3:
                self.__validateCharacter(self.__MASK_2BITS, context)
                context.ibitWorkArea = context.ibitWorkArea >> 2
                buffer[context.pos] = (context.ibitWorkArea >> 8) & self._MASK_8BITS
                context.pos += 1
                buffer[context.pos] = context.ibitWorkArea & self._MASK_8BITS
                context.pos += 1
            else:
                raise RuntimeError("Impossible modulus " + context.modulus)
