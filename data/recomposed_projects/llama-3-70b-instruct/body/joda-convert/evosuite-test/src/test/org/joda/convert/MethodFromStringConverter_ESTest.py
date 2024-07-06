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
from src.main.org.joda.convert.MethodFromStringConverter import *

# from src.test.org.joda.convert.MethodFromStringConverter_ESTest_scaffolding import *


class MethodFromStringConverter_ESTest(unittest.TestCase):

    def test0(self) -> None:

        class0 = RuntimeError
        methodFromStringConverter0 = None
        try:
            methodFromStringConverter0 = MethodFromStringConverter(class0, None, class0)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.joda.convert.MethodFromStringConverter", e)
