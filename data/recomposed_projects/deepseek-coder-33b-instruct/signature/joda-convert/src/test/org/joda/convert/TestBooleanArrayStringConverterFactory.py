from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.factory.BooleanArrayStringConverterFactory import *


class TestBooleanArrayStringConverterFactory(unittest.TestCase):

    def test_longArray(self) -> None:

        self.__doTest([], "")
        self.__doTest([True], "T")
        self.__doTest([False], "F")
        self.__doTest([True, True, False, True, False, False], "TTFTFF")

    def __doTest(self, array: typing.List[bool], str: str) -> None:

        test = StringConvert(True, BooleanArrayStringConverterFactory.INSTANCE)
        self.assertEqual(str, test.convertToString0(array))
        self.assertEqual(str, test.convertToString1(bool, array))
        self.assertTrue(array == test.convertFromString(bool, str))
