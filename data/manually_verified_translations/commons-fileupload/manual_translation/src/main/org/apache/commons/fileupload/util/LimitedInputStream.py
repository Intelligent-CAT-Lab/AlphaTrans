from __future__ import annotations
import re
from abc import ABC
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
import os
from src.main.org.apache.commons.fileupload.util.Closeable import *


class LimitedInputStream(ABC):

    __closed: bool = False

    __count: int = 0

    __sizeMax: int = 0

    def close(self) -> None:
        self.__closed = True
        super().close()

    def isClosed(self) -> bool:
        return self.__closed

    def read1(self, b: typing.List[int], off: int, len_: int) -> int:
        res = super().read(b, off, len_)
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
        raise IOError("Error: Maximum size exceeded.")
