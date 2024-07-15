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
from src.main.org.joda.convert.factory.NumericArrayStringConverterFactory import *


class TestNumericArrayStringConverterFactory(unittest.TestCase):

    def test_floatArray(self) -> None:

        self.__doTest4([], "")
        self.__doTest4([5.0], "5.0")
        self.__doTest4([5.1234], "5.1234")
        self.__doTest4([-1234.0, 5678.0], "-1234.0,5678.0")
        self.__doTest4(
            [float("nan"), float("-inf"), float("inf"), -0.0, 0.0, 0.0],
            "NaN,-Infinity,Infinity,-0.0,0.0,0.0",
        )
        self.__doTest4([0.0000006, 6000000000.0], "6.0E-7,6.0E9")

    def test_doubleArray(self) -> None:

        self.__doTest3([], "")
        self.__doTest3([5.0], "5.0")
        self.__doTest3([5.123456789], "5.123456789")
        self.__doTest3([-1234.0, 5678.0], "-1234.0,5678.0")
        self.__doTest3(
            [float("nan"), float("-inf"), float("inf"), -0.0, 0.0, 0.0],
            "nan,-inf,inf,-0.0,0.0,0.0",
        )
        self.__doTest3([0.0000006, 6000000000.0], "6e-07,6e+09")

    def test_shortArray(self) -> None:

        self.__doTest2([], "")
        self.__doTest2([5], "5")
        self.__doTest2([-1234, 5678], "-1234,5678")

    def test_intArray(self) -> None:

        self.__doTest1([], "")
        self.__doTest1([5], "5")
        self.__doTest1([-1234, 56789], "-1234,56789")

    def test_longArray(self) -> None:

        self.__doTest0([], "")
        self.__doTest0([5], "5")
        self.__doTest0([-1234, 56789], "-1234,56789")
        self.__doTest0(
            [12345678912345, 12345678912345], "12345678912345,12345678912345"
        )

    def __doTest4(self, array: typing.List[float], str: str) -> None:

        test = StringConvert(True, NumericArrayStringConverterFactory.INSTANCE)
        self.assertEqual(str, test.convertToString0(array))
        self.assertEqual(str, test.convertToString1(float, array))
        self.assertTrue(array == test.convertFromString(float, str))

    def __doTest3(self, array: typing.List[float], str: str) -> None:

        test = StringConvert(True, NumericArrayStringConverterFactory.INSTANCE)
        self.assertEqual(str, test.convertToString0(array))
        self.assertEqual(str, test.convertToString1(float, array))
        self.assertTrue(
            all(a == b for a, b in zip(array, test.convertFromString(float, str)))
        )

    def __doTest2(self, array: typing.List[int], str: str) -> None:

        pass  # LLM could not translate this method

    def __doTest1(self, array: typing.List[int], str: str) -> None:

        test = StringConvert(True, NumericArrayStringConverterFactory.INSTANCE)
        self.assertEqual(str, test.convertToString0(array))
        self.assertEqual(str, test.convertToString1(int, array))
        self.assertTrue(array == test.convertFromString(int, str))

    def __doTest0(self, array: typing.List[int], str: str) -> None:

        test = StringConvert(True, NumericArrayStringConverterFactory.INSTANCE)
        self.assertEqual(str, test.convertToString0(array))
        self.assertEqual(str, test.convertToString1(list, array))
        self.assertTrue(array == test.convertFromString(list, str))
