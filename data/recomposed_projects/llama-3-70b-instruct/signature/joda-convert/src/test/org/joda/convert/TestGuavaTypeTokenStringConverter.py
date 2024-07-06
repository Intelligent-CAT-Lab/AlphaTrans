from __future__ import annotations
import re
import numbers
import unittest
import pytest
import io
import typing
from typing import *
import unittest

# from src.main.com.google.common.reflect.TypeToken import *
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.TypeStringConverterFactory import *
from src.main.org.joda.convert.TypeTokenStringConverter import *
from src.main.org.joda.convert.TypedStringConverter import *


class TestGuavaTypeTokenStringConverter(unittest.TestCase):

    def doTest(self, obj: typing.TypeVar("T", bound=typing.Any), str: str) -> None:

        pass  # LLM could not translate this method

    def test_twoParamComplexExtends(self) -> None:
        token = TypeToken[
            Map[
                str,
                Map[
                    typing.Union[int, typing.Any],
                    typing.Union[List[typing.Union[Number, typing.Any]], typing.Any],
                ],
            ]
        ]()
        self.doTest(
            token,
            "java.util.Map<java.lang.String, java.util.Map<? super java.lang.Integer, ? extends java.util.List<? extends java.lang.Number>>>",
        )

    def test_twoParamComplex(self) -> None:
        token = TypeToken[Map[str, Map[int, float]]]()
        self.doTest(
            token,
            "java.util.Map<java.lang.String, java.util.Map<java.lang.Integer,"
            + " java.lang.Double>>",
        )

    def test_twoParamNestedExtends(self) -> None:
        token = TypeToken[
            Map[
                str,
                typing.Union[typing.List[typing.Union[int, typing.Any]], typing.Any],
            ]
        ]()
        self.doTest(
            token,
            "java.util.Map<java.lang.String, ? extends java.util.List<? extends"
            + " java.lang.Integer>>",
        )

    def test_twoParamNested(self) -> None:
        token = TypeToken[Map[str, List[int]]]()
        self.doTest(
            token, "java.util.Map<java.lang.String, java.util.List<java.lang.Integer>>"
        )

    def test_twoParamsSuper(self) -> None:
        token = TypeToken[Map[typing.Any, typing.Any]]()
        self.doTest(
            token, "java.util.Map<? super java.lang.String, ? super java.lang.Integer>"
        )

    def test_twoParamsExtends(self) -> None:
        token = TypeToken[
            Map[
                typing.TypeVar("T", bound=CharSequence),
                typing.TypeVar("T", bound=Number),
            ]
        ]()
        self.doTest(
            token,
            "java.util.Map<? extends java.lang.CharSequence, ? extends java.lang.Number>",
        )

    def test_twoParams(self) -> None:
        token = TypeToken[Map[str, int]]()
        self.doTest(token, "java.util.Map<java.lang.String, java.lang.Integer>")

    def test_oneSuper(self) -> None:
        token = TypeToken[List[typing.TypeVar("T", bound=typing.Any)]]()
        self.doTest(token, "java.util.List<? super java.lang.Integer>")

    def test_oneExtends(self) -> None:
        token = TypeToken[List[typing.TypeVar("T", bound=Number)]]()
        self.doTest(token, "java.util.List<? extends java.lang.Number>")

    def test_oneArray(self) -> None:
        token = TypeToken[List[str]]()
        test = TypeTokenStringConverter()
        asStr = test.convertToString(token)
        reverse1 = test.convertFromString(
            TypeToken, "java.util.List<java.lang.String[]>"
        )
        reverse2 = test.convertFromString(
            TypeToken, "java.util.List<[Ljava.lang.String;>"
        )
        self.assertEqual(reverse1, reverse2)
        expected = (
            "java.util.List<java.lang.String[]>"
            if asStr == "java.util.List<java.lang.String[]>"
            else "java.util.List<[Ljava.lang.String;>"
        )
        self.doTest(token, expected)

    def test_oneWild(self) -> None:
        token = TypeToken[List[typing.Any]]()
        self.doTest(token, "java.util.List<?>")

    def test_oneParam(self) -> None:
        token = TypeToken[List[str]]()
        self.doTest(token, "java.util.List<java.lang.String>")

    def test_primitive_char(self) -> None:
        token: TypeToken[typing.Any] = TypeToken.of(Character.TYPE)
        self.doTest(token, "char")

    def test_primitive_int(self) -> None:
        token: TypeToken = TypeToken.of(Integer.TYPE)
        self.doTest(token, "int")

    def test_simpleClass_rawList(self) -> None:
        token = TypeToken.of(List)
        self.doTest(token, "java.util.List")

    def test_simpleClass_Integer(self) -> None:

        pass  # LLM could not translate this method

    def test_simpleClass_String(self) -> None:
        token = TypeToken.of(String)
        self.doTest(token, "java.lang.String")
