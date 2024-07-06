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
from src.main.org.joda.convert.factory.ByteObjectArrayStringConverterFactory import *


class TestByteObjectArrayStringConverterFactory(unittest.TestCase):

    def test_ByteArray(self) -> None:
        self.__doTest([], "")
        self.__doTest([0], "00")
        self.__doTest([None], "--")
        self.__doTest([0, 1, None, None, 15, 16, 127, -128, -1], "0001----0F107F80FF")

    def __doTest(self, array: typing.List[int], str: str) -> None:
        test = StringConvert(True, ByteObjectArrayStringConverterFactory.INSTANCE)
        self.assertEqual(str, test.convertToString0(array))
        self.assertEqual(str, test.convertToString1(typing.List[int], array))
        self.assertTrue(array == test.convertFromString(typing.List[int], str))
