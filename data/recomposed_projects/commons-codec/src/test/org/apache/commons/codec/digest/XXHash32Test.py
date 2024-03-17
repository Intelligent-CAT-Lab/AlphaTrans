# Imports Begin
from src.main.org.apache.commons.codec.digest.XXHash32 import *
import unittest
import typing
from typing import *
import io
import pathlib

# Imports End


class XXHash32Test(unittest.TestCase):

    # Class Fields Begin
    __file: pathlib.Path = None
    __expectedChecksum: str = None
    # Class Fields End

    # Class Methods Begin
    def verifyIncrementalChecksum(self) -> None:

        h = XXHash32.XXHash321()
        with open(self.__file, "rb") as f:
            b = self.__toByteArray(f)
            h.update0(b[0])
            h.reset()
            h.update0(b[0])
            h.update1(b, 1, len(b) - 2)
            h.update1(b, len(b) - 1, 1)
            h.update1(b, 0, -1)
        Assert.self.assertEqual(
            "checksum for " + self.__file.getName(),
            self.__expectedChecksum,
            Long.toHexString(h.getValue()),
        )

    def verifyChecksum(self) -> None:

        h = XXHash32.XXHash321()
        with open(self.__file, "rb") as f:
            b = self.__toByteArray(f)
            h.update1(b, 0, len(b))
        Assert.self.assertEqual(
            "checksum for " + self.__file.getName(),
            self.__expectedChecksum,
            Long.toHexString(h.getValue()),
        )

    @staticmethod
    def factory() -> typing.Collection[typing.List[typing.Any]]:

        pass  # LLM could not translate method body

    def __init__(self, path: str, c: str) -> None:

        url = self.__class__.getClassLoader().getResource(path)
        if url is None:
            raise FileNotFoundError(f"couldn't find {path}")
        uri = url.toURI()
        self.file = File(uri)
        self.__expectedChecksum = c

    @staticmethod
    def __copy(
        input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        output: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        buffersize: int,
    ) -> int:

        pass  # LLM could not translate method body

    @staticmethod
    def __toByteArray(
        input: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> typing.List[int]:

        pass  # LLM could not translate method body

    # Class Methods End
