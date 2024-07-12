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
            last_read = status[BaseNTestData.__LAST_READ_KEY]
            while last_read != -1:
                buf = BaseNTestData.__resizeArray(buf)
                status = BaseNTestData.__fill(buf, size, in_)
                size = status[BaseNTestData.__SIZE_KEY]
                last_read = status[BaseNTestData.__LAST_READ_KEY]
            if len(buf) != size:
                smaller_buf = [0] * size
                for i in range(size):
                    smaller_buf[i] = buf[i]
                buf = smaller_buf
        finally:
            in_.close()
        return buf

    @staticmethod
    def streamToBytes0(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> typing.List[int]:

        os = BytesIO()
        buf = bytearray(4096)
        read = in_.readinto(buf)
        while read > 0:
            os.write(buf[:read])
            read = in_.readinto(buf)
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
        if read == -1:
            read = 0
        while last_read != -1 and read + offset < len(buf):
            last_read = in_.read(len(buf) - read - offset)
            if last_read != -1:
                read += last_read
        return [offset + read, last_read]
