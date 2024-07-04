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
from src.main.org.joda.convert.OptionalDoubleStringConverter import *

# from src.test.org.joda.convert.OptionalDoubleStringConverter_ESTest_scaffolding import *


class OptionalDoubleStringConverter_ESTest(unittest.TestCase):

    def test5(self) -> None:
        optionalDoubleStringConverter0 = OptionalDoubleStringConverter()
        class0 = optionalDoubleStringConverter0.getEffectiveType()
        self.assertEqual(17, class0.getModifiers())

    def test4(self) -> None:

        optionalDoubleStringConverter0 = OptionalDoubleStringConverter()
        class0 = int
        object0 = optionalDoubleStringConverter0.convertFromString(class0, "")
        string0 = optionalDoubleStringConverter0.convertToString(object0)
        self.assertEqual("", string0)

    def test3(self) -> None:

        optionalDoubleStringConverter0 = OptionalDoubleStringConverter()
        class0 = int
        object0 = optionalDoubleStringConverter0.convertFromString(class0, "78")
        string0 = optionalDoubleStringConverter0.convertToString(object0)
        self.assertEqual("78.0", string0)

    def test2(self) -> None:

        optionalDoubleStringConverter0 = OptionalDoubleStringConverter()
        class0 = int

        with pytest.raises(TypeError):
            optionalDoubleStringConverter0.convertFromString(class0, None)

    def test1(self) -> None:

        optionalDoubleStringConverter0 = OptionalDoubleStringConverter()
        class0 = int

        with pytest.raises(ValueError):
            optionalDoubleStringConverter0.convertFromString(class0, "AikOdfqjjTLCd<2")

    def test0(self) -> None:

        optionalDoubleStringConverter0 = OptionalDoubleStringConverter()

        try:
            optionalDoubleStringConverter0.convertToString(
                optionalDoubleStringConverter0
            )
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            self.verifyException("org.joda.convert.OptionalDoubleStringConverter", e)
