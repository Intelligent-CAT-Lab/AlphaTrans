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

        pass  # LLM could not translate this method

    @staticmethod
    def randomData(codec: BaseNCodec, size: int) -> typing.List[typing.List[int]]:
        r = Random()
        decoded = [0] * size
        r.nextBytes(decoded)
        encoded = codec.encode0(decoded)
        return [decoded, encoded]

    @staticmethod
    def streamToBytes1(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        buf: typing.List[int],
    ) -> typing.List[int]:

        pass  # LLM could not translate this method

    @staticmethod
    def streamToBytes0(
        in_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> typing.List[int]:
        os = io.BytesIO()
        buf = [0] * 4096
        read = 0
        while (read := in_.read(4096)) != b"":
            os.write(read)
        return os.getvalue()

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
        read = in_.read(buf, offset, len(buf) - offset)
        last_read = read
        if read == -1:
            read = 0
        while last_read != -1 and read + offset < len(buf):
            last_read = in_.read(buf, offset + read, len(buf) - read - offset)
            if last_read != -1:
                read += last_read
        return [offset + read, last_read]
