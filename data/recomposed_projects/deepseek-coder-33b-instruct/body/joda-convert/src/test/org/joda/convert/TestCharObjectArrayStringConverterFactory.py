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
from src.main.org.joda.convert.factory.CharObjectArrayStringConverterFactory import *


class TestCharObjectArrayStringConverterFactory(unittest.TestCase):

    def test_CharacterArray(self) -> None:

        self.__doTest([], "")
        self.__doTest(["T"], "T")
        self.__doTest(["-"], "-")
        self.__doTest([None], "\\-")
        self.__doTest(["J", "-", "T"], "J-T")
        self.__doTest(["\\", "\\", None], "\\\\\\\\\\-")
        self.__doTest(["-", "H", "e", None, None, "o"], "-He\\-\\-o")

    def __doTest(self, array: typing.List[str], str: str) -> None:

        test = StringConvert(True, CharObjectArrayStringConverterFactory.INSTANCE)
        self.assertEqual(str, test.convertToString0(array))
        self.assertEqual(str, test.convertToString1(list, array))
        self.assertTrue(array == test.convertFromString(list, str))
