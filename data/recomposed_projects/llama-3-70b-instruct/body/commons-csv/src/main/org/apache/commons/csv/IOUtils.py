from __future__ import annotations
import time
import copy
import re
from io import IOBase
from io import StringIO
import io
import typing
from typing import *


class IOUtils:

    DEFAULT_BUFFER_SIZE: int = 1024 * 4
    __EOF: int = -1

    @staticmethod
    def rethrow(throwable: BaseException) -> RuntimeError:
        raise throwable

    @staticmethod
    def copyLarge1(
        input: typing.Union[io.TextIOWrapper, io.BufferedReader],
        output: typing.Union[io.TextIOWrapper, io.BufferedWriter],
        buffer: typing.List[str],
    ) -> int:
        count: int = 0
        n: int
        while IOUtils.__EOF != (n := input.read(buffer)):
            output.write(buffer, 0, n)
            count += n
        return count

    @staticmethod
    def copyLarge0(
        input: typing.Union[io.TextIOWrapper, io.BufferedReader],
        output: typing.Union[io.TextIOWrapper, io.BufferedWriter],
    ) -> int:
        return IOUtils.copyLarge1(input, output, [None] * IOUtils.DEFAULT_BUFFER_SIZE)

    @staticmethod
    def copy1(
        input: typing.Union[io.TextIOWrapper, io.BufferedReader],
        output: typing.Union[typing.List, io.TextIOBase],
        buffer: typing.Union[str, typing.List[str], io.StringIO],
    ) -> int:
        count: int = 0
        n: int
        while IOUtils.__EOF != (n := input.read(buffer)):
            buffer.flip()
            output.append(buffer, 0, n)
            count += n
        return count

    @staticmethod
    def copy0(
        input: typing.Union[io.TextIOWrapper, io.BufferedReader],
        output: typing.Union[typing.List, io.TextIOBase],
    ) -> int:
        return IOUtils.copy1(
            input, output, CharBuffer.allocate(IOUtils.DEFAULT_BUFFER_SIZE)
        )

    def __init__(self) -> None:
        pass
