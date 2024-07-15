from __future__ import annotations
import time
import inspect
import re
import os
import typing
from typing import *
import enum
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.convert.EnumStringConverterFactory import *

# from src.test.org.joda.convert.EnumStringConverterFactory_ESTest_scaffolding import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.TypeStringConverterFactory import *


class EnumStringConverterFactory_ESTest(unittest.TestCase):

    def test6(self) -> None:

        enumStringConverterFactory0 = EnumStringConverterFactory.INSTANCE
        string0 = str(enumStringConverterFactory0)
        self.assertEqual("EnumStringConverterFactory", string0)

    def test5(self) -> None:
        class0 = object
        enumStringConverterFactory_EnumStringConverter0 = (
            EnumStringConverterFactory.EnumStringConverter(class0)
        )
        class1 = enumStringConverterFactory_EnumStringConverter0.getEffectiveType()
        self.assertFalse(inspect.isbuiltin(class1))

    def test4(self) -> None:
        enumStringConverterFactory0 = EnumStringConverterFactory.INSTANCE
        class0 = EnumStringConverterFactory
        stringConverter0 = enumStringConverterFactory0.findConverter(class0)
        self.assertIsNone(stringConverter0)

    def test3(self) -> None:
        enumStringConverterFactory0 = EnumStringConverterFactory.INSTANCE
        class0 = object
        stringConverter0 = enumStringConverterFactory0.findConverter(class0)
        self.assertIsNone(stringConverter0)

    def test2(self) -> None:

        class0 = EnumStringConverterFactory
        typeStringConverterFactory0 = TypeStringConverterFactory.INSTANCE

        try:
            typeStringConverterFactory0.findConverter(class0)
        except ValueError:
            pass

    def test1(self) -> None:

        enumStringConverterFactory0 = EnumStringConverterFactory.INSTANCE
        try:
            enumStringConverterFactory0.findConverter(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")

    def test0(self) -> None:

        typeStringConverterFactory0 = TypeStringConverterFactory.INSTANCE
        try:
            typeStringConverterFactory0.toString()
        except ValueError:
            pass
