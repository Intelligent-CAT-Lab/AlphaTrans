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

        for i in range(len(self.__data)):
            self.__data[i] = (31 - i) & 0xFF

        self.__check(0x113FDB5C)  # 5c db 3f 11

    def testIncreasing(self) -> None:

        for i in range(len(self.__data)):
            self.__data[i] = i

        self.__check(0x46DD794E)  # 4e 79 dd 46

    def testOnes(self) -> None:

        # Fill the data array with 0xFF
        self.__data = [0xFF] * 32

        # Call the check method with the expected value
        self.__check(0x62A8AB43)

    def testZeros(self) -> None:

        # Fill the data array with zeros
        self.__data = [0] * 32

        # Call the check method with the expected value
        self.__check(0x8A9136AA)

    def __check(self, expected: int) -> None:

        self.__crc.reset()
        self.__crc.update0(self.__data, 0, len(self.__data))
        actual = self.__crc.getValue()
        self.assertEqual(hex(expected), hex(actual))
