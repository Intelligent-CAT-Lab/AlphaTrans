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
from src.main.org.joda.convert.factory.BooleanObjectArrayStringConverterFactory import *


class TestBooleanObjectArrayStringConverterFactory(unittest.TestCase):

    def test_longArray(self) -> None:

        self.__doTest([], "")
        self.__doTest([True], "T")
        self.__doTest([False], "F")
        self.__doTest([None], "-")
        self.__doTest(
            [True, True, False, None, True, False, None, None, False], "TTF-TF--F"
        )

    def __doTest(self, array: typing.List[bool], str: str) -> None:

        test = StringConvert(True, BooleanObjectArrayStringConverterFactory.INSTANCE)
        self.assertEqual(str, test.convertToString0(array))
        self.assertEqual(str, test.convertToString1(bool, array))
        self.assertTrue(array == test.convertFromString(bool, str))
