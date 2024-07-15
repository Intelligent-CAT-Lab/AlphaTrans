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
        for i in range(0, len(self.__data)):
            self.__data[i] = 31 - i
        self.__check(0x113FDB5C)

    def testIncreasing(self) -> None:

        pass  # LLM could not translate this method

    def testOnes(self) -> None:
        for i in range(32):
            self.__data[i] = 0xFF
        self.__check(0x62A8AB43)

    def testZeros(self) -> None:
        for i in range(32):
            self.__data[i] = 0
        self.__check(0x8A9136AA)

    def __check(self, expected: int) -> None:
        self.__crc.reset()
        self.__crc.update0(self.__data, 0, len(self.__data))
        actual: int = self.__crc.getValue()
        self.assertEqual(hex(expected), hex(actual))
