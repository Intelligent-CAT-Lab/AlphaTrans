from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import typing
from typing import *
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.convert.TypeUtils import *

# from src.test.org.joda.convert.TypeUtils_ESTest_scaffolding import *


class TypeUtils_ESTest(unittest.TestCase):

    def test4(self) -> None:
        try:
            TypeUtils.parse("<2xxfzxUx' X9)u8b`(")
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            self.verifyException("org.joda.convert.TypeUtils", e)

    def test3(self) -> None:
        class0 = TypeUtils.parse("long")
        assert not isinstance(class0, type) or not issubclass(class0, typing.Protocol)

    def test2(self) -> None:
        try:
            TypeUtils.parse('D:jp"T08r^t^Z*Y')
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("org.joda.convert.TypeUtils", e)

    def test1(self) -> None:

        # Undeclared exception
        try:
            TypeUtils.parse(None)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.joda.convert.TypeUtils", e)

    def test0(self) -> None:
        try:
            TypeUtils.parse("m'<*bCfGMds(\"UH=")
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            self.verifyException("org.joda.convert.TypeUtils", e)
