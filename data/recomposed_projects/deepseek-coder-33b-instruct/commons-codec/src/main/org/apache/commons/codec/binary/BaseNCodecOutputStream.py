from __future__ import annotations
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import os
from src.main.org.apache.commons.codec.binary.BaseNCodec import *


class BaseNCodecOutputStream:

    __context: Context = Context()

    __singleByte: typing.List[int] = [0]
    __baseNCodec: BaseNCodec = None
    __doEncode: bool = None

    def write(self, i: int) -> None:

        self.write1(i)

    def close(self) -> None:

        self.eof()
        self.flush0()
        self.out.close()

    def write1(self, i: int) -> None:

        self.__singleByte[0] = i
        self.write0(self.__singleByte, 0, 1)

    def write0(self, array: typing.List[int], offset: int, len: int) -> None:

        if array is None:
            raise ValueError("array cannot be None")
        if offset < 0 or len < 0:
            raise IndexError("Offset and length must be non-negative")
        if offset > len(array) or offset + len > len(array):
            raise IndexError("Offset and length exceed array bounds")
        if len > 0:
            if self.__doEncode:
                self.__baseNCodec.encode2(array, offset, len, self.__context)
            else:
                self.__baseNCodec.decode1(array, offset, len, self.__context)
            self.__flush1(False)

    def isStrictDecoding(self) -> bool:

        if self.__baseNCodec is not None:
            return self.__baseNCodec.isStrictDecoding()
        else:
            raise ValueError("BaseNCodec is not initialized")

    def flush0(self) -> None:

        self.__flush1(True)

    def eof(self) -> None:

        if self.__doEncode:
            self.__baseNCodec.encode2(self.__singleByte, 0, EOF, self.__context)
        else:
            self.__baseNCodec.decode1(self.__singleByte, 0, EOF, self.__context)

    def __init__(
        self,
        output: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        basedCodec: BaseNCodec,
        doEncode: bool,
    ) -> None:

        self.__baseNCodec = basedCodec
        self.__doEncode = doEncode

    def __flush1(self, propagate: bool) -> None:

        avail = self.__baseNCodec.available(self.__context)
        if avail > 0:
            buf = bytearray(avail)
            c = self.__baseNCodec.readResults(buf, 0, avail, self.__context)
            if c > 0:
                self.out.write(buf[:c])
        if propagate:
            self.out.flush()
