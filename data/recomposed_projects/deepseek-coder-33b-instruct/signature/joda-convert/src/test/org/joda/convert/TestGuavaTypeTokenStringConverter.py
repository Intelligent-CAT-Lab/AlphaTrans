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
        converter3 = test3.findConverter(Type)
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

        token = typing.TypeVar(
            "T",
            Map[str, Map[typing.Any, List[Number]]],
            Map[str, Map[Union[int, Any], List[Union[int, float, complex, Number]]]],
        )

        self.doTest(
            token,
            "java.util.Map<java.lang.String, java.util.Map<? super java.lang.Integer, ? extends"
            + " java.util.List<? extends java.lang.Number>>>",
        )

    def test_twoParamComplex(self) -> None:

        class TypeToken(typing.Generic[T], typing.Protocol):
            pass

        token = TypeToken[Dict[str, Dict[int, float]]]
        self.doTest(
            token,
            "java.util.Map<java.lang.String, java.util.Map<java.lang.Integer, java.lang.Double>>",
        )

    def test_twoParamNestedExtends(self) -> None:

        token = typing.TypeVar("T", bound=typing.Mapping[str, typing.List[int]])
        self.doTest(
            token,
            "java.util.Map<java.lang.String, ? extends java.util.List<? extends java.lang.Integer>>",
        )

    def test_twoParamNested(self) -> None:

        # Define the nested type
        T = TypeVar("T", bound=Any)
        token = TypeToken(Map[String, List[Integer]])

        # Call the doTest method
        self.doTest(
            token, "java.util.Map<java.lang.String, java.util.List<java.lang.Integer>>"
        )

    def test_twoParamsSuper(self) -> None:

        class TypeToken(typing.Generic[T], typing.Protocol):
            pass

        token = TypeToken[Dict[Union[str, Any], Union[int, Any]]]()
        self.doTest(
            token, "java.util.Map<? super java.lang.String, ? super java.lang.Integer>"
        )

    def test_twoParamsExtends(self) -> None:

        token = typing.TypeVar("T", bound=typing.Mapping[typing.Any, typing.Any])
        self.doTest(
            token,
            "java.util.Map<? extends java.lang.CharSequence, ? extends java.lang.Number>",
        )

    def test_twoParams(self) -> None:

        class TypeToken(typing.Generic[T], typing.Protocol):
            pass

        token = TypeToken[Dict[str, int]]
        self.doTest(token, "java.util.Map<java.lang.String, java.lang.Integer>")

    def test_oneSuper(self) -> None:

        # TypeToken<List<? super Integer>> in Java is equivalent to typing.List[typing.Any] in Python
        token = typing.List[typing.Any]
        self.doTest(token, "java.util.List<? super java.lang.Integer>")

    def test_oneExtends(self) -> None:

        # TypeToken<List<? extends Number>> in Java is equivalent to typing.List[Number] in Python
        token = typing.List[Number]
        self.doTest(token, "java.util.List<? extends java.lang.Number>")

    def test_oneArray(self) -> None:

        token = TypeToken.get(List[List[str]])
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

        class ListWild(List[Any]):
            pass

        token = TypeToken(ListWild)
        self.doTest(token, "java.util.List<?>")

    def test_oneParam(self) -> None:

        class ListString(List[str]):
            pass

        token = ListString()
        self.doTest(token, "java.util.List<java.lang.String>")

    def test_primitive_char(self) -> None:

        # In Python, there is no direct equivalent to Java's Character.TYPE.
        # However, we can use the type() function to get the type of a variable.
        # Here, we are using the type() function to get the type of a character.
        token = type(chr(0))
        self.doTest(token, "char")

    def test_primitive_int(self) -> None:

        # TypeToken is a class in Guava library, which is not available in Python.
        # However, we can use typing.TypeVar to simulate it.
        token = typing.TypeVar("T", int, int)
        self.doTest(token, "int")

    def test_simpleClass_rawList(self) -> None:

        # TypeToken is not available in Python, so we can't directly translate this.
        # However, we can use typing.List to represent the same concept.
        token = typing.List
        self.doTest(token, "typing.List")

    def test_simpleClass_Integer(self) -> None:

        # Assuming TypeToken is a class in the same module
        token = TypeToken.of(int)
        self.doTest(token, "java.lang.Integer")

    def test_simpleClass_String(self) -> None:

        # Assuming TypeToken is a class in the same module
        token = TypeToken.of(str)
        self.doTest(token, "java.lang.String")
