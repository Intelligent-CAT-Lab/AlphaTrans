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
from src.main.org.joda.convert.factory.NumericObjectArrayStringConverterFactory import *


class TestNumericObjectArrayStringConverterFactory(unittest.TestCase):

    def test_FloatArray(self) -> None:
        self.__doTest4([], "")
        self.__doTest4([5.0], "5.0")
        self.__doTest4([None], "-")
        self.__doTest4([5.1234], "5.1234")
        self.__doTest4(
            [-1234.0, None, 5678.0, None, None, 5.0], "-1234.0,-,5678.0,-,-,5.0"
        )
        self.__doTest4(
            [float("nan"), float("-inf"), float("inf"), -0.0, +0.0, 0.0],
            "NaN,-Infinity,Infinity,-0.0,0.0,0.0",
        )
        self.__doTest4([0.0000006, 6000000000.0], "6.0E-7,6.0E9")

    def test_DoubleArray(self) -> None:
        self.__doTest3([], "")
        self.__doTest3([5.0], "5.0")
        self.__doTest3([None], "-")
        self.__doTest3([5.123456789], "5.123456789")
        self.__doTest3(
            [-1234.0, None, 5678.0, None, None, 5.0], "-1234.0,-,5678.0,-,-,5.0"
        )
        self.__doTest3(
            [float("nan"), float("-inf"), float("inf"), -0.0, 0.0, 0.0],
            "NaN,-Infinity,Infinity,-0.0,0.0,0.0",
        )
        self.__doTest3([0.0000006, 6000000000.0], "6.0E-7,6.0E9")

    def test_ShortArray(self) -> None:
        self.__doTest2([], "")
        self.__doTest2([5], "5")
        self.__doTest2([None], "-")
        self.__doTest2([-1234, None, 5678, None, None, 5], "-1234,-,5678,-,-,5")

    def test_IntegerArray(self) -> None:
        self.__doTest1([], "")
        self.__doTest1([5], "5")
        self.__doTest1([None], "-")
        self.__doTest1([-1234, None, 56789, None, None, 5], "-1234,-,56789,-,-,5")

    def test_LongArray(self) -> None:
        self.__doTest0([], "")
        self.__doTest0([5], "5")
        self.__doTest0([None], "-")
        self.__doTest0([-1234, None, 56789, None, None, 5], "-1234,-,56789,-,-,5")
        self.__doTest0(
            [12345678912345, 12345678912345], "12345678912345,12345678912345"
        )

    def __doTest4(self, array: typing.List[float], str: str) -> None:
        test = StringConvert(True, NumericObjectArrayStringConverterFactory.INSTANCE)
        self.assertEqual(str, test.convertToString0(array))
        self.assertEqual(str, test.convertToString1(Float, array))
        self.assertTrue(array == test.convertFromString(Float, str))

    def __doTest3(self, array: typing.List[float], str: str) -> None:

        pass  # LLM could not translate this method

    def __doTest2(self, array: typing.List[int], str: str) -> None:
        test: StringConvert = StringConvert(
            True, NumericObjectArrayStringConverterFactory.INSTANCE
        )
        self.assertEqual(str, test.convertToString0(array))
        self.assertEqual(str, test.convertToString1(typing.List[int], array))
        self.assertTrue(array == test.convertFromString(typing.List[int], str))

    def __doTest1(self, array: typing.List[int], str: str) -> None:
        test = StringConvert(True, NumericObjectArrayStringConverterFactory.INSTANCE)
        self.assertEqual(str, test.convertToString0(array))
        self.assertEqual(str, test.convertToString1(typing.List[int], array))
        self.assertTrue(array == test.convertFromString(typing.List[int], str))

    def __doTest0(self, array: typing.List[int], str: str) -> None:
        test: StringConvert = StringConvert(
            True, NumericObjectArrayStringConverterFactory.INSTANCE
        )
        self.assertEqual(str, test.convertToString0(array))
        self.assertEqual(str, test.convertToString1(typing.List[int], array))
        self.assertTrue(array == test.convertFromString(typing.List[int], str))
