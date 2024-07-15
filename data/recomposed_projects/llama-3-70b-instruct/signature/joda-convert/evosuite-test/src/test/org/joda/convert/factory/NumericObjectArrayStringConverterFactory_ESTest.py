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
from src.main.org.joda.convert.factory.CharObjectArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.NumericArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.NumericObjectArrayStringConverterFactory import *

# from src.test.org.joda.convert.factory.NumericObjectArrayStringConverterFactory_ESTest_scaffolding import *


class NumericObjectArrayStringConverterFactory_ESTest(unittest.TestCase):

    def test4(self) -> None:

        numericObjectArrayStringConverterFactory0 = (
            NumericObjectArrayStringConverterFactory.INSTANCE
        )
        string0 = numericObjectArrayStringConverterFactory0.toString()
        self.assertEqual("NumericObjectArrayStringConverterFactory", string0)

    def test3(self) -> None:

        numericObjectArrayStringConverterFactory0 = (
            NumericObjectArrayStringConverterFactory.INSTANCE
        )
        class0 = float
        stringConverter0 = numericObjectArrayStringConverterFactory0.findConverter(
            class0
        )
        self.assertIsNone(stringConverter0)

    def test2(self) -> None:

        class0 = object
        numericArrayStringConverterFactory0 = (
            NumericArrayStringConverterFactory.INSTANCE
        )

        try:
            numericArrayStringConverterFactory0.findConverter(class0)
        except ValueError:
            pass

    def test1(self) -> None:

        numericObjectArrayStringConverterFactory0 = (
            NumericObjectArrayStringConverterFactory.INSTANCE
        )

        with self.assertRaises(RuntimeError):
            numericObjectArrayStringConverterFactory0.findConverter(None)

    def test0(self) -> None:

        charObjectArrayStringConverterFactory0 = (
            CharObjectArrayStringConverterFactory.INSTANCE
        )
        try:
            charObjectArrayStringConverterFactory0.toString()
        except ValueError:
            pass
