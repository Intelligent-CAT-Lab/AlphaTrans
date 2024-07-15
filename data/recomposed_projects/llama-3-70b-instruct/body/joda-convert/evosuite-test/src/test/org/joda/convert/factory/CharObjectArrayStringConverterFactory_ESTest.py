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
from src.main.org.joda.convert.factory.CharObjectArrayStringConverterFactory import *

# from src.test.org.joda.convert.factory.CharObjectArrayStringConverterFactory_ESTest_scaffolding import *
from src.main.org.joda.convert.factory.NumericObjectArrayStringConverterFactory import *


class CharObjectArrayStringConverterFactory_ESTest(unittest.TestCase):

    def test3(self) -> None:

        charObjectArrayStringConverterFactory0 = (
            CharObjectArrayStringConverterFactory.INSTANCE
        )
        string0 = charObjectArrayStringConverterFactory0.toString()
        self.assertEqual("CharObjectArrayStringConverterFactory", string0)

    def test2(self) -> None:

        charObjectArrayStringConverterFactory0 = (
            CharObjectArrayStringConverterFactory.INSTANCE
        )
        class0 = object
        stringConverter0 = charObjectArrayStringConverterFactory0.findConverter(class0)
        self.assertIsNone(stringConverter0)

    def test1(self) -> None:

        booleanArrayStringConverterFactory0 = (
            BooleanArrayStringConverterFactory.INSTANCE
        )
        class0 = Character

        try:
            booleanArrayStringConverterFactory0.findConverter(class0)
        except ValueError:
            pass

    def test0(self) -> None:
        numericObjectArrayStringConverterFactory0 = (
            NumericObjectArrayStringConverterFactory.INSTANCE
        )
        try:
            numericObjectArrayStringConverterFactory0.toString()
        except ValueError:
            pass
