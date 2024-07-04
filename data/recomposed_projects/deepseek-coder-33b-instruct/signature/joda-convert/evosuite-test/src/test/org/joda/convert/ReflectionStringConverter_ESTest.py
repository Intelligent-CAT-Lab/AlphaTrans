from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.convert.ReflectionStringConverter import *

# from src.test.org.joda.convert.ReflectionStringConverter_ESTest_scaffolding import *
from src.main.org.joda.convert.TypedFromStringConverter import *


class ReflectionStringConverter_ESTest(unittest.TestCase):

    def test0(self) -> None:

        class0 = object
        reflectionStringConverter0 = None
        try:
            reflectionStringConverter0 = ReflectionStringConverter(class0, None, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.joda.convert.ReflectionStringConverter", e)
