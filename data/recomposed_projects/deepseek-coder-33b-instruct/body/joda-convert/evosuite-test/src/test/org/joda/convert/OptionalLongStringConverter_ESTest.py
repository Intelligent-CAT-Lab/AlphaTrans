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
from src.main.org.joda.convert.OptionalLongStringConverter import *

# from src.test.org.joda.convert.OptionalLongStringConverter_ESTest_scaffolding import *


class OptionalLongStringConverter_ESTest(unittest.TestCase):

    def test4(self) -> None:
        optionalLongStringConverter0 = OptionalLongStringConverter()
        class0 = optionalLongStringConverter0.getEffectiveType()
        self.assertFalse(class0.isSynthetic())

    def test3(self) -> None:

        class0 = int
        optionalLongStringConverter0 = OptionalLongStringConverter()
        object0 = optionalLongStringConverter0.convertFromString(class0, "")
        string0 = optionalLongStringConverter0.convertToString(object0)
        self.assertEqual("", string0)

    def test2(self) -> None:

        class0 = int
        optionalLongStringConverter0 = OptionalLongStringConverter()
        object0 = optionalLongStringConverter0.convertFromString(class0, "7")
        string0 = optionalLongStringConverter0.convertToString(object0)
        self.assertEqual("7", string0)

    def test1(self) -> None:

        optionalLongStringConverter0 = OptionalLongStringConverter()
        class0 = int

        with pytest.raises(ValueError):
            optionalLongStringConverter0.convertFromString(class0, "Q4Y L")

    def test0(self) -> None:

        optionalLongStringConverter0 = OptionalLongStringConverter()

        try:
            optionalLongStringConverter0.convertToString(optionalLongStringConverter0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.convert.OptionalLongStringConverter", e)
