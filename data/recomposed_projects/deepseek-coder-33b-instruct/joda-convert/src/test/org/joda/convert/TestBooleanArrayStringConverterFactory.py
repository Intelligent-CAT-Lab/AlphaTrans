from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.factory.BooleanArrayStringConverterFactory import *


class TestBooleanArrayStringConverterFactory:

    def test_longArray(self) -> None:

        def doTest(array: List[bool], str: str) -> None:
            pass

        doTest([], "")
        doTest([True], "T")
        doTest([False], "F")
        doTest([True, True, False, True, False, False], "TTFTFF")

    def __doTest(self, array: typing.List[bool], str: str) -> None:

        test = StringConvert(True, BooleanArrayStringConverterFactory.INSTANCE)
        assert test.convertToString0(array) == str
        assert test.convertToString1(bool, array) == str
        assert test.convertFromString(bool, str) == array
