from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import numbers
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.convert.OptionalIntStringConverter import *

# from src.test.org.joda.convert.OptionalIntStringConverter_ESTest_scaffolding import *


class OptionalIntStringConverter_ESTest(unittest.TestCase):

    def test4(self) -> None:
        optionalIntStringConverter0 = OptionalIntStringConverter()
        class0 = optionalIntStringConverter0.getEffectiveType()
        self.assertFalse(class0.isPrimitive())

    def test3(self) -> None:

        optionalIntStringConverter0 = OptionalIntStringConverter()
        class0 = int
        object0 = optionalIntStringConverter0.convertFromString(class0, "")
        string0 = optionalIntStringConverter0.convertToString(object0)
        self.assertEqual("", string0)

    def test2(self) -> None:

        optionalIntStringConverter0 = OptionalIntStringConverter()
        class0 = int
        object0 = optionalIntStringConverter0.convertFromString(class0, "9")
        string0 = optionalIntStringConverter0.convertToString(object0)
        self.assertEqual("9", string0)

    def test1(self) -> None:

        optionalIntStringConverter0 = OptionalIntStringConverter()
        class0 = int

        with pytest.raises(ValueError):
            optionalIntStringConverter0.convertFromString(class0, "isPresent")

    def test0(self) -> None:

        optionalIntStringConverter0 = OptionalIntStringConverter()
        object0 = object()

        with pytest.raises(ValueError) as e:
            optionalIntStringConverter0.convertToString(object0)

        verifyException("org.joda.convert.OptionalIntStringConverter", str(e.value))
