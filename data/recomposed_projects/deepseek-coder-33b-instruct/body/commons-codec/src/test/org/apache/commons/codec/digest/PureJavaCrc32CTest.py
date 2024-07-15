from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import os
import unittest
from src.main.org.apache.commons.codec.digest.PureJavaCrc32C import *


class PureJavaCrc32CTest(unittest.TestCase):

    __data: typing.List[int] = [0] * 32
    __crc: PureJavaCrc32C = PureJavaCrc32C()

    def testDecreasing(self) -> None:

        self.__data = [(31 - i) for i in range(32)]
        self.__check(0x113FDB5C)  # 5c db 3f 11

    def testIncreasing(self) -> None:

        self.__data = [i for i in range(32)]
        self.__check(0x46DD794E)  # 4e 79 dd 46

    def testOnes(self) -> None:

        self.__data = [0xFF] * 32
        self.__check(0x62A8AB43)  # 43 ab a8 62

    def testZeros(self) -> None:

        self.__data = [0 for _ in range(32)]
        self.__check(0x8A9136AA)  # aa 36 91 8a

    def __check(self, expected: int) -> None:

        self.__crc.reset()
        self.__crc.update0(self.__data, 0, len(self.__data))
        actual = self.__crc.getValue()
        self.assertEqual(hex(expected), hex(actual))
