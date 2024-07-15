from __future__ import annotations
import re
import random
import os
import unittest
import pytest
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *


class BaseNTestData:

    DECODED: typing.List[int] = None  # LLM could not translate this field

    __LAST_READ_KEY: int = 1
    __SIZE_KEY: int = 0

    @staticmethod
    def bytesContain(bytes: typing.List[int], c: int) -> bool:
        for b in bytes:
            if b == c:
                return True
        return False

    @staticmethod
    def randomData(codec: BaseNCodec, size: int) -> typing.List[typing.List[int]]:

        r = random.Random()
        decoded = bytearray(size)
        r.randbytes(decoded)
        encoded = codec.encode0(decoded)
        return [decoded, encoded]

    @staticmethod
    def streamToBytes1(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        buf: typing.List[int],
    ) -> typing.List[int]:

        try:
            status = BaseNTestData.__fill(buf, 0, in_)
            size = status[BaseNTestData.__SIZE_KEY]
            lastRead = status[BaseNTestData.__LAST_READ_KEY]
            while lastRead != -1:
                buf = BaseNTestData.__resizeArray(buf)
                status = BaseNTestData.__fill(buf, size, in_)
                size = status[BaseNTestData.__SIZE_KEY]
                lastRead = status[BaseNTestData.__LAST_READ_KEY]
            if len(buf) != size:
                smallerBuf = [0] * size
                smallerBuf[: len(buf)] = buf
                buf = smallerBuf
        finally:
            in_.close()
        return buf

    @staticmethod
    def streamToBytes0(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> typing.List[int]:

        os = BytesIO()
        buf = bytearray(4096)
        read = 0
        while (read := in_.read(buf)) > -1:
            os.write(buf[:read])
        return list(os.getvalue())

    @staticmethod
    def __resizeArray(bytes: typing.List[int]) -> typing.List[int]:

        biggerBytes = [0] * (len(bytes) * 2)
        for i in range(len(bytes)):
            biggerBytes[i] = bytes[i]
        return biggerBytes

    @staticmethod
    def __fill(
        buf: typing.List[int],
        offset: int,
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
    ) -> typing.List[int]:

        read = in_.read(len(buf) - offset)
        last_read = read
        if read is None:
            read = 0
        else:
            read = len(read)

        while last_read is not None and read + offset < len(buf):
            last_read = in_.read(len(buf) - read - offset)
            if last_read is not None:
                read += len(last_read)

        return [offset + read, -1 if last_read is None else 1]
