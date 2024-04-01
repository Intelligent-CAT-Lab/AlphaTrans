# Imports Begin
from src.main.org.apache.commons.codec.digest.PureJavaCrc32C import *
import unittest
import os
import typing
from typing import *

# Imports End


class PureJavaCrc32CTest(unittest.TestCase):

    # Class Fields Begin
    __crc: PureJavaCrc32C = PureJavaCrc32C()
    __data: typing.List[int] = ""  # LLM could not translate field
    # Class Fields End

    # Class Methods Begin
    def testDecreasing(self) -> None:

        for i in range(len(self.__data)):
            self.__data[i] = 31 - i
        self.__check(0x113FDB5C)

    def testIncreasing(self) -> None:

        for i in range(len(self.__data)):
            self.__data[i] = i
        self.__check(0x46DD794E)

    def testOnes(self) -> None:

        self.__data.fill(0xFF)
        self.__check(0x62A8AB43)

    def testZeros(self) -> None:

        self.__data.fill(0)
        self.__check(0x8A9136AA)  # aa 36 91 8a

    def __check(self, expected: int) -> None:

        self.__crc.reset()
        self.__crc.update0(self.__data, 0, len(self.__data))
        actual = int(self.__crc.getValue())
        Assert.self.assertEqual(
            Integer.toHexString(expected), Integer.toHexString(actual)
        )

    # Class Methods End
