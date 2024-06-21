from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.factory.CharObjectArrayStringConverterFactory import *


class TestCharObjectArrayStringConverterFactory:

    def test_CharacterArray(self) -> None:

        def __doTest(array: typing.List[str], str: str) -> None:
            pass

        __doTest([], "")
        __doTest(["T"], "T")
        __doTest(["-"], "-")
        __doTest([None], "\\-")
        __doTest(["J", "-", "T"], "J-T")
        __doTest(["\\", "\\", None], "\\\\\\\\\\-")
        __doTest(["-", "H", "e", None, None, "o"], "-He\\-\\-o")

    def __doTest(self, array: typing.List[str], str: str) -> None:

        test = StringConvert(True, CharObjectArrayStringConverterFactory.INSTANCE)
        assert test.convertToString0(array) == str
        assert test.convertToString1(typing.List[str], array) == str
        assert test.convertFromString(typing.List[str], str) == array
