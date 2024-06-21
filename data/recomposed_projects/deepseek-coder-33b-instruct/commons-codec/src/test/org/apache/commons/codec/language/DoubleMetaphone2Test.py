from __future__ import annotations
import re
from dataclasses import field
import unittest
import pytest
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.language.DoubleMetaphone import *


class DoubleMetaphone2Test(StringEncoderAbstractTest, unittest.TestCase):

    __TEST_DATA: typing.List[typing.List[str]] = (
        None  # LLM could not translate this field
    )

    __PRIMARY_INDEX: int = 1

    __ALTERNATE_INDEX: int = 2

    def testDoubleMetaphonePrimary(self) -> None:

        self.__checkDoubleMetaphone(self.__PRIMARY_INDEX, False)

    def testDoubleMetaphoneAlternate(self) -> None:

        self.__checkDoubleMetaphone(self.__ALTERNATE_INDEX, True)

    def _createStringEncoder(self) -> DoubleMetaphone:

        return DoubleMetaphone()

    def __checkDoubleMetaphone(self, typeIndex: int, alternate: bool) -> None:

        for i in range(len(self.__TEST_DATA)):
            value = self.__TEST_DATA[i][0]
            assert (
                self.getStringEncoder().doubleMetaphone1(value, alternate)
                == self.__TEST_DATA[i][typeIndex]
            ), ("Test [" + str(i) + "]=" + value)
