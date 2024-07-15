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
from src.main.org.joda.money.DefaultCurrencyUnitDataProvider import *

# from src.test.org.joda.money.DefaultCurrencyUnitDataProvider_ESTest_scaffolding import *


class DefaultCurrencyUnitDataProvider_ESTest(unittest.TestCase):

    def test0(self) -> None:

        defaultCurrencyUnitDataProvider0 = DefaultCurrencyUnitDataProvider()
        try:
            defaultCurrencyUnitDataProvider0.registerCurrencies()
            pytest.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("java.util.regex.Matcher", e)
