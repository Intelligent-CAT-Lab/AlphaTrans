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
from src.main.org.joda.convert.factory.BooleanObjectArrayStringConverterFactory import *
from src.main.org.joda.convert.factory.ByteObjectArrayStringConverterFactory import *

# from src.test.org.joda.convert.factory.ByteObjectArrayStringConverterFactory_ESTest_scaffolding import *
from src.main.org.joda.convert.factory.NumericArrayStringConverterFactory import *


class ByteObjectArrayStringConverterFactory_ESTest(unittest.TestCase):

    def test3(self) -> None:
        byteObjectArrayStringConverterFactory0 = (
            ByteObjectArrayStringConverterFactory.INSTANCE
        )
        string0 = byteObjectArrayStringConverterFactory0.toString()
        self.assertEqual("ByteObjectArrayStringConverterFactory", string0)

    def test2(self) -> None:

        byteObjectArrayStringConverterFactory0 = (
            ByteObjectArrayStringConverterFactory.INSTANCE
        )
        class0 = Byte
        stringConverter0 = byteObjectArrayStringConverterFactory0.findConverter(class0)
        self.assertIsNone(stringConverter0)

    def test1(self) -> None:

        numericArrayStringConverterFactory0 = (
            NumericArrayStringConverterFactory.INSTANCE
        )
        class0 = Byte

        try:
            numericArrayStringConverterFactory0.findConverter(class0)
        except ValueError:
            pass

    def test0(self) -> None:

        booleanObjectArrayStringConverterFactory0 = (
            BooleanObjectArrayStringConverterFactory.INSTANCE
        )
        try:
            booleanObjectArrayStringConverterFactory0.toString()
        except ValueError:
            pass
