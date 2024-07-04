from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
from src.main.org.joda.convert.ConstructorFromStringConverter import *

# from src.test.org.joda.convert.ConstructorFromStringConverter_ESTest_scaffolding import *


class ConstructorFromStringConverter_ESTest(unittest.TestCase):

    def test0(self) -> None:

        class0 = object
        constructorFromStringConverter0 = None
        try:
            constructorFromStringConverter0 = ConstructorFromStringConverter(
                class0, None
            )
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException("org.joda.convert.ConstructorFromStringConverter", e)
