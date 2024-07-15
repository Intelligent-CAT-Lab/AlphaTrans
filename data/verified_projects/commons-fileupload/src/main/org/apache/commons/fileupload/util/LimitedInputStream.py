import pytest

# Imports Begin
from src.main.org.apache.commons.fileupload.util.Closeable import *
import os
import typing
from typing import *
import io
from abc import ABC

# Imports End


class LimitedInputStream(Closeable, FilterInputStream, ABC):

    # Class Fields Begin
    __sizeMax: int = None
    __count: int = None
    __closed: bool = None
    # Class Fields End

    # Class Methods Begin
    def close(self) -> None:

        self.__closed = True
        super().close()

    def isClosed(self) -> bool:

        return self.__closed

    def read1(self, b: typing.List[int], off: int, len: int) -> int:

        res = super().read(b, off, len)
        if res > 0:
            self.__count += res
            self.__checkLimit()
        return res

    def read0(self) -> int:

        res = super().read()
        if res != -1:
            self.__count += 1
            self.__checkLimit()
        return res

    def __init__(
        self,
        inputStream: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        pSizeMax: int,
    ) -> None:

        super().__init__(inputStream)
        self.__sizeMax = pSizeMax

    def __checkLimit(self) -> None:

        if self.__count > self.__sizeMax:
            self._raiseError(self.__sizeMax, self.__count)

    def _raiseError(self, pSizeMax: int, pCount: int) -> None:

        raise IOError(f"Maximum size exceeded: {pSizeMax} bytes, {pCount} items")

    # Class Methods End
