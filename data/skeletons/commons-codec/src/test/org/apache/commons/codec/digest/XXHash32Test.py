from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.digest.XXHash32 import *
import unittest
import os
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO
import pathlib

# Imports End


class XXHash32Test(unittest.TestCase):

    # Class Fields Begin
    __file: pathlib.Path = None
    __expectedChecksum: str = None
    # Class Fields End

    # Class Methods Begin
    def verifyIncrementalChecksum_test4_decomposed(self) -> None:
        pass

    def verifyIncrementalChecksum_test3_decomposed(self) -> None:
        pass

    def verifyIncrementalChecksum_test2_decomposed(self) -> None:
        pass

    def verifyIncrementalChecksum_test1_decomposed(self) -> None:
        pass

    def verifyIncrementalChecksum_test0_decomposed(self) -> None:
        pass

    def verifyChecksum_test4_decomposed(self) -> None:
        pass

    def verifyChecksum_test3_decomposed(self) -> None:
        pass

    def verifyChecksum_test2_decomposed(self) -> None:
        pass

    def verifyChecksum_test1_decomposed(self) -> None:
        pass

    def verifyChecksum_test0_decomposed(self) -> None:
        pass

    @staticmethod
    def factory() -> typing.Collection[typing.List[typing.Any]]:
        pass

    def __init__(self, path: str, c: str) -> None:
        pass

    @staticmethod
    def __copy(
        input_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
        output: typing.Union[io.BytesIO, io.StringIO, io.BufferedWriter],
        buffersize: int,
    ) -> int:
        pass

    @staticmethod
    def __toByteArray(
        input_: typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]
    ) -> typing.List[int]:
        pass

    # Class Methods End
