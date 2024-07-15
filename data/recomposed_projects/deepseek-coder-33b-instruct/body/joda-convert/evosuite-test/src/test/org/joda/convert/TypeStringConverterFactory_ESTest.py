from __future__ import annotations
import time
import inspect
import re
import os
import unittest
import pytest
import io
import typing
from typing import *
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.TypeStringConverterFactory import *

# from src.test.org.joda.convert.TypeStringConverterFactory_ESTest_scaffolding import *
from src.main.org.joda.convert.Types import *


class TypeStringConverterFactory_ESTest(unittest.TestCase):

    def test7(self) -> None:

        typeStringConverterFactory0 = TypeStringConverterFactory.INSTANCE
        string0 = typeStringConverterFactory0.toString()
        self.assertEqual("TypeStringConverterFactory", string0)

    def test6(self) -> None:

        class0 = object
        typeStringConverterFactory_TypeStringConverter0 = (
            TypeStringConverterFactory.TypeStringConverter(class0)
        )

        try:
            typeStringConverterFactory_TypeStringConverter0.convertToString(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.evosuite.runtime.System", e)

    def test5(self) -> None:

        class0 = object
        typeStringConverterFactory_TypeStringConverter0 = TypeStringConverter(class0)
        class1 = typeStringConverterFactory_TypeStringConverter0.getEffectiveType()
        self.assertFalse(inspect.isbuiltin(class1))

    def test4(self) -> None:

        class0 = object
        typeStringConverterFactory_TypeStringConverter0 = (
            TypeStringConverterFactory.TypeStringConverter(class0)
        )
        class1 = Types.WildcardTypeImpl

        try:
            typeStringConverterFactory_TypeStringConverter0.convertFromString(
                class1, ""
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            self.verifyException("org.joda.convert.TypeUtils", e)

    def test3(self) -> None:
        typeStringConverterFactory0 = TypeStringConverterFactory.INSTANCE
        class0 = object
        stringConverter0 = typeStringConverterFactory0.findConverter(class0)
        self.assertIsNone(stringConverter0)

    def test2(self) -> None:
        typeStringConverterFactory0 = TypeStringConverterFactory.INSTANCE
        class0 = Types.WildcardTypeImpl
        stringConverter0 = typeStringConverterFactory0.findConverter(class0)
        self.assertIsNotNone(stringConverter0)

    def test1(self) -> None:
        typeStringConverterFactory0 = TypeStringConverterFactory.INSTANCE
        try:
            typeStringConverterFactory0.findConverter(None)
            self.fail("Expecting exception: RuntimeError")
        except TypeError:
            pass

    def test0(self) -> None:
        class0 = Types.WildcardTypeImpl
        typeStringConverterFactory_TypeStringConverter0 = (
            TypeStringConverterFactory.TypeStringConverter(class0)
        )
        string0 = typeStringConverterFactory_TypeStringConverter0.convertToString(
            class0
        )
        self.assertEqual("org.joda.convert.Types$WildcardTypeImpl", string0)
