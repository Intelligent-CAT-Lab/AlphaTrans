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

# from src.test.org.joda.convert.factory.BooleanArrayStringConverterFactory_ESTest_scaffolding import *
from src.main.org.joda.convert.factory.ByteObjectArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.NumericArrayStringConverterFactory import *


class BooleanArrayStringConverterFactory_ESTest(unittest.TestCase):

    def test3(self) -> None:

        booleanArrayStringConverterFactory0 = (
            BooleanArrayStringConverterFactory.INSTANCE
        )
        string0 = booleanArrayStringConverterFactory0.toString()
        self.assertEqual("BooleanArrayStringConverterFactory", string0)

    def test2(self) -> None:

        booleanArrayStringConverterFactory0 = (
            BooleanArrayStringConverterFactory.INSTANCE
        )
        class0 = object
        stringConverter0 = booleanArrayStringConverterFactory0.findConverter(class0)
        self.assertIsNone(stringConverter0)

    def test1(self) -> None:

        byteObjectArrayStringConverterFactory0 = (
            ByteObjectArrayStringConverterFactory.INSTANCE
        )
        class0 = int

        try:
            byteObjectArrayStringConverterFactory0.findConverter(class0)
            self.fail("Expecting exception: ValueError")
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
