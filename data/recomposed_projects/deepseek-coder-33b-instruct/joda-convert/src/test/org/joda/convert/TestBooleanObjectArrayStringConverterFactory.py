from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.factory.BooleanObjectArrayStringConverterFactory import *


class TestBooleanObjectArrayStringConverterFactory:

    def test_longArray(self) -> None:

        def doTest(array: List[Optional[bool]], str: str) -> None:
            pass

        doTest([], "")
        doTest([True], "T")
        doTest([False], "F")
        doTest([None], "-")
        doTest([True, True, False, None, True, False, None, None, False], "TTF-TF--F")

    def __doTest(self, array: typing.List[bool], str: str) -> None:

        test = StringConvert(True, BooleanObjectArrayStringConverterFactory.INSTANCE)
        assert test.convertToString0(array) == str
        assert test.convertToString1(typing.List[bool], array) == str
        assert test.convertFromString(typing.List[bool], str) == array
