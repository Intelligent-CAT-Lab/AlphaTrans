from __future__ import annotations
import re
import unittest
import pytest
import pathlib
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *
from src.main.org.apache.commons.codec.digest.XXHash32 import *


class XXHash32Test(unittest.TestCase):

    __expectedChecksum: str = None
    __file: pathlib.Path = None

    def verifyIncrementalChecksum(self) -> None:

        h = XXHash32.XXHash321()
        with open(self.__file, "rb") as s:
            b = self.__toByteArray(s)
            h.update0(b[0])
            h.reset()
            h.update0(b[0])
            h.update1(b, 1, len(b) - 2)
            h.update1(b, len(b) - 1, 1)
            h.update1(b, 0, -1)

        assert (
            "checksum for " + self.__file.name == self.__expectedChecksum
        ), Long.toHexString(h.getValue())

    def verifyChecksum(self) -> None:

        h = XXHash32.XXHash321()
        with open(self.__file, "rb") as s:
            b = self.__toByteArray(s)
            h.update1(b, 0, len(b))

        assert (
            "checksum for " + self.__file.name == self.__expectedChecksum
        ), Long.toHexString(h.getValue())

    @staticmethod
    def factory() -> typing.Collection[typing.List[typing.Any]]:

        return [
            ["org/apache/commons/codec/bla.tar", "fbb5c8d1"],
            ["org/apache/commons/codec/bla.tar.xz", "4106a208"],
            ["org/apache/commons/codec/small.bin", "f66c26f8"],
        ]

    def __init__(self, path: str, c: str) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __copy(
        input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        output: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        buffersize: int,
    ) -> int:

        buffer = bytearray(buffersize)
        n = 0
        count = 0
        while -1 != (n := input.readinto(buffer)):
            output.write(buffer[:n])
            count += n
        return count

    @staticmethod
    def __toByteArray(
        input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> typing.List[int]:

        output = io.BytesIO()
        XXHash32Test.__copy(input, output, 10240)
        return list(output.getvalue())
