from __future__ import annotations
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *


class BaseNCodecInputStream:

    __context: Context = Context()
    __buf: typing.List[int] = None

    __singleByte: typing.List[int] = [0]
    __doEncode: bool = False

    __baseNCodec: BaseNCodec = None

    def skip(self, n: int) -> int:
        if n < 0:
            raise ValueError("Negative skip length: " + n)
        b = [0] * 512
        todo = n
        while todo > 0:
            len = min(b.length, todo)
            len = self.read1(b, 0, len)
            if len == EOF:
                break
            todo -= len
        return n - todo

    def reset(self) -> None:
        raise IOException("mark/reset not supported")

    def markSupported(self) -> bool:
        return False

    def mark(self, readLimit: int) -> None:
        pass

    def available(self) -> int:
        return 0 if self.__context.eof else 1

    def read1(self, array: typing.List[int], offset: int, len: int) -> int:

        pass  # LLM could not translate this method

    def read0(self) -> int:
        r = self.read1(self.__singleByte, 0, 1)
        while r == 0:
            r = self.read1(self.__singleByte, 0, 1)
        if r > 0:
            b = self.__singleByte[0]
            return 256 + b if b < 0 else b
        return EOF

    def isStrictDecoding(self) -> bool:
        return self.__baseNCodec.isStrictDecoding()

    def __init__(
        self,
        input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        baseNCodec: BaseNCodec,
        doEncode: bool,
    ) -> None:
        super().__init__(input)
        self.__doEncode = doEncode
        self.__baseNCodec = baseNCodec
        self.__buf = [0] * (doEncode * 4096 + (not doEncode) * 8192)
