from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.factory.BooleanObjectArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.CharObjectArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.NumericArrayStringConverterFactory import *

# from src.test.org.joda.convert.factory.NumericArrayStringConverterFactory_ESTest_scaffolding import *


class NumericArrayStringConverterFactory_ESTest(unittest.TestCase):

    def test4(self) -> None:

        numericArrayStringConverterFactory0 = (
            NumericArrayStringConverterFactory.INSTANCE
        )
        string0 = numericArrayStringConverterFactory0.toString()
        self.assertEqual("NumericArrayStringConverterFactory", string0)

    def test3(self) -> None:

        numericArrayStringConverterFactory0 = (
            NumericArrayStringConverterFactory.INSTANCE
        )
        class0 = int
        stringConverter0 = numericArrayStringConverterFactory0.findConverter(class0)
        self.assertIsNone(stringConverter0)

    def test2(self) -> None:

        class0 = object
        booleanObjectArrayStringConverterFactory0 = (
            BooleanObjectArrayStringConverterFactory.INSTANCE
        )

        try:
            booleanObjectArrayStringConverterFactory0.findConverter(class0)
        except ValueError:
            pass

    def test1(self) -> None:

        numericArrayStringConverterFactory0 = (
            NumericArrayStringConverterFactory.INSTANCE
        )

        with self.assertRaises(RuntimeError):
            numericArrayStringConverterFactory0.findConverter(None)

    def test0(self) -> None:

        charObjectArrayStringConverterFactory0 = (
            CharObjectArrayStringConverterFactory.INSTANCE
        )
        try:
            charObjectArrayStringConverterFactory0.toString()
        except ValueError:
            pass
