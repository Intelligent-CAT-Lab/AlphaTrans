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

        test = TypeTokenStringConverter()
        self.assertEqual(TypeToken, test.getEffectiveType())
        self.assertEqual(str, test.convertToString(obj))
        self.assertEqual(obj, test.convertFromString(TypeToken, str))

        test2 = StringConvert.INSTANCE.findTypedConverterNoGenerics(TypeToken)
        self.assertEqual(TypeToken, test2.getEffectiveType())
        self.assertEqual(str, test2.convertToString(obj))
        self.assertEqual(obj, test2.convertFromString(TypeToken, str))

        test3 = TypeStringConverterFactory.INSTANCE
        converter3 = typing.cast(TypedStringConverter[Type], test3.findConverter(Type))
        self.assertEqual(Type, converter3.getEffectiveType())
        self.assertEqual(str, converter3.convertToString(obj.getType()))
        self.assertEqual(obj.getType(), converter3.convertFromString(Type, str))

        test4 = StringConvert.INSTANCE.findTypedConverterNoGenerics(Type)
        self.assertEqual(Type, test4.getEffectiveType())
        self.assertEqual(str, test4.convertToString(obj.getType()))
        self.assertEqual(obj.getType(), test4.convertFromString(Type, str))

        test5 = StringConvert.INSTANCE.findTypedConverterNoGenerics(ParameterizedType)
        self.assertEqual(ParameterizedType, test5.getEffectiveType())
        self.assertEqual(str, test5.convertToString(obj.getType()))
        self.assertEqual(obj.getType(), test5.convertFromString(ParameterizedType, str))

    def test_twoParamComplexExtends(self) -> None:

        token = TypeToken[
            Map[str, Map[Union[int, None], List[Union[int, float, complex, None]]]]
        ]()

        self.doTest(
            token,
            "java.util.Map<java.lang.String, java.util.Map<? super java.lang.Integer, ? extends"
            + " java.util.List<? extends java.lang.Number>>>",
        )

    def test_twoParamComplex(self) -> None:

        token = TypeToken.of(Map[str, Map[int, float]])
        str_val = "java.util.Map<java.lang.String, java.util.Map<java.lang.Integer, java.lang.Double>>"
        self.doTest(token, str_val)

    def test_twoParamNestedExtends(self) -> None:

        token = TypeToken.get(typing.Dict[str, typing.List[int]])
        self.doTest(
            token,
            "java.util.Map<java.lang.String, ? extends java.util.List<? extends java.lang.Integer>>",
        )

    def test_twoParamNested(self) -> None:

        token = TypeToken.get(typing.Dict[str, typing.List[int]])
        str_rep = "java.util.Map<java.lang.String, java.util.List<java.lang.Integer>>"
        self.doTest(token, str_rep)

    def test_twoParamsSuper(self) -> None:

        token = TypeToken.get(typing.Dict[typing.Any, typing.Any])
        self.doTest(
            token, "java.util.Map<? super java.lang.String, ? super java.lang.Integer>"
        )

    def test_twoParamsExtends(self) -> None:

        token = TypeToken.get(Map[str, int])
        self.doTest(token, "java.util.Map<java.lang.String, java.lang.Integer>")

    def test_twoParams(self) -> None:

        token = TypeToken[Dict[str, int]]
        self.doTest(token, "java.util.Map<java.lang.String, java.lang.Integer>")

    def test_oneSuper(self) -> None:

        token = TypeToken.get(List[Union[int, Any]])
        self.doTest(token, "java.util.List<? super java.lang.Integer>")

    def test_oneExtends(self) -> None:

        token = TypeToken(List[Extends[Number]])
        self.doTest(token, "java.util.List<? extends java.lang.Number>")

    def test_oneArray(self) -> None:

        token = TypeToken.of(List[String[[]]])
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

        token = TypeToken[List[Any]]()
        self.doTest(token, "java.util.List<?>")

    def test_oneParam(self) -> None:

        token = TypeToken[List[str]]
        self.doTest(token, "java.util.List<java.lang.String>")

    def test_primitive_char(self) -> None:

        token = TypeToken.of(char)
        self.doTest(token, "char")

    def test_primitive_int(self) -> None:

        token = TypeToken.of(int)
        self.doTest(token, "int")

    def test_simpleClass_rawList(self) -> None:

        token = TypeToken.of(List)
        self.doTest(token, "java.util.List")

    def test_simpleClass_Integer(self) -> None:

        token = TypeToken.of(int)
        self.doTest(token, "java.lang.Integer")

    def test_simpleClass_String(self) -> None:

        token = TypeToken.of(str)
        self.doTest(token, "java.lang.String")
