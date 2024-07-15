from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.factory.BooleanArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.BooleanObjectArrayStringConverterFactory import *

# from src.test.org.joda.convert.factory.BooleanObjectArrayStringConverterFactory_ESTest_scaffolding import *
from src.main.org.joda.convert.factory.NumericArrayStringConverterFactory import *


class BooleanObjectArrayStringConverterFactory_ESTest(unittest.TestCase):

    def test3(self) -> None:

        booleanObjectArrayStringConverterFactory0 = (
            BooleanObjectArrayStringConverterFactory.INSTANCE
        )
        string0 = booleanObjectArrayStringConverterFactory0.toString()
        self.assertEqual("BooleanObjectArrayStringConverterFactory", string0)

    def test2(self) -> None:

        booleanObjectArrayStringConverterFactory0 = (
            BooleanObjectArrayStringConverterFactory.INSTANCE
        )
        class0 = bool
        stringConverter0 = booleanObjectArrayStringConverterFactory0.findConverter(
            class0
        )
        self.assertIsNone(stringConverter0)

    def test1(self) -> None:

        class0 = object
        booleanArrayStringConverterFactory0 = (
            BooleanArrayStringConverterFactory.INSTANCE
        )

        try:
            booleanArrayStringConverterFactory0.findConverter(class0)
        except ValueError:
            pass

    def test0(self) -> None:

        numericArrayStringConverterFactory0 = (
            NumericArrayStringConverterFactory.INSTANCE
        )
        try:
            numericArrayStringConverterFactory0.toString()
        except ValueError:
            pass
