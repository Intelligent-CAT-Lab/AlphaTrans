# Imports Begin
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.MockDistanceStringConverter import *
from src.main.org.joda.convert.TypedStringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.convert.DistanceMethodMethod import *
import unittest
import typing
from typing import *

# Imports End


class Factory1(unittest.TestCase, StringConverterFactory):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:

        if cls == DistanceMethodMethod:
            return MockDistanceStringConverter.INSTANCE
        return None

    # Class Methods End


class TestStringConverterFactory(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test_registerFactory_cannotChangeSingleton(self) -> None:

        StringConvert.INSTANCE.registerFactory(Factory1())

    def test_registerFactory_null(self) -> None:

        test = StringConvert.StringConvert1()
        test.registerFactory(None)

    def test_registerFactory(self) -> None:

        pass  # LLM could not translate method body

    def test_constructor_nullInArray(self) -> None:

        with self.assertRaises(TypeError):
            StringConvert(True, [None])

    def test_constructor_null(self) -> None:

        StringConverter(True, None)

    def test_constructor(self) -> None:

        test = StringConvert(True, Factory1())
        self.assertEqual(
            DistanceMethodMethod,
            test.findTypedConverter(DistanceMethodMethod).getEffectiveType(),
        )

    # Class Methods End
