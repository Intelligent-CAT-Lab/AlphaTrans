from __future__ import annotations
import re
import unittest
import pytest
import io
import typing
from typing import *
import unittest
from src.test.org.joda.convert.DistanceMethodMethod import *
from src.main.org.joda.convert.StringConvert import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.TypedStringConverter import *
from src.test.org.joda.convert.MockDistanceStringConverter import *
from src.main.org.joda.convert.StringConverter import *


class Factory1(StringConverterFactory):

    def findConverter(
        self, cls: typing.Type[typing.Any]
    ) -> StringConverter[typing.Any]:

        if cls == DistanceMethodMethod:
            return MockDistanceStringConverter.INSTANCE
        return None


class TestStringConverterFactory(unittest.TestCase):

    def test_registerFactory_cannotChangeSingleton(self) -> None:

        with pytest.raises(ValueError):
            StringConvert.INSTANCE.registerFactory(Factory1())

    def test_registerFactory_null(self) -> None:

        test = StringConvert.StringConvert1()
        with pytest.raises(ValueError):
            test.registerFactory(None)

    def test_registerFactory(self) -> None:

        test = StringConvert.StringConvert1()
        test.registerFactory(Factory1())
        self.assertEqual(
            DistanceMethodMethod,
            test.findTypedConverter(DistanceMethodMethod).getEffectiveType(),
        )

    def test_constructor_nullInArray(self) -> None:

        with pytest.raises(ValueError):
            StringConvert(True, [None])

    def test_constructor_null(self) -> None:

        with pytest.raises(ValueError):
            StringConvert(True, None)

    def test_constructor(self) -> None:

        test = StringConvert(True, [Factory1()])
        self.assertEqual(
            DistanceMethodMethod,
            test.findTypedConverter(DistanceMethodMethod).getEffectiveType(),
        )
