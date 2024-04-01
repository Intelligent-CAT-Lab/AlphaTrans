# Imports Begin
from src.main.org.joda.convert.factory.NumericObjectArrayStringConverterFactory import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.StringConvert import *
import unittest
import typing
from typing import *

# Imports End


class TestNumericObjectArrayStringConverterFactory(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test_FloatArray(self) -> None:

        self.__doTest4([], "")
        self.__doTest4([5.0], "5.0")
        self.__doTest4([None], "-")
        self.__doTest4([5.1234], "5.1234")
        self.__doTest4(
            [-1234.0, None, 5678.0, None, None, 5.0], "-1234.0,-,5678.0,-,-,5.0"
        )
        self.__doTest4(
            [float("nan"), float("-inf"), float("inf"), -0.0, 0.0, 0.0],
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

        pass  # LLM could not translate method body

    def __doTest3(self, array: typing.List[float], str: str) -> None:

        pass  # LLM could not translate method body

    def __doTest2(self, array: typing.List[int], str: str) -> None:

        pass  # LLM could not translate method body

    def __doTest1(self, array: typing.List[int], str: str) -> None:

        pass  # LLM could not translate method body

    def __doTest0(self, array: typing.List[int], str: str) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
